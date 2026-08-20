import pandas as pd
from dragon import DRAGONExperiment
from models import RegimeModel
from features import build_dragon_features

FEATURES=["state_a","state_b","state_c"]

def test_regime_features():
    df=pd.read_csv("example_data.csv")
    raw=df[FEATURES]
    m=RegimeModel(3,23).fit(raw.iloc[:300])
    z,l,d=m.transform(raw)
    f=build_dragon_features(z,l,d)
    assert len(f)==len(df)
    assert "dragon_transition_score" in f.columns
    assert f["dragon_transition_score"].between(0,1).all()

def test_experiment_runs():
    df=pd.read_csv("example_data.csv")
    out=DRAGONExperiment(
        time_column="time",
        feature_columns=FEATURES,
    ).run(df)
    assert "results" in out
    assert "dragon" in out["results"]
    assert "raw_state" in out["results"]

def test_regime_summary_present():
    df=pd.read_csv("example_data.csv")
    out=DRAGONExperiment(
        time_column="time",
        feature_columns=FEATURES,
    ).run(df)
    assert "transition_count" in out["regime_summary_all"]
