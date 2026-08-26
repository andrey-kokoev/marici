# Delayed-choice quantum eraser as record factorization

## Question

Can the apparent retrocausal puzzle of the delayed-choice quantum eraser be reduced to an exact distinction between local trace-forgetting and later classical record conditioning?

## Frozen construction

Use a two-qubit path--marker state with perfectly correlated labels. The signal port has a phase-selectable two-output interferometric detector. The marker port can be read either in the which-path basis or in the complementary eraser basis.

Every detector record is represented by a local Lüders instrument. A joint record is therefore a subnormalized continuation state. Its trace is the associated record probability.

The calculation uses four phase samples: zero, one quarter turn, one half turn, and three quarter turns. This discrete experiment is enough to distinguish a flat pattern from complementary fringe and antifringe patterns using exact rational complex arithmetic.

## Two readout maps

The same joint continuation admits two different readouts.

The local trace-forgetting readout sums over the unobserved marker record. It produces a signal probability of one half at either signal detector for every phase and for either later marker basis.

The classical-join readout retains trial identifiers and conditions the signal records on an eraser-basis marker record. The two conditioned signal patterns are complementary. One has probabilities 1, 1/2, 0, 1/2 across the four phase samples; the other has 0, 1/2, 1, 1/2. Their equally weighted sum is flat.

Nothing is erased from an earlier physical record. The later join chooses a partition of an already defined joint record table. Without that join, neither conditional pattern is locally available.

## Delayed-choice statement

Signal and marker instruments act on different tensor factors, so their exact matrix representatives commute. Applying the signal instrument first or the marker instrument first produces the same subnormalized joint continuation for every setting and record pair. This is the finite absence-of-retrocausality theorem in the representation.

It does not assert a preferred time ordering for spacelike events. It asserts only that the joint probabilities and stable local records are invariant under the two algebraic evaluation orders.

## Decoherence hostile

Complete dephasing of the signal path before detection removes the off-diagonal path coherence. The checker verifies that the two eraser-conditioned patterns then both become flat. Classical conditioning can reveal preserved coherence; it cannot manufacture coherence after the continuation law has lost it.

## What becomes obvious

The word "eraser" suggests that a later action changes whether an earlier photon interfered. The factorization shows instead that three objects had been conflated:

1. the flat local signal record stream;
2. the joint signal--marker record law;
3. the conditioned subensembles constructed by a later classical join.

Once those maps are typed separately, the apparent backward influence disappears. This is a clarification of standard quantum mechanics, not a new physical theory or an empirical discrepancy with current science.

## Claim boundary

This is a finite exact two-path, two-marker-level, four-phase theorem with ideal projective instruments. It does not model detector loss, finite visibility, timing-window bias, multipair emission, or a loophole-free laboratory realization. It does not select an interpretation of measurement.

## Verification

Run:

```text
python research/aspect/checkers/check_delayed_choice_quantum_eraser_factorization.py
```

The checker is dependency-free and uses exact rational complex matrices.
