# The source star constructs the opposite-polarity dagger on minimal generated feature carriers

## Objective

Construct the first missing symmetry cell

\[
\dagger:
\mathcal C_{semi}^+
\to
(\mathcal C_{semi}^-)^{op}
\]

without assuming the unresolved positive tetrahedral filler.

The correct unconditional domain is the source-generated Schur--defect feature carrier. Descent to a defect-absorbed positive quotient remains conditional on Douglas acceptance.

## Source star

Let

\[
\iota_r:E_r\to E_r
\]

be the convolution involution

\[
\iota_r(p)=p^*.
\]

It is antilinear, involutive, and reverses products:

\[
\iota_{r+s}(p*q)
=
\iota_s(q)*\iota_r(p).
\]

In the centered Mellin coordinate, its analytic action is

\[
m_{p^*}(z)
=
\overline{m_p(-\bar z)}.
\]

Thus it exchanges the two endpoint evaluations.

## Endpoint dagger

Define

\[
J_\partial
\begin{pmatrix}u_+\\u_-\end{pmatrix}
=
\begin{pmatrix}\overline{u_-}\\\overline{u_+}\end{pmatrix}.
\]

Then

\[
J_\partial^2=I
\]

and

\[
\beta_r\iota_r
=
J_\partial\beta_r.
\]

In the even/odd endpoint basis, \(J_\partial\) is ordinary conjugation on the even line and minus conjugation on the odd line. Hence it preserves endpoint parity and its metric sign.

## Kernel conjugation

Let \(q\in\{S,B\}\) denote the Schur and Blaschke feature types. Their opposite-polarity kernels satisfy the source reflection identity

\[
k_q^-(z,w)
=
\overline{k_q^+(-\bar w,-\bar z)}.
\]

Consequently the source pullback Grams obey

\[
\left\langle
A_{q,r}^-p^*,
A_{q,r}^-q^*
\right\rangle
=
\overline{
\left\langle
A_{q,r}^+p,
A_{q,r}^+q
\right\rangle
}.
\]

This identity is algebraic for finite kernel packets and extends to the completed generated ranges by continuity.

## Minimal feature dagger

On the algebraic source-generated range, define

\[
D_{q,r}(
A_{q,r}^+p)
=
A_{q,r}^-p^*.
\]

The Gram identity shows that this map is well defined and anti-isometric. It therefore extends uniquely to an antiunitary

\[
D_{q,r}:
\overline{\operatorname{ran}A_{q,r}^+}
\to
\overline{\operatorname{ran}A_{q,r}^-}.
\]

Applying the construction twice gives

\[
D_{q,r}^-D_{q,r}^+=I
\]

on the minimal generated feature carrier.

For the full Krein--Langer feature, set

\[
D_r^{KL}
=
D_{S,r}
\oplus
D_{B,r}.
\]

It commutes with the fundamental symmetry

\[
I\oplus(-I).
\]

After adjoining endpoints, use

\[
D_r^{aug}
=
D_r^{KL}
\oplus
J_\partial.
\]

This is the unconditional opposite-polarity dagger on the complete signed feature.

## Edge reversal

Let

\[
d_{ij}^+
\]

be a source-generated edge map. Define its negative mate by

\[
d_{ji}^-
=
D_i
d_{ij}^{+*}
D_j^{-1},
\]

with the source and target reversed.

Then

\[
(d_{ij}^+)^\dagger
=d_{ji}^-.
\]

Because each \(D_i\) is antiunitary, dagger reverses composition:

\[
(gf)^\dagger
=f^\dagger g^\dagger.
\]

## Face homotopies

For a positive-polarity face homotopy

\[
H_{ijk}^+:
d_{jk}^+d_{ij}^+
\Rightarrow
d_{ik}^+,
\]

define

\[
H_{kji}^-
=
(H_{ijk}^+)^\dagger.
\]

