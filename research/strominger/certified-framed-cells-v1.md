# Certified framed cells at actual endpoint contexts

`agda/CertifiedFramedCells.agda` fills a parameter-producer gap between the canonical compiler and the mixed-tree interface.

The old compiler expects its target Fragment at the literal index `act m v`. Mixed trees instead retain arbitrary actual endpoint objects, with the required index relation derived propositionally from a full cell. These interfaces cannot be identified by reflexivity.

## Explicit frame conversion and restoration

`Synthesis` reindexes the actual target along a checked source-mode frame, invokes the existing compiler, and transports its full result back along the explicit target-object path.

The emitted `Full m a b` refers to the **original actual a and b**. Its native compare-rule derivation consumes their original native histories. `operands-recovered` proves this by reflexivity: the transported compiler target is not substituted for the actual native operand.

Frame agreement is necessary but insufficient. The compiler must also succeed on the full reader images. The combined frame/success guard is proposition-valued, using vertex sethood and Boolean guard irrelevance—not sethood of Resolve or of origin certificates.

## Certified-input producer discipline

A cell `Program m a b` requires existing producer certificates for both actual endpoint Fragments and the checked frame/success guard. It has no Full, equivalence, selected-value path or reader-function field.

This is an **explicit certified actual-input interface**, not a claim to have reconstructed a pure initial-word-only global script for every mixed tree. Unchecked Fragment inputs are not licensed.

For every compatible full cell between certified endpoints, `certify` constructs such a program and a path matching the entire computed full cell to the actual supplied one. `native-match` preserves the whole native Closure pair. This is propositional producibility, not judgmental canonicalization or unique historical origin.

## Evaluated-cell algebra

The certificates close under identity, composition and attachment. Attachment uses the actual target request derived from the supplied full cell, and its endpoint certificates lift the actual operand-origin paths through attachment.

These results certify **evaluated comparison cells**. They do not turn a compiled endpoint certificate into a retained raw compose/attachment history certificate. In particular an outer endpoint comparison can omit intermediate history that the recursive history certificate must retain.

## Remaining gate

Next apply the new discipline recursively to every core/mixed node, including intermediate endpoints and compositions inside imported core subtrees. Then certify the actual retained raw roots, their native bridges and the higher producers over root comparisons on that same input discipline.

The overall objective remains open. No raw package identification, unrestricted Body action or universal native origin certificate is inferred.

## Verification

    python research/strominger/checkers/check_certified_framed_cells.py

Fresh safe Cubical/guarded closure passed with ignored interfaces, disabled implicit libraries, stable inputs and a conservative 2,370-file manifest. Three UnequalTerms controls reject an incorrect source frame, a valid frame with incompatible carrier images (the guard computes false), and replacing full canonical matching by reflexivity.

No repository-source warnings; Cubical dependency warnings are recorded.

Contract: `contracts/certified-framed-cells.v1.json`.
Receipt and dependency manifest: `results/certified-framed-cells/`.

Predecessor sources, native rules, seed policies and immutable packets are unchanged.
