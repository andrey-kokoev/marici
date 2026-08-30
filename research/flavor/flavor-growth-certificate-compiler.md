# Growth certificate compiler

Owner: `marici.Figueiredo`.

## Question

WP173-WP176 show that recurrence-growth selector authority depends on three
typed inputs: finite-order cap, legal finite-quotient domain, and detector
resolution. This packet turns those examples into a small exact compiler.

## Frozen domain

- Source cap: finite closure order `K`.
- Legal quotient domains: rectangular products and arbitrary HNF quotients.
- Detector model: absolute count error `tau`.
- Audited range: `4 <= K <= 64`, `tau in {0,1}`.

## Exact claim

For each typed triple `(K, domain, tau)`, the certificate radius is the first
radius `R` such that

`min_finite [growth_Z2(R)-growth_finite(R)] > 2 tau`.

At `K=64`, the compiled radii reproduce the corrected chain:

- rectangular, exact: `4`;
- rectangular, `tau=1`: `5`;
- arbitrary HNF, exact: `5`;
- arbitrary HNF, `tau=1`: `6`.

The compiler is not a new selector. It is the admission gate that prevents
porting a radius or detector margin across a changed state domain.

## Exact checker

- Checker: `checkers/wp177_growth_certificate_compiler.py`
- Result: `results/wp177_growth_certificate_compiler.json`

The checker enumerates both quotient domains for every `K` from `4` through
`64`, compiles the first robust radius for `tau=0` and `tau=1`, and verifies
monotonicity and the known WP173-WP176 values.

## Calibration

- Pre excitement: `9/10`.
- Pre confidence: `10/10`.
- Pre expected information gain: `8/10`.
- Post excitement: `9/10`.
- Post confidence: `10/10`.
- Post information gain: `8/10`.
- Frozen optionality: recurrence-growth claims must cite the compiled gate or
  provide an equivalent exact margin proof.

## Report to `marici.Nima`

- Admitted state domain: parameterized finite quotient families of `Z^2`.
- Faithful quotient coordinate: recurrence-growth counts with error intervals.
- Source-authorized probe family: conditional growth windows after `K`, domain,
  `tau`, and executable radius are typed.
- Contextual partition: computed by the compiled radius for the declared
  triple.
- Classification: exact gate compiler; not itself a physical selector.
- Smallest exact falsifier class: any claim that imports the rectangular
  radius-four gate into arbitrary HNF quotients or noisy counts.
- Remaining physical-instrument gate: source must provide `K`, legal quotient
  domain, count calibration, and executable recurrence radius.
