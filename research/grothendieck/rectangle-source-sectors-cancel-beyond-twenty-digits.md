# Rectangle source sectors cancel beyond twenty digits

## Observation

The completed parity numerators were polarized into endpoint, archimedean, prime, and all mixed-sector contributions at `t=0.03,0.05,0.08`. The calculation used 80-digit arithmetic and a prime Gaussian tail exponent of 100; it is discovery evidence rather than directed certification.

At `t=0.08`, the normalized plus determinant is approximately `4.32e-9`, while individual normalized polarization terms reach `1.61e14`. The minus determinant is approximately `1.05e-10`, while individual terms reach `9.49e12`. Thus the positive residual is only about `1e-23` of the largest canonical-sector contribution.

The same cancellation pattern is already visible at `t=0.03`:

- plus-sector terms of order `1e5` leave `7.85e-4`;
- minus-sector terms of order `1e4` leave `1.90e-5`.

The endpoint self determinant is zero to the working precision, while its mixed terms are large and oppositely signed.

## Consequence

Directly proving positivity by separately bounding the six canonical polarization pieces is numerically and structurally ill-conditioned. Bounds tight enough for the total source kernel can still be useless after determinant polarization. The cancellation worsens as the Gaussian spectral weight approaches single-pair domination.

A successful source proof must expose the cancellation symbolically before numerical enclosure. Plausible admissible forms are:

1. an exact transform turning the completed distribution into positive spectral wedges;
2. paired summation identities that combine endpoint, gamma, and prime terms before bounding;
3. a rescaled Turan identity whose leading cancellations are algebraically removed.

Independent absolute bounds on endpoint, gamma, and prime sectors are not a viable certification method at these parameters.

## Reproducibility

Checker: `research/grothendieck/checkers/weil_rectangle_sector_polarization_scout.py`.

Result: `research/grothendieck/results/weil-rectangle-sector-polarization-scout.json`.

Every polarized reconstruction residual was below `4e-67` after normalization, confirming the quadratic accounting at the working precision. This checks arithmetic reconstruction, not the signs by intervals.

## Disposition

The naive sector-bound route is rejected. The unresolved frontier is an algebraic cancellation mechanism for the two completed Turan numerators. Further precision increases without such a mechanism would repeat the same ill-conditioned subtraction rather than advance the proof.
