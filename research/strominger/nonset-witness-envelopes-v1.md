# Non-set witness envelopes: admission versus projection

## Generic result without sethood

`agda/NonsetWitnessEnvelopes.agda` takes an arbitrary index type F, actual packages q(f), and actual native derivations of each q(f). It constructs the usual E envelope of reflexive branches under the original Seeds and rules.

The section `f ↦ (f,refl)` lifts any supplied index path and any supplied higher path. Projection recovers each exactly. Native reflexivity/path transport and the unchanged higher rule admit these lifted cells. No sethood or truncation hypothesis is used for this construction.

For **arbitrary envelope values**, the exact nontruncated boundary is:

    Σ (p : fst u = fst v), PathP (fiber along p) (snd u) (snd v).

This type is equivalent to the full envelope path type. The inverse law recovers both the base path and the dependent fiber path. Given an actual derivation at the left value, this supplied full boundary is natively admitted. Equal indices alone are not enough.

These theorems admit/recover supplied cells; they do not discover a missing fiber compatibility or higher cell.

## Exact projection condition

The existing `CoherentDependentExtensions.Projection` theorem supplies both directions: the particular first projection is an equivalence exactly when every retained loop fiber is contractible. The new module binds that condition to this envelope. Faithful path recovery through a section does **not** imply projection equivalence.

## Sourced non-set test

The test reuses `SourceCircleProvenanceAudit.NativeCircle A`, its actual original-seed derivation, and its already-declared pushout span. No new geometric target or source-selection claim is introduced. The predecessor's explicit policy/parameter origin remains part of the scope.

Its equivalence to the existing circle transports the known nonreflexive circle loop back to the selected native carrier point. The module proves:

- the native carrier is not a set;
- its selected loop fiber is not contractible;
- the nonreflexive loop has an actual native path-package derivation;
- a Unit-indexed envelope of that carrier has two distinct values over the same index;
- therefore its first projection is not an equivalence.

The loop fiber is shown **noncontractible**, not itself non-set. The carrier is non-set. No assertion is made that both distinct values are natively admitted at the exact retained envelope Code; the canonical envelope is derived and the nontrivial loop is separately admitted at its native path Code. Keeping these distinctions avoids turning a value-level obstruction into an unsupported native reachability claim.

## Verification

    python research/strominger/checkers/check_nonset_witness_envelopes.py

Fresh safe Cubical/guarded closure passed with ignored interfaces, disabled implicit libraries, stable inputs and a conservative 2,339-file manifest. Three UnequalTerms controls reject index equality as a full envelope path, reflexive contraction of arbitrary loop values, and automatic equality of arbitrary higher boundaries. No repository-source warnings; Cubical dependency warnings are recorded.

Contract: `contracts/nonset-witness-envelopes.v1.json`.
Receipt and manifest: `results/nonset-witness-envelopes/`.

## Net disposition

`nonset-witness-fibers` is constructed at its stated conditional-theorem/test-case scope: full compatibility boundaries and faithful admission are separated from projection contractibility, with a concrete noncontractible residual on an existing native carrier.

The next gate is `coherence-induction`. It must construct the needed compatibility cells for an explicitly stated fragment; faithful admission alone does not provide them. Common-witness producer certification and the overall objective remain open.
