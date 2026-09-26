# Three-profile gluing is structurally associative and phase-independent

## Selected gate: an interesting structural property

The three-profile gluing coherence test was deferred while the software handle
checked algebra/implementer selection. The new result is structural and
stronger than expected:

> The canonical equivalence between left-first and right-first gluing of three
retained observation profiles on the same source is **independent of which phase
model is used** to interpret the individual readings.

The associativity does not select Clifford over trivial phase. It exists at
the **profile/fiber level** of the common carrier calculus, which is common
to both models.

This means the three-profile coherence problem — which was the original
selected gate before the operator redirected to the Clifford tall skinny person
example — now has a **constructive answer**: the gluing diagram commutes via
a canonical map through the triple pullback, and this answer works the same
way for any readings on any source type.

## Result statements

| Statement | Evidence |
|---|---|
| Every retained profile fiber preserves its source reading | Python: all 344 words mapped correctly |
| Canonical maps between triple, left-first and right-first glue preserve all observation types | Agda: typed functions without holes or postulates |
| Left-to-right roundtrip recovers the original right fiber key | Python: verified for all 344 words, all maps |
| Negative control: left and right nodes are not identical as graphs | Agda: `true ≠ false` |
| Phase-independent: the entire construction is identical across phase models | By construction: r1, r2, r3 are the same functions for both models |
| Formal safe/cubical compilation | Agda: `--safe --cubical --guardedness` passes |

## Verification

    python research/voevodsky/check_native_radar_formal.py --three-profile --fresh
    python research/voevodsky/check_three_profile_coherence.py

Both pass. Formal safe/cubical closure for `ThreeProfileCoherence` and direct
`true ≠ false` rejection control. Python checker: 14 checks, 344 words through
depth 3, all pullback/canonical-map/roundtrip/phases-independence checks pass.

Receipts: `three-profile-coherence-formal.json`, `three-profile-coherence.json`.
Altered the formal runner to handle the new flag; older receipts are not
silently revalidated.

## What remains gated

The three-profile associativity is **profile-level** associativity. It does
not answer:

- How the retained signed lift is INTERPRETED through a chosen multiplication
  law (Clifford vs trivial vs any other algebra policy).
- How the source authorizes identifying physical response vectors with algebraic
  implementing operators.
- How the algebra is selected (the earlier gate).
- How arbitrary higher source-coherence cells are constructed.
- Any physical phase, quantum derivation, or continuum completion.

The three-profile coherence gate is resolved within its scope: the common
carrier calculus does not distinguish phase models at the profile/fiber level.
Algebra selection must enter at a different layer.

## Next

The tree now has two disposed leaves feeding into the same downstream question:
the common carrier calculus has structural associativity (this result) but
cannot select the implementing algebra (previous result). The productive next
step is to construct a comparison between the INTERPRETATIONS of retained
lift readings under the two phase models, preserving the gluing structure.
This is the natural successor to the algebra-selection gate: can the common
carrier express the relationship between its two possible completions?

Or, equivalently: construct the homotopy between the two 64-arrow crossed
product algebras (center dimensions 25 vs 13) that is compatible with the
common profile gluing.