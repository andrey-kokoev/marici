# H6 — preparation uncertainty propagated through peaks and readouts

This checker uses the outward endpoint intervals of the Krawczyk-certified Gaussian weights and coherent coefficients. It does not substitute their centers or assume independent rounded weights solve the exact moment equations. Treating interval entries independently overestimates the family but includes the exact root preparation.

The ball/Taylor global exclusion proof is repeated for this **enclosed preparation family**, not merely the prior fixed coefficients. The peak bracket half-width is fixed at 0.002 before the run. Every enclosed preparation's global maximum in [-100,100] lies inside its bracket. This handles peak movement caused by the certified preparation uncertainty on stored kernels. Uniqueness is not required.

Occupation/current are enclosed throughout those brackets by direct ball evaluation and Taylor derivative bounds. Whole-packet transport and probability are enclosed with interval moment weights. As before, kernels, energies and saved per-energy probabilities are exact binary inputs to this subcalculation, not exact stationary solutions.

The independent 17/33 readout intervals prove the three 1% comparisons if their separation upper bounds are below 0.01 times the baseline lower bound. Reduced remaining error budgets are recorded for subsequent solver/kernel/reference perturbations. Preparation uncertainty and its associated peak movement are already included, so they should not be charged again for the same stored-grid preparation.

## Remaining gate

H6 stays open. Solver-to-field/kernel errors and any ideal-grid/source energy-reference differences still have to fit the reduced budgets. Those perturbations may move the peak further and require their own stability control. Full-untruncated H7 is not a prerequisite for this fixed-response problem.

Four of the original six H6 cycles are spent; two remain. Next target: finite-response residual-to-observable sensitivity, not another preparation/root/peak replay.

Replay:

    uv run --with numpy --with python-flint python research/scattering/high-energy/check_prepared_readouts.py --check
