# Interpretation comparison gate: sign-diff and cocycle structure verified

## Result

The comparison between trivial and Clifford interpretations of retained signed lifts
is now explicitly constructed as `sign-diff: History → Bool`, recording exactly when
the two models disagree on the sign of a word.

## Properties verified

| Property | Status | Evidence |
|---|---|---|
| `sign-diff(e1) = sign-diff(e2) = false` | Definitional | Agda `refl` |
| `sign-diff(e1*e2) = false`, `sign-diff(e2*e1) = true` | Definitional | Agda `refl` |
| Not constant | Agda `false≢true` | `not-constant` proof |
| Cocycle formula: `sign-diff(times h k) = sign-diff h ⊕ sign-diff k ⊕ b_and_c(h,k)` | Exhaustive (344×344 = 118,336 pairs) | Python |
| Reversal formula: `sign-diff(reversal h) = sign-diff h ⊕ a_and_b(h)` | Exhaustive (344 words) | Python |
| Same action, different sign (e1*e2 vs e2*e1) | Verified | Python |
| Compatible with profile gluing | By construction | Interpretation is word-level, independent of glue structure |

## What this establishes

The trivial and Clifford interpretations are related by a KNOWN, structured cocycle.
The sign-diff map records the disagreement and satisfies the cocycle identities.
This is NOT a map that selects one model over the other — it records their
relationship at the comparison level.

## What remains

The sign-diff cocycle operates at the level of Signed lift readings. Extending it
to the full 64-arrow crossed product algebras (center dimensions 25 vs 13) would
require constructing an algebra homomorphism between them that is compatible with
the source action and the profile gluing. This is the natural successor.

## Verification

    python research/voevodsky/check_native_radar_formal.py --comparison --fresh
    python research/voevodsky/check_interpretation_comparison.py

Both pass. Formal safe/cubical closure with direct `sign-diff ≡ const false` rejection.
Exhaustive Python: 344 words, 118,336 multiplication pairs, 344 reversal cases.
Receipts: `interpretation-comparison-formal.json`, `interpretation-comparison.json`.

## Scope

This is the comparison BETWEEN two concrete models. It does not:
- Prove that one model is correct or derived from source axioms
- Construct the algebra homomorphism between the 64-arrow crossed products
- Select a physical phase or quantum completion
- Construct arbitrary higher source-coherence cells