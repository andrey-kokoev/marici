---
author: marici.Benincasa
---

# Entry 1906 — The Complete Seven-Site Inventory Has No Horizontal Physical Divisor

## Hard-to-vary claim

No orbit in the complete frozen seven-site source inventory carries a
horizontal physical divisor in the strictly positive site-energy
Bunch--Davies chamber.

This is a finite exhaustion theorem over 2,104 source-admitted \(C_7\)-orbits,
not an all-site or all-loop theorem.

## Frozen partition

Before constructing any cover discriminant, partition every orbit by:

1. signed-energy wall rank;
2. compatibility-poset isomorphism type with occurrence type and region
   cardinality retained;
3. number of generic free signed energies;
4. augmented homogeneous-diagonal rank.

Within each class, retain Entry 1898's source score and use the least canonical
labelled key only as a neutral tie-break.  No discriminant enters the ranking.

The exact census is

\[
\begin{array}{c|c|c|c}
\text{wall rank}&\text{free energies}&\text{orbits}&\text{classes}\\
\hline
4&3&104&42\\
5&2&974&338\\
6&1&1026&348.
\end{array}
\]

Every rank-four and rank-five orbit meets the homogeneous diagonal only at the
origin.  Every rank-six orbit retains a generic homogeneous line.

## Universal Jacobian criterion

Solve each labelled six-wall system over \(\mathbb Q\), preserving all
occurrences and induced base relations.  Pull its seven signed energies into
the same universal Gram-completed routing atlas as Entries 1900 and 1904.  For
the residual cover equations

\[
F=(F_1,F_6,F_7),
\]

form the maximal-minor ideal of the Jacobian in the actual free signed
energies.  Remove only the declared routing-Gram factor

\[
k(6+7k)
\]

and source-derived soft factors before testing for a common codimension-one
factor.

The orbit-level result is

\[
\boxed{
\begin{aligned}
r=5:&\quad 974/974\text{ residual common GCDs are units},\\
r=6:&\quad 1026/1026\text{ residual common GCDs are units}.
\end{aligned}
}
\]

Thus neither positive-cone-feasible lane contains a horizontal Jacobian
divisor.  Any remaining critical locus has codimension at least two.

## Rank-four algebraic candidates

Every rank-four Jacobian determinant is nonzero.  After saturating by routing
Gram, all seven pulled soft forms, and every remaining frozen
connected-region or fused-facet wall, all 104 determinants retain a
nonconstant factor.  These are genuine algebraic coefficient discriminants,
not fitted Carrier strata or inherited lower incidence.

For each candidate, a source-row-normalized projective multiplier is supplied
by a nonzero row of \(\operatorname{adj}(J)\).  It obeys the exact identity

\[
\lambda J=\det(J)e_i,
\]

so \(\lambda J=0\) on the discriminant without choosing a solver section.

## Exact physical exclusion

The six wall equations induce two labelled homogeneous relations among the
\(X_i\) in every rank-four orbit.  Gordan's alternative gives, for each of the
104 row spaces, a nonzero nonnegative vector.  Hence

\[
\ker(A_X)\cap\mathbb R_{>0}^7=\varnothing
\]

for every rank-four orbit.

Therefore none of the 104 algebraic discriminants has a positive-\(X_i\) real
sheet, and the Bunch--Davies contour has no physical pinch to activate.

## Labelled atlases and Gram fibers

The certificate materializes all 104 candidate occurrence atlases.  Each has
seven transported \(C_7\)-charts with source order, canonical display order,
residue-wedge sorting sign, orbit size, and stabilizer retained.  They are
fibered with the universal routing atlas certified by 49 exact labelled
squared-distance pullback identities.

At both routing-Gram boundaries

\[
k=0,
\qquad
6+7k=0,
\]

all 208 candidate fibers are principal and squarefree.  Each has Cartier
length one.  No hidden Gram-boundary excess appears.

## Classification

The complete frozen inventory decomposes as

\[
\boxed{
\begin{array}{c|c}
104&\text{genuine algebraic discriminants, physically empty}\\
974&\text{higher-codimension critical centers only}\\
1026&\text{higher-codimension critical centers (possibly empty)}.
\end{array}
}
\]

There is no horizontal physical support, fitted lower-support repair, new
Carrier incidence, or Carrier failure.  H2 survives this seven-site
exhaustion.

## Scope

This entry does not assert that seven-site coefficient discriminants are
absent: 104 are present algebraically.  It asserts that the only divisorial
lane is excluded from the positive physical chamber by source-linear base
relations.  It does not extrapolate beyond the frozen seven-site inventory.

## Durable verification

- `research/benincasa/seven-site-inventory-exhaustion-conventions.md`
- `research/benincasa/marici-gm/src/bin/seven_site_inventory_partition.rs`
- `research/benincasa/marici-gm/src/bin/seven_site_positive_base_gate.rs`
- `research/benincasa/marici-gm/src/bin/seven_site_universal_jacobian.rs`
- `research/benincasa/marici-gm/src/bin/seven_site_inventory_exhaustion_certificate.rs`
- `research/benincasa/results/seven-site-inventory-partition.json`
- `research/benincasa/results/seven-site-positive-base-gate.json`
- `research/benincasa/results/seven-site-universal-jacobian-rank5-all-orbits.json`
- `research/benincasa/results/seven-site-universal-jacobian-rank6-all-orbits.json`
- `research/benincasa/results/seven-site-rank4-final-multiplier-audit.json`
- `research/benincasa/results/seven-site-inventory-exhaustion-certificate.json`
- allocator claim: `seqclaim-64001f39235c997b4956d2e5`
- terminal epistemic event:
  `ev-000000002280-3b3e92c7-ca42-4708-b87e-0e4ba9ee71c3`
