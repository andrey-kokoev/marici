# The rank-two gamma integral is stable at the scouted positive margins

## Audit

The gamma contribution to the antisymmetric two-translate deficit is

\[
\frac1{2\pi}
\int_0^\infty
 e^{-2\sigma u^2}
 \operatorname{Re}\psi(1/4+iu/2)
 (1-\cos(du))du.
\]

It was recomputed at the narrow-width test points using:

- 6,000, 12,000, and 24,000 Simpson panels;
- two integration cutoffs differing by a factor of \(1.25\);
- recurrence of the digamma argument to modulus at least twelve;
- eight Bernoulli terms in the asymptotic expansion.

## Result

Across all tested resolutions and cutoffs, the largest spread was approximately

\[
3.40\times10^{-14}.
\]

It occurred at \(\sigma=0.005\) and \(d=0.5\). Every tested spread was below \(10^{-12}\).

The smallest positive rank-two margin in the non-roundoff regime was approximately \(6.15\times10^{-10}\). The observed quadrature variation is therefore more than four orders of magnitude smaller.

Combined with the elementary prime-tail estimate, this makes the sampled narrow-width positivity numerically robust against the two principal truncation parameters.

## Scope

This remains a convergence audit, not a proof. Agreement of refinements does not replace a directed error bound. In particular, the following must still be bounded rigorously:

- the composite Simpson remainder;
- the digamma asymptotic remainder after recurrence;
- floating roundoff in the cancellation of the four source sectors.

The wider-width samples are too close to zero for ordinary double-precision certification and should not be targeted first.

## Disposition

The best first interval certificate is the point

\[
(\sigma,d)=(0.05,0.5),
\]

where the reported positive margin is about \(6.15\times10^{-10}\), the prime tail is below \(10^{-129}\), and quadrature variation is near machine precision.

## Verification

```text
python research/voevodsky/checkers/check_two_translate_gamma_quadrature_convergence.py
```

Artifacts:

- `research/voevodsky/checkers/check_two_translate_gamma_quadrature_convergence.py`
- `research/voevodsky/results/two_translate_gamma_quadrature_convergence.json`
