# 935 — Unit Normal Shifts Exchange the Two Cartier Sheets

## Beck--Chevalley gate

Entry 934 constructs a global rank-eight finite-difference system in the
tangential exponent directions. To compare it with the normal-symbol
calculus, test integer shifts against Cartier specialization.

Write one normal monodromy coordinate as

\[
N=e^{i\pi s}.
\]

The two resonance sheets have Cartier ideals

\[
I_+=(N-1),
\qquad
I_-=(N+1).
\]

A unit exponent shift acts by \(T_N:N\mapsto-N\). Therefore

\[
\boxed{
T_N(I_+)=-I_-,
\qquad
T_N(I_-)=-I_+.
}
\]

## Consequence

Unit normal shift is not an endomorphism of the associated grade at
\(N=1\). Indeed,

\[
\left.T_N(N-1)\right|_{N=1}=-2.
\]

Thus the proposed commutator

\[
\operatorname{gr}_{N=1}T_N
-
T_N\operatorname{gr}_{N=1}
\]

is not a nonzero endomorphism: its two terms have different target sheets.
The one-sheet comparison is mistyped.

The two-sheet union is preserved:

\[
I_+I_-=(N^2-1),
\qquad
T_N(N^2-1)=N^2-1.
\]

Hence unit normal shifts act canonically on the Cartier atlas

\[
D_+\sqcup D_-,
\]

exchanging its components. Even normal shifts preserve each component.

## Tangential shifts

For any tangential coordinate \(C\neq N\), substitutions commute:

\[
\boxed{
\operatorname{Sp}_{N=1}T_C
=
T_C\operatorname{Sp}_{N=1}.
}
\]

Therefore the one-sheet stabilizer is

\[
\boxed{
\text{arbitrary tangential integer shifts}
+
\text{even normal integer shifts}.
}
\]

## Narrow result

The rank-eight system of Entry 934 descends through the tested Cartier grade
for its tangential shift lattice. Extending it to all unit shifts requires no
new carrier incidence, but it does require retaining both source-derived
resonance sheets:

\[
\boxed{
\text{full unit-shift transport}
\Rightarrow
\text{two-sheet Cartier coefficient atlas}.
}
\]

This is a coefficient occurrence refinement, not a new geometric divisor:
both sheets are the two roots of the existing coarse equation \(N^2=1\).

## Next falsifier

Compute the source-normalized transition between the \(+\) and \(-\)
Cartier normal-symbol fibers. Test whether the unit normal shift carries the
rank-eight tangential module across sheets with only its forced sign, or
whether a new off-diagonal extension appears. The transition must be derived
from the unspecialized six-point kernel; choosing an identification of the two
fibers is inadmissible.

## Durable verification

- checker:
  research/benincasa/marici-gm/src/bin/string_shift_cartier_beck_chevalley.rs;
- packet:
  research/benincasa/string-shift-cartier-beck-chevalley.json;
- allocator claim:
  seqclaim-40073494299ad1bd630f445d.
- epistemic event:
  ev-000000000552-7c116e0d-0aa6-4df5-b387-715102aa32b2.
