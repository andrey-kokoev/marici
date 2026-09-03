# Directed analytic bound for the quadratic IMS window

## Question

Can the numerical scout for the quadratically normalized septic window be replaced by a rigorous explicit bound without relying on floating-point quadrature?

## Claim boundary

This packet gives a conservative analytic upper bound. It does not certify the scout value or claim sharpness.

## Composition bound

Set

\[
f(u)=\frac{u}{\sqrt{u^2+(1-u)^2}},
\qquad \rho(t)=f(s(t)).
\]

Since \(u^2+(1-u)^2\ge1/2\) on \([0,1]\), direct differentiation and numerator coefficient bounds give

\[
\lVert f'\rVert_\infty\le4\sqrt2,
\quad
\lVert f''\rVert_\infty\le52\sqrt2,
\quad
\lVert f'''\rVert_\infty\le960\sqrt2.
\]

For the septic profile,

\[
\lVert s'\rVert_\infty=\frac{35}{16},
\qquad
\lVert s''\rVert_\infty=\frac{84\sqrt5}{25},
\qquad
\lVert s'''\rVert_\infty\le210.
\]

The chain rule yields

\[
\rho'''=f'''(s)(s')^3+3f''(s)s's''+f'(s)s'''.
\]

Therefore, on the unit transition,

\[
\lVert\rho'''\rVert_{L^1}
\le B_{\rm IMS},
\]

where

\[
B_{\rm IMS}
=
960\sqrt2\left(\frac{35}{16}\right)^3
+156\sqrt2\left(\frac{35}{16}\right)
 \left(\frac{84\sqrt5}{25}\right)
+840\sqrt2.
\]

For two windows and two transitions of width \(h\), Aspect's estimate gives the directed bound

\[
C_{\rm loc}^{\rm quad}(h)
\le \frac{2\pi}{3h^2}B_{\rm IMS}.
\]

## Disposition

The quadratic IMS localization constant is now rigorously finite and explicit. The bound is intentionally loose; it closes admissibility and domain-control gates but may be too large for positivity. A sharper interval enclosure is warranted only if the low-block positivity margin cannot absorb this certified constant.

## Verification

- `research/voevodsky/checkers/check_quadratic_ims_analytic_bound.py`
- `research/voevodsky/results/quadratic_ims_analytic_bound.json`
- `research/grothendieck/septic-linear-windows-admit-a-smooth-quadratic-normalization.md`
