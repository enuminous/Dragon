import numpy as np
import pandas as pd

def future_transition(labels, horizon=10):
    labels=np.asarray(labels,dtype=int)
    out=np.zeros(len(labels),dtype=int)
    for i in range(len(labels)):
        end=min(len(labels),i+horizon+1)
        if i+1<end:
            out[i]=int(np.any(labels[i+1:end] != labels[i]))
    return out

def build_dragon_features(z, labels, distances, horizons=(3,7,23)):
    z=np.asarray(z,dtype=float)
    labels=np.asarray(labels,dtype=int)
    distances=np.asarray(distances,dtype=float)
    n=len(labels)

    out=pd.DataFrame(index=np.arange(n))
    assigned_distance=distances[np.arange(n),labels]
    out["assigned_distance"]=assigned_distance

    # Margin between closest and second-closest regimes.
    ordered=np.sort(distances,axis=1)
    if distances.shape[1] >= 2:
        out["regime_margin"]=ordered[:,1]-ordered[:,0]
    else:
        out["regime_margin"]=0.0

    velocity=np.zeros(n)
    acceleration=np.zeros(n)
    direction_change=np.zeros(n)

    if n>1:
        diffs=z[1:]-z[:-1]
        velocity[1:]=np.linalg.norm(diffs,axis=1)
    if n>2:
        acceleration[2:]=np.abs(velocity[2:]-velocity[1:-1])
        v1=z[1:-1]-z[:-2]
        v2=z[2:]-z[1:-1]
        denom=np.linalg.norm(v1,axis=1)*np.linalg.norm(v2,axis=1)+1e-8
        cos=np.sum(v1*v2,axis=1)/denom
        direction_change[2:]=1.0-np.clip(cos,-1,1)

    out["velocity"]=velocity
    out["acceleration"]=acceleration
    out["direction_change"]=direction_change

    # Persistence and recurrence.
    same_prev=np.r_[0,(labels[1:]==labels[:-1]).astype(float)]
    out["same_regime_previous"]=same_prev

    run=np.ones(n,dtype=float)
    for i in range(1,n):
        run[i]=run[i-1]+1 if labels[i]==labels[i-1] else 1
    out["regime_run_length"]=run

    # Escape pressure = distance + velocity + direction instability + shrinking margin.
    out["escape_pressure"]=(
        out["assigned_distance"].rank(pct=True)
        +out["velocity"].rank(pct=True)
        +out["direction_change"].rank(pct=True)
        +(1.0-out["regime_margin"].rank(pct=True))
    )/4.0

    # Recursive organization state.
    base=(
        (1.0-out["assigned_distance"].rank(pct=True))
        +out["regime_run_length"].rank(pct=True)
        +(1.0-out["direction_change"].rank(pct=True))
    )/3.0
    rec=np.zeros(n)
    for i,v in enumerate(base.to_numpy()):
        prev=rec[i-1] if i else 0.0
        rec[i]=0.7*prev+0.3*np.tanh(float(v)+prev)
    out["recursive_attractor_strength"]=rec

    for h in horizons:
        out[f"distance_mean_{h}"]=out["assigned_distance"].rolling(h,min_periods=1).mean()
        out[f"escape_mean_{h}"]=out["escape_pressure"].rolling(h,min_periods=1).mean()
        out[f"velocity_mean_{h}"]=out["velocity"].rolling(h,min_periods=1).mean()
        out[f"persistence_mean_{h}"]=out["same_regime_previous"].rolling(h,min_periods=1).mean()

    components=[
        out["escape_pressure"],
        out["assigned_distance"],
        out["velocity"],
        out["acceleration"],
        out["direction_change"],
        1.0/(out["regime_run_length"]+1.0),
        1.0-out["recursive_attractor_strength"].rank(pct=True),
    ]
    for h in horizons:
        components.extend([
            out[f"distance_mean_{h}"],
            out[f"escape_mean_{h}"],
            out[f"velocity_mean_{h}"],
            1.0-out[f"persistence_mean_{h}"],
        ])

    ranked=pd.concat(components,axis=1).replace([np.inf,-np.inf],np.nan).fillna(0.0).rank(pct=True)
    out["dragon_transition_score"]=ranked.mean(axis=1).fillna(0.0)
    out["regime_label"]=labels

    return out
