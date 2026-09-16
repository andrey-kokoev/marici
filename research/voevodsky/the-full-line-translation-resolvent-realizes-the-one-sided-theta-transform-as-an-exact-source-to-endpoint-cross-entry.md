# The full-line translation resolvent realizes the one-sided theta transform as an exact source-to-endpoint cross-entry

## Selfadjoint history generator

Take

\[
\mathcal H=L^2(\mathbb R,dq)
\]

and

\[
D=-i\partial_q,
\qquad
\operatorname{Dom}D=H^1(\mathbb R).
\]

Then \(D\) is selfadjoint. Endpoint evaluation

\[
E_0u=u(0)
\]

is continuous on \(H^1(\mathbb R)\), so its transpose is the rigged vector

\[
E_0^\times=
\delta_0.
\]

## Reflected theta source

Place the one-sided theta source on the negative history axis:

\[
f_-(q)
=
\mathbf1_{q<0}
\Phi(-q).
\]

Let

\[
B_f c=cf_-.
\]

For \(z\) in the upper half-plane, solve

\[
(D-z)u=f_-.
\]

The outgoing resolvent formula gives

\[
u(q)
=
i e^{izq}
\int_{-\infty}^q
 e^{-izt}f_-(t)
\,dt.
\]

At the endpoint,

\[
E_0(D-z)^{-1}B_f
=
i
\int_{-\infty}^0
 e^{-izt}
\Phi(-t)
\,dt.
\]

Changing variables \(r=-t\) yields

\[
E_0(D-z)^{-1}B_f
=
i
\int_0^\infty
\Phi(r)e^{izr}
\,dr.
\]

Therefore

\[
E_0(D-z)^{-1}B_f
=
iF(-iz).
\]

This is an exact source-to-endpoint realization of the causal theta branch.

## Two-port Weyl carrier

Use

\[
J^\times u
=
\begin{pmatrix}
\langle f_-,u\rangle\\
u(0)
\end{pmatrix}.
\]

Then

\[
M(z)
=
J^\times(D-z)^{-1}J
\]

is a two-by-two Weyl matrix. Its lower-left entry is exactly

\[
M_{21}(z)
=
iF(-iz).
\]

Because \(D\) is selfadjoint, the resolvent identity gives

\[
M(z)-M(w)^*
=
(z-
\overline w)
J^\times(D-z)^{-1}
(D-
\overline w)^{-1}J,
\]

with the conventional sign adjusted according to whether the resolvent is written as \((D-z)^{-1}\) or \((z-D)^{-1}\).

Thus the reciprocal--determinant--Green mate is exact for the causal theta branch on an admitted selfadjoint bulk generator.

## First-moment ports

Replacing the source by

\[
f_{-,1}(q)
=
(-q)
\mathbf1_{q<0}
\Phi(-q)
\]

produces

\[
E_0(D-z)^{-1}f_{-,1}
=
i
\int_0^\infty
r\Phi(r)e^{izr}
\,dr.
\]

Hence the vectors

\[
f_{-,\pm}(q)
=
(1\pm(-q))
\mathbf1_{q<0}
\Phi(-q)
\]

realize the one-sided Clark combinations \(F\mp F'\) as cross Weyl entries.

## Why this does not yet realize completed Xi

For \(\operatorname{Im}z>0\), the outgoing resolvent at \(q=0\) sees only the negative-history source. The reflected positive-history source belongs to the opposite resolvent orientation.

The completed functions combine both:

\[
F(-iz)
\quad\text{and}\quad
F(iz).
\]

A single selfadjoint resolvent chart naturally supplies one as the analytic branch and the other as its adjoint boundary chart. Their completed entire sum is a reciprocal sewing of two charts, not one resolvent matrix coefficient.

This is consistent with the earlier branch-orientation obstruction.

## Consequence

The bulk selfadjoint descriptor is no longer merely formal for the causal branch. It is the ordinary full-line translation generator with:

- negative-axis theta forcing;
- endpoint delta observation;
- first-moment source ports;
- exact resolvent/Weyl identity.

The remaining constructor is the reciprocal gluing of upper and lower resolvent charts into the completed entire determinant package while retaining the oriented cross minor.

## Disposition

The shared reciprocal--determinant--Green triangle is explicitly realized on each oriented Hardy chart. What remains for the prospective 4-simplex is chart gluing plus the incidence-chamber theorem, not construction of the local bulk generator.
