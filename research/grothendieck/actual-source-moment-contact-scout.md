# Actual-source moment/contact scout

## Question

Do the value--slope ellipse and curvature covariance inequality reduce the possible finite-contact set to a narrow corridor near zero character, or does a large part of the compact parameter region survive?

## Scout configuration

The exploratory checker evaluates the Marici positive-half-divisor source formula using:

- 48 logarithmically spaced `t` values on `[0.08,3]`;
- 501 character values on `[0,25]`;
- prime powers through `2,000,000`;
- 96-node floating-point Gauss--Hermite quadrature for the digamma integral;
- actual von Mangoldt weights and moments `M0,M2,M4`;
- the value--slope ellipse and curvature covariance filters.

Files:

- `research/grothendieck/checkers/actual_source_moment_contact_scout.py`
- `research/grothendieck/results/actual-source-moment-contact-scout.json`
- `research/grothendieck/checkers/high_precision_source_spot_audit.py`
- `research/grothendieck/results/high-precision-source-spot-audit.json`

## Raw result

The low-order filters do not confine survivors to a narrow zero-character corridor. The survivor fraction rises from approximately `0.275` at `t=0.08` to more than `0.99` by `t=0.275`, and remains approximately `0.998` over much of the larger-`t` grid. At those parameters, survivors extend across nearly the entire sampled interval in `xi`.

Thus moments through order four are far too weak to construct global finite-double-contact exclusion. They may still remove bounded subregions at small `t`, but they do not identify zero character as the sole hard residue.

## Numerical defect found

The same run reports negative values of `Theta` and apparent near contacts at scales where severe source-side cancellation occurs. For example, its smallest normalized contact score occurs near

\[
(t,\xi)=(0.94356,6.6)
\]

at approximately `8.2e-18`, which is at double-precision cancellation scale. The reported minimum values are not trustworthy: endpoint, gamma, and prime blocks are much larger than the residual, Gauss--Hermite quadrature is not interval enclosed, and the finite prime cutoff has no certified tail. At larger `t`, comparison between cutoffs `10^6` and `2\times10^6` changes `M4` by as much as `2.9e-4` relatively.

The scout therefore fails any positivity or contact-verification claim. Its only defensible output is qualitative feasibility evidence that the low-order outer moment body leaves most grid points admissible. Even that conclusion requires a higher-precision spot audit before promotion.

## High-precision spot audit

A 60-decimal-digit recomputation used adaptive transformed-variable digamma quadrature, prime-power cutoffs at `500,000`, `1,000,000`, and `2,000,000`, and an independent sum over the first 60 computed critical-line zeros.

At `t=0.275`, the source and zero-side values agree to the displayed precision at `xi=0,15,25`; at `xi=5` they agree to absolute error `6.7e-25`. The values range from `1.38e-24` at zero character to approximately `0.407` and `0.507` at characters 15 and 25. This validates the source normalization and the numerical arithmetic on the slice where the moment scout leaves `99.4%` of grid points admissible. The conclusion that the low-order moment body leaves essentially the full character interval therefore survives the spot audit.

The audit also localizes the earlier numerical defect. At `t=0.94356, xi=6.6`, source cancellation is at `1e-23` while the last prime-cutoff change is `2.2e-21`; at `t=2, xi=10`, the cutoff change is `3.3e-10` while the zero-side answer is `7.1e-16`. Finite prime-cutoff source evaluation is unusable there without an analytic tail treatment. These failures do not affect the validated `t=0.275` slice.

## Strongest falsification attempt

The conjecture was that value, slope, and curvature constraints would leave only a narrow neighborhood of `xi=0`. The raw grid contradicts this: for `t` above approximately `0.275`, more than 99 percent of sampled characters survive. The exact residual is numerical noncertification, not a theorem that contacts exist.

## Next discriminating test

The high-precision discriminating test has left the survivor fraction near one on the `t=0.275` slice. Stop refining the three-moment grid. Replace low-order scalar moments by a stronger Toeplitz/Hankel semidefinite moment hierarchy or a different arithmetic inequality. Any future source evaluation above this slice requires an analytic prime-tail treatment rather than merely a larger cutoff.

## Disposition

The hypothesis that the hard residue is only a narrow corridor around zero character is rejected for moments through order four: a high-precision-validated slice leaves essentially the entire sampled compact character interval feasible. No RH claim is advanced; the higher-`t` finite-cutoff source values remain explicitly nonverified.
