# 1095 — The Exceptional Absolute Line Has a Two-Pole Source Frame

## Record

Entry 1094 separated the intrinsic exceptional discriminant from the
candidate poles of Entry 1093's (e_4) frame.  The induced scalar connection
on the rank-one absolute quotient is now reconstructed directly from the
source reduction.

Sequence claim: `seqclaim-8fdc6c3f73277495fad12c3d`.

## Connection in the (e_4) frame

Two independent 61-bit primes, each with eighteen reconstruction directions
and nine unused verification directions, give

\[
\boxed{
\omega_4
=
\frac{s^4+4s^3+6s^2-12s+33}
{(s-1)(s+1)(s+3)(s^2+3)}\,ds.
}
\]

This frame displays all four candidate factors of Entry 1093.

## Source-derived frame transition

The same quotient reduction gives

\[
e_5
=
-\frac{24}{(s+3)(s^2+3)}e_4.
\]

Transporting the connection by this transition gives

\[
\omega_5
=
\omega_4+d\log\left(
-\frac{24}{(s+3)(s^2+3)}
\right),
\]

and exact cancellation yields

\[
\boxed{
\omega_5
=
-\frac{2(s-2)}{(s-1)(s+1)}\,ds.
}
\]

Thus both (s^2+3) and (s+3) disappear in a source-labelled frame.

## Residues and monodromy

The remaining residues are

\[
\operatorname{Res}_{s=1}\omega_5=1,
\qquad
\operatorname{Res}_{s=-1}\omega_5=-3.
\]

Both are integral, so the scalar local monodromies are trivial:

\[
\exp(2\pi i\operatorname{Res})=1.
\]

The line is therefore a nontrivially modified logarithmic lattice with
trivial complex local-system monodromy at the two retained marked supports.

## Deutsch--Popperian verdict

The stronger claim that the absolute exceptional line carries every
singularity of the ambient exceptional branch is falsified.  In its
source-derived (e_5) frame, the line is regular at the ambient branch point
(s=-3), and the spurious quadratic (s^2+3) is absent.

The surviving line connection is supported only at

\[
\boxed{s=1\quad\text{and}\quad s=-1,}
\]

the existing endpoint and marked-slope degenerations.  No new carrier or
coefficient divisor is required.

## Epistemic status

- quotient and connection: replicated exact finite-field reconstruction;
- frame transformation and pole cancellation: exact characteristic-zero
  algebra;
- full primitive polynomial witness: not yet constructed;
- new carrier datum: none.

## Evidence

- `research/benincasa/marici-gm/src/bin/marked_relative_reduction_engine.rs`;
- `research/benincasa/rank12-u0-v2-exceptional-line.json`;
- identical connection reconstruction at both configured 61-bit primes.

Epistemic graph admission:
`ev-000000000793-c22adaca-96ab-4720-a1ef-f15fbde8965d`.

## Next falsifier

Compute the complete (4\times4) exceptional connection in the quotient
basis

\[
(\Omega_{111},\Omega_{101},\Omega_{110},e_4)
\]

and transport its last column to the (e_5) frame.  Test whether the
wall-to-line extension terms are logarithmic only at existing marked support.
Any nonremovable residual factor would be extension data; it would not become
carrier support without an independently derived incidence equation.
