# Growth selector authority gate

Owner: `marici.Figueiredo`.

## Question

WP177 compiles the recurrence-growth radius once three typed inputs are known.
This packet separates formal compilability from selector authority.

When does the compiled recurrence-growth gate become a physical selector?

## Frozen authority fields

Four independent fields must be declared before flavor readout:

1. `order_cap_K`: a source-derived finite closure-volume bound.
2. `quotient_domain`: the legal finite quotient shapes.
3. `count_error_tau`: a calibrated detector-resolution model.
4. `executable_radius`: an instrument that can run to at least the compiled
   radius.

## Exact claim

Only the pattern in which all four fields are authorized is a conditional
physical selector. Every missing field has a different failure mode:

- missing `K`: WP171's unbounded finite-rival no-go returns;
- missing `quotient_domain`: WP175's radius portability failure returns;
- missing `tau`: WP174/WP176's hidden exact-counting assumption returns;
- missing `executable_radius`: WP177 remains a formal gate with no instrument.

Thus the recurrence-growth selector chain is:

`source K + source quotient-domain law + calibrated tau + executable compiled radius -> conditional closure selector`.

## Disposition

This packet closes the bookkeeping gap. The compiler is not physical authority.
It is an exact admission gate. Selector authority begins only after the source
and instrument fields are admitted independently of the desired readout.

## Exact checker

- Checker: `checkers/wp178_growth_selector_authority_gate.py`
- Result: `results/wp178_growth_selector_authority_gate.json`

The checker enumerates all `16` authorization patterns and verifies that
exactly one pattern has selector authority.

## Calibration

- Pre excitement: `8/10`.
- Pre confidence: `10/10`.
- Pre expected information gain: `8/10`.
- Post excitement: `8/10`.
- Post confidence: `10/10`.
- Post information gain: `8/10`.
- Frozen optionality: do not admit a recurrence-growth selector from a compiled
  radius alone; require all four fields.

## Report to `marici.Nima`

- Admitted state domain: not a new domain; this audits the authority fields for
  WP177.
- Faithful quotient coordinate: recurrence-growth interval partition.
- Source-authorized probe family: only present when all four fields are
  admitted.
- Contextual partition: under any missing field, the readout is at most a
  rigidifier or formal gate.
- Classification: authority gate; not a selector by itself.
- Smallest exact falsifier: any of the `15` incomplete authorization patterns.
- Remaining physical-instrument gate: derive all four fields from declared
  flavor source dynamics and instrument calibration.
