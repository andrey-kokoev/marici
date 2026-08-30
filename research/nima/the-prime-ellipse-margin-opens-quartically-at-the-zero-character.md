# The prime ellipse margin opens quartically at the zero character

The exact pairwise-square identity from event 10293 determines the
small-character asymptotic of the ellipse deficit.

Let

\[
\mathcal D(t,\xi)
=
1-\frac{R(t,\xi)^2}{M_0(t)^2}
-\frac{I_1(t,\xi)^2}{M_0(t)M_2(t)}.
\]

For \(x_n=\log n\),

\[
\sin(\xi x_n)
=
\xi x_n-\frac{\xi^3x_n^3}{6}+O(\xi^5x_n^5),
\]

\[
\cos(\xi x_n)
=
1-\frac{\xi^2x_n^2}{2}
+\frac{\xi^4x_n^4}{24}
+O(\xi^6x_n^6).
\]

In the pairwise decomposition,

\[
x_m\sin(\xi x_n)-x_n\sin(\xi x_m)
=
-\frac{\xi^3}{6}
x_mx_n(x_n^2-x_m^2)
+O(\xi^5),
\]

so the sine-slope incompatibility begins at order \(\xi^6\).

The cosine incompatibility begins earlier:

\[
\cos(\xi x_m)-\cos(\xi x_n)
=
-\frac{\xi^2}{2}(x_m^2-x_n^2)
+O(\xi^4).
\]

Therefore

\[
\mathcal D(t,\xi)
=
\frac{\xi^4}{4M_0(t)^2}
\sum_{m<n}
c_m(t)c_n(t)
(x_m^2-x_n^2)^2
+
O_t(\xi^6).
\]

Using the pairwise variance identity,

\[
\sum_{m<n}c_mc_n(x_m^2-x_n^2)^2
=
M_0M_4-M_2^2,
\]

one obtains the exact leading coefficient

\[
\mathcal D(t,\xi)
=
\frac{
M_0(t)M_4(t)-M_2(t)^2
}{
4M_0(t)^2
}
\xi^4
+
O_t(\xi^6).
\]

Since the prime-power log squares are not constant,

\[
M_0M_4-M_2^2>0.
\]

Thus the strict ellipse margin opens quartically, not quadratically, away
from \(\xi=0\).

## Contact consequence

A uniform nonzero-character margin cannot simply be extended through the
zero character. Near \(\xi=0\), the available prime incompatibility budget is

\[
\delta_{\mathrm{prime}}
\sim
\frac{M_0M_4-M_2^2}{4M_0^2}\xi^4.
\]

Therefore exclusion of near-zero double contacts requires comparing the
archimedean contact ratio through fourth order in \(\xi\). A second-order
Taylor audit is structurally incapable of seeing the first prime deficit.

The character regions should be split into:

1. \(\xi=0\): exact scalar heat-positivity gate;
2. \(0<|\xi|\le\xi_0\): quartic jet comparison using \(M_0,M_2,M_4\);
3. \(\xi_0\le|\xi|\le X\): finite-pair compact margin;
4. \(|\xi|>X\): character coercivity.

This is a sharper finite attack plan than treating all nonzero characters
uniformly.

## Constructor interpretation

At \(\xi=0\), all prime characters share the same coherent phase, so both the
value and first-order disagreement observers are dark. The first surviving
glue defect is the variance of \((\log n)^2\), encoded by

\[
M_0M_4-M_2^2.
\]

Hence the zero-character tangent is a fourth-order contact of the prime phase
cell. This explains why the curvature covariance gate in Grothendieck’s
moment analysis is the first nontrivial local refinement beyond value and
slope.
