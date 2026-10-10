# DRAGON

<!-- ENUMINOUS-NETWORK:START -->
**eNuminous network:** [All repositories](https://enuminous.github.io/EFMW/repositories.html) · [EFMW](https://enuminous.github.io/EFMW/) · [102 equations](https://github.com/enuminous/Monolithic_102_EFMW) · [165 triplets](https://enuminous.github.io/FieldSpace/) · [Zoo](https://enuminous.github.io/Tortoise/) · [Lean](https://enuminous.github.io/Aristotle-102-Monolithic-Lean/) · [Engine](https://enuminous.github.io/Archimedes-Engine/) · [Papers](https://enuminous.github.io/medium/papers-essays-index.html) · [Audit](https://github.com/enuminous/EFMW_Post156_Zoo_Audit/blob/main/portfolio/INTERLOCK_AUDIT.md)

[Repository](https://github.com/enuminous/Dragon) · This repository is linked through its source; GitHub Pages is not enabled.
<!-- ENUMINOUS-NETWORK:END -->

**Distributed Recursive Attractor and Gradient Organization Network**

DRAGON is the EFMW animal for **attractors, regimes, and systemic phase transitions**.

Its narrow question is:

> Is the system settling into a stable behavioral regime, escaping from one, or transitioning between regimes in a way that can be detected before the transition is complete?

## Intended uses

- control systems
- AI-agent state
- distributed networks
- markets
- organizational dynamics
- industrial processes
- logistics
- robotics
- complex multivariate telemetry

## Core path

```text
multivariate state
→ normalized state space
→ local trajectory
→ attractor candidate
→ persistence
→ gradient organization
→ transition pressure
→ regime assignment
→ attractor entry / escape
→ DRAGON regime score
```

## Flat-stack repository

```text
README.md
LICENSE
CITATION.cff
pyproject.toml
requirements.txt
dragon.py
features.py
models.py
metrics.py
freeze.py
regime_schema.json
example_config.yaml
example_data.csv
example_run.py
test_dragon.py
MANIFEST.sha256
```

## Scientific hypothesis

> Complex systems may exhibit stable or metastable behavioral regimes, and changes in trajectory geometry, persistence, and gradient organization may provide early evidence of regime entry or escape.

DRAGON does not assume that every cluster is a meaningful attractor.

## Operational definitions

### Regime

A recurring region of state space with measurable persistence.

### Attractor candidate

A regime toward which local trajectories show convergent behavior.

### Escape pressure

Increasing distance, velocity, or directional inconsistency relative to the current regime center.

### Transition

A sustained move from one regime assignment to another.

## Important caution

A clustering algorithm can always produce clusters.

DRAGON must not equate "cluster" with "physical attractor" without additional evidence such as:

- persistence
- recurrence
- convergence
- transition reproducibility
- perturbation response
- external validation

## Baselines

Included:

- raw-state logistic transition predictor
- distance-to-centroid baseline
- velocity-only baseline
- rolling-variance baseline
- base-rate predictor

## Primary endpoint

> Does DRAGON improve out-of-sample prediction of a future regime transition over matched raw-state and simple geometric baselines?

Primary metric:

- Brier score

Secondary metrics:

- log loss
- ROC-AUC
- average precision
- transition lead behavior
- regime persistence
- recurrence rate

## Installation

```bash
python -m pip install -r requirements.txt
```

## Run

```bash
python example_run.py
```

## Tests

```bash
pytest -q
```

## Freeze discipline

Freeze before prospective evaluation:

- state variables
- normalization
- number of candidate regimes
- clustering method
- development segment
- transition definition
- horizons
- recursion rule
- baseline models
- metrics
- exclusions
- random seed

Then:

```bash
python freeze.py
```

## Negative results

If simple state, distance, velocity, or variance baselines match DRAGON, then explicit attractor/gradient structure has not demonstrated incremental predictive value.

## Status

Research software. Experimental.
