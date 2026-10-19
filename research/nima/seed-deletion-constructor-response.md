# Rebuilding the source after indirect-edge deletion

## Result

The unchanged directed-triangle coefficient constructor was rerun on all 16
subsets of deletions from BC, CA, AD, DB, keeping vertices and primitive AB/BA
fixed. **85 exact checks pass.**

The constructor genuinely responds to the changed source. However, it does not
preserve the coefficient interface needed for the fixed two-port AB/BA experiment.
Missing ports are recorded as unavailable, never as zero responses.

## Actual reconstruction, not pruning a frozen exchange model

Input: `inputs/proton-six-arrows.json`.
Constructor: `checkers/assemble_triangle_arrow_source.py`, called unchanged.

The constructor derives complete oriented triangle permutations, their rotation
group and the centroid-triangle orbit, then rebuilds local selection, alignment
and collective feedback. No old exchange feature, graph-dependent fit or new
preparation law is inserted.

| Deleted indirect edge | Surviving source cycle | Generated outer-arrow mode ports |
| --- | --- | --- |
| none | ABC and ADB | all twelve directed tetrahedral edges |
| BC or CA | ADB | AD, DB, BA |
| AD or DB | ABC | AB, BC, CA |

The baseline has 12 triangles and stage supports 108, 432, 1296 (1836 total).
Each single deletion produces 3 triangles and supports 27, 27, 81 (135 total),
with a nonzero geometric boundary. This is an accepted open output of this
constructor, not a new closed proton.

Over all 16 deletion subsets, seven assemble and nine are rejected because
neither complete oriented triangle remains. In particular, the seam-only input
has no triangle reference frame and is rejected by the existing constructor.

## Fixed reader and the precise missing interface

Use the baseline normalized local-mode reader at the named AB and BA ports.
Inject the unchanged baseline mode vector into an aligned-stage source block;
read its amplitude in a raw-stage target block after the existing collective
map. In the full construction the resulting two-by-two response has every
entry 1/12.

After deleting BC or CA, primitive AB remains in the input but no AB coefficient
mode is generated. Conversely deleting AD or DB leaves primitive BA in the input
but generates no BA coefficient mode. Thus no nonempty deletion variant supports
the unchanged joint reader.

This is a concrete distinction between an input primitive occurrence and a
mode port generated from complete-cycle orbits. The constructor does not expose
a persistent coefficient slot for every surviving input edge. Reusing the absent
baseline slot as zero would add a new interface convention.

## Positive control: environment changes a surviving response

Where a named seam mode survives, its local vector is verified to be exactly the
same as in the baseline. The injection and normalized reader are unchanged.
Its collective self-response changes from **1/12 to 1/3**.

This change is derived by the unchanged constructor's reduced orbit and collective
normalization, not by retuning the probe. It establishes whole-source dependence
of that existing coefficient response. It is a partial-port control, not a
replacement for the unavailable two-port experiment.

The constructor outputs a mode and operators, not a physically prepared exchange
state. Nothing here identifies the coefficient response with the AB–BA record
exchange, derives its feature kernel, or supplies a physical excitation scale.

## Synthesis

Two claims must remain separate:

1. **Positive:** deleting an indirect relationship changes the source-generated
   collective operator and a fixed surviving local response.
2. **Boundary:** the same constructor removes one of the seam coefficient ports,
   so the unchanged two-port interaction comparison cannot yet be executed.

The missing construction rule is now specific: a persistent primitive-to-
coefficient interface for surviving edges when their complete source cycle is
broken, together with its intended response semantics. A terminal/open-channel
constructor may be relevant, but an absent port must not simply be replaced by
an arbitrary vector or an old frozen exchange feature.

This finding concerns the directed-triangle coefficient pipeline. The separate
proton/electron affine geometry pipeline is not silently treated as having the
same edge-deletion input semantics.

## Verification

    python research/nima/checkers/check_seed_deletion_constructor_response.py

Receipt: `results/seed-deletion-constructor-response.json`.
All source variants, generated ports, partial response matrices and rejection
reasons are recorded. Input and constructor hashes are checked again at the end.
No source file or historical owner receipt is modified.
