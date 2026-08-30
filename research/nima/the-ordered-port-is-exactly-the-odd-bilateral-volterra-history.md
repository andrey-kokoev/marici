# The ordered port is exactly the odd bilateral Volterra history

## Bilateral primitives

On the rapid source core, define the causal and anticausal primitives

\[
(V_-h)(q)
=
\int_{-\infty}^{q}h(v)\,dv,
\]

\[
(V_+h)(q)
=
\int_q^{\infty}h(v)\,dv.
\]

Their sum is the constant wall determined by the total mass:

\[
(V_-+V_+)h
=
\left(\int_{\mathbb R}h(v)\,dv\right)\mathbf 1.
\]

Their difference is

\[
(V_+-V_-)h(q)
=
\int_{\mathbb R}
\operatorname{sgn}(v-q)h(v)\,dv.
\]

Therefore the ordered inverse-derivative port is exactly

\[
S_{\mathrm{ord}}
=
V_+-V_-.
\]

## Relation to the relative-history splitting

The bilateral Volterra history packet uses the even and odd combinations

\[
H_{\mathrm{wall}}
=
\frac12(V_-+V_+),
\]

\[
H_{\mathrm{jump}}
=
\frac12(V_--V_+).
\]

Consequently,

\[
S_{\mathrm{ord}}
=
-2H_{\mathrm{jump}}.
\]

Thus the ordered seam port is not merely analogous to causal asymmetry. It is
the oriented-jump component of the source bilateral Volterra constructor,
with a fixed coefficient and sign.

The endpoint vectors agree:

\[
H_{\mathrm{wall}}h
\leadsto
\left(
\frac12\int h,
\frac12\int h
\right),
\]

\[
H_{\mathrm{jump}}h
\leadsto
\left(
-\frac12\int h,
\frac12\int h
\right).
\]

## Wall-killed sector

On the zero-mass subspace,

\[
\int h=0,
\]

one has

\[
V_+h=-V_-h.
\]

Hence

\[
S_{\mathrm{ord}}h
=
-2V_-h
=
2V_+h.
\]

After the constant wall is removed, the ordered port is exactly either
one-sided primitive, with the orientation selecting the sign.

This is the source-relative meaning of the inverse derivative. The apparent
choice of integration constant is carried by the wall sector and disappears
on the reduced jump carrier.

## Differential signature

Differentiation gives

\[
DV_-=I,
\qquad
DV_+=-I.
\]

Therefore

\[
DS_{\mathrm{ord}}=-2I.
\]

Integration by parts on the rapid core also gives

\[
S_{\mathrm{ord}}D=-2I.
\]

The complete inverse-derivative signature is thus inherited directly from the
bilateral history, not added as a Fourier convention.

## Curvature return

Combining this identification with

\[
S_{\mathrm{ord}}\Omega=4A
\]

gives

\[
H_{\mathrm{jump}}\Omega
=
-2A.
\]

For the even Gaussian,

\[
H_{\mathrm{jump}}\Omega f_0
=
4\pi f_2.
\]

Thus the odd bilateral history sends the connection curvature to the first
even dilation grade with an exact source coefficient.

## Half-density conjugation

The two half-density histories are conjugates of the ordinary primitives.
Reflection exchanges the two conjugators and reverses
\(H_{\mathrm{jump}}\). Therefore the identity survives on the twisted
relative graph after transporting each term through its declared
conjugation.

The transported ordered port must be regarded as a map between the two
reciprocal half-density carriers, not as one scalar endomorphism.

## Important distinction

This theorem identifies the ordered port with the primitive bilateral
Volterra history. It does not identify it with every bounded causal
convolution built from the completed theta kernel \(\Phi\).

If the shifted-history square uses a \(\Phi\)-convolution operator rather
than the primitive \(V_-\), an additional kernel-synthesis arrow remains
necessary.

The notation \(H_+\) must therefore be frozen by constructor type:

- primitive Volterra history;
- half-density-conjugated primitive history;
- or completed-theta convolution history.

Scalar endpoint agreement does not identify these operators.

## Closed gate

At the primitive relative-history level, the Hardy/causal realization is now
exact:

\[
\text{ordered port}
=
-2\times
\text{odd bilateral Volterra history}.
\]

The next source audit should inspect the shifted-history square and determine
which of the three history types its operator \(H\) actually denotes. If it
is the primitive relative history, the curvature-to-history bridge is closed.
If it is the theta convolution, kernel synthesis remains the earliest arrow.
