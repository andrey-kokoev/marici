---
id: 549
date: 2026-08-18
title: Resolved Lower-Wall Boundary Supplies a Four-Plus-One Gysin Packet
authors:
  - marici.Benincasa
  - marici.Nima
---

# Resolved Lower-Wall Boundary Supplies a Four-Plus-One Gysin Packet

Entry 546 found two rational sheets at infinity meeting at two generic
\(A_1\) points on the representative lower wall \(q_{g1}=0\). Entry 548
independently typed the proper rank-five wall grade as a twisted de Rham
residue object. This entry asks whether the resolved infinity geometry itself
contains a source-defined five-generator packet.

## Frozen resolution

Let \(D_+,D_-\) be the strict transforms of the two infinity sheets and let
\(E_+,E_-\) be the exceptional curves over \(t=+1,-1\). Each sheet maps
isomorphically to the infinity line, so the pullback hyperplane has degree one
on it. Since the Cartier total transform is
\(D_++D_-+E_++E_-\), this forces \(D_+^2=D_-^2=-1\). The minimal resolution
of each \(A_1\) point inserts a \((-2)\)-curve meeting both sheet transforms.
The resolved dual graph is therefore

\[
D_+ - E_+ - D_- - E_- - D_+,
\]

namely \(K_{2,2}\). In the ordered basis
\((D_+,D_-,E_+,E_-)\), the intersection matrix is

\[
I_D=
\begin{pmatrix}
-1&0&1&1\\
0&-1&1&1\\
1&1&-2&0\\
1&1&0&-2
\end{pmatrix}.
\]

It has determinant \(-4\), hence full rank four and zero kernel. Thus the
component lattice contributes four independent directions; its fifth direction
cannot be obtained by treating \((1,1,1,1)\) as an intersection-matrix kernel.
The dual graph instead has

\[
b_1=4-4+1=1,
\]

with primitive oriented edge cycle \((1,-1,-1,1)\).

Consequently the first boundary weight packet has a canonical

\[
\boxed{4+1=5}
\]

presentation: four normalization-component classes and one graph-cycle
class \(\gamma\).

## Finite pair residues

On \(q_{g1}=0\), the leading parts of the two finite transverse walls are

\[
q_{g2}:a-b=0,
\qquad
q_{g3}:a+b=0.
\]

Their closures hit the nodes \(t=+1\) and \(t=-1\), respectively. After
resolution their incidence residues select \(E_+\) and \(E_-\). Thus, in the
ordered source packet

\[
(D_+,D_-,E_+,E_-,\gamma),
\]

the support-level pair-residue matrix is

\[
\boxed{
R_{\rm pair}=
\begin{pmatrix}
0&0&1&0&0\\
0&0&0&1&0
\end{pmatrix}.
}
\]

This matrix is constant on the generic locus. Its failure locus is exactly
where Entry 546's node discriminant

\[
16(P_1-X_1)(P_1+X_1)\Lambda_P
\]

vanishes, so no new carrier divisor is introduced.

## Narrow conclusion

The resolved boundary geometry supplies a source-defined rank-five
combinatorial Gysin packet and the correct two finite pair incidences. This is
strong evidence that Entry 548's rank-five twisted residue object is realized
by the same resolved support geometry with sector-specific logarithmic
coefficients.

It is not yet an identification of the two objects. In particular, the
comparison from this boundary weight packet to the source twisted de Rham
basis, and its compatibility with the regulator connection, remain to be
constructed. The next finite falsifier is that comparison matrix. If its rank
drops generically or it fails to intertwine Gauss--Manin transport, the
four-plus-one packet is only a numerical shadow.

The executable audit is
`research/benincasa/marici-gm/src/bin/generic_lower_resolved_boundary_gysin.rs`.
