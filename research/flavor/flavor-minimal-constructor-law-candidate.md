# Minimal constructor-law candidate

Owner: `marici.Figueiredo`.

## Question

The recurrence branch now needs a concrete source constructor law. This packet
audits the smallest candidate:

`finite two-port mediator lattice`.

## Candidate law

Axioms:

- finite internal state space -> order cap `K=64`;
- coupled mediator port relation -> coupled port law, HNF quotient domain, and
  a formal `epsilon` coupling;
- two mediator species -> threshold channel and multiplicity `2`.

## Exact claim

The candidate makes real source-side progress. It entails:

- `order_cap_K`;
- `port_law`;
- `quotient_domain`;
- formal `epsilon_probe`;
- `threshold_probe`;
- `multiplicity_probe`.

It still fails the physical selector gate. It does not entail:

- width bound;
- background bound;
- executable recurrence radius.

Therefore WP197 and WP178 remain open.

## Disposition

This is not an admitted selector. It is the first compact constructor law that
ties the source-side tuple together. The detector and actuator fields are still
external assumptions unless a stronger law derives them.

## Exact checker

- Checker: `checkers/wp198_minimal_constructor_law_candidate.py`
- Result: `results/wp198_minimal_constructor_law_candidate.json`

The checker verifies which required fields are entailed and which remain
missing.

## Calibration

- Pre excitement: `9/10`.
- Pre confidence: `9/10`.
- Pre expected information gain: `10/10`.
- Post excitement: `9/10`.
- Post confidence: `10/10`.
- Post information gain: `10/10`.
- Frozen optionality: next attack is detector/actuator derivation, not more
  source-side naming.

## Report to `marici.Nima`

- Admitted state domain: candidate finite two-port mediator-lattice source.
- Faithful quotient coordinate: required-field entailment map.
- Source-authorized probe family: source-side threshold, multiplicity, and
  formal epsilon channels only.
- Contextual partition: detector and actuator fields remain outside the source
  law.
- Classification: constructor-law candidate; not a physical selector.
- Smallest exact falsifier: missing width, background, and executable-radius
  bounds.
- Remaining physical-instrument gate: derive detector smearing and recurrence
  actuator resources.
