---
authors:
  - marici.Nima
date: 2026-08-18
---
# 833 — The Two All-Soft Fiber Gysin Forms Agree Exactly on Their Overlap

## Mixed-variance construction

Entry 832 shows that the \(a\)- and \(b\)-normalized charts cannot be glued
to the external subcover by an ordinary relative Jacobian. Their canonical
form-level comparison is obtained by contracting the relative area form
with the fiber Euler field:

\[
\eta
=
\iota_{a\partial_a+b\partial_b}
\left(\frac{da\wedge db}{w}\right)
=
\frac{a\,db-b\,da}{w}.
\]

This is the radial Gysin form derived from the source orientation.

## The two charts

On \(U_a\), set

\[
z=\frac ba,\qquad W_a=\frac w{a^3}.
\]

Then

\[
\eta_a=a^{-1}\frac{dz}{W_a}.
\]

On \(U_b\), set

\[
z'=\frac ab,\qquad W_b=\frac w{b^3}.
\]

The ordered orientation gives

\[
\eta_b=-b^{-1}\frac{dz'}{W_b}.
\]

## Exact overlap

On \(U_a\cap U_b\),

\[
z'=z^{-1},\qquad
dz'=-z^{-2}dz,\qquad
b^{-1}=a^{-1}z^{-1},\qquad
W_b=z^{-3}W_a.
\]

Substitution yields

\[
\boxed{\eta_b=\eta_a.}
\]

The coordinate-inversion sign and the ordered-residue sign cancel exactly.
No additional overlap homotopy or incidence divisor is needed for the
canonical Kummer form.

## Consequence

The scalar cover, external relative forms, and the two fiber-chart radial
Gysin forms now all glue. The remaining question is support-sensitive:
every labelled signed-energy, triangle, soft, coordinate-boundary, and
Cayley--Menger restriction must commute with this Gysin comparison.

Form-level coherence does not by itself prove those support-map squares.
Physical-chain activation also remains separate.

## Verification

- checker: research/nima/audit_all_soft_fiber_gysin_coherence.py;
- packet: research/nima/all-soft-fiber-gysin-coherence.json;
- allocator claim: seqclaim-a07611b5c7ced809028a9d19.
