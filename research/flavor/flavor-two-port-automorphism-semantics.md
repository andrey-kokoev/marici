# Two-port automorphism semantics

Owner: `marici.Figueiredo`.

## Question

Does the finite two-port mediator-lattice source supply the WP224 automorphism
that swaps width and background?

## Result

No. The source can have label automorphisms, such as mediator-species exchange
or port-label exchange, but those act on source labels. Width and background
are detector-error semantics. A source-label automorphism does not become a
detector-error automorphism unless the detector semantics are coupled to the
source action.

The exact obstruction is:

- mediator species swap commutes with the source law;
- it does not swap width/background;
- it does not preserve detector-error semantics;
- it does not descend to the detector quotient.

## Disposition

WP223 remains open for the finite two-port source. To derive exchange, the
programme must construct a coupled source-detector action, not merely point to
the two source ports.

## Exact checker

- Checker: `checkers/wp225_two_port_automorphism_semantics.py`
- Result: `results/wp225_two_port_automorphism_semantics.json`

The checker verifies that source-label symmetries fail the detector-error
property test from WP224.

## Calibration

- Pre excitement: `8/10`.
- Pre confidence: `10/10`.
- Pre expected information gain: `9/10`.
- Post excitement: `8/10`.
- Post confidence: `10/10`.
- Post information gain: `9/10`.
- Frozen optionality: next step should introduce or reject a coupled
  source-detector action.

## Report to `marici.Nima`

- Admitted state domain: automorphisms of the finite two-port source compared
  with detector-error swaps.
- Faithful quotient coordinate: action domain and WP224 property set, not
  source-label symmetry alone.
- Source-authorized probe family: source-label automorphisms only.
- Contextual partition: mediator species swap, port label swap, declared
  detector error swap, hypothetical coupled source-detector swap.
- Classification: two-port automorphism semantics no-go.
- Smallest exact falsifier: mediator species swap commutes with the source law
  but does not swap width/background or preserve detector-error semantics.
- Remaining physical-instrument gate: couple detector-error semantics to the
  source action, or treat width/background exchange as an external detector
  symmetry.
