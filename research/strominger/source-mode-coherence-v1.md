# Chosen source composition: triple and unit overlaps

The exact `ForwardSourceLiftComposition.TripleExchangeOverlap` is now inhabited for **every retained Total history**, with arbitrary initial native proofs and every extension edge retained. The actual composition paths for all eight mode triples and both unit boundaries are compatible.

This closes the scoped `source-comparison-composition` gate. It does not establish a fully homotopy-coherent C2 action, a global Body action, general envelope admission, or the separate coherence-completion/producer-integration objectives.

## Construction

1. **`agda/TransportCancellationCoherence.agda`** proves the triangle for the library's existing `transport⁻Transport` witnesses. No alternate adjoint equivalence replaces them. For a constant type line put `T r a = transp (λ _ → X) r a` and `cancel r a j = T (r ∨ j) (T (r ∨ j) a)`. At extent 1 both triangle paths are reflexivity. Transporting that equality along the extent parameter proves the constant-line triangle; path induction gives arbitrary type paths. The paired-round-trip theorem then uses path induction on the inverse-comparison square plus explicit left-unit corrections.
2. **`agda/SourceInitialOverlap.agda`** applies that generic theorem and the already-proved exact inverse-square cube to all four original `InitialOverlapA/B/C/D` signatures. Fibers are unrestricted; no native proof sethood is assumed. Abstract theorem boundaries avoid re-normalizing the large witness implementations when the lemmas are reused.
3. **`agda/SourceChainOverlap.agda`** propagates through all six extension constructors. A constructor-normalized square is used internally, but `chosen-square-agrees` proves its equality to the OLD square by induction and `cong-∙`. The final triple-overlap term is transported back through this comparison. Thus the theorem concerns the old chosen witness, not a silently substituted involution proof.
4. **`agda/SourceModeCoherence.agda`** supplies the actual associativity-path boundary for all eight mode triples and both units. A dependent path explicitly accounts for the mode-associativity endpoint. It also projects the triple overlap through native `closure`.

The original forward-square, inverse-square, retained history and covariance files were not edited. The revision-11 base-cube packet remains an immutable scoped predecessor; its former residual signatures are inhabited here, not retrospectively claimed by its receipt.

## Verification

    python research/strominger/checkers/check_source_mode_coherence.py

Fresh safe Cubical/guarded closure passed with `--ignore-interfaces`, no implicit libraries, stable input hashes and a conservative 2,319-file manifest. Three negative controls reject:

- the finite mode-table equality offered as the higher overlap (`UnequalLevel`);
- bare reflexivity offered as the chosen-square normalization comparison (`UnequalTerms`);
- the double-exchange square offered as single-exchange identity (`UnequalTerms`).

These are shortcut rejection tests, not impossibility claims about the positive theorems. Two initial repository indexed-match warnings were eliminated by factoring the initial-proof cases out of the recursive chain matches. The final receipt records only Cubical dependency warnings and no repository-source warnings.

Contract: `contracts/source-mode-coherence.v1.json`.
Receipt and manifest: `results/source-mode-coherence/`.
Current net: `wg-source-determination-conjecture-net-v1.md`, revision 12.

## Remaining frontier

`policy-classification` is the next dependency-ready gate, followed by `nonset-witness-fibers`. Do not repeat the already classified free/filled topology alternatives without an independently supplied task or filling. Continuation-side policy remains available for explicit classification.

General coherence/completion, non-set envelope behavior, common-witness integration with the root-only producer grammar, and the overall objective remain open. The new unbounded chain induction proves this particular overlap; it is not the separate theorem about arbitrary diagram coherence.
