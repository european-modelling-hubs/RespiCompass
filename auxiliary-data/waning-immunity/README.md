# Waning Immunity

This folder provides vaccine efficacy (VE) trajectories over time since vaccination, for use as the waning immunity input in models, together with the parameters used to generate them.

## Files

- `waning_curves.csv`: baseline VE-over-time curves, with waning as estimated from data.
- `waning_curves_faster.csv`: VE-over-time curves in the same format as `waning_curves.csv`, but with immunity assumed to wane **2x faster** than estimated from data. Use this file for scenarios that assume faster waning of immunity.
- `waning-curve-params/`: parameters used to generate the curves (see below).

## Curve columns

Both `waning_curves.csv` and `waning_curves_faster.csv` share the same format:

- `rep`: repetition index (1–500), sampling uncertainty in the waning curve.
- `month`: months since vaccination (0–36).
- `VE_inf`: vaccine efficacy against infection.
- `VE_sev`: vaccine efficacy against severe disease.

## Curve parameters

The `waning-curve-params/` folder holds the parameters used to generate the curves, one row per repetition (`rep`):

- `waning_curve_params.csv`: parameters for `waning_curves.csv`.
- `waning_curve_params_faster.csv`: parameters for `waning_curves_faster.csv`. Identical to `waning_curve_params.csv` except that the waning rate `a` is doubled, producing immunity that wanes 2x faster.

Columns:

- `rep`: repetition index (1–500), matching the `rep` in the curve files.
- `VE0_inf`: initial vaccine efficacy against infection (at `month` 0).
- `VE0_sev`: initial vaccine efficacy against severe disease (at `month` 0).
- `delta`: difference between initial VE against severe disease and infection (`VE0_sev - VE0_inf`).
- `a`: waning rate. In `waning_curve_params_faster.csv` this is `2 x` the value in `waning_curve_params.csv`.
- `d`: floor / residual efficacy the curve decays toward.
- `mean`: mean duration of immunity implied by the baseline curve.
- `half_life`: half-life of immunity implied by the baseline curve.

Note: `mean` and `half_life` in `waning_curve_params_faster.csv` are carried over from the baseline parameters and are not recomputed from the doubled `a`.

## Usage

Each `rep` is one plausible realization of the VE-over-time curve. Models should account for uncertainty by running across (a subset of) the 500 repetitions rather than using a single curve. Use `waning_curves.csv` for the data-based waning assumption and `waning_curves_faster.csv` for scenarios assuming immunity wanes twice as fast.
