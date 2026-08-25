# Exponent-bound closure certificate

Owner: `marici.Figueiredo`.

## Question

WP167 proves a no-go for certifying infinite two-port closure with a bounded
relation protocol when finite rivals have unbounded period. This packet tests
the exact positive boundary:

If the source independently bounds every finite rival's exponent by `E`, does
the bounded relation protocol become faithful?

## Frozen domain

- State domain: two labelled nontrivial finite abelian closure rivals with
  generator periods `n1,n2 <= E`, plus the infinite free closure `Z^2`.
- Faithful coordinate: exact identity-relation language in
  `+e1,-e1,+e2,-e2`.
- Instrument: exhaustive relation/fusion test through word depth `E`.
- Frozen numerical audit value: `E=8`.

The source exponent cap is part of the state domain. It is not inferred from
the relation readout.

## Exact claim

For a finite rival `(Z/n1Z) x (Z/n2Z)` with `n1,n2 <= E`, at least one
nontrivial port relation appears by depth `E`: `e1^n1=1` and `e2^n2=1`. No
corresponding positive-length relation exists in `Z^2`.

Thus the exhaustive depth-`E` relation protocol separates `Z^2` from every
finite rival in the frozen exponent-bounded domain.

The bound is sharp. `(Z/EZ)^2` has the same relation language as `Z^2` through
depth `E-1`, because no nonzero coordinate sum of a word that short can be a
multiple of `E`. The first separating witness is `+e1^E`.

For `E=8`, the hostile finite rival is `(Z/8Z)^2`, order `64`, matching `Z^2`
through depth seven and separating at depth eight.

## Disposition

This is the positive complement of WP167, not a contradiction. The relation
protocol is a conditional selector only after the source supplies a true
exponent cap. Without that cap, the same finite-depth protocol remains merely
a presentation rigidifier because a larger finite rival can always be chosen.

Selector authority therefore factors as:

`source exponent cap -> finite relation protocol -> closure class readout`.

The first arrow is the live physical gate. If the exponent cap is fitted from
the relation data, selector authority is circular.

## Exact checker

- Checker: `checkers/wp168_exponent_bound_closure_certificate.py`
- Result: `results/wp168_exponent_bound_closure_certificate.json`

The checker enumerates all rectangular two-port finite rivals with
`2 <= n1,n2 <= 8`, confirms that every rival is separated from `Z^2` by depth
eight, and verifies sharpness by showing that `(Z/8Z)^2` matches through
depth seven.

## Calibration

- Pre excitement: `9/10`.
- Pre confidence: `9/10`.
- Pre expected information gain: `8/10`.
- Post excitement: `9/10`.
- Post confidence: `10/10`.
- Post information gain: `8/10`.
- Frozen optionality: search for a source-derived exponent cap before
  claiming closure selection; otherwise keep WP167 as the governing no-go.

## Report to `marici.Nima`

- Admitted state domain: two-port finite abelian rivals with source-bound
  exponent `E`, plus `Z^2`.
- Faithful quotient coordinate: identity-relation language in the labelled
  closure generators.
- Source-authorized probe family: exhaustive relation/fusion tests through
  depth `E`, conditional on the source exponent cap.
- Contextual partition: at `E=8`, all finite rivals with `n1,n2 <= 8` are
  separated from `Z^2`; `(Z/8Z)^2` remains equivalent through depth seven.
- Classification: conditional selector if the cap is source-derived; otherwise
  rigidifier only.
- Smallest exact falsifier to under-depth certification: `Z^2` versus
  `(Z/8Z)^2`, indistinguishable through depth seven.
- Remaining physical-instrument gate: derive the exponent cap from flavor
  source dynamics or geometry, not from the closure readout.
