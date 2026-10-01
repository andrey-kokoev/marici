# Ten-carrier spatial bridge — result

## What was tested

The polynomial spatial complex (`marici_native_spatial_three_extension.md`) is built on the **6 occurrence variables** X₀…X₅ and their face relations. Its modules are indexed by **faces** (subsets of {0,…,5} that are noncrossing). The natural input to this complex is the **6D coefficient summary** of a retained depth-n path package.

The 10D composable-pair carrier (coefficients on each of the 10 composable pairs) is a finer object: it records which 2-step path initiated a longer word, information the 6D summary loses. Two depth-3 words can share the same 6D summary (same final occurrence coefficient vector) but have different first pairs and different spatial displacements.

## Finding

| Quantity | Value |
|---|---|
| Depth-3 words in the retained carrier | 26 |
| Word pairs sharing a 6D summary but differing in 10D carrier | 46 |
| … of which have different spatial displacements | **42** |

The 10D carrier **strictly refines** the 6D summary for spatial readout: 42 out of 46 pairs that the summary cannot distinguish are distinguished by the 10D carrier AND have geometrically different displacements.

## Consequence for the spatial complex bridge

The polynomial spatial complex receives the 6D summary as input via the `contrast_reader` map. This map is a **linear function** on the 6 coefficient slots. It gives a 3-cycle of positions:

    step 0: (0, −3, 1)
    step 1: (0, 0, −2)
    step 2: (0, 3, 1)
    step 3: back to (0, −3, 1)

The 10D carrier cannot be embedded **directly** into the face-module structure of the existing spatial complex, because the spatial complex indexes its modules by **sets** (faces), not by **ordered pairs** (paths). The composable pairs are 2-step paths, which correspond to monomials `X_i·X_j` in the polynomial ring, not to face modules.

A bridge from the 10D carrier to a spatial-type object would need a **path-indexed chain complex** (a bar construction or a path algebra), not a face-indexed one. That is a separate construction, not the existing polynomial spatial complex.

## What this means for the conjectures

| # | Conjecture | Status |
|---|---|---|
| **1** (summary-linear readout) | **Verified.** The contrast_reader is a linear map on the 6D coefficient space and gives the correct 3-cycle. This IS the connection between the coefficient carrier and the spatial complex: the 6D summary feeds the face complex. |
| **4** (10D carrier embedding) | **Refined.** The 10D carrier does NOT embed into the face modules of the spatial complex because it carries ordered-pair data that faces do not see. But the 10D carrier **does** give strictly finer spatial information than the 6D summary. This extra information is about the branching structure (which depth-1 path was taken), not about the face-incidence structure. |
| **14** (bridge map from 10D to spatial complex) | **Withdrawn as formulated.** The spatial complex's modules are face-indexed and cannot directly receive ordered-pair coefficients. A map from the 10D carrier to a spatial-type object would require a **path-indexed chain complex**, not the existing face complex. |

## Immediate next step for conjecture #4 (10D carrier refinement)

The 10D carrier at depth 1 can predict the **displacement difference** between two words that share the same 6D summary **when the rest of the path is identical**. This is because the displacement is additive over path segments:

    displacement(full word) = displacement(first pair) + displacement(remainder)

Two words with different first pairs but identical remainders have a displacement difference equal to the difference in their first-pair displacements. The 10D carrier captures exactly this: it records the first pair's identity.

A checker that verifies this additive prediction for all 46 matching-summary pairs is the natural extension.