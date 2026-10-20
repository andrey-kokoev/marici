# Recursive mixed-history certificates and root coherence

## Constructed native order bridge

`agda/NativeAttachmentHistoryBridge.agda` supplies the generic native compare/attach-order bridge for a full cell and its actual frame-derived request. It contracts the comparison graph only by a proved equivalence, transports the old loop witness, and proves the full point/reader laws.

Both native orders and the actual preceding compiled comparison premise are recovered. Their Complete packages are provably unequal. No target request, filler, fresh root or raw package equality is supplied as a shortcut.

## Explicit recursive interface

`agda/MixedHistoryCertificates.agda` recursively traverses every core and mixed tree node, including compositions inside imported core trees. Certificates retain:

- the exact original tree;
- each local retained native history and its native comparison bridge;
- equations extracting the exact compiled child premises consumed by composition/attachment;
- the compiled endpoint closure and actual root-history closure.

**Parents consume compiled child endpoint outputs.** Each child's retained local history and bridge remain separately present in the recursive certificate. This is the declared compilation interface, not an assertion that a raw retained compose output can directly fill a rule input expecting a plain endpoint comparison. The original native rules and Body operations are unchanged.

The certificates do not make raw trees, Code objects, or arbitrary Resolve witnesses equal. They also do not certify the origins of supplied leaves or arbitrary initial proofs.

## Coherence of retained roots

`agda/MixedRootHistoryCoherence.agda` constructs a pointed reader-preserving view of each actual root history into its actual target endpoint carrier. The attachment case uses the inverse of the new native order bridge; composition uses the proved retained/compiled carrier equivalence.

For arbitrary parallel mixed trees with the **same actual endpoint objects and mode**, these views construct a full root-history comparison. Its inverse recovers the entire carrier value, and its native compare-rule derivation retains both actual root closures.

Root reader normal forms are derived through those views from the established generated-fragment normal form. Consequently their full comparison fibers are contractible. Direct/composite comparison triangles and path/square coherence are constructed and faithfully natively admitted through the generic envelope. They are not merely supplied as opaque higher parameters.

The existing constant-reader admitted Body positively refutes extending this normalization claim to unrestricted Body. No sethood of native histories is assumed. Differing endpoint objects or mode indices still require explicit comparison/transport; they are not silently identified.

## Disposition

This closes `coherence-induction` for the stated finite mixed compilation fragment: explicit generators, structural certificates, full boundary invariants, derived native comparisons and higher coherence, and exact witness/premise recovery.

It does not claim a global Body functor, an unrestricted fully homotopy-coherent C2 action, equality of raw retained packages, or a recursively nested raw-compose interface. Nor are the three policy adapters automatically new generated-fragment objects merely because they have native derivations.

The overall source-certified objective remains open. The next step must bind the exact forward histories, policy presentations and mixed programs to a common certified grammar or explicitly certified input context. The old root-only grammar does not certify every arbitrary initial Resolve proof.

## Verification

    python research/strominger/checkers/check_mixed_history_coherence.py

Fresh safe Cubical/guarded closure passed with ignored interfaces, disabled implicit libraries, stable inputs and a conservative 2,354-file manifest. Three UnequalTerms controls reject omitting an attachment node's evidence, equating retained root packages, and applying the generated normalization to the existing constant-reader Body. No repository-source warnings; Cubical dependency warnings are recorded.

Contract: `contracts/mixed-history-coherence.v1.json`.
Receipt and manifest: `results/mixed-history-coherence/`.

Earlier packets remain immutable scoped predecessors. No other-owner implementation, native seed policy or rule datatype was modified.
