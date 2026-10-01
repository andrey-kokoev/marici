# Seed endpoint sections and a unique reversible cycle

## Scope

Continue `seed-packet-rung4-realization-audit.md` using only the actual directed seed AB, BC, CA, AD, DB, BA. A source section chooses one outgoing edge per vertex. A target section chooses one incoming edge per vertex. Each choice retains its edge witnesses. These are sections of finite endpoint families, not yet a physical promotion law.

## Enumerated families

| Vertex | Outgoing fiber | Incoming fiber |
|---|---|---|
| A | AB, AD | CA, BA |
| B | BC, BA | AB, DB |
| C | CA | BC |
| D | DB | AD |

Every fiber is inhabited. Each endpoint family has 2*2*1*1=4 global sections. Their choices have four edge members; neither a section nor the set of sections is the original six-row dependent total.

Exactly one edge subset is simultaneously a source section and a target section:

    {AD, DB, BC, CA}, or A -> D -> B -> C -> A.

This follows directly: C must choose CA and D must choose DB, occupying targets A and B. B must therefore choose BC, and A must choose AD. No metric, averaging or completed tetrahedron is required.

The resulting permutation sigma is reversible. Sigma^4=I and sigma^-1=sigma^3. Its selection is equivariant under all 24 vertex relabellings. Thus the seed itself selects one reversible routing if the objective is one incoming and one outgoing edge at every vertex.

## Primitive versus composite return

The inverse one-step edges would be DA, BD, CB, AC, none present in this seed. Nevertheless three successive forward steps implement the inverse permutation. This is a concrete positive compositional return, not a signed inverse of an averaging operation.

This is deterministic routing of state values. It does not preserve arbitrary six-arrow amplitudes or every seed cycle responsibility. The criterion selecting this routing is stated here; it has not been derived as the physical packet evolution law.

## Pruning and completion controls

Under the objective 'retain a cycle cover of all four vertices', AB and BA can be deleted. Each of AD, DB, BC, CA is indispensable because the cover is unique. The minimum for that objective is four directed edges, attained by this cycle; one outgoing edge per vertex gives the lower bound.

This is not the desired physical primitive-cost result: deleting AB and BA removes the supplied two-cycle and breaks the original triangular cycles. A construction requiring those structures has a different pruning objective.

Completing the support to directed K4 changes the census to 81 source sections, 81 target sections and nine simultaneous covers (the derangements of four vertices). Completion therefore removes this uniqueness. The count four here is not a rung identification, and nine is not a mass or comparison-slot derivation.

## Consequence for the next endpoint construction

The actual seed supplies inhabited source and target section spaces and one canonical simultaneous routing under the declared cover objective. This is more specific than an arbitrary transport matrix. It supplies a candidate reversible suboperation to trace through retained presentations.

It does not yet say whether the promoted endpoints should be individual sections, the whole section types, or another witnessed construction. Nor does it derive the relationships between promoted endpoints. Those choices must be connected to the confirmed rung diagram rather than inferred from section counts.

## Verification

    python research/nima/checkers/check_seed_endpoint_sections.py

Exact finite enumeration checks all sections, the unique cover, every single-edge deletion, absence of Hall obstructions, four-step return, three-step inverse, all vertex relabellings and the completed-K4 control. All pass. An initial development assertion incorrectly predicted no simultaneous cover; enumeration rejected it, and the final certificate explicitly exhibits the unique cover above.
