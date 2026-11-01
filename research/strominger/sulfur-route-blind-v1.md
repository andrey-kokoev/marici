# Su-32 route-blind local continuation test

## Result: the old rule is incomplete; an angular completion passes

The plane-only rule leaves **three native departures in every case**. It keeps
the correct exit but uniquely predicts none of the sixteen observed passages.
Knowing only that flow does not ascend is still insufficient. Requiring an
explicit equatorial phase resolves eight cases, leaving both rim senses for
the other eight. Picking the nearest centre point gets four exits wrong.

A more precise, reference-calibrated angular rule uniquely predicts **16/16**
actual next edges without receiving the target outgoing-port pair. Its model
is learned separately for each target carrier from the other seven carriers;
both target records are excluded. Target routes are consulted afterward by the
checker, not by the candidate-generating solver.

This completes a conditional **one-step generativity test**. It does not yet
generate the carrier itself, a complete strand route, or wiring from the layers.

## What the solver receives

- The complete native radius-one cell geometry: 51 cells, 44 vertices, 168 edges.
  This includes every unit edge, not just edges used by the reference wiring.
- The known oriented carrier (tail and head), the current incoming point, and
  its polarity tuple (a,b,p,e).
- An oblique incoming point that fixes the input plane. This is obtained from
  the two observed incoming prefixes, without reading their successors.
- A model calibrated on the other seven carriers. No strand ID or target
  next-port table is supplied to the solver.
- A declared flow axis for diagnostic alternatives only. The successful angular
  profile does not use equatorial phase, height, surface flags or radial ranking.

Candidate generation imports the native cell builder only. Unexpected query
fields, including injected future ports, are rejected. Tests delete all target
successor and output-port fields and recover the same predictions. Ties are
returned as ambiguities, never resolved by list order.

## The completed local rule

Use native coordinates. Let d be the forward carrier vector and o the oblique
incoming arm directed outward from the tail. Both have squared length 2 and
**d·o = −1**. Encode polarity signs as ±1 and put **χ = a b p e**.
The active sign s is p when a=+, and e when a=−.

- **s=−:** outgoing direction **w = χ(d+o)**. This is coplanar.
- **s=+:** select the unit native direction satisfying **d·w=−1** and
  **o·w=+1**. This is the skew departure.

Equivalently, project the oblique arm and departure perpendicular to d:

| Active sign | Cosine to forward carrier | Transverse cosine to oblique arm |
|---|---|---|
| + | −1/2 | 1/3 |
| − | χ/2 | χ |

These are angles against the **forward** carrier, not the backward carrier arm
at its head. The parity uses already-retained polarity state; no new payload
field is invented. The earlier planar/skew classification omitted these angular
constraints and therefore could not identify a unique native exit.

Calibration searches a bounded family: one coefficient times one product of a
subset of the four polarity signs, separately for each angular quantity and
active-sign class. Constants are included. There is no table indexed by identity,
carrier, or coordinates. Each held-out fit identifies the same constant/χ rule.
Ambiguous or inconsistent calibration is rejected rather than tie-broken.

## Checks beyond the occupied reference ports

Every reference head has six non-backtracking candidate edges in the radius-one
geometry. In a larger native sector it has the full twelve-neighbor lattice
star. The completed rule still uniquely selects all sixteen correct exits there,
even when the diagnostic flow axis and candidate order are changed. Uniqueness
is therefore not produced by deleting unoccupied edges or by boundary truncation.

There are 12 unit native directions and **48** compatible ordered (d,o) frames.
For all **16** polarity tuples in each frame, exactly one direction satisfies the
completed rule: **768 synthetic uniqueness checks**. The tests exercise the
fitted predictor on these frames; the fresh checker also enumerates roots with
exact integer inner products as an independent certificate.

For an algebraic explanation, write d=e_i−e_j. There are two cases:

