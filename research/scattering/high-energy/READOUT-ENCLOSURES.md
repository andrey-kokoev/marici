# H6 — stored-readout ball comparisons with peak uncertainty

The stored occupation global maxima have been localized in PEAK-ENCLOSURE.md. This follow-up encloses peak transport J/P at **every time** in each bracket, not merely the optimizer's point. For occupation and current, it evaluates exact-binary kernels and coefficients at the bracket's reference time with Arb, bounds the first derivative there and bounds the second derivative everywhere by sum_ij |a_ij| |K_j-K_i|². Taylor's theorem gives an enclosure throughout the bracket. A positive enclosed occupation allows safe division.

Whole-packet transport is ball-evaluated from the stored binary moment weights and kernel diagonals. Product probability is ball-evaluated from those weights and the saved binary per-energy probability scalars. No exact stationary probability is inferred from those scalars. The receipt exposes these reference choices; exact moment constraints and coefficient construction are not silently assumed.

For each diagnostic the checker compares independent intervals, bounding |x33-x17| from above and |x17| from below. The 1% threshold uses the exact rational 1/100. A positive margin

    budget = 0.01 min|x17| - max|x33-x17|

is a sufficient remaining allowance for exact-model/preparation errors:

    epsilon33 + 1.01 epsilon17 <= budget.

The peak bracket variation is already included; it must not be charged again as an unresolved stored-readout location error. Exact-kernel/preparation perturbations can change the peak, however, so the allowance still has to cover that separate stability effect.

## Disposition

All three comparisons are certified only for the explicitly defined **stored binary readouts**. H6 stays open until the differences between those readouts and the specified exact finite-model/moment-matched preparation are enclosed within the remaining budgets. Small stationary residuals are not such bounds. Full-untruncated H7 remains unnecessary for this fixed-response task.

Two of the original six H6 cycles are spent (peak localization and readout propagation); four remain. Next work should target preparation certification and finite-response solver-to-kernel sensitivity, not repeat the enclosed binary comparisons.

Replay:

    uv run --with numpy --with python-flint python research/scattering/high-energy/check_readout_enclosures.py --check
