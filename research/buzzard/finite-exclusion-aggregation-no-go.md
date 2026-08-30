# Finite exclusion aggregation: Lean packet

## Source boundary

This increment formalizes the finite-support branch of Grothendieck's
`no-scalar-weighted-reduced-exclusion-energy-is-both-finite-and-gapped.md`.
It does not formalize infinite sums, operator domains, spectral gaps, or
closed range.

## Formal objects and coefficient types

Ports and labels are natural numbers. `exclusionVisible p n` means `p` does
not divide `n`. For a finite port set, `supportProduct` is its product. No
primality assumption is needed for the finite obstruction; the stronger
assumption `2 ≤ p` merely certifies that the product label is not the vacuum
label `1`.

## Theorems and hostile

- `member_divides_supportProduct` proves that every supported port divides
  the product label.
- `finiteSupport_productLabel_invisible` proves that every finite exclusion
  profile vanishes on that label.
- `finiteSupport_not_jointlyFaithful_on_nonvacuum` proves that a nonempty
  family of nontrivial ports misses a nonvacuum label.
- `ports_two_three_miss_six` is the executable finite hostile: ports `2` and
  `3` both miss label `6`.

## Missing interfaces

The infinite-support branches require positive real weights, a declared
summability notion, extended-valued energy for the divergent case, a Hilbert
coefficient space, operator or quadratic-form domains, and a definition of
uniform spectral gap. Closed-range and primorial-escape conclusions need the
corresponding topology. A product-valued completion also needs a
source-authorized product topology and boundary law.

## Verification boundary

The intended targeted command is:

```text
lake env lean MariciFormal/FiniteExclusionAggregationNoGo.lean
```

It was not run because Nima's active no-build instruction remains in force.
The module remains outside `MariciFormal.lean`.
