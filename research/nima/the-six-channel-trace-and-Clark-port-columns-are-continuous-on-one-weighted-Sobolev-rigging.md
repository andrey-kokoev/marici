# The six-channel trace and Clark port columns are continuous on one weighted Sobolev rigging

## Common test space

Choose

\[
r>\frac32,
\qquad
m>\frac32,
\]

and define

\[
\mathcal X_{r,m}
=
H^r(\mathbb R)
\cap
L^2\!\left(\mathbb R,(1+x^2)^m dx\right)
\]

with its intersection graph norm. Its continuous dual is

\[
\mathcal X_{r,m}'
=
H^{-r}(\mathbb R)
+
L^2\!\left(\mathbb R,(1+x^2)^{-m}dx\right).
\]

## Six trace bounds

The fixed-seam packet is

\[
\Gamma_6=(B_0,Q_0,M,J,A_0,C_0).
\]

All six components are continuous on `X_(r,m)`.

### Local traces

Sobolev trace gives

\[
|B_0(g)|+|M(g)|
=|g(0)|+|g'(0)|
\le C_r\|g\|_{H^r}
\]

for `r>3/2`.

### Global moments

Weighted Cauchy--Schwarz gives

\[
|Q_0(g)|+|A_0(g)|
\le C_m\|g\|_{L^2((1+x^2)^m)}
\]

for `m>1/2`, and

\[
|J(g)|
\le C_m'\|g\|_{L^2((1+x^2)^m)}
\]

for `m>3/2`.

### Principal-value channel

The distribution `pv(1/x)` has bounded Fourier multiplier proportional to
`sgn(xi)` and belongs to `H^{-r}` for every `r>1/2`. Therefore

\[
|C_0(g)|
\le C_r''\|g\|_{H^r}.
\]

Hence

\[
\Gamma_6:\mathcal X_{r,m}\to\mathbb C^6
\]

is bounded.

## Transpose columns

The six canonical source columns

\[
\delta_0,
\quad\mathbf1,
\quad-\delta_0',
\quad x,
\quad\mathbf1_{(-\infty,0]},
\quad\operatorname{pv}\frac1x
\]

all belong to `X_(r,m)'`. Thus

\[
W_6=\Gamma_6^\times:
\mathbb C^6\to\mathcal X_{r,m}'
\]

is bounded, and both moment and history Clark columns are bounded projections
of one common transpose map.

The compensator primitive

\[
K_0=-\frac12|x|+\delta_0
\]

also belongs to `X_(r,m)'`.

## Grushin graph

Let `P_loc(z)` be closed from a domain `D(P_loc) subset X_(r,m)` to
`X_(r,m)'`, equipped with its graph norm. Since the projected Clark columns
and rows are bounded, the bordered operator

\[
\mathcal G_{\rm Cl}(z)
=
\begin{pmatrix}
P_{\rm loc}(z)&-W_{\rm Cl}\\
-W_{\rm Cl}^\times&0
\end{pmatrix}
\]

is bounded from

\[
\mathcal D(P_{\rm loc})\oplus\mathbb C^2
\]

with graph norm into

\[
\mathcal X_{r,m}'\oplus\mathbb C^2.
\]

Its odd doubling is consequently a well-defined closed two-term graph
complex whenever `P_loc(z)` is closed.

## Status

Continuity of the six-channel traces, transpose columns, Clark projections,
and defect primitive is closed on one explicit rigging. The remaining analytic
input is no longer port continuity; it is the closed/Fredholm realization of
the independently defined pencil `P_loc(z)` on this same domain.