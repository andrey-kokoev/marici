# Lift-aware incidence records on four actual PN facet ports

## Fresh inputs and actual ports

The complementary native assembly summary, both complete fixtures, both freshly checked field receipts and the four-lift-context receipt were reread and their direct pins checked. Select the lowest-ID actual PN operation on each root facet; no synthetic eligible port is substituted.

| Facet | Independent assembly context | PN operation | PN-target packet | Lift |
|---|---|---|---|---|
|0|base|0|1|0|
|1|complement|0|1|1|
|2|base|6|7|0|
|3|complement|6|7|1|

The repeated local IDs are scoped to their assembly context, not identified across contexts. Each port retains the complete source and target packet/chart/cell records, the actual operation, its history positions, and its parent triangle's two-M certificate. Outside references remain inside those chart records.

## Geometric support restriction with full parent retention

Every pair of distinct facets has a two-vertex intersection, giving six geometric edges and twelve directed edge records. Every triple has a one-vertex intersection, giving four geometric triple vertices and24 ordered comparison cells. The fourfold geometric intersection is empty.

An edge record carries its two parent ports, both parent permits and the common support. Restricting it to a triple vertex keeps those parent keys and permits; it does not turn a triangle permit into a PN law on an edge or point. Both face-edge-vertex paths select the same vertex and retain the same parents.

There are16 directed vertex-role disagreements on the shared edges. They are explicitly listed, not erased by geometric incidence or by the field comparison. Thus this construction does not revive strict C/M-role gluing.

## Full-field comparisons anchored to the actual PN targets

The field attached to a port is the actual target N field from that operation's sewing receipt—not a terminal E packet silently substituted for it. Let U_a be that packet's source-bound local frame and P_a its retained coefficient permutation. Under the declared context convention, use

    F_a = D_a U_a,
    B'_a = D_a B_a,
    R'_a = R_a D_a^-1,

where D_a is identity for the base context and diag(I36,Q_E) for the complement. The unused E block is retained even at the N anchor. The same common-root field identification is an explicit candidate policy, not a newly source-selected physical equality between differently marked assemblies.

The checker recomputes normalization on every coordinate:

    R'_a F_a = P_a R_root,
    F_a^-1 B'_a = B_root P_a^-1.

Consequently C_ab=F_b F_a^-1 and Pi_ab=P_b P_a^-1 satisfy the full44-input readout and five-input binding squares. These are verified through exact normalized matrices and the already checked invertible factor words, rather than via scalar overlap tests.

All12 directed pairs and24 ordered triple-vertex comparisons pass. Intermediate full frames cancel in execution order, so C_bc C_ab=C_ac. Reverse edges use the inverse lift. A second forward half-turn instead produces the nonidentity central action and is explicitly rejected as an inverse control.

## Exact scope and next gate

This supplies a source-bound finite incidence/comparison candidate on all four facets, including actual PN occurrences, separate role-law contexts and retained lift data.

It does **not** yet supply a geometric field restriction observable from44 coordinates to an edge or vertex. The current restriction is of support **with full parent retention**. A full-field isomorphism may compare two such records while providing no independently sourced measurement supported on their common edge. Calling that measurement already constructed would overstate the result.

Likewise these Python records and exact field calculations are not native higher-WG derivations. The next work must distinguish:

1. native admission and restriction of the structured retained incidence packages under an explicit input policy;
2. any stronger source-defined geometric field readout on edges/vertices and its compatibility with those packages.

The former can be tested without pretending the latter exists. Neither alone should close the parent until its exact four-facet descent claim is matched. Electron face labels remain distinct from Ramsey facet labels; equal numerical permutations do not bind them.

## Reproduction

Contract: `contracts/ramsey-lifted-facet-incidence-attempt.v1.json`.
Checker: `checkers/check_ramsey_lifted_facet_incidence.py`.
Receipt with full ports, field bindings and incidence records: `results/ramsey-lifted-facet-incidence-v1.json`.
Passing freeze: `scc-freezes/ramsey-lifted-facet-incidence-v1.428930f8b083d307.json`.

The frozen SCC challenge passes. The matrices are exact multiradical calculations, not kernel proofs. No graph verdict, net revision or Git checkpoint was changed; general face-chart descent and the Ramsey root remain open.
