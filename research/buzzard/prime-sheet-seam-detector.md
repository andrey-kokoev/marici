# Native prime-sheet seam detector: Lean packet

## Source boundary

This increment formalizes the algebraic log-amplitude core of Grothendieck's
`native-prime-sheet-adjoint-matching-occurs-exactly-on-the-seam.md`.

## Formal objects and coefficient types

Over any characteristic-zero field, `base` is the common exponent offset,
`displacement` is the centered spectral displacement, and `logPrime` is the
nonzero logarithmic prime weight. Direct and reciprocal log-amplitudes are
`(base-displacement)*logPrime` and `(base+displacement)*logPrime`.

The unitary no-repair theorem is stated over real amplitudes using absolute
value. It requires only that the frame multiplier have modulus one.

## Theorems and hostile

- `reciprocal_sub_direct_eq_mismatch` computes the mismatch as twice the
  displacement times the prime logarithm.
- `primeSheetMatching_iff_seam` proves native log-amplitude matching is
  equivalent to zero displacement when the prime logarithm is nonzero.
- `logModulusMismatch_eq_zero_iff` states the same detector through the
  mismatch observable.
- `unitModulus_transport_cannot_repair` proves a unit-modulus frame change
  cannot repair unequal amplitude moduli.
- `scalarCancellation_does_not_imply_primeSheetMatching` gives a rational
  two-term cancellation with nonzero sheet mismatch.

Thus the local native pair detects the seam if adjoint matching is independently
required, but scalar cancellation does not supply that requirement.

## Missing analytic and operator interfaces

The exact source theorem still needs positive real primes, nonvanishing of
`log p`, complex powers `p^z`, conjugation and modulus identities, the labelled
Hilbert shift and its adjoint, and a proof that equality of exponential
amplitudes is faithfully reflected by equality of their logarithmic exponents.
Most importantly, no source theorem currently makes a scalar theta zero impose
native Hilbert-adjoint matching. That bridge remains gated and is not assumed.

## Verification boundary

The intended targeted command is:

```text
lake env lean MariciFormal/PrimeSheetSeamDetector.lean
```

It was not run because Nima's active no-build instruction remains in force.
The module remains outside `MariciFormal.lean`.
