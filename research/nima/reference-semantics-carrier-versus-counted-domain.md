# Reference semantics: retained carrier versus counted domain

## Source trace

The existing documents specify a retained direct reference:

- docs/theory-page.md, 'Fine-structure constant: comparison slots': the direct
  relationship supplies the reference and is excluded FROM THE COMPARISON SLOTS;
  the assembled comparison is assessed against that relationship.
- comparison-slot-normalization-and-carrier-closure-residual-hypothesis.md:
  physical realization retains a reference relationship while the counted domain
  has121 arrow slots and16 state slots.
- checkers/check_comparison_slot_reference_assembly.py: x_i:A->U and y_j:U->B
  supply121 composites, the state legs supply16, and d:A->B is a separate
  retained reference. The residual is assemble(x,y,s,t)-d. Changing d by H
  with every comparison fixed changes the residual by -H.

The later137-slot fibration checker constructs only the excluded-reference
comparison view. Its deletion describes that view's domain. Using that deletion
as the topology of the entire retained carrier was an additional interpretation.

## Explicit record model

Retain all12 primitive arrows E and mark q in E as reference. Define the counted
leg selection E_counted=E minus {q}. This has11 members without removing q from
storage or identifying its endpoints with other labels.

For two local marked carriers:

    full arrow-pair relation: E_A x E_B, size144,
    counted arrow pairs: (E_A minus {q_A}) x (E_B minus {q_B}), size121.

There are23 reference-touching pairs outside the counted view. Their membership
is recoverable from the retained primitive factors; the count does not require
materializing those pairs as extra comparison readouts. The16 state slots bring
the counted domain to137. The corresponding full relation plus state slots has
160 entries. These are different interfaces to explicitly specified data.

A fixed reference is also an edit policy. The test denies ordinary edits to the
marked arrow and allows a separately requested reference edit with a fresh
version. Either policy keeps its record and endpoint incidence intact. Changing
the mark changes the counted view while preserving the retained relation.

## Topological consequence

The full marked primitive relation still has Dowker complex S^2. Its counted
11-arrow subrelation has Dowker complex D^2. Marking a reference does not require
a boundary quotient or restoration operation to keep the full carrier's sphere.

The earlier exact computations remain valid for their stated relations:

    full carrier product -> S^2 x S^2,
    counted arrow product -> D^2 x D^2.

The b2=1,2,4 product recurrence belongs to the full retained relation under
independent recursive comparison. The137-slot readout domain is a selected
subrelation with different topology. Its slot count is not the dimension or
homology of the full carrier.

## Typed adapter still to specify

The direct reference d:A->B in the existing assembly is not yet identified with
the two local primitive marks q_A and q_B by a carrier realization. The record
checker keeps those roles distinct. That adapter must explain how a direct
inter-carrier relationship induces the two11-leg selections and how its allowed
changes propagate to them.

Likewise, the assembly's common intermediate TYPE U makes every x_i,y_j pair
composable without imposing an equality between independently chosen labels.
The earlier 'composable-pair' independence control imposed equality of VARIABLE
primitive endpoints. Its rank0 result applies to that constraint, not to every
composition through a fixed intermediate type. The121 assembly composites retain
independent leg indices.

## Verification

    python research/nima/checkers/check_retained_reference_semantics.py

Exact checks distinguish12 retained edges from11 selected edges, primitive sphere
from counted disk,144 full pairs from121 selected and23 excluded pairs, changing
marks from deletion, pinned versus explicit reference edits, and stale versions.
The earlier matrix assembly is rerun and its reference-only residual change is
verified with137 counted slots unchanged.

The current evidence selects retained-reference plus counted-domain exclusion as
the documented semantics. The next implementation is the typed adapter linking
that retained direct reference to local carrier marks and the comparison legs.
