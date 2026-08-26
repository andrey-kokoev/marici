# Finite reciprocal-shell transport: Lean packet

## Source boundary

This increment formalizes finite cores shared by Grothendieck's packets
`theta-two-shell-seam-confinement-requires-nondecreasing-outer-weight.md`,
`theta-third-positive-shell-reverses-the-inward-zero-flow.md`,
`theta-uniform-parity-paired-inward-flow-requires-outer-even-dominance.md`,
and `theta-positive-even-spectral-transport-still-allows-off-seam-zeros.md`.

## Formal objects and coefficient types

The two-shell quotient polynomial is defined over an arbitrary commutative
ring:

\[
P_c(x)=2cx^2+x-c.
\]

The velocity results use real coefficients and the source phase law
`(-1)^k cosh(k a)`. `simpleZeroVelocity h d = -h/d` records the ordinary
implicit simple-root velocity after its nonzero derivative has been supplied.

## Theorems and hostiles

- `positive_twoShell_offSeam_quotient_hostile` gives the exact rational
  instance `c=2/7`, `x=-2`: the weight is positive and decreasing, `x<-1`,
  and `P_c(x)=0`.
- `third_positive_shell_moves_outward` proves that shell index `3` produces
  positive horizontal velocity for every positive base derivative.
- `oddEvenBlock_wrong_sign_at_seam_of_outer_lt` proves that an odd/even paired
  block already has the wrong sign at zero displacement whenever its outer
  even coefficient is smaller than its inner odd coefficient.

Together these disprove confinement from positivity, atomwise inward flow,
and undominated parity pairing at the finite algebraic level.

## Missing interfaces

Lifting a quotient root `x<-1` to an off-seam zero requires the complex
identity `x=cosh z`, a fixed `arcosh` branch, and the reciprocal/reflection
packet convention. The exact all-root threshold `c≥1` requires the quadratic
root classification and complex `cosh` preimage theorem. Monotonicity of the
two-shell branch uses differentiation of the square-root and `arcosh`
formulas. Uniform paired-shell dominance for all positive displacement needs
the monotonic ratio theorem for consecutive hyperbolic cosines. None of these
analytic claims is assumed here. The proposed completed-theta inward flow is
active conjectural input.

## Verification boundary

The intended targeted command is:

```text
lake env lean MariciFormal/TwoShellSpectralHostile.lean
```

It was not run because Nima's active no-build instruction remains in force.
The module remains outside `MariciFormal.lean`.
