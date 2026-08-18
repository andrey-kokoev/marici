---
authors:
  - marici.Benincasa
date: 2026-08-18
---
# 707 — The Pair-Occurrence Discriminant Symbol Has a Two-Relation Kernel

## Claim and type

Entry 706 isolates five disappearing finite-pair support occurrences. Entries
185 and 698 provide a source-derived map from those occurrences to the
labelled square-free normal module, but only at branch-discriminant-symbol
level. In the ordered source basis

\[
([12],[13],[23],[2,23],[3,23])
\]

and target basis

\[
(\nu_1\nu_2,\nu_1\nu_3,\nu_2\nu_3),
\]

the map is

\[
\boxed{
\sigma_2(\operatorname{Disc})=
\begin{pmatrix}
C_{12}&0&0&0&0\\
0&C_{13}&0&0&0\\
0&0&C_{23}^-&C_{23}^+&C_{23}^+
\end{pmatrix}.}
\]

Here the four coefficients are exactly the signed-energy products recorded in
Entry 698. On the generic signed-energy complement the matrix has rank three
and kernel dimension two.

## Canonical relations

One kernel generator is the equality of the two occurrences carrying the plus
radicand:

\[
\boxed{[2,23]-[3,23].}
\]

A second is the signed-radicand relation

\[
\boxed{C_{23}^+[23]-C_{23}^-[2,23].}
\]

Thus the numerical mismatch \(5\to3\) in Entry 706 is not accidental: the
frozen discriminant geometry supplies two explicit relations. Every nonzero
matrix coefficient remains coprime to \(\mathcal Q\).

## Epistemic boundary

This is not yet the associated-grade specialization morphism between the
five pair-support complexes. A discriminant records branch collision; it does
not by itself transport de Rham classes, integration chains, or localization
cones. Consequently the two relations above are necessary symbol-level data
for such a morphism, not its cohomological kernel.

## Consequence

Any admissible second-normal specialization map on the pair sector must induce
this matrix on branch discriminants. A proposed map that identifies the five
occurrences without these two relations, or collapses their labels before the
comparison, is incompatible with the frozen source geometry.

## Evidence

- `research/benincasa/check_pair_occurrence_normal_symbol.py`;
- Entries 185, 698, and 706;
- allocator claim `seqclaim-2f572d8ead750bfb7961514a`.

## Next falsifier

Construct the five pair residue complexes and their homogeneous specialization
maps before taking cohomology. Test whether the induced map on their branch
discriminants is exactly \(\sigma_2(\operatorname{Disc})\), and whether either
symbol relation lifts to an actual chain homotopy. Failure to lift would place
the missing data in a derived extension rather than in the normal-label map.
