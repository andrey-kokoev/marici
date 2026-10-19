# H7 — lower-threshold inertia margin search

The original threshold 16 gives a negative block-LDL/Frobenius robustness margin. A certified bound need not recover that exact threshold: the closed-radial envelope only needs a lower omitted energy with gap at least 2 rho above the packet band. This attempt fixes four total-energy thresholds in advance: 9.5, 10, 12 and 14, all more than 2 above the source packet's top total energy. No response direction or stationary solve is changed.

For each shift, the checker rebuilds the raw native operator, counts negative block pivots and measures the factor residual, triangular inverse Frobenius norm and sufficient separation candidate as in INERTIA-MARGIN-ATTEMPT.md. The count must not exceed 420. If certified, a count <=420 would imply that the exact 421st ordered eigenvalue exceeds that threshold; transferring this fact to the stored approximate 420-dimensional response frame remains a separate spectral-subspace obligation. A count smaller than 420 does not justify discarding retained response directions.

A positive **floating** margin would identify a more viable interval-factorization target, not certify inertia, the stored projector or H7. A negative margin only rejects this sufficient route as measured. The bounded threshold set and the selection criterion (separation/residual ratio) are explicit so no universal conclusion is extracted from an unspecified adaptive search.

## Measured result

Thresholds 10 and 14 have positive floating margins; 9.5 and 12 do not. Threshold 10 is the best conditioning target: count 130, candidate band gap 2.9293718, inverse-factor Frobenius norm 4453.806, separation candidate 5.55647e-8 and factor residual 2.76931e-10 (ratio about 200.64). Threshold 14 has count 304 and ratio about 6.79. The lower threshold is therefore selected for an outward-rounded robustness attempt, not as an already certified gap. Any implementation must account for factor arithmetic, D-block spectral reconstruction and the spectral-frame transfer; copying these floats into an interval assertion is not sufficient.

This attempt spends one further H7 cycle; three of the original eight-cycle budget remain. Certified gap/frame and full coupled inverse bounds remain outstanding regardless of the numerical search outcome.
