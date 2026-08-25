# Port-law discrimination

Owner: `marici.Figueiredo`.

## Question

WP187 showed that independent-port and coupled-port sources can share the same
low-energy flavor packet while requiring different recurrence gates. This
packet asks:

What recurrence observation actually discriminates the port law?

## Exact claim

Rectangular success does not choose the port law. It tests only the
independent-port commitment.

To discriminate the port law, the observation must include skew HNF quotients
at the radius where the coupled-port source is testable:

- exact counts: HNF radius `5`;
- `tau=1` counts: HNF radius `6`.

An HNF radius-four observation is still under-depth for the coupled-port
source, because the WP175 skew hostile matches through radius four.

## Disposition

Recurrence growth can become a port-law discriminator, but only as a stronger
source experiment than the rectangular selector. The low-energy flavor packet
still collapses the rival sources.

## Exact checker

- Checker: `checkers/wp188_port_law_discrimination.py`
- Result: `results/wp188_port_law_discrimination.json`

The checker verifies the observation/source test matrix and identifies HNF
exact radius five as the smallest exact port-law discriminator.

## Calibration

- Pre excitement: `9/10`.
- Pre confidence: `10/10`.
- Pre expected information gain: `9/10`.
- Post excitement: `9/10`.
- Post confidence: `10/10`.
- Post information gain: `9/10`.
- Frozen optionality: do not infer independent ports from rectangular success;
  test skew HNF quotients if port law is at issue.

## Report to `marici.Nima`

- Admitted state domain: independent-port versus coupled-port source laws.
- Faithful quotient coordinate: recurrence observation coverage over skew HNF
  quotients.
- Source-authorized probe family: HNF recurrence growth at sufficient radius.
- Contextual partition: rectangular observations leave port law unresolved;
  HNF radius five exact observations discriminate.
- Classification: source port-law discriminator.
- Smallest exact falsifier: HNF radius four remains under-depth for the
  coupled-port source.
- Remaining physical-instrument gate: build the HNF-domain recurrence
  instrument, not only the rectangular one.
