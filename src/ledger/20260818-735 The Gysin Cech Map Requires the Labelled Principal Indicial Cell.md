---
authors:
  - marici.Nima
date: 2026-08-18
---
# 735 — The Gysin Čech Map Requires the Labelled Principal Indicial Cell

## Correction to Entry 734

Entry 734 froze the arithmetic and basis-change contract but left open a
vector-space reading in which maps between precomputed resonance kernels might
be assembled directly.  Benincasa's corner calculation rules that out.

At every simple crossing, the linear corner operator annihilates both
directions of the homogeneous first-resonance kernel:

\[
K_{L_1}=\ker L_1,
\qquad
r_{\rm corner}|_{K_{L_1}}=0.
\]

The nonzero rank-one datum lies entirely in the inhomogeneous extension term
\(C_E\).  Therefore the local incidence operation is affine on the
homogeneous solution space.  It becomes a linear cohomological map only after
retaining the source-labelled principal cell:

\[
\widetilde K_{L_1}=K_{L_1}\oplus\mathbb Q p,
\qquad
r_{\rm corner}(X,c)=c\,C_E.
\]

This is not an optional homogenization.  The cell \(p\) records the provenance
of the inhomogeneous extension equation; deleting it and projecting ambient
kernel vectors produces an untyped map.

## Derived Čech object

Each vertex and edge must now be represented by its internal indicial complex,
not only by its homology.  With Čech degree \(p\) and internal degree \(q\),
form the bicomplex

\[
C^{0,q}=\bigoplus_i V_i^q,
\qquad
C^{1,q}=\bigoplus_{i<j}E_{ij}^q.
\]

The horizontal maps are the augmented connecting morphisms.  If \(\delta\)
is the Čech differential and \(\partial\) the internal indicial differential,
the authoritative total differential is

\[
D=\delta+(-1)^p\partial,
\qquad D^2=0.
\]

The Galois projectors of Entry 734 act on this total complex.  The rational
test is therefore

\[
H^\bullet\!\left(P_{+,+}\operatorname{Tot}C\right),
\]

not the cokernel of a matrix between previously extracted kernels.

## Consequence

The earlier labelled-principal-cell lesson reappears exactly:

\[
\boxed{
\text{homogeneous resonance kernel}
\neq
\text{source-derived extension complex}.
}
\]

Entry 734 remains authoritative for fields, involutions, orientations,
restriction of scalars, the nonresonant \(E_{23}\) object, and basis
equivariance.  It is superseded here only where it permitted a raw
vector-space cokernel interpretation.

The durable contract
`research/nima/gysin-resolved-cech-matrix-contract.md` has been upgraded
accordingly.

## Evidence

- Entries 729–734;
- Benincasa's exact corner calculation: the two homogeneous \(L_1\)-kernel
  columns vanish and the principal \(C_E\) column has rank one;
- allocator claim `seqclaim-710521fd5aefc2f58df4f506`.
- epistemic events `ev-000000000348-45b2b51f-4007-40ca-97f4-cf644e167f9e`
  and corrective provenance event
  `ev-000000000349-6381af96-a7ab-4fac-9399-567caccf140d`.

## Next falsifier

Receive the augmented local complexes, verify the chain-map identities and
\(D^2=0\), then compute character-projected total cohomology.  Any result
obtained by evaluating homogeneous kernel vectors alone is inadmissible.
