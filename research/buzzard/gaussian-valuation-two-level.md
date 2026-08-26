# Gaussian-weighted valuation chain: Lean packet

## Source boundary

This increment formalizes the convention-fixed finite core of Grothendieck's
`local-fock-confinement-is-broken-only-by-the-gaussian-boundary-coupling.md`.
It separates the source-derived quadratic valuation recurrence from the
spectral and analytic identifications used later in that packet.

## Objects and coefficient types

`quadraticValuationWeight p k = p^(2*k)` is defined over an arbitrary
commutative monoid. Its successor theorem is the scalar basis form of
`Q S = p^2 S Q`.

The two-level occupation readout is formalized over an arbitrary linearly
ordered field:

\[
G(w_0,w_1;\lambda)=w_0+w_1\lambda.
\]

Its unique root, when `w₁ ≠ 0`, is `-w₀/w₁`.

## Theorems and hostile

- `quadraticValuationWeight_succ` proves the exact `p²` recurrence.
- `twoLevelRoot_vanishes` and `twoLevel_zero_iff` prove existence and
  uniqueness of the two-level root.
- `equalWeight_twoLevel_root_abs` proves that equal positive weights give a
  root of absolute value one.
- `decreasingWeight_twoLevel_root_abs_gt_one` proves that positive weights
  with `w₁ < w₀` force the root strictly outside the unit-modulus locus.
- `positive_decreasing_packet_off_unit_hostile` instantiates the phenomenon
  over the rationals with weights `2,1` and root `-2`.

The hostile establishes that positivity of each coefficient does not preserve
the equal-weight unit-modulus conclusion.

## Missing interfaces

The source specialization

\[
w_k(t)=\exp(-\pi t p^{2k})
\]

requires real-exponential monotonicity plus assumptions `t > 0` and `p > 1`.
The identification `λ = p^(1/2-s)` requires a fixed complex-power branch and
the coordinate convention converting `|λ|` into `Re(s)`. The all-level
geometric-polynomial statement requires a separate finite-sum root theorem.
The global all-prime reciprocal completion remains an analytic source gate.

## Verification boundary

The intended targeted command is:

```text
lake env lean MariciFormal/GaussianValuationTwoLevel.lean
```

It was not run because Nima's active no-build instruction remains in force.
The module remains outside `MariciFormal.lean`.
