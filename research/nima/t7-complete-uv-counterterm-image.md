# The complete frozen T7 residual is ultraviolet counterterm data

The supported logarithmic/Cut-nearby cospan leaves a two-dimensional quotient,
detected in the frozen frame by

\[
r_1=e_1^\vee,
\qquad
r_2=e_2^\vee-e_4^\vee+180v_{\rm alg}^\vee.
\]

The leading quartic divergence gives a mixed residual counterterm vector

\[
c_4=(1,\kappa),
\]

where the exact value of \(\kappa\) is immaterial here.  It is nonzero in the
first coordinate.

There is a second, lower-grade direction.  Put the loop momentum origin on the
edge occurring in

\[
q_{\mathcal G_{12}}=E+y_{12}.
\]

For a fixed vector \(p\), the exact three-dimensional angular asymptotic is

\[
\left\langle |r n+p|\right\rangle_{S^2}
=r+\frac{|p|^2}{3r}+O(r^{-3}).
\]

At the frozen total-energy fiber \(E=0\), this gives

\[
\int^{\Lambda}d^3l\,
\frac{y_{23}-y_{31}}{y_{12}}
=\frac{x^2-y^2}{3}\Lambda+O(\log\Lambda).
\]

Meanwhile the algebraic generator has coefficients

\[
A=(x^2-y^2)x^2y^2,
\quad B=2x^2y^2,
\quad C=-2x^2y^2
\]

on \((e_7,e_8,e_9)\).  Since

\[
\langle |rn+p|^2\rangle=r^2+|p|^2
\]

and \(B+C=0\), its angularly averaged numerator is constant.  It contributes
a quadratic divergence but no linear divergence.  Therefore, at \((x,y)=(2,3)\),

\[
c_1=(0,-5/3).
\]

Consequently

\[
\operatorname{rank}\langle c_4,c_1\rangle=2.
\]

Thus the whole two-dimensional residual of the frozen supported cospan is
occupied by UV subtraction directions.  After quotienting by the full
subtraction image, no bulk-period class remains:

\[
\boxed{\dim R_{\rm after\ full\ UV\ subtraction}=0.}
\]

This does not yet prove that both directions are admissible local cosmological
counterterms.  Their locality and symmetry typing is the next gate.  Conditional
on that gate, finite constants require renormalization conditions or physical
input and are not predicted by the supported cospan alone.  The earlier
rank-one upper bound is sharpened to zero after full UV subtraction on this
frozen source-normalized fiber.

The exact audit is
`research/nima/checkers/check_t7_complete_uv_counterterm_image.py`.
