# What task needs 137? Response reconstruction versus compatibility auditing

## Freeze the question before counting

Use the existing two-factor marked four-state comparison domain: an 11×11
arrow block and a 4×4 state block. No measured electromagnetic number enters.
Test distinct tasks on explicit admitted input classes, rather than defining
a task as “output 137 labels” and calling that an explanation.

## Task A: recover every first-order comparison response

At the all-unit scalar-leg baseline, each block obeys

    r_ij = dx_i + dy_j.

Choose one pivot row and column. Then

    r_ij = r_i0 + r_0j - r_00.

Consequently 21 arrow measurements and 7 state measurements recover all
137 responses. This is not just a numerical rank report: the checker
constructs exact coefficient expressions for every recovered slot.

Minimality within linear scalar measurements follows from the response
rank 21+7=28. For slot measurements, the selected bipartite graph must be
connected in each block; a tree achieves the bound. Removing any edge of
the tree gives an explicit primitive perturbation invisible on the surviving
measurements but visible on an omitted slot.

By contrast, deleting ANY SINGLE slot from the full 137 preserves recovery.
A duplicate 138th sensor changes nothing. Restoring the excluded reference
legs gives a DIFFERENT 160-slot domain with response rank 30, not a special
failure at 137.

The 28-slot frame can preserve the existing reference stabilizer. Use the
reverse-reference arrow as the arrow pivot and the reference-source state
as the state pivot. Both are fixed by the independent exchanges of the two
unmarked vertices, so the frame is invariant under the declared S2×S2 action.
No unmarked S4-equivariant selection is asserted.

**Result:** 137 is not necessary for Task A. This proposed explanation of
137 fails; a smaller symmetry-compatible interface performs the same task.
The result is about first-order responses, not all native histories.

## Task B: recover independently variable comparison records

If each of the 137 slots has an independent stored residual, omitting any
coordinate hides a change in that record. Full linear scalar recovery then
requires 137 measurements. The checker constructs all 137 omitted-coordinate
hostiles.

This is a genuine task distinction but not an independent derivation of
137: the 137-dimensional storage domain was assumed. The earlier exchange
model's independent normals use precisely these extra record coordinates.

## The useful structural decomposition

For an arbitrary slot table define

    D_ij = r_ij - r_i0 - r_0j + r_00,  i,j ≠ 0.

Then the table is exactly recoverable from

    28 anchored frame responses + 109 rooted mixed differences.

There are `(11-1)²+(4-1)²=100+9=109` such differences. Each interior-only
change leaves all anchored measurements unchanged and changes its own
rooted difference. The checker verifies the decomposition and these hostiles.

This recovers a significant PRIOR result, rather than inventing a new
numerology: `typed-assembly-boundary-and-mixed-defect.md` derives the same
109 relations from the actual shared-leg path assembly, and
`shared-leg-dg-realization-and-base-coherence.md` supplies higher products.
The previous typed-assembly checker was freshly rerun and passes.

For finite matrix composites `R_ij=y_j*x_i-d`, the mixed response is

    D_ij = (y_j-y_0)*(x_i-x_0).

It vanishes at first order and under a change of only one leg family but
can be nonzero when both change. The existing exact example gives
`(2/5) K H`. Nonzero D is therefore NOT automatically an inconsistency:
a compatibility test must compare it with the expected factored mixed term.
Nor are the 109 values freely independent under shared-leg provenance.

Even finite scalar product outputs can be reconstructed from pivot row and
column when the pivot is nonzero, using multiplication/division. Thus the
presence of mixed terms alone does not prove that 137 measurements are
needed for every nonlinear reconstruction task.

## Better explanatory hypothesis

137 may organize a complete REFERENCE-RELATIVE RESPONSE/AUDIT INTERFACE:
28 local response coordinates plus 109 checks of joint composition.
This is more precise than 137 independent possibilities or depth 137.
It remains conditional on the four-state factors, marked references,
selected typed domain, source realization, and allowed interventions.

A next task worth testing is whether native-admitted simultaneous
perturbations require access to particular mixed comparisons to distinguish
valid composition from a false lower-order reconstruction. The existing
matrix example establishes sensitivity; it does not yet prove a minimal
physical interface or identify those perturbations with electron charge.

## Fresh verification

    python research/nima/checkers/check_137_task_minimality.py
    python research/nima/checkers/check_typed_assembly_boundary_adapter.py

436 new exact checks pass; the prior typed-assembly assertions also pass.
Results: `results/137-task-minimality.json`.
No electron count, graph-depth bound, charge law, or fine-structure constant
is derived by this task audit.
