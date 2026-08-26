# The third theta quarter-turn freezes source and endpoint as two ports

## Status

Exact correction and finite hostile theorem. The failed one-port equality is
retained as evidence that forcing and endpoint observation are distinct source
ports. Their natural completion is a two-port Weyl matrix. A cross-transfer
entry of a selfadjoint system can have nonreal zeros, so selfadjointness of the
fixed history Dirac core does not by itself imply RH.

## Fixed first and second layers

Keep the history Dirac core

\[
D_H
=
\begin{pmatrix}
0&H^*\\
H&0
\end{pmatrix}
\]

fixed.

Keep the feedback-extension architecture fixed as well: a scalar
characteristic function becomes spectral only when its input and output ports
are adjoints.

For the currently derived theta node, Grothendieck's exact port audit gives

\[
b_fc=cf
\]

and

\[
b_f^*G=\langle f,G\rangle,
\]

whereas the scalar Evans observation is

\[
\ell_0G=G(0).
\]

The residual

\[
R_{\mathrm{port}}
=
\ell_0-b_f^*
\]

is nonzero. Compactly supported interior states and endpoint-supported graph
states separate the two functionals exactly.

## Rotate the mismatch into a second port

Do not fit a metric to identify \(\ell_0\) with \(b_f^*\). Instead retain two
typed ports:

1. the forcing port \((b_f,b_f^*)\);
2. the endpoint port \((b_0,b_0^*)\), where \(b_0^*=\ell_0\) in the appropriate
   rigged boundary pairing.

Assemble

\[
B=
\begin{pmatrix}
b_f&b_0
\end{pmatrix}.
\]

The natural boundary object is the matrix-valued Weyl function

\[
W(\lambda)
=
A-\lambda I
-
B^*(D_H-\lambda)^{-1}B,
\]

with a source-derived Hermitian direct term \(A\).

Its entries include:

- forcing self-response;
- endpoint self-response;
- source-to-endpoint transfer;
- endpoint-to-source transfer.

The scalar completed theta readout is naturally a candidate cross-transfer
entry, not automatically the determinant of \(W\).

## Port-space quarter-turn

A unitary change of port coordinates

\[
B\longmapsto BU
\]

acts by

\[
W(\lambda)\longmapsto U^*W(\lambda)U.
\]

The eigenvalues and determinant of \(W\) are invariant under this rotation.
An individual off-diagonal entry is not.

The source may canonically freeze the forcing and endpoint axes, making their
cross-entry meaningful. But selfadjointness of the internal operator constrains
the full matrix-valued function, not the zero set of one chosen cross-entry.

## Exact selfadjoint hostile

Take the selfadjoint matrix

\[
D=
\begin{pmatrix}
-1&0\\
0&1
\end{pmatrix}.
\]

Choose two source-fixed port vectors

\[
b_f=\binom{1}{1},
\qquad
b_0=\binom{1}{-i}.
\]

The source-to-endpoint cross resolvent is

\[
m_{0f}(z)
=
b_0^*(D-z)^{-1}b_f
=
\frac1{-1-z}
+
\frac{i}{1-z}.
\]

Its numerator vanishes at

\[
z=-i.
\]

Thus a cross-transfer entry of an exactly selfadjoint finite system can have a
strictly nonreal zero. The reciprocal cross-entry has the conjugate zero.

This hostile preserves:

- a selfadjoint internal operator;
- adjoint closure of each individual port;
- finite-dimensional exactness;
- reciprocal conjugation between cross entries.

It falsifies the claim that selfadjointness alone confines zeros of a
source-to-detector amplitude.

## Full matrix positivity is insufficient for a cross-entry

For selfadjoint \(D_H\), the matrix resolvent has the standard half-plane
orientation. Its imaginary part is a positive matrix-valued Gram with the
appropriate sign convention. This controls

\[
v^*W(\lambda)v
\]

for a common port vector \(v\). It does not prevent

\[
e_0^*W(\lambda)e_f=0
\]

for two distinct port directions.

This is the operator version of the earlier geometric-algebra observation: a
scalar pairing can vanish while the full oriented relationship remains
nonzero.

## Three surviving ways forward

### Source-derived port collapse

Prove that forcing and endpoint ports are the same ray after the complete
arithmetic boundary construction:

\[
b_0=\rho b_f,
\qquad
\rho\ne0.
\]

The current compact-support hostile disproves this for the present node. A
larger boundary carrier would need to derive the identification.

### Determinant promotion

Prove that the completed scalar section is a zero-free factor times the
invariant determinant

\[
\det W(\lambda),
\]

not merely a cross-entry. Determinant equality must preserve lower
determinantal ideals and kernel profiles.

### Exterior-power readout

Retain the two-port relationship as an exterior product. The invariant
quantity is then a determinant-line section rather than a scalar dot product.
Its source construction must precede any zero comparison.

## Third-round fixed object

After this rotation, the object to hold fixed is

\[
(D_H,B,A,W),
\]

where \(D_H\) is the history Dirac core, \(B\) contains both typed ports, \(A\)
is the direct boundary relation, and \(W\) is the full matrix Weyl function.

The scalar cross-entry is a projection of this object and must not replace it.

## Finite compiler

At cutoff \(X\), construct

\[
B_X=
\begin{pmatrix}
b_{f,X}&b_{0,X}
\end{pmatrix}
\]

and

\[
W_X(\lambda)
=
A_X-\lambda I
-
B_X^*(D_{H,X}-\lambda)^{-1}B_X.
\]

Test separately:

1. selfadjointness of \(D_{H,X}\);
2. Hermiticity of \(A_X\);
3. adjoint closure of each port;
4. port rank and observability;
5. the cross-entry comparison with the scalar theta readout;
6. the determinant comparison;
7. lower determinantal ideals and Smith profile;
8. completion stability and essential-spectrum type.

## Falsifiers

The determinant route fails if:

1. the theta scalar matches only a cross-entry;
2. determinant equality hides different lower-minor profiles;
3. the required direct term \(A_X\) is fitted from zeros;
4. port rank collapses under completion;
5. hostile signed prime data preserve the same determinant relation;
6. the determinant zero is a threshold singularity rather than an eigenstate.

The port-collapse route fails upon any nonzero component of

\[
b_{0,X}-\rho_Xb_{f,X}
\]

outside the authorized source ray.

## Verdict

The failed equality \(\ell_0=b_f^*\) should be fixed in place as a structural
fact: theta forcing and endpoint observation are distinct ports. The third
quarter-turn promotes their scalar interaction to a full two-port Weyl matrix.
This exposes a decisive no-go: cross-transfer zeros are not confined by
selfadjointness. Any surviving RH mechanism must promote the completed scalar
from a cross-entry to an invariant determinant/exterior section, or derive a
new source law collapsing the two ports.
