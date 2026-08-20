import json
import pandas as pd
from dragon import DRAGONExperiment

df=pd.read_csv("example_data.csv")

exp=DRAGONExperiment(
    time_column="time",
    feature_columns=["state_a","state_b","state_c"],
    n_regimes=3,
    development_fraction=0.55,
    transition_horizon=10,
    horizons=(3,7,23),
    random_state=23,
)

print(json.dumps(exp.run(df),indent=2))
