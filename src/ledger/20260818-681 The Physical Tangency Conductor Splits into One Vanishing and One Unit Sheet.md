---
authors:
  - marici.Nima
date: 2026-08-18
---
# 681 — The Physical Tangency Conductor Splits into One Vanishing and One Unit Sheet

## Question

Entry 680 determined the sheet-independent norm of the physical residue but
left open whether opposite valuations on the two tangency sheets concealed a
failure of the logarithmic lattice. Resolve the two sheets over a generic
physical conductor component before taking the norm.

## Exact split over the first conductor

For wall (g_1), the reduced cover is (h_1(t)=0), and its physical
numerator is

\[
N_1=t+z-x.
\]

Let (R_1=operatorname{Res}_t(h_1,N_1)). Direct substitution gives

\[
h_1(x-z)=R_1,
\qquad
h_1(-x+z)=R_1.
\]

Thus over the generic point of (R_1=0), the cover splits into the two
sections (t=x-z) and (t=-x+z). Their numerator values are

\[
N_1(x-z)=0,
\qquad
N_1(-x+z)=-2(x-z).
\]

Both (h_1') and the remaining physical denominator are generically units
on these sections. Consequently the residue valuations are

\[
(v_{R_1}(ho_+),v_{R_1}(ho_-))=(1,0).
\]

## Exact split over the second conductor

For wall (g_2), (N_2=t+z-y). On (R_2=0), the sections are

\[
t=y-z,
\qquad
t=-y+z,
\]

with

\[
N_2(y-z)=0,
\qquad
N_2(-y+z)=-2(y-z).
\]

Again the tangent derivative and remaining denominator are generically
units, so the sheet valuations are also

\[
(1,0).
\]

## Deck action and lattice

The deck involution exchanges the two sections. It therefore exchanges the
vanishing and unit generators; it does not exchange a zero with a pole. The
norm's simple conductor zero is the sum (1+0), not a cancellation of
opposite valuations.

Hence the physical rank-one image admits a saturated logarithmic lattice at
the generic points of (R_1=0) and (R_2=0):

\[
\boxed{
\text{generic sheet valuations }(1,0),
\quad
\text{no hidden opposite-sheet torsion or pole.}
}
\]

This is a statement at generic conductor points. Intersections with the
soft, signed-energy, or tangency-discriminant divisors require separate
two-parameter local models.

## Quartic consequence

Because Entry 680 proves (gcd(mathcal Q,R_1R_2)=1), resolving the sheets
does not restore quartic support. The credible home of (mathcal Q) remains
an off-diagonal supported comparison or algebraic–elliptic extension class,
not the carrier, determinant lattice, or individual-sheet conductor lattice.

## Evidence

- `research/benincasa/check_physical_tangency_individual_sheets.py`;
- `research/benincasa/physical-tangency-individual-sheets.json`;
- Entries 677 and 680;
- allocator claim `seqclaim-171d8e77ee3035314a0b5455`.

## Next falsifier

Construct a two-parameter local model at a conductor/discriminant
intersection and test whether deck ramification creates torsion there. If it
does not, move the quartic search entirely to the supported
algebraic–elliptic extension map.
