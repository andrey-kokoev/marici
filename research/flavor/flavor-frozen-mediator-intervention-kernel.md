# Frozen mediator intervention kernel

Owner: `marici.Figueiredo`.

## Question

WP190 separated local hard constraints from mediator elimination by varying a
coupling `epsilon` through zero. This packet tests the hostile case:

What if the mediator coupling exists but is frozen away from zero?

## Exact claim

If the authorized intervention family cannot reach `epsilon=0`, then a
mediator-elimination source can remain observationally equivalent to a hard
local constraint.

Under the restricted intervention family:

- local hard constraint -> HNF gate `5/6`;
- frozen nonzero mediator -> HNF gate `5/6`;
- zero-accessible mediator -> HNF gate `5/6` and rectangular gate `4/5` at
  `epsilon=0`.

Thus WP190's discriminator is faithful only relative to an intervention family
that includes zero-coupling access.

## Disposition

This is the expected hostile refinement. Intervention existence is not enough;
the accessible control range matters. A mediator origin is not identified unless
the source authorizes a control path that changes the recurrence gate, or a
different threshold/coupling probe is admitted.

## Exact checker

- Checker: `checkers/wp191_frozen_mediator_intervention_kernel.py`
- Result: `results/wp191_frozen_mediator_intervention_kernel.json`

The checker compares the observable recurrence-gate traces for a local
constraint, a frozen nonzero mediator, and a zero-accessible mediator.

## Calibration

- Pre excitement: `9/10`.
- Pre confidence: `10/10`.
- Pre expected information gain: `9/10`.
- Post excitement: `9/10`.
- Post confidence: `10/10`.
- Post information gain: `9/10`.
- Frozen optionality: every intervention probe must state accessible control
  range, not only the formal parameter.

## Report to `marici.Nima`

- Admitted state domain: local and mediator coupled origins with restricted
  intervention families.
- Faithful quotient coordinate: accessible `epsilon` response trace.
- Source-authorized probe family: only the declared `epsilon` controls.
- Contextual partition: local constraint and frozen nonzero mediator remain in
  the same class; zero-accessible mediator separates.
- Classification: intervention-family kernel.
- Smallest exact falsifier: local constraint and frozen mediator both produce
  only HNF `5/6`.
- Remaining physical-instrument gate: derive zero-coupling access or an
  alternative origin-sensitive threshold probe.
