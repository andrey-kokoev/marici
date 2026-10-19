# Fiber loom: a first obstruction above local fittings

## Question, boundary, disposition

Can four fittings have admissible connections and invertible local comparisons,
yet fail the required coherence of the complete four-fitting configuration?

This is a DECLARED finite prototype of the operator's loom picture, not a native
P/N/E realization. Q^2 is one two-component test fiber; it does not interpret
"2x2 dimensional spaces", the 12/3/1 enrichment, or physical fiber flow/time.
P/N/E remain prospective configurations of a common apparatus, not three fitted
primitive maps. Execution disposition is in `results/fiber-loom-tetrahedron/`.

## Source operation and types

Four vertices label fittings. All six edge transports are identity on Q^2.
Each triangular face carries a comparison weight in the abelian group
{I,Z,-I,-Z}, Z=diag(1,-1). All are invertible orthogonal maps. Regard these as
formal abelian 2-form/surface comparison data. Identity edges do not construct
or determine the face weights. We explicitly enlarge the prototype source by
supplying them. We do not pretend arbitrary matrices are chain homotopies or
natural transformations of the whole category of vector spaces.

The tetrahedron is DECLARED to have a mandatory flat 3-cell: two decompositions
of its same filling must compare identically on an admissible state:

    L = a023 a012,       R = a013 a123,
    D = L-R,            admissible fiber = ker D.

The third-level comparison is fixed to identity BEFORE testing. A freely fitted
third-level correction would eliminate the risk and is not permitted. This is a
state-level flatness constraint, not a claim that every nontrivial holonomy is
physically forbidden. Without the declared filling, different surface patterns
would simply be different patterns. Matrix multiplication remains associative;
the tested issue is compatibility of the SUPPLIED face comparisons, not failure
of matrix associativity.

## Prospective predictions and falsifiers

All faces except a012 are identity in the named examples:

| a012 | rank D | dim ker D | Interpretation |
|---|---:|---:|---|
| I | 0 | 2 | Whole fiber extends |
| Z | 1 | 1 | One sector extends; the other is obstructed |
| -I | 2 | 0 | No nonzero state extends |

Every local map remains invertible in all three. A nonzero D does NOT by itself
prove the state space empty: retain ker D, the full residual and the excluded
sector. For Z, (1,0) survives and (0,1) does not. For -I only the zero vector
satisfies the filling. All partial and full failures must be visible in SCC's
whole-fiber cell check, but their admissible-state dimensions remain distinct.

Exhaust the 4^4=256 face assignments. Expected dimensions: 64 cases at zero,
128 at one, 64 at two. For each named case, exhaust all 4^6=4096 edge-frame
relabellings: a'ijk=bjk bik^-1 bij aijk. The abelian coboundary cancels around
the tetrahedron, so the holonomy and admissible fiber cannot be repaired by
these changes. Also transport all maps and the metric under one nonorthogonal
rational basis change and retain the conjugated D.

An independent sign-character calculation counts the two surviving coordinate
sectors. This cross-check must agree with exact matrix rank in every case.
Changing the obstructed face itself is a NEW source configuration, not a gauge
repair. Keeping all face weights identity works on arbitrarily large finite
complexes: higher coherence alone is not a universal maximum-size theorem.

Distinct XZ and ZX braids supply a negative control: noncommuting transport
products are not rejected when no equality cell was requested. Only the declared
same-configuration comparisons are tested.

## Issue-boundary DPC

1. Problem: boundary sharing alone never exhausted the admissible boundary
   state. The loom proposal points instead to compatibility of local comparisons.
2. Bold conjecture under test: a mandatory tetrahedral filling can obstruct
   extension even when all edges and all face comparisons remain admissible.
3. Rivals: local invertibility guarantees extension; every nonzero defect empties
   the fiber; arbitrary braid differences are forbidden; a fitted 3-cell or a
   basis change repairs the same frozen configuration; this toy is native data.
4. Risky consequences: exact surviving dimensions 2/1/0, unchanged local gates,
   fixed predicted census and covariance; no automatic rejection of distinct braids.
5. Strongest test: full face census, independent character count, all allowed
   edge coboundaries and honest metric transport; retain full rank-one residual.
6. Disposition criterion: if controls pass, the prototype demonstrates a mechanism
   for configuration-specific obstruction. It does not establish any observed
   molecular capacity, maximum region size, or actual P/N/E face comparisons.

## Reproduce and native reopening boundary

    python research/aspect/scc/scc.py check fiber-loom-tetrahedron-v1 --verbose

The checker is exact standard-library arithmetic. It writes complete supplied
face maps, evaluated composites, kernel witnesses, census, residuals and SCC
cells. SCC's token comparison is backed by the owner calculation of the actual
matrices; it is not a theorem about undeclared higher morphisms.

Native application requires independently constructed fitting interfaces, face
comparison maps, and the source reason why a particular filling is required.
These are a stopping boundary, not an invitation to invent particle-dependent
phases or another waiting-only branch. No change to the earlier native common-law
claim or the proved boundary-sharing result is inferred.
