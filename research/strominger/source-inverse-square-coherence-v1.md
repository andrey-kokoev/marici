# The chosen source inverse squares are coherent under reversal

## Constructed result

`agda/SourceInverseSquareCoherence.agda` proves, for the actual existing witnesses:

    pointed-inverse y x q p
      = cong sym (sym (pointed-inverse x y p q)).

This is a cube comparing the two chosen inverse squares. It is not a replacement inverse witness chosen to make the next theorem easier. All four A/B, B/A, C/D and D/C specializations are checked.

Two explicit reflexivity bindings enforce provenance:

- `pointed-binding` identifies the pointed-carrier path with the existing retained `Complete` path;
- `inverse-binding` identifies the reconstructed square with the exact `ForwardSourceLiftComposition.pointed-inverse`, including its selected dependent value square.

Neither predecessor was edited.

## Proof boundary

Let `PointedType = Σ (X : Type), X`. Paths between `(Vertex,x)` and `(Vertex,y)` are equivalent to pairs consisting of a type path and a dependent value path.

The type-path space is a set, by univalence and the proved sethood of Vertex. Each dependent value-path fiber is a proposition. Consequently this particular pointed-carrier path space is a set, so its parallel inverse squares agree. Projecting that cube through the unchanged graph-retaining atom encoding gives the displayed theorem.

This uses **local sethood of a pointed-carrier path space**. It does not assume sethood of Code, Complete, Chain, Resolve, or arbitrary native histories.

## What remains open

The actual `forward-square-initial` is not just the inverse square: it composes its transported image with the existing `subst⁻Subst` cancellation witness. The proved base cube does not alone inhabit the native triple-overlap type.

The source records exact, currently uninhabited-by-this-packet signatures:

- `TransportCancellationTriangle`, for arbitrary type fibers and the library's chosen cancellation witnesses;
- `InitialOverlapA/B/C/D`, comparing the unchanged initial forward-square paths on arbitrary actual native proofs.

These signatures are not postulates or impossibility claims. Next work must supply the transport/naturality/composition bridge, then propagate the resulting initial overlap through retained chain extensions. No sufficiency/equivalence theorem for these proposed intermediate signatures is claimed yet.

A development attempt to push the cube directly through the native family and bind the resulting homotopy exceeded a 600-second headless checker budget. That attempted addition was removed. The final retained theorem was freshly rechecked successfully; the timeout is neither evidence of inconsistency nor an obstruction theorem. Explicit intermediate typing/opacity and the generic transport triangle are preferable next steps to repeating unrestricted normalization.

## Verification

    python research/strominger/checkers/check_source_inverse_square_coherence.py

Fresh safe Cubical/guarded closure passed, with ignored interfaces, disabled implicit libraries, stable inputs and a conservative 2,312-file include-root/primitive manifest. Three compiler controls reject:

1. treating the base cube as the native `TripleExchangeOverlap`;
2. substituting Vertex sethood for native-proof sethood;
3. filling the native initial overlap by bare reflexivity.

The checker records exact diagnostics: `UnequalTerms` for the first two and `UnequalLevel` for the third on this compiler. These are failed shortcut regressions, not proofs that the desired overlap is impossible. Cubical warnings are recorded; no repository-source warnings were reported.

- Proof: `agda/SourceInverseSquareCoherence.agda`
- Contract: `contracts/source-inverse-square-coherence.v1.json`
- Receipt: `results/source-inverse-square-coherence/verification.json`
- Lock: `results/source-inverse-square-coherence/dependency-manifest.json`
- Net: `wg-source-determination-conjecture-net-v1.md`

## Net disposition

A new constructed support node records the exact base-cube result. `source-comparison-composition` remains open and recommended, with its next action narrowed to the actual transport/cancellation bridge and chain propagation. No coherent C2 action, global Body action, or completed coherence induction is inferred.
