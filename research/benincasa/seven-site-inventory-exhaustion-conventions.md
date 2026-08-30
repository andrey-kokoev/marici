# Seven-site inventory exhaustion conventions

## Frozen question

Determine whether the absence of horizontal physical support in Entries 1900
and 1904 persists across the complete frozen seven-site source inventory.  The
inventory is

`research/benincasa/results/seven-site-full-source-inventory.json`.

No facet, occurrence, support summand, normalization, or Carrier cell may be
added after inspecting a cover discriminant.

## Predeclared partition

Every labelled \(C_7\)-orbit is assigned to exactly one class using:

1. the rank \(r\) of its six signed-energy wall rows;
2. the isomorphism type of the six-object compatibility structure, retaining
   region/fused-facet type, region cardinality, inclusion, disjointness, and
   overlap;
3. the number \(7-r\) of generic free signed energies (and therefore generic
   free loop-square variables before squaring);
4. the augmented rank obtained by adjoining the homogeneous site-energy
   coefficient.

The homogeneous diagonal is classified as `generic_homogeneous_line` exactly
when augmented rank equals wall rank, and as `origin_only` otherwise.

This partition is computed before any cover, Jacobian, resultant, Gram
saturation, or real-sheet calculation.

## Predeclared representative ranking

Within each class, maximize the frozen Entry 1898 score

\[
(\text{wall count},\text{nesting depth},
\text{separated region pairs},|C_7\text{-orbit}|),
\]

then select the lexicographically least canonical labelled key.  A tie is
reported, not interpreted as a complexity distinction.  The discriminant is
not consulted.

## Universal Jacobian gate

For each wall system, solve the labelled linear wall equations over the
generic \(X_i\) base without identifying occurrences.  Pull the seven signed
energies through the same universal Gram-completed routing atlas used in
Entries 1900 and 1904.  Let \(F=(F_1,F_6,F_7)\) be its three residual cover
equations and let \(z_1,\ldots,z_{7-r}\) be the free signed energies.

The predeclared critical test is the maximal-minor ideal of

\[
J_zF=\left(\frac{\partial F_i}{\partial z_j}\right).
\]

Before classifying horizontal support, saturate by the universal routing-Gram
factor \(k(6+7k)\).  The three allowed classifications are:

- `Gram-forced transverse`: the saturated maximal-minor ideal is the unit
  ideal on the cover;
- `higher-codimension critical center`: its projection to the labelled base
  has codimension at least two;
- `candidate horizontal divisor`: its projected radical has a codimension-one
  component not contained in frozen Gram, soft, or lower-incidence support.

No representative is expanded before this criterion and the class ranking
are frozen.

## Candidate-divisor obligations

Every candidate must receive, in order:

1. the complete seven-chart labelled Cayley--Menger atlas;
2. saturation by Gram, soft, and lower-incidence support;
3. exact real-sheet equations and the full projective multiplier kernel;
4. positive-\(X_i\) and Bunch--Davies activation tests;
5. Cartier specializations at \(k=0\) and \(6+7k=0\).

Occurrence order, residue-wedge signs, stabilizers, and source normalization
are retained in every packet.  A physical claim requires a source-derived
positive chamber and contour pinch; an algebraic divisor alone is coefficient
support.

## Current partition census

The exact partition checker finds 2,104 orbits in 728 classes:

| wall rank | free signed energies | diagonal behavior | orbits | classes |
|---:|---:|---|---:|---:|
| 4 | 3 | origin only | 104 | 42 |
| 5 | 2 | origin only | 974 | 338 |
| 6 | 1 | generic homogeneous line | 1,026 | 348 |

This census is a source/combinatorial theorem only.  It does not yet classify
the universal Jacobian ideals.

## First universal gates

For the neutral representative of the first rank-four class, the exact
three-by-three Jacobian determinant is nonzero and factors as

\[
t_1t_4t_6\,k^2(6+7k)^2D.
\]

The first three factors are frozen soft support and the next two are routing
Gram support.  The residual factor \(D\) is therefore an algebraic horizontal
discriminant candidate, not yet a physical divisor.

Independently, apply Gordan's alternative to the induced homogeneous base
relations.  A nonzero nonnegative vector in their row span excludes every
strictly positive \(X_i\) vector.  The exact all-orbit census is:

| wall rank | obstructed positive cone | positive-cone feasible |
|---:|---:|---:|
| 4 | 104 | 0 |
| 5 | 0 | 974 |
| 6 | 0 | 1,026 |

Hence the complete rank-four lane is physically excluded before multiplier or
Bunch--Davies analysis, even though residual algebraic discriminants may
exist.  Rank five and rank six remain subject to the universal Jacobian
classification.

## Terminal inventory theorem

The orbit-level maximal-minor audit gives:

- all 104 rank-four orbits retain a nonconstant determinant factor after
  saturation by routing Gram, all seven pulled soft forms, and every remaining
  frozen connected-region/fused-facet wall;
- all 974 rank-five orbits have constant common GCD after Gram/soft removal;
- all 1,026 rank-six orbits have constant common GCD after Gram/soft removal.

The latter two lanes are assigned to the conservative predeclared bucket
`higher-codimension critical center`: the GCD certificate excludes every
height-one component but does not promote an empty center to proven
Gram-forced transversality.

Thus the rank-four factors are genuine algebraic coefficient discriminants,
not inherited Carrier incidences.  Their source-row-normalized projective
multipliers are supplied by rows of \(\operatorname{adj}(J)\), satisfying

\[
\lambda J=\det(J)e_i,
\]

and hence \(\lambda J=0\) on the discriminant without a fitted solver section.
Nevertheless every rank-four orbit is disjoint from the strictly positive
\(X_i\) chamber by its exact Gordan certificate, so none supplies a
Bunch--Davies pinch.

All 208 routing-Gram fibers of the 104 candidates are principal and
squarefree, with Cartier length one.  The complete candidate atlas contains
104 labelled occurrence objects, each with seven transported charts, source
order, residue-wedge sorting sign, and frozen stabilizer.

Therefore

\[
\boxed{
\text{the complete frozen seven-site inventory contains no horizontal
physical divisor.}
}
\]

This is a finite seven-site theorem, not an all-site or all-loop theorem.

## Durable artifacts

- `research/benincasa/marici-gm/src/bin/seven_site_inventory_partition.rs`
- `research/benincasa/results/seven-site-inventory-partition.json`
- `research/benincasa/marici-gm/src/bin/seven_site_universal_jacobian.rs`
- `research/benincasa/results/seven-site-universal-jacobian.json`
- `research/benincasa/marici-gm/src/bin/seven_site_positive_base_gate.rs`
- `research/benincasa/results/seven-site-positive-base-gate.json`
- `research/benincasa/results/seven-site-universal-jacobian-rank5-all-orbits.json`
- `research/benincasa/results/seven-site-universal-jacobian-rank6-all-orbits.json`
- `research/benincasa/results/seven-site-rank4-final-multiplier-audit.json`
- `research/benincasa/marici-gm/src/bin/seven_site_inventory_exhaustion_certificate.rs`
- `research/benincasa/results/seven-site-inventory-exhaustion-certificate.json`
- partial-milestone epistemic event:
  `ev-000000002277-18ddea90-c5c8-4f38-b859-b0d4773741fb`
- terminal theorem epistemic event:
  `ev-000000002280-3b3e92c7-ca42-4708-b87e-0e4ba9ee71c3`
