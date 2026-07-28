# Waning Immunity

`waning_curves.csv` provides vaccine efficacy (VE) trajectories over time since vaccination, for use as the waning immunity input in models.

## Columns

- `rep`: repetition index (1–500), sampling uncertainty in the waning curve.
- `month`: months since vaccination (0–36).
- `VE_inf`: vaccine efficacy against infection.
- `VE_sev`: vaccine efficacy against severe disease.

## Usage

Each `rep` is one plausible realization of the VE-over-time curve. Models should account for uncertainty by running across (a subset of) the 500 repetitions rather than using a single curve.
