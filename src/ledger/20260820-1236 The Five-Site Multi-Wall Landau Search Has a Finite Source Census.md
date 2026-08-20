# Entry 1236 — The Five-Site Multi-Wall Landau Search Has a Finite Source Census

## Admission rule

Use only the 180 frozen OFPT terms. A labelled wall pair or triple is admitted as an active Landau set only when all its members occur together in at least one ten-denominator source term.

No pair or triple is added from geometric plausibility alone.

## Exact pair census

Across the source packet there are

\[
\boxed{245}
\]

distinct compatible labelled pairs. Under the exact five-cycle action they form

\[
\boxed{49}
\]

free $C_5$-orbits, with no fixed orbit.

Their wall-kind, arc-size, and cut-support intersection data form 29 coarse profiles. These profiles are discovery partitions only; exact elimination retains the labelled orbit representatives.

## Exact triple census

There are

\[
\boxed{1210}
\]

distinct compatible labelled triples. They form

\[
\boxed{242}
\]

free $C_5$-orbits, again with no fixed orbit.

Their corresponding coarse incidence data form 93 profiles.

## Source multiplicity

The durable packet records, for every subset:

- its exact labelled representative;
- its $C_5$ orbit representative;
- the number of OFPT terms containing it;
- its wall types and cut-support intersections.

Thus term multiplicity remains available as source provenance and is not replaced by orbit counting.

## Meaning

The compatible multi-wall search is finite:

\[
\boxed{
49\text{ pair representatives}
+
242\text{ triple representatives}.
}
\]

This entry makes no claim that any representative has a Landau solution. It only closes the admissible search domain.

## Artifacts

- `research/benincasa/marici-gm/src/bin/five_site_compatible_landau_subsets.rs`
- `research/benincasa/results/five-site-compatible-landau-subsets.json`

## Next falsifier

Derive the Landau equations in a label-generic form using the cut-incidence vectors. Solve the 29 pair profiles first, while preserving exact representatives for certification. If profile data fail to determine the elimination ideal, split the profile using source-derived routing invariants rather than fitting individual outcomes.
