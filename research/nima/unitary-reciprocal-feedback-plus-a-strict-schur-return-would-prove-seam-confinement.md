# Unitary reciprocal feedback plus a strict Schur return would prove seam confinement

The finite-rank sewing reduction isolates a particularly clean RH theorem.

Let
\[
G(z):\mathcal B\to\mathcal B
\]
be the propagated boundary return and let
\[
C:\mathcal B\to\mathcal B
\]
be reciprocal sewing. Suppose:

\[
\|G(z)\|<1
\]
for every off-seam \(z\) in the upper half-plane, and
\[
C^{*}C=I.
\]
Then
\[
\|C G(z)\|<1,
\]
so
\[
I-CG(z)
\]
is invertible by the Neumann series. Therefore the finite sewing determinant has no off-seam zeros.

If reciprocal reflection supplies
\[
G(\bar z)^{*}
\]
on the opposite sheet, the same argument excludes the lower half-plane. Possible collisions are confined to the real \(z\)-axis, which is the critical seam.

This is the scattering form of the desired theorem:

> A conservative reciprocal closure of a strictly passive arithmetic return can resonate only on the lossless boundary.

The quantitative margin is
\[
\delta_{\mathrm{return},C}
=
1-\sup_{z\in C}\|G(z)\|
\]
on every compact off-seam set \(C\). The sewing contributes no norm loss when it is unitary.

However, the expression
\[
G(z)=V^{*}(I-S(z))^{-1}U
\]
is not automatically Schur. Even when \(\|S(z)\|<1\), the resolvent may amplify, and arbitrary \(U,V\) can make \(\|G(z)\|>1\). Contractivity must come from a passive colligation containing all four blocks.

The required source object is a contractive or unitary colligation
\[
\mathfrak U
=
\begin{pmatrix}
A&B\\
C_0&D
\end{pmatrix}
:
\mathcal H_{\mathrm{state}}\oplus\mathcal B
\longrightarrow
\mathcal H_{\mathrm{state}}\oplus\mathcal B.
\]
Its transfer function has the form
\[
G(\lambda)
=
D+\lambda C_0(I-\lambda A)^{-1}B
\]
in disk coordinates, or the corresponding half-plane realization. If \(\mathfrak U\) is contractive, then
\[
I-G(\lambda)^{*}G(\lambda)\ge0.
\]
If the realization is minimal and has genuine interior dissipation, strict inequality holds off the boundary.

The transfer defect identity is the constructor certificate. In a unitary disk realization,
\[
I-G(\lambda)^{*}G(\lambda)
=
(1-|\lambda|^{2})
B^{*}(I-\bar\lambda A^{*})^{-1}
(I-\lambda A)^{-1}B,
\]
up to the convention determined by which block is the input incidence. This identifies the strict margin with observability of the boundary injection through the state evolution.

Thus the earlier five global margins can be reinterpreted as the factorized proof that the assembled colligation is strictly passive and observable:

- prime and analytic observability prevent dark state channels;
- glue transversality prevents lossless internal loops;
- diagonal observability prevents a dark common boundary mode;
- mixed angle prevents output cancellation.

The completed return contraction is their transfer-level consequence.

The reciprocal sewing must also be source-unitary in the same boundary metric:
\[
C^{*}G_{\mathcal B}C=G_{\mathcal B}.
\]
Unitary in a separately chosen metric is insufficient.

The smallest hostile has a diagonal Schur state operator \(S\) and bounded incidence maps, but the assembled block colligation is not contractive. Its transfer \(G\) crosses norm one off seam and produces a false resonance.

A second hostile has \(\|G(z)\|<1\) for each finite cutoff while
\[
\sup_X\|G_X(z_X)\|\to1
\]
on a compact off-seam set. Every finite packet is stable, but completion loses the RH margin.

The next source-native theorem is therefore:

1. assemble the prime delays, primitive injection, tail observation, and direct boundary term into one colligation;
2. prove its Green metric contractivity;
3. derive the transfer defect identity;
4. prove boundary observability gives strictness;
5. prove reciprocal sewing is unitary in the same metric;
6. identify
   \[
   \det(I-CG(z))
   \]
   with \(\xi(\tfrac12-iz)\) up to a nowhere-zero factor.

If these steps hold, the categorical tower reaches a genuine seam-confinement proof architecture: zeros are conservative feedback resonances of a strictly passive return, and such resonances cannot occur off the lossless seam.
