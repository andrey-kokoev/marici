# Frozen history-dependent four-mode codec: restricted success, missing source selection

## Candidate fixed before testing

The preceding fixed-endpoint codec was falsified. Here the encoding may depend on retained history, but its initial admissible sector is fixed from an existing source candidate rather than adjusted after a failed path.

Use the stored full-five N projector reduction. Its collective return is

```
N = m m^dagger,
m = (0,1,1,1,0)/sqrt(3).
```

Choose `ker(N)` as the four-dimensional sector. The initial codec E uses the existing two active contrasts plus the two outside context coordinates. Exactly,

```
E^dagger E = I4,
E E^dagger = I5-N,
(2I-L-G)E = E.
```

Thus the candidate is the unit-defect sector inside this particular five-mode binding. It is not selected merely by finding four arbitrary columns. It still needs a source reason why the signed wire occupies this sector.

For history h, freeze the rule `E_h=Pi_h E_root`. The P-root codec is pulled back through the existing PN coefficient map. No changes to this rule are made in response to the tests.

## What passed

Every transported codec remains isometric. For the two stored native paths used by the existing full-five field candidate, the endpoint coefficient encodings differ, while the encoded physical-field columns agree after applying their respective retained field bindings.

This is the expected escape from the five-cycle fixed-codec obstruction. It is an exact matrix check against the existing conditional field-binding receipt, not a fresh derivation of that candidate's physical couplings or a certification of the complete assemblies.

**The restricted-domain history-dependent candidate is not falsified by this test.**

## What fails if promoted beyond that restriction

The omitted mean m is a genuine retained native state:

```
||m||^2=1,
N m=m,
E^dagger m=0.
```

It and zero have identical four-mode decodings. Therefore this is not a faithful encoding of the unrestricted five-slot packet. Calling the omitted mode gauge or zero would contradict the actual return operator.

There is also a counterexample to reapplying the same local sector condition after every advance. The outside-slot vector `(0,0,0,0,1)` initially belongs to `ker(N)`. After the actual NN permutation, its projection onto the local mean has norm squared `1/3`. A fixed current-reader `ker(N)` is not invariant. Only the explicitly transported projector supplies the successful admissible sector.

These are failures of unrestricted faithfulness and fixed-current-sector invariance. They are not counterexamples inside the declared transported sector; the distinctions must not be hidden.

## What the experiment resolves

A mathematically valid four-dimensional, history-dependent model can be made from the existing candidate operators. More endpoint replay cannot determine whether this is the operator's signed P/E wire.

The missing source statement is now concrete:

> Does the arriving signed wire exclude the collective-return component, and is its admissibility projector transported with the retained coefficient frame rather than reset by the current local reader?

The current signed-pair specification does not supply that statement. It also does not give an alternative rule deriving the mean from four independently retained wire records. The candidate remains unbound until such a rule is derived, not merely assumed to obtain the desired rank.

The broad existential conjecture has therefore **not** been falsified. Neither has it been validated by this restricted construction. No new state is discarded from the actual packet implementation, and no physical charge, route, boundary law or renderer is changed.

## Replay

```sh
python research/strominger/checkers/check_history_dependent_four_mode_codec.py --record
```

Receipt: `results/history-dependent-four-mode-codec-v1/verification.json`.
The checker uses exact multiradical arithmetic and reads the existing field candidate without rewriting it. It retains the codec, omitted-mode witness, mean-leak counterexample, path-dependent encodings, source hashes and false admission flags.
