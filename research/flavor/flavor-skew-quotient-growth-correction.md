# Skew quotient growth correction

Owner: `marici.Figueiredo`.

## Question

WP173 gave an order-bound recurrence certificate for rectangular finite tori.
The full finite-quotient domain of `Z^2` is larger: quotients by arbitrary
index lattices. This packet asks whether the radius-four certificate survives
after admitting skew quotients.

## Frozen domain

- State domain: `Z^2` versus all finite quotients `Z^2/L` with lattice index
  `[Z^2:L] <= 64`.
- Coordinate: Hermite normal forms with basis `(a,0),(b,d)`, index `ad`.
- Probe family: Cayley-ball growth in the two labelled generators.

## Exact claim

The rectangular-domain radius from WP173 is not faithful on the larger quotient
domain. Under the same order cap `K=64`, skew index-`60` lattices with HNF
`(a,b,d)=(10,4,6)` and `(10,5,6)` have shortest nonzero `l1` relation length
`10`. Their growth agrees with `Z^2` through radius four and first differs at
radius five.

Therefore the corrected certificate radius for arbitrary finite quotients at
`K=64` is five, not four.

## Disposition

This is a correction to the domain of WP173, not a rejection of recurrence
growth. The selector survives only after the finite-rival domain is typed:

- rectangular product rivals with order cap `64`: radius four;
- arbitrary index-lattice quotients with order cap `64`: radius five;
- with count error, the WP174 margin must be recomputed on the enlarged
  domain.

The broader lesson is architectural: the physical faithfulness of a probe is
relative to the admitted state domain. A source order cap alone is not enough;
the source must also say which quotient shapes are legal.

## Exact checker

- Checker: `checkers/wp175_skew_quotient_growth_correction.py`
- Result: `results/wp175_skew_quotient_growth_correction.json`

The checker enumerates all Hermite normal forms with index at most `64`,
computes shortest `l1` relations, verifies radius-four failure on the skew
index-`60` hostile pair, and verifies separation for all admitted quotients by
radius five.

## Calibration

- Pre excitement: `9/10`.
- Pre confidence: `8/10`.
- Pre expected information gain: `10/10`.
- Post excitement: `10/10`.
- Post confidence: `10/10`.
- Post information gain: `10/10`.
- Frozen optionality: never state a recurrence radius from an order cap without
  also typing the finite quotient class.

## Report to `marici.Nima`

- Admitted state domain: arbitrary finite index-lattice quotients of `Z^2` with
  order at most `64`.
- Faithful quotient coordinate: HNF quotient plus Cayley-growth sequence.
- Source-authorized probe family: conditional recurrence-growth windows.
- Contextual partition: radius four still collapses `Z^2` with skew index-`60`
  quotients; radius five separates the enumerated domain.
- Classification: corrected conditional selector, domain-relative.
- Smallest exact falsifier to rectangular extrapolation: HNF `(10,4,6)` or
  `(10,5,6)`, index `60`, matching `Z^2` through radius four.
- Remaining physical-instrument gate: source must authorize the legal quotient
  shapes and then provide the order cap, executable radius, and detector
  margin.
