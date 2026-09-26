# Full-data groupoid descent equivalence, including the original constructor

Fresh safe Cubical Agda --ignore-interfaces check passes for `agda/ObserverGroupoidDescentEquivalence.agda`; log: `results/agda-groupoid-descent-equivalence.log`. The older programme audit is not a current receipt for this addition.

## The result

For groupoid-valued output Z, the complete type of witnessed image factors is equivalent to the complete type of coherent fibre data:

    ImageFactors(f,g) ≃ CoherentFibres(f,g).

Both inverse laws are checked. The factor side retains its source-arrival equality family. The coherence side retains pairwise links AND triangle squares. This is stronger than maps witnessing existence in both directions, and is not obtained by truncating either side.

## Construction

1. Pin the point-map component of Cubical's full groupoid truncation equivalence. The pinning equality stays in the fibre, so this gives a full-data equivalence between a truncation extension with its arrival equation and its 3-Constant coherence record.
2. Apply that equivalence fibrewise over y:Y.
3. Repack the family of fibre extensions into an image postprocessor with a law at every actual origin (x,e).
4. Prove by path induction that this origin law is equivalent to the ordinary source-arrival law at (x,refl), with both roundtrips.
5. Compose these equivalences and retain their inverse laws.

The module additionally proves that its certified decoder agrees with the PREVIOUS explicit `Sufficient.factor` constructor. Encoding that original constructor recovers the supplied coherence. Thus the constructive recipe that previously retained links and triangles is connected to the new equivalence, not replaced by an unrelated existence argument.

## Precise remaining boundary

The equivalence supplies a certified encoder. We have not separately identified that encoder with the older `necessary` implementation, whose endpoint transport uses a different explicit formula. Consequently the statement is NOT that both old functions have now been shown inverse exactly as written. The original decoder is identified; the new encoder and full-data inverse laws are checked.

The result is scoped to groupoid-valued targets, not arbitrary higher types. It neither makes image factors unique nor renders their equality witnesses irrelevant. In particular, equal visible postprocessing functions can carry different source-arrival comparison data.

## Next

Construct a concrete higher-valued regression with the SAME visible postprocessor but different source-arrival comparisons. Test whether these full factors are genuinely distinct and how that distinction appears in their coherent comparison actions. This will expose the witness content of the equivalence rather than suggesting that its two sides describe only output values. Alignment with the older encoder remains an independent proof-engineering question.