The source reflection identity ensures that this definition agrees with the independently computed signed pullback on the analytic core.

Thus the negative face is not a second choice on the minimal generated carrier. It is the dagger mate of the positive face.

## Tetrahedral modification

Apply dagger to the positive tetrahedral pasting equation. Contravariance reverses the order of every whiskered composite and reverses the orientation of the tetrahedron.

Because dagger is involutive, the resulting equation is exactly the negative-polarity tetrahedral equation. Therefore the modification

\[
K^-
=(K^+)^\dagger
\]

is coherent whenever \(K^+\) is defined.

At the signed level, where the four face homotopies already exist, this constructs the opposite tetrahedron and its meeting along Hermitian polarization.

## Left and right convolution successors

The source star does not preserve a chosen left-successor convention by itself. Define

\[
L_a^{(r)}p=a*p
\]

and

\[
R_a^{(r)}p=p*a.
\]

Then

\[
\iota_{r+s}L_a^{(r)}
=
R_{a^*}^{(r)}\iota_r.
\]

Hence dagger exchanges left convolution successors with right convolution successors.

On a commutative convolution source, \(L_a=R_a\), and this reduces to the familiar successor-polarity square. In a noncommutative source, retaining both successor orientations is necessary for correct typing.

## Successor interchange

Let \(D_{a,q}^{L,+}\) and \(D_{a^*,q}^{R,-}\) be the target mates of the left and right successors. On generated feature vectors,

\[
D_{q,r+s}
D_{a,q}^{L,+}
=
D_{a^*,q}^{R,-}
D_{q,r}.
\]

The equality follows by applying both sides to \(A_{q,r}^+p\) and using the source star identity. Density extends it to completed generated ranges.

This is the required successor--polarity interchange homotopy. It is strict on the minimal source-labelled model.

## Aperture compatibility

The reflection

\[
z\mapsto-\bar z
\]

preserves every centered inner strip. Therefore the feature daggers commute with aperture restriction and define a dagger on the projective graph completion.

No endpoint limiting argument is needed for this compatibility because the endpoint graph is retained as an independent summand.

## Conditional descent to the positive quotient

Suppose both polarities are Douglas accepted and let

\[
C_r^+A_{S,r}^+
=A_{B,r}^+.
\]

Dagger transports this contraction to

\[
C_r^-
=
D_{B,r}C_r^+D_{S,r}^{-1}.
\]

It remains contractive because the \(D\)'s are antiunitary. Moreover,

\[
C_r^-A_{S,r}^-
=A_{B,r}^-.
\]

Thus acceptance of one polarity implies acceptance of the opposite polarity, and the absorbed positive quotients are dagger equivalent.

If Douglas acceptance fails, dagger still exists on the full signed Krein feature but does not create a positive quotient.

## Physical comparison boundary

The construction is canonical on minimal source-generated feature carriers. An independently completed physical prolate or Clifford carrier may contain orthogonal summands not reached by the source.

Extending dagger to those summands requires an additional choice unless their physical symmetry operator is already specified. Equality of source pullback Grams determines the dagger only on the generated subspace.

Therefore this construction does not yet identify the abstract dagger with a physical ambient antiunitary outside the source-generated closure.

## Result

The opposite-polarity symmetry is now defined on the completed minimal carriers:

1. source star gives the contravariant involution;
2. endpoint exchange gives its boundary mate;
3. kernel reflection gives antiunitary Schur and defect daggers;
4. edge maps reverse by adjoint conjugation;
5. face homotopies and tetrahedral modifications are transported by dagger;
6. left successors are exchanged with right successors;
7. aperture and graph completions are preserved;
8. accepted positive quotients inherit the dagger automatically.

## Remaining symmetry cell

What remains is not the opposite-polarity dagger itself. It is comparison with independently completed physical symmetry operators on any source-orthogonal ambient summands, together with the common-positive-bulk condition needed to fill the full polarity cube.
