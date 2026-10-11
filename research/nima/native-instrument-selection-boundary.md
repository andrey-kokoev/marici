# Exact selection boundary for the native Boolean instrument

## Stop iterating isolated counterexamples

The prior formal module constructed two reversible native query recorders
with different source back-action. The new checker enumerates ALL 8!
permutations of the actual Vertex × Bool state set. Fix the task:

- record the ABC-to-B query correctly when memory starts blank;
- preserve that query value in the source (repeatability);
- keep the full joint update reversible.

No metric, cost function, probability, numerical force or duration enters.

## Complete finite classification

Exactly 36 maps satisfy those requirements. The query is true only at A,
so that source fiber forces the memory flip. On the false-answer sources
B,C,D, each of the two input-memory slices admits its own permutation of
those three vertices. Thus the class is exactly S3 × S3, not merely a pair
of selected rivals. The checker reconstructs all 36 from this formula and
compares them with the full 40,320-map census.

Now protect extra native queries from the SAME ABC transport with different
targets. Those are actual additional source readouts, not new dynamics.

| Protection policy | Reversible recorders remaining |
|---|---:|
|Measured query only|36|
|One additional target query|4|
|Two additional target queries|1|
|All target queries / entire source vertex|1|

The unique fully source-preserving instrument is the existing XOR recorder:

    (x,b) -> (x,b XOR answer(x)).

This completes a conditional selection result: specifying these protected
observables removes the back-action freedom. The protection policy itself
is explicit, not a theorem that physical observation must satisfy it.

## Consequence for today's physics objective

The uniquely selected fully protected recorder has ZERO source back-action.
It therefore does not yield charge–mass–recoil. Relaxing protection admits
many maps, but the source's permission to construct them does not select
which one occurs physically.

We have reached a concrete input boundary rather than another missing
recovery proof. To choose a nontrivial interaction, one needs a justified
change-permission/control law: which source observables may change and how
the retained controller/memory couples to them. A fitted force, least-change
metric or unexplained gain would simply supply that missing law externally.

The Boolean record is also not automatically a growing retained history:
the selected recorder is involutive, so reusing the same bit twice erases
its first stored answer reversibly. Fresh memory or an execution log is a
separate resource; neither creates a physical time scale or energy supply.

## Verification

    python research/nima/checkers/check_native_instrument_policy_classification.py

54 checks pass, exhaustive over 40,320 reversible maps. The fresh Agda receipt
and source digest of the preceding instrument theorem are checked. This new
36-map classification is exact Python verification, not an Agda census of
36 individually instantiated native fillers.

Receipt: `results/native-instrument-policy-classification.json`.
