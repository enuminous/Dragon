# DRAGON

<!-- ENUMINOUS-UNIFIED-NAV:START -->
## Repository navigation

**eNuminous network:** [All public repositories](https://github.com/enuminous/EFMW/blob/main/REPOSITORY_NAVIGATION.md) · [EFMW](https://github.com/enuminous/EFMW) · [102 equations](https://github.com/enuminous/Monolithic_102_EFMW) · [Frozen Lean](https://github.com/enuminous/Monolithic-102-Zoo-Lean4) · [Zoo](https://github.com/enuminous/Tortoise) · [Papers](https://github.com/enuminous/papers) · [Quantum geometry](https://github.com/enuminous/Base888-Quantum-Geometry)

**This project:** [Repository home](https://github.com/enuminous/Dragon) · [Subject index](https://github.com/enuminous/EFMW/blob/main/REPOSITORY_NAVIGATION.md#zoo-index-and-agents)

<details open>
<summary><strong>On this page</strong></summary>

- [Intended uses](#intended-uses)
- [Core path](#core-path)
- [Flat-stack repository](#flat-stack-repository)
- [Scientific hypothesis](#scientific-hypothesis)
- [Operational definitions](#operational-definitions)
  - [Regime](#regime)
  - [Attractor candidate](#attractor-candidate)
  - [Escape pressure](#escape-pressure)
  - [Transition](#transition)
- [Important caution](#important-caution)
- [Baselines](#baselines)
- [Primary endpoint](#primary-endpoint)
- [Installation](#installation)
- [Run](#run)
- [Tests](#tests)
- [Freeze discipline](#freeze-discipline)
- [Negative results](#negative-results)
- [Status](#status)


</details>

**Related repositories:** [Tortoise](https://github.com/enuminous/Tortoise) · [Monolithic-Zoo-Lean4](https://github.com/enuminous/Monolithic-Zoo-Lean4) · [Monolithic-102-Zoo-Lean4](https://github.com/enuminous/Monolithic-102-Zoo-Lean4) · [Turtle](https://github.com/enuminous/Turtle) · [Crocodile](https://github.com/enuminous/Crocodile) · [Magpie](https://github.com/enuminous/Magpie) · [Hedgehog](https://github.com/enuminous/Hedgehog)

> **Evidence boundary:** A link between projects is navigation, not an assertion of proven equivalence, experimental validation, or shared authorship. See each repository’s own status and review notes.
<!-- ENUMINOUS-UNIFIED-NAV:END -->


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
