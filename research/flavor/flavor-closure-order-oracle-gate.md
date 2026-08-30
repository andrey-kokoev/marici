# Closure-order oracle gate

Owner: `marici.Figueiredo`.

## Question

WP167-WP169 close the finite relation-test route. This packet tests the other
escape: a nonlocal readout that directly reports whether the generated closure
is finite or infinite.

Does such a readout produce a selector?

## Frozen domain

- State domain: two labelled finite abelian closures
  `(Z/n1Z) x (Z/n2Z)`, with `2 <= n1,n2 <= 8`, plus the infinite free closure
  `Z^2`.
- Formal probe: exact closure order, with value `infinite` for `Z^2`.
- Comparison probe: exact closure exponent.
- Relation baseline: WP167-WP169 word-depth instruments.

## Exact claim

An exact closure-order readout separates `Z^2` from every finite rival in one
shot. So does an exact closure-exponent readout.

But this is not a bounded relation/fusion protocol. It is a new nonlocal probe
family. It changes the admitted readout, and therefore cannot inherit selector
authority from WP168's relation instrument.

The readout also does not fully identify finite source stories. For example:

- `(Z/2Z) x (Z/6Z)` and `(Z/3Z) x (Z/4Z)` both have order `12`.
- `(Z/2Z) x (Z/6Z)` and `(Z/3Z) x (Z/6Z)` both have exponent `6`.

Thus even the formal oracle is only a finite-versus-infinite selector on this
domain, not a complete source identifier.

## Disposition

The order oracle is the precise shape of the missing nonlocal escape. If flavor
source dynamics supplies a physical closure-order, return-volume, or recurrence
growth instrument, the closure question becomes a genuine relational
experiment. Until then, it is a formal oracle.

This matters for the Deutsch-Popperian audit: a proposed explanation may be
mathematically distinguishing while still lacking a physical instrument. The
instrument, not the notation `infinite`, carries selector authority.

If such a probe is added as a reference port, it defines a new relational
experiment over the enlarged groupoid. It does not reveal an absolute phase of
the original two-port experiment.

## Exact checker

- Checker: `checkers/wp170_closure_order_oracle_gate.py`
- Result: `results/wp170_closure_order_oracle_gate.json`

The checker verifies one-shot separation of `Z^2` from all `49` finite rivals
by order and exponent, verifies finite-rival collisions, and records that the
oracle changes the probe family.

## Calibration

- Pre excitement: `8/10`.
- Pre confidence: `9/10`.
- Pre expected information gain: `8/10`.
- Post excitement: `8/10`.
- Post confidence: `10/10`.
- Post information gain: `8/10`.
- Frozen optionality: search specifically for a physical closure-order or
  recurrence-growth instrument; do not relabel a formal oracle as a flavor
  selector.

## Report to `marici.Nima`

- Admitted state domain: finite two-port abelian closures up to period eight,
  plus `Z^2`.
- Faithful quotient coordinate: formal closure order or exponent.
- Source-authorized probe family: none yet; this packet only types the formal
  nonlocal probe.
- Contextual partition: finite closures versus `Z^2` are separated; finite
  source stories still collide by order and exponent.
- Classification: formal finite-versus-infinite selector, not an admitted
  physical selector.
- Smallest exact falsifier: finite source identification fails because
  `(2,6)` and `(3,4)` share order `12`; `(2,6)` and `(3,6)` share exponent
  `6`.
- Remaining physical-instrument gate: derive an executable closure-order,
  return-volume, or recurrence-growth readout from flavor source dynamics.
