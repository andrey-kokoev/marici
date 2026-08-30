# Open-world origin rival

Owner: `marici.Figueiredo`.

## Question

WP193 proved joint faithfulness for threshold plus `epsilon` probes on a frozen
three-origin class. This packet tests open-world stability:

Does the joint probe remain faithful after adding a new origin?

## Hostile expansion

Add a fourth origin:

`composite_hidden_mediator`.

It shares the same probe signature as the frozen nonzero mediator:

- threshold vector: `(false,true,false)`;
- epsilon trace: `("hnf")`.

## Exact claim

The WP193 joint probe remains faithful on the original three-origin class, but
not on the expanded four-origin class. The new origin collides with the frozen
nonzero mediator.

Thus:

`joint faithfulness is domain-relative`.

The durable rule reappears:

`finite fiber != singleton fiber`.

## Disposition

This does not invalidate WP193. It prevents overclaiming it. Before claiming
source identification, the origin domain must be closed by source theory, or a
new probe must separate the open-world rival.

## Exact checker

- Checker: `checkers/wp194_open_world_origin_rival.py`
- Result: `results/wp194_open_world_origin_rival.json`

The checker verifies discreteness on the three-origin domain and a collision
after adding the fourth origin.

## Calibration

- Pre excitement: `8/10`.
- Pre confidence: `10/10`.
- Pre expected information gain: `9/10`.
- Post excitement: `8/10`.
- Post confidence: `10/10`.
- Post information gain: `9/10`.
- Frozen optionality: every joint-faithfulness result must carry its admitted
  source domain explicitly.

## Report to `marici.Nima`

- Admitted state domain: three-origin base class plus open-world rival.
- Faithful quotient coordinate: joint threshold and epsilon signature.
- Source-authorized probe family: unchanged from WP193.
- Contextual partition: base partition is discrete; expanded partition
  collides frozen mediator with composite hidden mediator.
- Classification: open-world domain-expansion falsifier.
- Smallest exact falsifier: composite hidden mediator with same signature as
  frozen nonzero mediator.
- Remaining physical-instrument gate: close the source-origin domain or add an
  origin-sensitive probe for the new rival.
