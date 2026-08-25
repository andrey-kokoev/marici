# Two-port source detector entailment

Owner: `marici.Figueiredo`.

## Question

Can the finite two-port mediator-lattice source serve as the concrete
source-derived detector dynamics required by WP219?

## Test

The source-side tuple entails:

- `order_cap_K64`;
- HNF quotient domain;
- coupled port law;
- formal epsilon probe;
- threshold probe;
- multiplicity probe;
- source coupling/descent.

It does not entail:

- strict interval comparator;
- single-fault sentinel;
- exchangeable width/background channels;
- executable operation;
- calibrated error contract.

Those are exactly the fields added by the self-reading declaration.

## Disposition

The finite two-port source is not enough. It supplies useful source structure
and source coupling/descent, but it does not derive the detector tuple. The
self-reading law formally covers the WP219 requirements only by appending the
missing detector fields. WP204 remains the exact hostile falsifier: the same
source-side tuple admits different self-reading variants.

## Exact checker

- Checker: `checkers/wp220_two_port_source_detector_entailment.py`
- Result: `results/wp220_two_port_source_detector_entailment.json`

The checker verifies which WP219 fields are entailed by the source alone and
which are added by self-reading declaration.

## Calibration

- Pre excitement: `7/10`.
- Pre confidence: `10/10`.
- Pre expected information gain: `8/10`.
- Post excitement: `7/10`.
- Post confidence: `10/10`.
- Post information gain: `8/10`.
- Frozen optionality: next step should derive one of the missing detector
  fields, not restate the two-port source tuple.

## Report to `marici.Nima`

- Admitted state domain: finite two-port mediator-lattice source and
  self-reading extensions.
- Faithful quotient coordinate: source-field entailment map into the WP219
  detector tuple over original `physical16`.
- Source-authorized probe family: source-side threshold, multiplicity, and
  formal epsilon channels; not the detector tuple.
- Contextual partition: source-only tuple, self-reading declaration, and
  variant self-reading constants.
- Classification: two-port source detector-entailment no-go.
- Smallest exact falsifier: same two-port source-side tuple with variant
  self-reading detector constants, as in WP204.
- Remaining physical-instrument gate: derive the self-reading additions from a
  source action rather than appending them.
