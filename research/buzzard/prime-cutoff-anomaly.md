# Prime-cutoff anomaly exactness: Lean packet

## Source boundary

This increment formalizes the finite algebra in Grothendieck's frozen
`prime-cutoff-adjoint-anomaly-cocycle-is-exact-and-universal.md`. It does not
formalize the analytic claim that native complex prime coefficients match
their Hilbert adjoints exactly on the critical seam.

## Formal objects and coefficient types

`Label` is any decidable label type and `R` any commutative ring. A finite
cutoff is `Finset Label`; `weight : Label → R` abstracts the prime logarithm,
and `displacement : R` abstracts the centered real spectral displacement.
`cutoffAnomaly` is twice the displacement times the finite weight sum.

## Theorems and hostile

- `cutoffAnomaly_insert` proves that a fresh-label increment is independent of
  the old cutoff.
- `exactCountercurrent_insert` gives the opposite increment.
- `anomaly_add_countercurrent` proves exact conservation.
- `countercurrent_unique` proves that every scalar countercurrent with those
  increments is the canonical one plus its cutoff-independent empty value.
- `zero_total_charge_offSeam_hostile` uses two unit integer weights at
  displacement one: anomaly plus countercurrent vanishes although the
  displacement is nonzero.

The abstraction therefore specializes the common exact-cocycle vocabulary but
rejects any promotion of conserved cutoff bookkeeping to seam-selection
authority.

## Missing analytic interfaces

The prime specialization needs positive real logarithms and the complex
coefficients `p^(-1/2-z)` and `p^(-1/2+z)`, including conjugation, injectivity of
the real exponential for `p > 1`, and the Hilbert adjoint of the labelled shift.
Those interfaces are required for the theorem that native adjoint matching is
equivalent to zero real displacement. No scalar zero-state supplies that
matching, and none is assumed here.

## Verification boundary

The intended targeted command is:

```text
lake env lean MariciFormal/PrimeCutoffAnomaly.lean
```

It was not run because Nima's active no-build instruction remains in force.
The module remains outside `MariciFormal.lean`.
