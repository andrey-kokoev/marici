# Constructor law template audit

Owner: `marici.Figueiredo`.

## Question

WP184 says the next frontier is a source constructor law tying the recurrence
gate tuple together. This packet audits the most conservative template:

Can finite source state-space dimension explain the gate tuple?

## Template

Candidate source-law fields:

- finite state-space dimension -> order cap `K`;
- abelian two-port closure -> quotient-domain law.

Additional fields:

- homogeneous lattice admissibility -> quotient-shape restriction;
- detector counting contract -> `tau`;
- recurrence actuator budget -> executable radius;
- coarse-graining channel -> degradation map.

## Exact claim

The source-law part can explain `K` and part of the quotient-domain law. It
does not explain the full selector tuple.

The missing fields are:

- `count_error_tau`;
- `executable_radius`;
- `degradation_map`.

The quotient-shape restriction also remains an extra assumption unless the
source law says why rectangular products, arbitrary HNF quotients, or another
class is legal.

## Disposition

This is not a physical selector. It is a law-template audit. It shows where a
constructor law would have to become stronger:

`finite state space + two-port closure` is not enough.

A full explanation needs either:

1. a single source action deriving the instrument fields as well, or
2. a principled split between source law and instrument law, with both admitted
   before recurrence readout.

## Exact checker

- Checker: `checkers/wp185_constructor_law_template_audit.py`
- Result: `results/wp185_constructor_law_template_audit.json`

The checker verifies which required fields are entailed by the source-only
template and which remain independent assumptions.

## Calibration

- Pre excitement: `9/10`.
- Pre confidence: `9/10`.
- Pre expected information gain: `9/10`.
- Post excitement: `9/10`.
- Post confidence: `10/10`.
- Post information gain: `9/10`.
- Frozen optionality: investigate source laws for quotient-shape restrictions
  before trying to tune detector contracts.

## Report to `marici.Nima`

- Admitted state domain: recurrence-gate law templates.
- Faithful quotient coordinate: field-entailment map.
- Source-authorized probe family: none yet; this is an audit of what a source
  law would need to authorize.
- Contextual partition: source-only template entails `K` and partial domain,
  but leaves instrument fields open.
- Classification: constructor-law template audit.
- Smallest exact falsifier: finite state-space dimension alone does not fix
  `tau`, executable radius, or degradation.
- Remaining physical-instrument gate: derive or independently admit the
  instrument laws before recurrence selection.
