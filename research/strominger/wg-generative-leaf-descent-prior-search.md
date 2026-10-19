# Generative leaf descent: recovered constructor and the 137 counting boundary

## Operator correction and net consequence

The intended descent generates an expanding retained construction whose rung4 interface has137 leaves. Decreasing rung labels do not imply decreasing leaf count. This is the operator's target specification; the intermediate schedule is still to be recovered/constructed.

The completed twelve-row schedule comparison remains valid as a comparison of retained presentations. It is NOT a realization of that generative descent. Likewise the existing confirmed-diagram fixture starts with137 records at its rung12; moving that fixture to rung4 does not explain generation of137 leaves. Do not discard those supporting results, but do not substitute them for the requested process.

## Prior work actually found

### Independent family comparison generates records

`research/nima/recursive-independent-family-comparison.md` supplies a genuine successor. For q:E->V, promote F_v=q^-1(v) as a labelled family, then independently compare two families, retaining every ordered member pair and its parents. The exact law is

    (q x q)^-1(v,w) = F_v x F_w.

Thus comparison-before-grouping and grouping-before-comparison agree on the full next records. Family size multiplies. Repeated comparison gives:

| Source relation | Initial | One comparison | Two comparisons |
|---|---:|---:|---:|
| All directed four-state arrows | 12 | 144 | 20736 |
| Counted arrow view, one mark excluded | 11 | 121 | 14641 |

Operand arities are1,2,4; family counts are4,16,256. These are independent Cartesian comparisons, NOT endpoint-matched path concatenation. The checker retains parent IDs and all primitive-origin tuples. The source explicitly leaves the auxiliary state branch's recursive role unspecified.

This is the missed generative operation. Grouping preserves members; independent comparison creates a new member-pair domain. Neither grouping alone nor the number of fresh family labels expresses that growth.

### Where137 is constructed

`research/nima/137-comparison-fibration-weight-audit.md`, `research/nima/reference-semantics-carrier-versus-counted-domain.md`, and the earlier `check_comparison_slot_reference_assembly.py` give:

    D = (E'_A x E'_B) disjoint-union (S_A x S_B)
    |E'_A|=|E'_B|=11; |S_A|=|S_B|=4
    |D|=121+16=137.

All twelve primitive arrows remain in each retained carrier. A local reference mark selects eleven counted legs; it does not delete the reference from the carrier. Full arrow pairs number144;23 touch an excluded mark. With the state branch the full interface has160 slots, while the selected counted interface has137.

In the typed assembly, x_i:A->U and y_j:U->B supply121 composites. State legs s_a:A->V and t_b:V->B supply16. The independent direct reference d:A->B remains separately attached. This is a concrete generation of comparison slots from supplied leg families, not a derivation of a rung-by-rung source schedule or of the reference policy.

The reference-semantics audit distinguishes local marks q_A,q_B from d; their carrier adapter is not supplied merely by the count. Requiring equality of original variable endpoints instead would give30 selected arrow pairs in the tested domain, not121. Common intermediate type U makes all declared leg pairs composable without imposing that different restriction.

### Existing recursive composition is a different generator

`research/nima/recursive-comparison-record-closure.md` retains comparison records (C,d) and their children, with

    rho_new = d2*rho1 + rho2*d1 + rho2*rho1.

It distinguishes repeated occurrences from independent operands and rejects composing parallel A->B records without a matching interface. It gives no additive uncertainty/energy budget. This operation must not be silently identified with independent all-pairs family comparison.

### Already documented fixture mismatch

`research/nima/executable-rung4-chain-first-missing-seed-link.md` explicitly locates137 composite records BEFORE the fixture's rung12. It identifies an upstream seed/realization adapter as missing from that executable chain. Thus the current operator correction is not refuted by that fixture; the fixture labels and initial condition simply do not instantiate the intended growth schedule.

### A tested growth rival is not137

`research/nima/retained-flag-shape-growth.md` gives barycentric face-promotion counts (4,6,4,1), then (15,50,60,24), then (149,796,1224,576). That chosen policy grows retained structure, but does not select137. It is not a substitute merely because it is generative.

## Counting contract needed for the next task

Keep distinct:

1. rung designation;
2. independent operand arity;
3. selected comparison records (137 at the target);
4. primitive operand occurrences inside those records;
5. unique primitive factors shared between records;
6. promoted outer-family labels;
7. retained witnesses and direct references.

The137 entries above are composite comparison slots. Calling them leaves relative to an outer family view does not make them137 distinct primitive generators. The typed assembly uses30 primitive legs plus a separate reference; each comparison uses two legs. No universal leaf count can be read off a flattened tree without stating what the terminal leaves denote and whether shared factors are deduplicated.

The next net task must locate independent comparison and the state branch in the intended diagram, and bind the terminal137 slots to its rung4. Do not invent intermediate counts by interpolating between12 and137, or replace that task with transporting an already137-row input. The exact all-rung growth schedule was not located in this bounded search; this is not an absence theorem.

## Fresh verification

Executed successfully, without changing source-owner implementations:

    python research/nima/checkers/check_recursive_independent_comparison.py
    python research/nima/checkers/check_comparison_slot_reference_assembly.py
    python research/nima/checkers/check_retained_reference_semantics.py
    python research/nima/checkers/check_137_fibration_weights.py

The outputs verify the two generating comparison stages, parent provenance and commuting grouping/comparison squares;121+16 assembly; retained12 versus counted11 reference semantics; and32 families containing137 members with correct transported weights. No new Agda closure, physical normalization, intermediate rung assignment or uncertainty conservation is claimed.
