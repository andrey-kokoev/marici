# The Relative Connection Carries All Active Hodge Control

## Question

Given an independent Hodge connection \(A\) and the composite phase connection
\(A_C\), where does the genuinely new selector capability live?

## Canonical factorization

On the nonzero radiative locus define

\[
B=A-A_C.
\]

Both \(A\) and \(A_C\) transform by subtraction of \(d\alpha\). Therefore

\[
B\mapsto B.
\]

The connection decomposes as

\[
A=A_C+B,
\qquad
F_A=F_{A_C}+dB.
\]

In polar fiber coordinates the covariant derivative becomes

\[
D_A C
=dr\,e_r+BJC.
\]

The composite term removes the presentation phase. Every remaining angular
coupling is carried by the gauge-invariant relative field \(B\). Thus active
selector capability resides exactly in \(B\), not in the gauge-shifting part
of \(A\).

## Zero-defect law

For a zero of winding \(n\),

\[
\oint A_C=-2\pi n.
\]

If the total connection \(A\) extends regularly across a shrinking loop around
the zero, its loop integral tends to zero. Consequently

\[
\oint B=2\pi n.
\]

Regularity of the total connection does not erase the defect. It transfers the
opposite quantized holonomy into the relative control field.

## Meaning

This is the first invariant separation between phase gauge and selector
control. The affine space of connections is not itself the capability space;
its quotient by the composite phase connection is. Zeros of the radiative
field force typed attachment data for that quotient.

An independent gravitational constructor must therefore supply both:

1. a gauge-invariant relative one-form \(B\);
2. attachment rules whose puncture holonomy cancels the winding divisor of
   \(C\) whenever the total connection is required to be regular.

## Disposition

The missing active connection has been reduced to a gauge-invariant relative
field with a quantized zero-defect law. The remaining question is whether BMS
or normal-bundle source data construct such a \(B\), rather than merely a
connection presentation.

## Verification

```powershell
uv run --with sympy python research/strominger/checkers/relative_hodge_control_zero_defect_checks.py
```
