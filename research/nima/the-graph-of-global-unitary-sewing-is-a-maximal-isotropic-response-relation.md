# The graph of global unitary sewing is a maximal isotropic response relation

## Hyperbolic endpoint space

Let \(U\) be the source-input boundary space and \(U^*\) its response dual.
At each endpoint use the hyperbolic pairing

\[
h((c,r),(c',r'))
=
\langle c,r'\rangle+\langle r,c'\rangle.
\]

On the two-ended boundary space

\[
\mathcal B_\partial
=
(U\oplus U^*)_-
\oplus
(U\oplus U^*)_+,
\]

the Green flux form is

\[
\Sigma
=
-h_-\oplus h_+.
\]

For one state, this is

\[
\Sigma(\mathbf b,\mathbf b)
=
2\operatorname{Re}\langle c_+,r_+\rangle
-
2\operatorname{Re}\langle c_-,r_-\rangle.
\]

## Unitary sewing relation

Let

\[
W:U_-\longrightarrow U_+
\]

be unitary. Transport the response contragrediently:

\[
W^{-*}:U_-^*\longrightarrow U_+^*.
\]

Define

\[
\Lambda_W
=
\left\{
(c_-,r_-;c_+,r_+):
c_+=Wc_-,
\quad
r_+=W^{-*}r_-
\right\}.
\]

Then

\[
\langle c_+,r_+\rangle
=
\langle Wc_-,W^{-*}r_-\rangle
=
\langle c_-,r_-\rangle.
\]

Therefore

\[
\Sigma|_{\Lambda_W}=0.
\]

The graph has half the dimension of the doubled nondegenerate boundary space,
and its \(\Sigma\)-orthogonal complement is itself. Hence
\(\Lambda_W\) is maximal isotropic.

The same proof holds for closed Hilbert relations when \(W\) is a unitary
between object-indexed boundary fibers.

## Source sewing operator

The global Fourier--Poisson boundary cylinder already carries a unitary sewing
operator:

- every unramified observer vacuum is Fourier fixed;
- local constant--delta exchange is unitary;
- the wall--jump Hadamard frame diagonalizes its reciprocal character;
- the archimedean Tate multiplier has unit modulus on the sewing axis;
- the restricted product is unitary on the cylinder completion.

Let this operator be \(W_{\mathrm{FP}}\). Its graph supplies a canonical
maximal isotropic candidate

\[
\Lambda_{\mathrm{FP}}
=
\Lambda_{W_{\mathrm{FP}}}.
\]

No fitted boundary phase or positive bulk metric is required.

## Response termination

If a completed kernel state has boundary trace in
\(\Lambda_{\mathrm{FP}}\), then

\[
\operatorname{Re}\langle c_+,r_+\rangle
-
\operatorname{Re}\langle c_-,r_-\rangle
=
0.
\]

Inserted into the native response Green identity,

\[
2a\int|u|^2\,dq
=
-\Sigma(\operatorname{Tr}u,c,r)
\]

after the declared bulk endpoint term is included, this gives

\[
a\int|u|^2\,dq=0.
\]

For a nonzero kernel state with positive bulk norm,

\[
a=0.
\]

Thus unitary boundary sewing has exactly the maximal-isotropic force needed
for seam confinement.

## What is not yet proved

The existence of \(\Lambda_{\mathrm{FP}}\) does not prove that the response
trace of the scalar Schur kernel lies in it.

The missing comparison is

\[
\operatorname{Tr}_{\mathrm{resp}}
\mathcal D_{\mathrm{sc}}(s)^{-1}
\quad\Longrightarrow\quad
\Lambda_{\mathrm{FP}}.
\]

More concretely, one needs an intertwining square

\[
\mathcal O_{\partial,+}\operatorname{Tr}_+
=
W_{\mathrm{FP}}
\mathcal O_{\partial,-}\operatorname{Tr}_-
\]

on the complete kernel domain, with the response dual transported by
\(W_{\mathrm{FP}}^{-*}\).

Scalar functional-equation agreement verifies only one matrix coefficient of
this square. It does not place the full primitive, square, connected,
wall--jump, and response packet in the graph relation.

## Three-stratum requirement

The response \(r\) is not one ordinary Hilbert vector. Its arithmetic
components retain three modalities:

- primitive: distributional;
- square: Hilbert;
- connected: determinant-class.

Therefore \(W_{\mathrm{FP}}^{-*}\) must act continuously on the corresponding
dual/test scale, and the graph relation must be closed in the stratified
boundary topology.

A scalar restricted-product unitary is insufficient unless its transpose
actions on all three strata are constructed.

## Reciprocal sign

The wall line is reciprocal even and the jump line reciprocal odd. The
contragredient response action must retain these signs. Replacing
\(W_{\mathrm{FP}}\) by its absolute-value multiplier preserves endpoint energy
but changes the graph relation and can reverse the oriented response current.

## Completion margin

Unitary sewing itself has no norm loss. Completion stability reduces to:

1. bounded endpoint trace into the boundary cylinder;
2. closedness of the three-stratum response graph;
3. uniform equivalence of the object-indexed source boundary metrics;
4. absence of a dark kernel state with zero bulk norm.

No additional small-gain margin is needed for maximal isotropy.

## Hostiles

1. Use the graph of a merely invertible nonunitary sewing map.
2. Transport \(r\) by \(W\) instead of \(W^{-*}\).
3. Check only the scalar Tate matrix coefficient.
4. Collapse the three response strata before applying the dual sewing action.
5. Ignore the reciprocal odd sign.
6. Assume every scalar Schur kernel trace lies in the sewing graph.

## Verdict

The global Fourier--Poisson unitary already determines a canonical maximal
isotropic response relation: its graph with contragredient dual transport.

The remaining RH-bearing arrow is no longer construction of an isotropic
boundary relation. It is the full response-trace intertwining theorem placing
every completed scalar-kernel state in that graph.
