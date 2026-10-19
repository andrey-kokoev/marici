# H7 — threshold-10 arithmetic propagation screen

The positive floating factor margin at threshold 10 does not include arithmetic-enclosure cost. This attempt tests a conservative standard-roundoff model before spending the remaining budget on full interval machinery.

For complex matrix products of inner dimension k, use the conditional Frobenius bound gamma_(8k+16) ||A||_F ||B||_F. Norms are inflated to model accumulation error. The factor product is reconstructed separately from the solve; no backward-stability claim for the factor-generating solve is needed if the reconstruction is actually enclosed. D-block spectral reconstructions and eigenframe Gram defects are included rather than treating computed eigenvalues as exact.

The inverse-factor covariance recurrence propagates a Frobenius error e_j by

    e_j <= ||L_j||_F² e_(j-1) + local_product_roundoff,

with trace error at most sqrt(250) e_j. This is deliberately conservative: replacing the multiplier spectral norm by its Frobenius norm may make the enclosure unusable despite a good floating recurrence. The receipt reports that cost explicitly.

For a D eigenframe U with Gram defect <=g<1 and reconstructed matrix error <=s, a sufficient separation bound is (1-g)min|computed eigenvalues|-s. This uses the singular value of U, not an assumption that U is exactly unitary. The inertia count remains conditional on those same enclosures.

## Authority boundary

This is a **conditional arithmetic-model screen**, not an interval certificate. NumPy/BLAS does not expose directed bounds here; the bound-estimator's scalar accumulation and library arithmetic contract are not formally verified. Source assembly and the pose/threshold reference also require enclosures. A positive model margin would indicate whether this approach is promising, not prove a gap. A negative model margin rejects this conservative propagation route, not the source separation.

## Measured result

The model margin is negative. D-block separation remains about 1.1022, but the inverse-factor squared bound grows to 1.44e106 and the factor residual model bound is 2.66e-5. The resulting separation model is only 7.65e-107. This exposes the cost of the loose normwise/Frobenius propagation: it does not disprove the favorable floating factorization. A viable implementation needs tighter verified inverse-factor bounds (for example componentwise enclosure or residual-controlled inverse reconstruction), and tighter/higher-precision factor-product residual evaluation. Outward rounding of the current formulas alone will not suffice.

This spends one H7 cycle. Two of the original eight-cycle budget remain. Do not repeat the floating threshold search; use the arithmetic-cost result to choose a sharper inverse-factor enclosure or a different certificate implementation.
