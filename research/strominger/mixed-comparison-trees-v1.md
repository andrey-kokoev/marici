# Mixed comparison trees and local native history bridges

## Derived attachment

`agda/MixedComparisonTrees.agda` extends the finite comparison language with attachment. The constructor retains its whole input subtree. Its target request is computed from the folded full comparison's actual frame, composing the mode edge equivalence with dependent transport. No independently chosen target request or agreement is an input.

The attachment full cell uses this request equivalence and the old pointed loop equivalence. Its selected-value and full return-port laws are proved. Structural folding gives full evaluation coherence and dependent native endpoint-comparison coherence for arbitrary finite mixed trees with fixed actual endpoints and mode.

For composable full cells, sequential and fused requests agree by the actual return laws, mode composition and the justified injectivity of the declared Out reader. This is a proved path, not a judgmental simplification. The full mixed boundary varies its target attached object along that request path, preserving the selected-value and reader data.

## Actual native composition, not substitution

`agda/NativeComposeHistoryBridge.agda` constructs the actual compose-rule output from the two endpoint-comparison derivations. An extractor recovers both input closures exactly.

That output retains the intermediate comparison packages. Its carrier is pointed-equivalent to the compiled endpoint comparison, but their Complete packages are **provably unequal** by the outer Code constructor. A separate native compare-rule application retains both actual histories and compares their full readers. It supports the existing next-edge interchange.

`MixedHistory` then compares the retained sequential compose-rule history of the two attachments to the fused attachment comparison. Its carrier map is transport along the proved mixed package path; its point and reader laws are derived by dependent path conversion and transport filling. Both the retained sequential history and fused native derivation are recovered from the resulting native comparison. The sequential compose inputs remain recoverable too.

No actual compose-rule derivation is replaced by an endpoint-comparison derivation. No native-history sethood is used.

## What is still open

These are local native bridges and an unbounded mixed **evaluation** theorem. The parent coherence gate stays open for:

1. the generic native compare/attach-order bridge on the new frame-routed full cells (distinct from the already proved fusion of two attachment comparisons);
2. recursive assembly of local bridges and premise-recovery witnesses into a common history-aware certificate for an entire mixed tree;
3. inherited operand and supplied leaf-origin certification, at the separate common-witness interface.

Existing stay-framed native interchange is reused where its hypotheses match. It is not silently promoted to all mode/frame-indexed history diagrams. Raw tree/history equality and a global Body action remain unclaimed.

## Verification

    python research/strominger/checkers/check_mixed_comparison_trees.py

Fresh safe Cubical/guarded closure passed with ignored interfaces, disabled implicit libraries, stable inputs and a conservative 2,348-file manifest. Three UnequalTerms controls reject judgmental route composition, retained/compiled package equality, and substituting an endpoint proof for the native compose-rule output. No repository-source warnings; Cubical dependency warnings are recorded.

Contract: `contracts/mixed-comparison-trees.v1.json`.
Receipt and manifest: `results/mixed-comparison-trees/`.

The original finite-tree, source-adapter and native comparison implementations are unchanged. Their immutable packets remain scoped predecessors.
