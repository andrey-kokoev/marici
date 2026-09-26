# Identical output maps, distinct coherent witnesses, different readouts

Fresh safe Cubical Agda --ignore-interfaces check passed for `agda/ObserverWitnessRegression.agda`; log: `results/agda-witness-regression.log`. Earlier programme-wide receipts predate this module.

## Concrete result

Two image factors share EXACTLY the same postprocessing function. Both always expose the same base index. Their source is Bool; the first observer forgets it into Unit.

The flat factor uses the trivial source-arrival comparison at each source. The twisted factor changes only the false source's arrival comparison, inserting the nontrivial index loop. Both are genuine factors. Unlike the earlier deliberately invalid loop-on-identity assignment, their induced actions satisfy identity and composition. The twisted true→false→true comparison route cancels coherently.

Nevertheless the full factors are unequal. Their comparison actions on the true/false source collision are respectively reflexivity and the nontrivial loop. No equality of full factors can identify these actions.

This is not only a formal inequality invisible to every observer. Define a comparison-sensitive readout by transporting true in the double cover along the induced comparison. The flat factor reads true; the twisted factor reads false. A value-only observer sees the same postprocessor, whereas this comparison-sensitive observer distinguishes them.

## Connection to the full groupoid theorem

The module proves the imported index type is a groupoid by retracting its custom circle to the Cubical library circle, using the library's checked groupoid theorem and closure under dependent sums. Thus this is an actual instance of the preceding equivalence's hypothesis, not merely an assumed truncation level.

Encoding the two factors through the certified descent equivalence gives DISTINCT full coherence records. The proof uses the certified inverse laws. Thus the equivalence demonstrably retains information that equality of output functions alone would erase.

## Interpretation and next test

An observer's access specification matters beyond positivity: access only to values differs from access to comparison evidence. The readout here is mathematical transport, not an assumed temporal process or a physical measurement claim.

Next return to the existing explicit dependent-machine fragment and construct a tightly scoped execution/observation bridge. Determine which parts of a finite computation admit a direction-free observation description, and which operational orientation/history data remain additional. Do not infer the universal identity execution=positive observation from this higher-witness example. This addresses the foundational interpretation directly rather than indefinitely extending coherence lemmas without a computational cross-check.
