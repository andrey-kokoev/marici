# The Celestial Spin-Two Bundle Forces Polarization Zeros

## Question

Can the nonzero locus used by the composite polarization connection cover the
entire celestial sphere for a generic radiative state?

## Polarization bundle

The real symmetric trace-free rank-two tensors form an oriented real
two-plane bundle associated to the celestial tangent-frame bundle through the
weight-two representation of \(SO(2)\). The tangent bundle of \(S^2\) has
Euler number

\[
e(TS^2)[S^2]=2.
\]

Passing to weight two doubles the clutching degree. Therefore the polarization
bundle \(\mathcal P\) has

\[
e(\mathcal P)[S^2]=4.
\]

Equivalently, the tangent clutching map has degree two and the spin-two
component map has degree four.

## Forced zeros

Because the Euler class is nonzero, \(\mathcal P\) admits no nowhere-zero
section. For every transverse radiative polarization section, the signed sum
of its local zero indices is

\[
\sum_p \operatorname{ind}_p(C)=4
\]

with the displayed sign fixed by the chosen celestial orientation.

Thus the singularities of the composite phase connection are not exceptional
states that can be excluded globally. They are forced by the topology of the
spin-two bundle.

## Consequence for relative control

The composite connection contributes total puncture holonomy

\[
\sum_p\oint_p A_C=-8\pi.
\]

If the total active connection is required to extend regularly, the relative
control field must carry the opposite total defect:

\[
\sum_p\oint_p B=8\pi.
\]

Local selector control therefore cannot be specified by one globally regular
scalar one-form in a fixed polarization chart. It requires connection data on
the nontrivial polarization bundle plus attachment data at a zero divisor of
total degree four.

## Claim boundary

This is a bundle-topology theorem for radiative spin-two data on an oriented
celestial sphere. It does not identify the locations or individual signs of
the zeros, which depend on the section, nor does it construct the active
relative connection.

## Disposition

The zero-defect requirement is universal, not an accidental hostile fixture.
Any proposed global Hodge selector that omits a degree-four defect packet is
topologically incomplete.

## Verification

```powershell
uv run --with sympy python research/strominger/checkers/spin_two_polarization_euler_obstruction_checks.py
```
