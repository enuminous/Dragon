from dataclasses import dataclass
import numpy as np
import pandas as pd

from models import RegimeModel, LogisticModel
from features import build_dragon_features, future_transition
from metrics import binary_metrics, regime_summary

@dataclass
class DRAGONExperiment:
    time_column: str
    feature_columns: list
    n_regimes: int=3
    development_fraction: float=0.55
    transition_horizon: int=10
    horizons: tuple=(3,7,23)
    random_state: int=23

    def run(self,df):
        df=df.sort_values(self.time_column).reset_index(drop=True).copy()
        raw=df[self.feature_columns].astype(float).ffill().fillna(0.0)
        cut=max(30,int(len(df)*self.development_fraction))

        regime=RegimeModel(self.n_regimes,self.random_state).fit(raw.iloc[:cut])
        z,labels,distances=regime.transform(raw)

        drf=build_dragon_features(z,labels,distances,self.horizons)
        y=future_transition(labels,self.transition_horizon)

        # Prediction model trains on development period, evaluates prospectively afterward.
        full=pd.concat([raw.reset_index(drop=True),drf.drop(columns=["regime_label"])],axis=1)
        distance=drf[["assigned_distance","regime_margin"]]
        velocity=drf[["velocity","acceleration","direction_change"]]
        variance=pd.DataFrame({
            "rolling_variance":raw.rolling(max(self.horizons),min_periods=2).var().mean(axis=1).fillna(0.0)
        })

        sets={
            "dragon":full,
            "raw_state":raw,
            "distance_only":distance,
            "velocity_only":velocity,
            "variance_only":variance,
        }

        results={}
        for name,X in sets.items():
            m=LogisticModel(self.random_state).fit(X.iloc[:cut],y[:cut])
            p=m.predict_proba(X.iloc[cut:])
            results[name]=binary_metrics(y[cut:],p)

        base_rate=float(np.mean(y[:cut]))
        p_base=np.full(len(y)-cut,base_rate)
        results["base_rate"]=binary_metrics(y[cut:],p_base)

        return {
            "n_total":len(df),
            "development_n":cut,
            "heldout_n":len(df)-cut,
            "n_regimes":self.n_regimes,
            "transition_horizon":self.transition_horizon,
            "regime_summary_all":regime_summary(labels),
            "regime_summary_heldout":regime_summary(labels[cut:]),
            "results":results,
            "primary_delta_brier_raw_minus_dragon":(
                results["raw_state"]["brier"]-results["dragon"]["brier"]
            ),
            "interpretation":(
                "Positive ΔBrier favors DRAGON over raw state. "
                "KMeans regimes are operational state clusters, not automatically physical attractors."
            )
        }
