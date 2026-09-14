# The omitted gamma tail is below the scout resolution

## Digamma majorant

For the tail region used in the scout, the convergent series for the digamma function gives the deliberately coarse bound

\[
\left|
\operatorname{Re}\psi(1/4+iu/2)
\right|
\leq21+2u.
\]

One obtains it by separating the series summand into the difference between \((k+1)^{-1}\) and \((k+1/4)^{-1}\), plus the absolutely convergent imaginary-coordinate correction. The constant is intentionally enlarged.

## Gaussian tail

The omitted gamma contribution is bounded using

\[
|1-\cos(du)|\leq2.
\]

For a cutoff \(U\), the standard estimates

\[
\int_U^\infty e^{-tu^2}du
\leq
\frac{e^{-tU^2}}{2tU}
\]

and

\[
\int_U^\infty2u e^{-tu^2}du
=
\frac{e^{-tU^2}}t
\]

give the explicit bound

\[
\frac{e^{-tU^2}}\pi
\left(
\frac{21}{2tU}+rac1t
\right),
\qquad t=2\sigma.
\]

## Result

The scout chose \(U\) so that

\[
tU^2\geq35.
\]

Across the scanned parameters, the largest resulting omitted-tail bound is approximately

\[
2.37\times10^{-14}.
\]

It is below \(10^{-12}\) everywhere and far below the positive narrow-width margins.

## Remaining uncertainty

Both infinite tails are now controlled at the required scale:

- omitted prime tail: negligible by the log-Gaussian estimate;
- omitted gamma tail: below \(2.37\times10^{-14}\).

The remaining certification work lies entirely on a finite interval:

- directed evaluation of the digamma approximation;
- a rigorous composite-quadrature remainder;
- floating-roundoff control during sector cancellation.

## Verification

```text
python research/voevodsky/checkers/check_two_translate_gamma_tail_bound.py
```

Artifacts:

- `research/voevodsky/checkers/check_two_translate_gamma_tail_bound.py`
- `research/voevodsky/results/two_translate_gamma_tail_bound.json`
