# Su-32 incoming-prefix neighbourhood generation

## Result

From four actual incoming-prefix neighbourhoods, generated **eight shared
carriers**, their incoming frames, and the next exits of **all sixteen records**.
Every generated four-vertex neighbourhood matches the existing reference exactly;
every identity, colour, polarity tuple and opaque payload is preserved.

The solver receives no carrier head, frame witness, future port list, reference
edge list, or supplied assignment of records to shared carriers. All proposed
edges are checked against the complete native cell geometry. Ambiguities and
missing complementary arrivals remain unresolved instead of being tie-broken.

This is a **conditional local generator**, not a geometry-only or layer-derived
wiring law. Crucially, its incoming b bit is already a route-choice label in the
reference. The result demonstrates how that state steers the native geometry,
not where the state originates.

## Inputs and calibration boundary

Each query contains only an arrival vertex and the arriving records, each with
its previous vertex and retained state. Reference guides are cut after their
first three vertices, before the carrier begins. Inference uses those prefixes;
only the separate checker later reads the withheld suffixes.

The rule is frozen from the previous angular-completion experiment. It is not
refitted here, and this is **not** a new leave-one-junction-out calibration test.
Tests check that the frozen model agrees with every prior-style held-out fit.

## How the carrier and frame are recovered

1. The calibrated a convention identifies the active polarity: p for a=+,
   e for a=−.
2. Group records that agree on a, b and the held polarity. Require exactly two
   complementary active signs; do not group by strand ID or future route.
3. Agreement of active sign with b marks the **oblique** arrival; disagreement
   marks the **straight** arrival.
4. If t is the common arrival vertex and s the previous vertex of the straight
   record, the only possible straight continuation has head **h=2t−s**. The
   implementation enumerates native neighbours and checks this condition rather
   than manufacturing an edge.
5. With d=h−t and o the other incoming arm, require **d·o=−1**. The other arrival
   then supplies the oblique plane witness automatically.
6. Apply the already-calibrated angular rule to each intact record. The generator
   does not use a global flow axis, equatorial phase, nearest-centre ranking,
   coordinate port ordering, or reference successor lookup to select these exits.

Without deciding which incoming record is straight, the learned one-straight /
one-oblique template allows two carrier directions at each tested pair. The b
state resolves the assignment.

| Arrival vertex | b | Generated carrier head | Generated oblique witness | Records |
|---|---|---|---|---|
| (-1,1,1,0) | + | (-1,2,0,0) | (-1,0,1,1) | 2 |
| (-1,1,1,0) | - | (-1,2,1,-1) | (-1,0,2,0) | 2 |
| (0,0,0,1) | + | (0,1,-1,1) | (-1,0,1,1) | 2 |
| (0,0,0,1) | - | (1,0,-1,1) | (0,-1,1,1) | 2 |
| (1,-1,1,0) | + | (2,-1,0,0) | (0,-1,1,1) | 2 |
| (1,-1,1,0) | - | (2,-1,1,-1) | (0,-1,2,0) | 2 |
| (0,0,2,-1) | + | (0,1,2,-2) | (-1,0,2,0) | 2 |
| (0,0,2,-1) | - | (1,0,2,-2) | (0,-1,2,0) | 2 |

## State-ablation and counterfactual controls

- Reordering arrivals and replacing strand IDs with opaque names leaves the
  geometric predictions unchanged.
- Removing supplied b values is rejected; they are not recovered by parsing IDs.
- After erasing b, there are **eight pairs** with the same incoming position,
  remaining declared polarity state (a,p,e), and colour. Their required carrier
  heads differ. With IDs and opaque payloads excluded as routing instructions,
  those inputs cannot identify the original assignment without additional state.
- Flipping b while holding incoming geometry, identities, p/e colours and all
  other polarity values fixed changes the selected carrier for **all sixteen**
  records. This is a counterfactual test of the mechanism, not another reference
  match or a new physical route claim.
- Missing partners and unavailable native carriers remain explicitly unresolved.
- Attempts to supply a future carrier head or frame are rejected by the query
  boundary.

## Meaning of the remaining gap

The reference builder explicitly defines a and b as its successive binary route
choices. Using them successfully is therefore **decoding retained route-choice
state**, not deriving those choices from unlabelled geometry. This distinction
is essential: the incoming records and their meeting vertices are still given
by the input prefixes.

The next useful target is an **incoming-state correspondence**: show that actual
layer path history or lane information supplies the distinguishing state,
especially b, without assigning it by looking at the desired native carrier.
The ablation test says what information must be retained, not how the layers
supply it. No mapping of the eight layers to that state is established here.

No original route, viewer geometry, or inter-layer connection was changed.

## Reproduction

- node --test tests/sulfur-neighbourhood-generator.test.mjs
- node scripts/check-sulfur-neighbourhood.mjs
- Generator: research/realization-tower/sulfur-neighbourhood-generator.mjs
- Frozen calibration: research/realization-tower/sulfur-upper-local-calibration.v1.json
- Full prefix queries, generated neighbourhoods, comparisons, state-ablation
  witnesses and source hashes: results/sulfur-neighbourhood-v1/verification.json
