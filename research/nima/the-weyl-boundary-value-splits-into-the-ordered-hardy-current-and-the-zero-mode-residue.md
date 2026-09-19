# The Weyl boundary value splits into the ordered Hardy current and the zero-mode residue

## Rigged spectral boundary value

Let

\[
A=iD
\]

be the self-adjoint bilateral history generator, and let `B_theta` be the
weighted interior theta-profile synthesis. On the metaplectic test core and
its strong dual, the resolvent has the distributional boundary values

\[
(A-(x+i0))^{-1}
=
\operatorname{pv}(A-x)^{-1}
+i\pi\delta(A-x),
\]

\[
(A-(x-i0))^{-1}
=
\operatorname{pv}(A-x)^{-1}
-i\pi\delta(A-x).
\]

The signs follow from

\[
\frac1{t-x\mp i0}
=
\operatorname{pv}\frac1{t-x}
\pm i\pi\delta(t-x).
\]

Therefore the theta Weyl function has boundary values

\[
M_{\theta,\pm}(x)
=
B_\theta^*\operatorname{pv}(A-x)^{-1}B_\theta
\pm i\pi B_\theta^*\delta(A-x)B_\theta.
\]

Its mean and jump are

\[
\frac12(M_{\theta,+}+M_{\theta,-})
=
B_\theta^*\operatorname{pv}(A-x)^{-1}B_\theta,
\]

\[
M_{\theta,+}-M_{\theta,-}
=
2\pi i B_\theta^*\delta(A-x)B_\theta.
\]

Thus the seam naturally has two separately typed coordinates: principal
value and spectral residue.

## Ordered port at zero frequency

At `x=0`, Fourier transformation diagonalizes `A`. With the convention in
which `D` has multiplier `i xi`, `A=iD` has multiplier `-xi`; the harmless
orientation sign is fixed by the chosen Fourier chart. The principal-value
inverse of `A` is therefore the inverse-frequency distribution.

Since

\[
S=-2D^{-1},
\]

one obtains, after applying the chart orientation,

\[
S
\longleftrightarrow
2i\operatorname{pv}\!\left(\frac1\xi\right).
\]

Consequently the mean Weyl boundary coordinate at zero is exactly the
ordered Hardy current, up to the already frozen factor `-2` converting the
resolvent inverse into `S`:

\[
B_\theta^*SB_\theta
=-2i\,
B_\theta^*\operatorname{pv}(A^{-1})B_\theta
\]

with sign adjusted to the `A=iD` Fourier convention.

## Zero-mode residue

The spectral atom

\[
\delta(A)
\]

projects distributionally onto the zero-frequency mode. For a radial source
`g`, its coefficient is proportional to

\[
\widehat g(0)=\int_{\mathbb R}g(q)\,dq.
\]

This is the same datum carried by the opposite endpoint constants of the
ordered primitive:

\[
(Sg)(-\infty)=\int g,
\qquad
(Sg)(+\infty)=-\int g.
\]

Hence

\[
B_\theta^*\delta(A)B_\theta
\]

is the zero-mode/endpoint Gram coordinate. It is not an arbitrary delta term
that may be added to the odd principal-value multiplier. Reciprocal oddness
fixes the ordered operator, while the delta channel remains a separate even
boundary coordinate exchanged with the constant wall under Fourier
transport.

## Reciprocal orientation

Reflection sends the inverse-frequency principal value to its negative and
fixes the zero spectral atom. Therefore the two boundary coordinates carry
different reciprocal characters:

\[
R:\text{PV}\mapsto-\text{PV},
\qquad
R:\delta(A)\mapsto\delta(A).
\]

This reproduces the odd tail--Hardy plane and even constant--delta plane of
the five-component Fourier tail cell.

## Labelled completion

For finite prime/grade cutoffs the compressed formulas are exact matrix-valued
distribution identities. On the projective ordered source core, both
coordinates are continuous:

- the principal-value coordinate through the saturated ordered graph;
- the residue coordinate through the retained mass/endpoint trace.

Cutoff convergence of `B_theta` therefore passes the identities to the
completed strong dual without combining the two channels.

## Result

The off-seam theta Weyl gamma-field has a canonical generalized boundary
value whose:

1. mean is the ordered Hardy principal-value current;
2. jump is the zero-frequency spectral residue;
3. residue is the retained endpoint/constant-wall packet;
4. reciprocal characters agree with the five-component Fourier tail cell.

The remaining coupling question is no longer identification of the seam
coordinates. It is whether the native wall boundary relation and this
interior Weyl boundary value satisfy the complete conservative Green
relation on the faithful joint graph, including the arithmetic backreaction
row.
