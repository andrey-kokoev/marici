# The central continuum problem is a fourth-order Xi-log inequality

Define the symmetry-reduced completed source

\[
 \ell(t)=\log\Xi\left(\frac12+\sqrt t\right).
\]

Because `Xi(s)=Xi(1-s)`, the logarithm is locally even in
`q=s-1/2`; hence `ell` is analytic in `t=q^2` wherever `Xi` is nonzero.
Moreover,

\[
 \frac{\Xi'}{\Xi}(s)=2q\ell'(t),
 \qquad S(t)=\frac1{2s-1}\frac{\Xi'}{\Xi}(s)=\ell'(t).
\]

Therefore the reduced Pick source has the cancellation-free form

\[
 \boxed{F(t)=(4t-1)\ell'(t).}
\]

Its first three derivatives are

\[
 F'=4\ell'+(4t-1)\ell'',
\]

\[
 F''=8\ell''+(4t-1)\ell''',
\]

\[
 F'''=12\ell'''+(4t-1)\ell''''.
\]

For `H=(F')^(-1/2)`, direct differentiation gives

\[
 H''=-\frac{2F'F'''-3(F'')^2}{4(F')^{5/2}}.
\]

Thus, where `F'>0`, continuum reciprocal-slope concavity is exactly

\[
 \boxed{2F'F'''-3(F'')^2\ge0,}
\]

with `F',F'',F'''` given by the four displayed Xi-log derivatives.

## Why this changes the certification problem

The earlier evaluator separately formed a singular prefactor and a vanishing
completed logarithmic derivative in the square-root coordinate. Point
intervals survived that cancellation, but interval boxes in `t` would suffer
severe dependency blow-up. The `ell(t)` formulation cancels the square root
symbolically before interval evaluation.

The next continuum certificate is now concrete: construct outward-rounded
Taylor models for `ell',...,ell''''` on subintervals of `[0,10^-2]` and test
the boxed polynomial directly. A negative interval box would be a genuine
local falsifier; positive boxes covering the range would prove central
concavity on the continuum.

The reduction is exact, but those interval Taylor models have not yet been
constructed. No continuum positivity or RH proof is claimed.

The chord-average margin gives a second route using oscillation. With `g=F'`,

\[
 H'''=\frac{18gg'g''-4g^2g'''-15(g')^3}{8g^{7/2}},
\]

where

\[
 F''''=16\ell''''+(4t-1)\ell'''''.
\]

Thus a boxwise `H'''` bound needs the Xi-log jet only one order higher, through
`ell'''''`. Multiplying that bound by a cell width controls the oscillation of
`H''`; if it is below the certified average-curvature margin, the entire cell
is concave. This is the next sufficient continuum criterion.

## Durable verification

- Checker: `checkers/central_xi_log_curvature_identity.py`
- Result: `results/central-xi-log-curvature-identity.json`
