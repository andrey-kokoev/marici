# A Commutative Context Atlas Does Not Fix Product Orientation

## Bounded question

Does the family of locally commutative readout contexts, even when its static
overlap structure is retained, determine the ordered upstream realization?

## Hostile pair

Take the same two-dimensional complex carrier with the same labelled
observables and compare two products:

- ordinary composition, `a * b = ab`;
- opposite composition, `a *op b = ba`.

The two realizations have the same symmetrized product
`a circle b = (ab + ba)/2`. Consequently, every statement expressible only
through individual commutative contexts and their static Jordan compatibility
is insensitive to the choice of orientation.

For the Pauli observables `X` and `Z`, the symmetrized product is zero in both
realizations. But the ordered words differ: `XZ = -ZX`. The continuation probe
obtained by pairing the ordered word with `Y` changes sign when the product is
reversed. Thus a sequentially authorized experiment distinguishes structures
that the static context atlas identifies.

## Control-theory reading

The context atlas specifies instantaneous output charts. Its overlaps constrain
which charts describe the same present behavioral state. It does not yet specify
the transition monoid: which labelled intervention follows which, or how order
acts on the retained state. Ordinary and opposite multiplication are two
oriented realizations of the same static output geometry.

This isolates the missing datum more precisely than “noncommutativity.” The
missing datum is an orientation of composition, operationally exposed by
authorized sequential continuations. A static atlas can retain the symmetric
part of composition while erasing the antisymmetric part that controls order.

## Consequence for a Marici object

A Marici object cannot generally be reconstructed from commuting Carrier views
plus overlap equalities alone. If its source task distinguishes ordered
interventions, the object must retain one of the following equivalent forms of
additional structure:

- an oriented transition action on contextual states;
- sequential instrument or continuation data;
- a source-authorized rule distinguishing a composite from its reverse;
- enough order-sensitive probes to recover that distinction behaviorally.

This is not permission to insert an arbitrary orientation. Nima's refinement
result applies: when several refined lifts realize one coarse operation,
choosing a lift is a constructor decision requiring source authority. The atlas
establishes compatibility; it does not authorize a control law.

## Claim boundary

The checker supplies a finite exact counterexample to static reconstruction. It
does not prove that every complete contextual system with sequential data
reconstructs a unique noncommutative algebra. Nor does it prove that product
orientation is primitive in every Marici sector. It proves only that any sector
whose task observes ordered continuations cannot quotient orientation away.

## Verification

Run:

```text
python research/sontag/checkers/opposite_orientation_hostile.py
```

The dependency-free checker verifies eight exact identities and writes
`research/sontag/results/opposite_orientation_hostile.json`.
