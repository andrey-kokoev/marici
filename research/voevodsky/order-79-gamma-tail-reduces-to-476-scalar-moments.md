# The order-79 gamma tail reduces exactly to 476 scalar moments

The spherical-Bessel recurrence

\[
j_{n+1}(x)=\frac{2n+1}{x}j_n(x)-j_{n-1}(x)
\]

was used with

\[
j_0(x)=\frac{\sin x}{x},\qquad
j_1(x)=\frac{\sin x}{x^2}-\frac{\cos x}{x}
\]

to generate exact integer arrays through `n=79`:

\[
j_n(x)=S_n(x^{-1})\sin x+C_n(x^{-1})\cos x.
\]

The largest coefficient has 140 decimal digits, so floating expansion is not
appropriate; exact integers followed by ball evaluation are required.

Every product `j_m(Lu)j_n(Lu)` now reduces via

\[
\sin^2x=\frac{1-\cos2x}{2},\quad
\cos^2x=\frac{1+\cos2x}{2},\quad
\sin x\cos x=\frac{\sin2x}{2}
\]

to scalar tail moments of the gamma multiplier against

\[
u^{-k},\qquad u^{-k}\cos(2Lu),\qquad u^{-k}\sin(2Lu),
\]

with `2<=k<=160`. After removing structurally absent combinations, exactly
476 distinct scalar moments suffice for the complete 80-dimensional gamma
tail matrix.

This closes the algebraic reduction. The remaining analytic implementation is
to enclose those scalar moments on `[R,infinity)` using the Binet expansion of
the digamma function and repeated integration by parts for the oscillatory
families. The resulting 476 intervals can then be assembled with exact
integer coefficients into both parity blocks.

Artifacts:

- `checkers/build_spherical_bessel_inverse_power_expansions.py`
- `results/spherical_bessel_inverse_power_expansions.json`
- `checkers/build_gamma_tail_scalar_moment_manifest.py`
- `results/gamma_tail_scalar_moment_manifest.json`