- o=e_j−e_k: the + departure is e_j−e_l.
- o=e_k−e_i: the + departure is e_l−e_i.

Here l is the remaining fourth index. The − departure is ±(d+o), also a unit
native direction. These statements establish local existence and uniqueness;
they do not establish globally valid or physical wiring for the synthetic cases.

## Diagnostic alternatives

Every row below is evaluated on the same sixteen held-out target passages.
Additional constraints are explicit hypotheses, not consequences of the original
plane-only rule. Rejected means that the reference exit is absent, even if some
other candidate is uniquely selected.

| Constraints | Unique correct | Ambiguous, truth retained | Reference rejected |
|---|---|---|---|
| plane only | 0 | 16 | 0 |
| plane + nonascending flow | 0 | 16 | 0 |
| plane + equatorial phase | 8 | 8 | 0 |
| plane + equatorial phase + surface | 0 | 8 | 8 |
| plane + equatorial phase + interior | 8 | 0 | 8 |
| plane + equatorial phase + nearest centre | 12 | 0 | 4 |
| plane + equatorial surface + positive chirality | 0 | 0 | 16 |
| plane + equatorial surface + negative chirality | 8 | 0 | 8 |
| plane + fitted angular signature | 16 | 0 | 0 |

## Actual withheld exits

| Motif | Reference identity (checker only) | Active sign | Plane-only choices | Completed choices | Verified next point |
|---|---|---|---|---|---|
| 1 | `wire:++++` | + | 3 | 1 | (0,1,0,0) |
| 1 | `wire:++-+` | - | 3 | 1 | (-1,2,1,-1) |
| 2 | `wire:+-++` | + | 3 | 1 | (0,1,1,-1) |
| 2 | `wire:+--+` | - | 3 | 1 | (-1,2,2,-2) |
| 3 | `wire:-+++` | + | 3 | 1 | (0,1,0,0) |
| 3 | `wire:-++-` | - | 3 | 1 | (-1,2,-1,1) |
| 4 | `wire:--++` | + | 3 | 1 | (1,0,0,0) |
| 4 | `wire:--+-` | - | 3 | 1 | (0,1,-1,1) |
| 5 | `wire:+++-` | + | 3 | 1 | (1,0,0,0) |
| 5 | `wire:++--` | - | 3 | 1 | (2,-1,-1,1) |
| 6 | `wire:+-+-` | + | 3 | 1 | (1,0,1,-1) |
| 6 | `wire:+---` | - | 3 | 1 | (2,-1,0,0) |
| 7 | `wire:-+-+` | + | 3 | 1 | (0,1,1,-1) |
| 7 | `wire:-+--` | - | 3 | 1 | (1,0,2,-2) |
| 8 | `wire:---+` | + | 3 | 1 | (1,0,1,-1) |
| 8 | `wire:----` | - | 3 | 1 | (2,-1,2,-2) |

## Limits and next gate

The angular completion was formulated during this investigation. Its
leave-one-carrier-out tests are within-reference checks, not an independent
validation of the discovery procedure. Its sign conventions are calibrated to
an existing candidate wiring whose middle matching was explicitly chosen.
They have not been derived from the eight-layer reflection operations.

The result is conditional on a known carrier, its incoming plane, and a labelled
polarity tuple. It does not yet determine those inputs from the layer geometry,
nor prove conservation, closure, or absence of collisions across a whole route.
The productive next gate is to determine whether a layer neighbourhood supplies
that frame and polarity context without using the target wiring as a lookup.
No viewer geometry, original route, or inter-layer connection was changed.

## Reproduction

- node --test tests/sulfur-route-blind.test.mjs
- node scripts/check-sulfur-route-blind.mjs
- Solver: research/realization-tower/sulfur-route-blind.mjs
- Separate calibration/checker: scripts/lib/sulfur-route-blind-probe.mjs
- Full queries, models, candidates, scores and source hashes:
  results/sulfur-route-blind-v1/verification.json
