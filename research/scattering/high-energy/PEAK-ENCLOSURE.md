# H6 — certified localization of stored-kernel peaks

The peak search window remains [-100,100]. The checker uses Arb at 128 bits to bound the occupation quadratic form defined by exact binary stored energies, kernels and reconstructed coefficient values. It localizes every global maximizer in a 0.002-wide bracket around each independently found 17/33-node peak. Uniqueness is not asserted.

The nearly uniform energy differences are grouped into Fourier coefficients, but binary frequency differences are **not** assumed exactly equal to multiples of the first step. Their deviations are bounded by |exp(i a t)-exp(i b t)|<=|a-b| |t|, with |t|<=100, and a corresponding derivative bound. These allowances accompany every ball evaluation. The exact-binary quadratic form also gives an absolute second-derivative bound M2=sum_ij |a_ij| |K_j-K_i|².

For each outside interval, a midpoint m and exact-endpoint radius r give the upper bound

    P(t) <= P(m)+|P'(m)|r+M2 r²/2.

The checker excludes the interval only if its ball upper bound is below a ball lower bound for occupation at the reference peak time. Otherwise it subdivides, subject to explicit finite work/depth limits. All of [-100,100] outside the retained bracket is covered; finite scanning is not used as the proof.

## Scope boundary

This certifies localization for the **stored binary readout**, not exact stationary solutions or exact moment-matched preparation. The coefficient reconstruction uses rounded packet weights and NumPy square roots. Their exactness and the kernel's solver error are not assumed. Perturbations can move a peak, so this certificate does not automatically discharge H6's original peak/observable gate. Readout variation over the bracket and kernel/preparation errors still need propagation into the acceptance budgets. H6 remains open.

This spends one of the six H6 certification effort cycles; five remain. H7's exhausted budget is not renewed.

Replay:

    uv run --with numpy --with python-flint python research/scattering/high-energy/check_peak_enclosure.py --check
