# Instrument-law rival kernel

Owner: `marici.Figueiredo`.

## Question

WP201 closes the conditional selector gate with a sharp radius-six instrument
law. Deutsch's caveat remains:

Is that instrument law hard to vary, or can rival instruments attach to the
same source and change selector authority?

## Exact claim

The same finite two-port mediator-lattice source admits rival instrument laws:

- `I_sharp_radius6`: detector and actuator pass;
- `I_borderline_radius6`: actuator passes, detector fails;
- `I_sharp_radius5`: detector passes, actuator fails.

Only `I_sharp_radius6` authorizes the selector.

Thus WP201 is not a source-only explanation. The sharp instrument law must be
derived from the constructor or independently admitted as part of the physical
experiment.

## Disposition

This preserves WP201 and blocks overclaiming it. Conditional source+instrument
closure is real. Hard-to-vary source explanation is still absent.

## Exact checker

- Checker: `checkers/wp202_instrument_law_rival_kernel.py`
- Result: `results/wp202_instrument_law_rival_kernel.json`

The checker verifies that the same source has different selector outcomes under
three rival instrument laws.

## Calibration

- Pre excitement: `9/10`.
- Pre confidence: `10/10`.
- Pre expected information gain: `9/10`.
- Post excitement: `9/10`.
- Post confidence: `10/10`.
- Post information gain: `9/10`.
- Frozen optionality: distinguish conditional closure from hard-to-vary source
  explanation.

## Report to `marici.Nima`

- Admitted state domain: one source law with rival instrument laws.
- Faithful quotient coordinate: detector/actuator/selector signature.
- Source-authorized probe family: only after instrument law is admitted.
- Contextual partition: same source has passing and failing instrument
  outcomes.
- Classification: instrument-law rival kernel.
- Smallest exact falsifier: same source with borderline detector or radius-five
  actuator fails selector authority.
- Remaining physical-instrument gate: derive or admit the sharp radius-six
  instrument law.
