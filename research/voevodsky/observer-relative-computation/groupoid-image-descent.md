# Positive higher-valued image descent, with a specified scope

Fresh safe Cubical Agda --ignore-interfaces check passes for `agda/ObserverGroupoidImageDescent.agda`; output: `results/agda-groupoid-image-descent.log`. The older programme audit predates this module.

## Scope and actual data

The target output Z is a GROUPoid type: identity types are sets. Nontrivial paths are allowed; this is strictly broader than set-valued outputs. No claim is made for arbitrary untruncated target types.

For every y:Y, consider the actual fibre Fibre(f,y). Each origin in this fibre determines an admissible g-output. `CoherentFibres` supplies a Cubical `3-Constant` structure on this origin-output function: a comparison link for every pair of origins, and a triangle square for every triple. The data are a dependent function of y, not unrelated choices at disconnected points.

## Checked theorem

Given this data and the groupoid condition on Z, the checked Cubical groupoid eliminator for propositional truncation constructs an image factor. It does NOT choose or return an origin from the truncated fibre.

- Arrival of a source value commutes definitionally with the constructed factor.
- The supplied pairwise link is retained by computation.
- The supplied triangle square is retained by computation.

Conversely, EVERY existing image factor supplies `CoherentFibres`. This direction does not need the groupoid condition. Its source-arrival comparisons are used to transport the whole coherence record to the specified origin outputs, not discarded as if they were reflexivity.

Thus, for groupoid-valued Z, we now have constructive maps in both directions between the proposed coherent fibre data and witnessed image factorizations. This is a necessary-and-sufficient existence criterion with explicit witness retention in the construction. It is NOT yet a proved equivalence of the complete data types: the two composite roundtrip laws remain open.

## What the result means

The previous non-retainable loop-on-identity assignment lacked precisely the kind of coherent structure required here. Supplying endpoints alone was insufficient; supplying checked triangle-coherent links now yields a factor within this truncation-level scope.

This is a positive mathematical reconstruction theorem, not just another counterexample. It still supplies no clock, metric observer area, physical record mechanism or universal identification of execution with observation. The library eliminator is the constructive mathematical mechanism used, not an arbitrary evaluator hidden behind a rule.

Next test the two roundtrips while retaining the full source-arrival and triangle data. Do not call the current bidirectional existence result an equivalence or assert uniqueness by importing the set-valued proof into the higher-valued case.
