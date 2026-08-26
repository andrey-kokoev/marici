# Prime-translation boundary cocycle: Lean packet

## Source boundary

This increment formalizes the finite exact algebra in Grothendieck's
`a-scalar-zero-is-a-completion-class-jump-of-the-prime-boundary-current.md`.
It deliberately stops before the prime asymptotics and restricted-product
completion assertions.

## Formal objects and assumptions

Over an arbitrary commutative ring, a source is a sequence `source : ℕ → R`
and `phase : R` is a multiplicative translation phase. The length-`n`
boundary prefix is

\[
B_n=\sum_{k<n}q^k a_k.
\]

`shiftedBoundarySource source m` retains the source beginning at label `m`.

## Theorems and hostile

- `weightedBoundaryPrefix_add` proves
  `B_(m+n) = B_m + q^m B_n(shift_m source)`.
- `two_stage_boundary_paths_agree` states the same identity as exact equality
  of the staged and direct routes. There is no finite cocycle anomaly.
- `zero_total_with_nonzero_boundary_prefix` uses the integer packet `(1,-1)`:
  its length-two scalar aggregate vanishes while its length-one boundary
  prefix is nonzero.

The hostile prevents a scalar zero from being interpreted as termwise or
intervalwise disappearance of the boundary state.

## Missing interfaces and gates

The continuous source formula needs a typed locally integrable amplitude,
translation on its function space, and interval-integral concatenation. The
claimed completion-class jump additionally needs all of the following source
theorems:

- super-exponential tail estimates locally uniform in the spectral variable;
- the exact asymptotic remainder for each prime-power depth;
- divergence of the prime sums at exponents `1/2` and `1`;
- absolute convergence at depths at least `3`;
- a proof that cancellation of the leading coefficient is sufficient for
  convergence of the complete remainder, and conversely that a nonzero
  coefficient cannot be cancelled by it.

Those analytic results are not encoded as assumptions masquerading as a Lean
proof. The RH-facing statement that such a completion jump extends to a
star-compatible continuous boundary cocycle remains active conjectural input.

## Verification boundary

The intended targeted command is:

```text
lake env lean MariciFormal/PrimeBoundaryCocycle.lean
```

It was not run because Nima's active no-build instruction remains in force.
The module remains outside `MariciFormal.lean`.
