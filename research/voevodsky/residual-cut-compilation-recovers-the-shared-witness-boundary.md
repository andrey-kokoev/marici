# Residual cut compilation recovers the shared-witness boundary

## Frozen representation and construction

Freeze the independently verified behavioral source packet, its eighteen-label alphabet, local tuple observations and observable acceptance/rejection. The proposed residual representation is a finite cut-state table with at most 70 classes; no concrete execution word is retained as live state.

Start from the 61 local-view classes. Refine classes by differences in label acceptance or successor class, repeating to a fixed point. This construction reads transition behavior, not a predeclared origin-bit selector. It gives sizes 61 -> 70 -> 70.

The nine split classes each have an exported distinguishing continuation. Different initial local tuples are already distinguished by observation. Consequently every one of the 70 resulting classes is necessary under this frozen alphabet and output contract.

## Composition certificate

The old local projection has 12 strict failures among the 1,296 accepted/rejected stratum-pair compositions. The compiled residual projection has none. All 36 transpose identities and all 1,260 step-lift conditions pass.

In this instance the residual encoding is bijective on the existing 70 behavioral witness rows. Therefore pointwise lift through its inverse preserves every finite marked path, not only two-step tests. Joining adjacent relations shares the same residual state, which identifies the same behavioral witness; existentially removing a middle cut gives exactly the admitted endpoint relation.

Retaining marks permits queries about those cuts. Removing a mark intentionally forgets its historical distinction; the construction does not claim endpoint summaries answer erased-cut questions.

## DPC disposition

Corroborated for this finite behavioral source. A bounded representation derived from transition semantics suffices for exact relational composition and reversal. It stores behavioral cut states and transition relations rather than whole developments.

The result also establishes a lower bound: the full audit language admits no further compression of these 70 states. The nine binary distinctions are precisely where equality of local observations fails to identify a shared middle witness.

This is a compiler certificate for an already independently verified finite source packet. It does not establish that arbitrary analytical or nonlocal source constraints have finite residual representations, nor derive the source packet from unknown dynamics. Since every behavioral row is retained, the final composition proof is bijective transport; the substantive minimization result is that this amount of boundary information is necessary for the frozen language.

## Reproduction

    python research/voevodsky/checkers/compile_residual_cut_relations.py

Artifacts:

- `results/residual-cut-relation-contract.json`
- `results/compiled-residual-cut-relations.json`
- `results/residual-cut-relation-verification.json`
