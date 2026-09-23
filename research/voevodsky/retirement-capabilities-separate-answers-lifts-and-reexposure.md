# Retirement capabilities separate answers, lifts and re-exposure

## Frozen owning state

Use the three-atom tail box with slopes 1,1/128,1/16384. Fine evidence fixes the public moments to those of (50,51,52): U=153 and V=50+51/128+52/16384. Keep all atom coordinates as the fine schema. The public image is one point, but the fine fiber is a nondegenerate line segment.

A source-bound migration to that public singleton has an exact proof: old moment equalities imply its public image lies in the singleton; the displayed admitted source point supplies the reverse inclusion. No other hidden restriction is introduced.

## Three capability profiles

The executable reference exposes three separate retired-state constructors:

- Answer-only: retains the exact public singleton and public refinement history. Public membership and threshold queries are supported. Fine lifting and fine re-exposure are refused.
- Lift-enabled: additionally retains the displayed source point as an admitted section of the singleton. It supports an old-compatible witness when the public state is nonempty. Fine re-exposure is still refused.
- Archive-enabled: additionally retains the complete expected original fine evidence and source interpretation. It can reconstruct the old fine relation, conjoined with later public refinements.

The third profile is not inferred from the second. The source point retained by the section is just one member of the fine fiber. The API never coerces it into the whole fine state or into an observation of the actual source.

These profiles are application-level capability checks, not a sandbox or cryptographic secrecy mechanism. The fixture's source and migration context are public, so another program could deliberately reconstruct the original relation. The contract concerns which claims this returned state makes from its retained evidence and which operations its methods authorize.

## Decisive negative control

The vector k=(-1/128,129/128,-1) has zero total and zero weighted moment. Thus (50,51,52) and (50,51,52)+k are distinct admitted points in the same fine fiber. The lift-enabled state returns the first, but must not present its singleton as the restored relation. The archived fine relation accepts both.

A public refinement that retains the sole public point leaves the fiber intact. A refinement excluding it makes the state empty, disables admitted lifting, and is also enforced on archive-based re-exposure. Re-exposure does not reopen an earlier unrefined source.

## Scope and costs

This is an end-to-end reference on a deliberately simple exact owning state, not a general projection compiler or a change to Nima's API. The migration proof is the singleton-image argument above. The test checks source equations directly and records canonical payload byte counts separately for public state, selected lift and archive. Those counts are local encodings, not minimal-information bounds; the shared implementation and proof context are not free if retained elsewhere.

The archive's compactness in this fixture is accidental: two equalities specify the whole fine fiber. No universal ordering between archive size and witness size follows. Future production integration should accept independently verified migration objects from the existing elimination compiler instead of hardcoding this fixture.

## Reproduction

    python research/voevodsky/checkers/check_retirement_capabilities.py

Artifact: `results/retirement-capabilities.json`.

The controls are direct exact checks, not a separate packet verifier. No source-observation authentication or new analytical admission is claimed.
