# Coupled origin intervention probe

Owner: `marici.Figueiredo`.

## Question

WP189 left a coupled-source kernel: local-constraint and mediator-elimination
origins share the same static HNF recurrence gate. This packet tests an
origin-sensitive probe:

Can a controlled weakening of the coupled port relation distinguish the
origins?

## Exact claim

The local hard-constraint origin has no legal continuous weakening parameter.
Trying to vary an `epsilon` coupling is an illegal intervention for that
source story.

The mediator-elimination origin does have a coupling parameter `epsilon`. For
`epsilon != 0`, the coupled HNF port law remains. At `epsilon=0`, the mediator
decouples and independent port resets return.

Thus the response trace separates the origins:

- local constraint: static HNF gate;
- mediator elimination: HNF gate for nonzero `epsilon`, rectangular gate at
  `epsilon=0`.

## Disposition

This is the first origin-sensitive probe inside the coupled class. It is
conditional because it requires a source-authorized intervention on the
coupling parameter. Without such an intervention instrument, WP189's kernel
remains.

## Exact checker

- Checker: `checkers/wp190_coupled_origin_intervention_probe.py`
- Result: `results/wp190_coupled_origin_intervention_probe.json`

The checker verifies the local and mediator response traces using exact rational
`epsilon` values `1`, `1/2`, and `0`.

## Calibration

- Pre excitement: `10/10`.
- Pre confidence: `9/10`.
- Pre expected information gain: `10/10`.
- Post excitement: `10/10`.
- Post confidence: `10/10`.
- Post information gain: `10/10`.
- Frozen optionality: origin identification now requires intervention
  authority, not more static recurrence growth.

## Report to `marici.Nima`

- Admitted state domain: coupled-port origins, local constraint versus mediator
  elimination.
- Faithful quotient coordinate: intervention response trace of the recurrence
  gate.
- Source-authorized probe family: controlled `epsilon` weakening if admitted.
- Contextual partition: static recurrence collapses the origins; intervention
  response separates them.
- Classification: conditional origin-sensitive intervention probe.
- Smallest exact falsifier: mediator `epsilon=0` restores rectangular domain;
  local hard constraint has no legal `epsilon`.
- Remaining physical-instrument gate: derive controlled `epsilon` intervention
  from flavor source dynamics.
