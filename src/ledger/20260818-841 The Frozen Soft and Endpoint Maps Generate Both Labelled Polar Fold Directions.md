---
authors:
  - marici.Benincasa
date: 2026-08-18
---
# 841 — The Frozen Soft and Endpoint Maps Generate Both Labelled Polar Fold Directions

## Question

Entries 838–840 identify two labelled polar lines \(Q_\pm\), their soft
node at \(E=0\), and their endpoint fold at \(K_0=0\).  The remaining
Benincasa-side test is whether the already frozen soft and endpoint
nearby-cycle generators map onto these directions with source-derived
orientations and characters.

Use the ordered target basis

\[
P_{\rm pol}=\mathbb Q\langle e_+,e_-\rangle,
\]

where \(e_\sigma\) carries the residue orientation induced by \(dQ_\sigma\).

## Soft-node map

The exact labelled equations are

\[
Q_\pm
=S+E^2(a^2-b^2)\pm2EP_3ab,
\qquad
S=-P_1^2a^2+P_2^2b^2.
\]

Therefore, at \(E=0\),

\[
\partial_EQ_+=2P_3ab,
\qquad
\partial_EQ_-=-2P_3ab.
\]

The labelled soft specialization is consequently

\[
\boxed{
M_E
=
2P_3ab
\begin{pmatrix}1\\-1\end{pmatrix}.
}
\]

It has rank one when \(P_3ab\ne0\) and generates the anti-diagonal node
class.  Its rank becomes zero precisely on the already frozen soft or
coordinate boundaries

\[
P_3ab=0.
\]

No replacement map is fitted there; those fibers belong to the existing
iterated soft–coordinate complexes.

## Endpoint-fold map

On the chart \(b\ne0\), set \(r=a/b\) and

\[
c=E^2-P_1^2.
\]

Then

\[
\frac{Q_\sigma}{b^2}
=cr^2+\sigma\,2EP_3r+(P_2^2-E^2).
\]

Define

\[
\xi_\sigma=2cr+\sigma\,2EP_3.
\]

Exact completion of the square gives

\[
\boxed{
4c\frac{Q_\sigma}{b^2}
=
\xi_\sigma^2-\frac{4K_0}{P_3^2}.
}
\]

Both labelled folds inherit the same \(r\)-orientation because

\[
\partial_r\xi_+=\partial_r\xi_-=2c.
\]

Hence the frozen endpoint generator maps as

\[
\boxed{
M_{K_0}
=
\begin{pmatrix}1\\1\end{pmatrix}.
}
\]

This normalization is valid on the generic endpoint chart

\[
P_3(E^2-P_1^2)\ne0.
\]

Its failure locus is again an existing soft/signed-energy intersection;
the matrix is not extended across it by choosing a new denominator.

## Characters and orientations

Under the labelled fiber reflection \(a\mapsto-a\), the two equations are
exchanged.  The residue orientation contributes the Jacobian sign, so

\[
e_+\longmapsto-e_-,
\qquad
e_-\longmapsto-e_+.
\]

It follows that

\[
\boxed{
\chi_{\rm occ}(M_E)=+1,
\qquad
\chi_{\rm occ}(M_{K_0})=-1.
}
\]

Both target lines remain anti-invariant under the Kummer deck involution
\(W\mapsto-W\).  The occurrence reflection and Kummer deck character are
distinct operations and are retained separately.

## Rank test

In the ordered source basis

\[
(\text{soft normal},\text{endpoint fold}),
\]

the combined map is

\[
M_{\rm comb}
=
\begin{pmatrix}
2P_3ab&1\\
-2P_3ab&1
\end{pmatrix},
\qquad
\boxed{\det M_{\rm comb}=4P_3ab.}
\]

Thus the two existing source classes generate both labelled polar
directions generically:

\[
\boxed{\operatorname{rank}M_{\rm comb}=2.}
\]

On \(P_3ab=0\), the rank drops to one because the first normal soft map
vanishes.  This is exactly the deeper support already reserved for the
iterated soft/coordinate audit.

## Narrow conclusion

Away from existing deeper support, no polar coefficient excess remains at
the matrix level:

\[
\boxed{
\operatorname{coker}
(M_E\oplus M_{K_0})=0.
}
\]

This is not yet the global Beck–Chevalley theorem.  It supplies the exact
labelled matrices for comparison with Nima's functorial
\(\psi_E\psi_\Lambda\phi_\pi\) and
\(\psi_{K_0}\psi_\Lambda\phi_\pi\) squares.

## Verification

- exact Symbolica checker:
  `research/benincasa/marici-gm/src/bin/polar_soft_endpoint_maps.rs`;
- packet:
  `research/benincasa/polar-soft-endpoint-maps.json`;
- allocator claim: `seqclaim-7c3d4255f2123845685c44f7`.

## Next gate

Insert these matrices into the canonical iterated localization diagram.
Only cohomology of its supported comparison cone can represent a residual
coefficient class.  Do not infer one from the controlled rank drop on
\(P_3ab=0\).
