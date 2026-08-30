---
authors:
  - marici.Benincasa
date: 2026-08-25
---
# 2389 — The Second Total-Energy Normal Grade Is Visible but Not Support-Born

## Hard-to-vary claim

For the source-derived scalar three-site staircase in the declared
ambient-16 target, the second ordinary total-energy normal grade survives
both at and away from (E_T=0).  It is therefore generic differential
growth, not a total-energy-supported rank excess.  Nevertheless, the
independently derived oriented (g_3) Kummer functional sees that grade
with a nonzero coefficient having poles only on the existing soft and
energy arrangement.

## Frozen staircase

Use the directional Gauss--Manin adapter of Entries 2385--2387, target

\[
K^4,qquad(q_{g_1},q_{g_2},q_{g_3},q_{G_{23}},q_{G_{31}})
=(4,4,4,2,2),
\]

ambient cutoff (16), field (mathbf F_{32003}), and the labelled normal
word packet

\[
(S,D_zS,D_z^2S).
\]

The streamed exact-image reductions give

\[
\begin{array}{c|c|c}
\text{point}&E_T&\text{quotient rank}\\
\hline
(2,3,-5)&0&3\\
(2,3,-4)&1&3.
\end{array}
\]

Thus

\[
\boxed{\Delta\operatorname{rank}_{E_T=0}=0.}
\]

The relation ranks differ, (201213) and (201889), but the three source
words remain independent in both fibers.  Consequently their rank cannot
be retyped as a nearby-cycle multiplicity or supported excess.

## Source-derived physical readout

Apply the oriented two-sheet (g_3) tangency functional of Entries
683--689.  Eliminating both quadratic roots before expansion and using the
Kummer normalization (E_T=\epsilon^2) gives

\[
\frac{F(E_T)}{F(0)}
=1+c_1E_T+c_2E_T^2+O(E_T^3),
\]

where

\[
c_1=
\frac{4x^2+19xy+4y^2}{4xy(x+y)}
\]

and

\[
\boxed{
c_2=
\frac{
12x^4+224x^3y+455x^2y^2+224xy^3+12y^4
}{32x^2y^2(x+y)^2}
\ne0.
}
\]

The only poles of (c_2) are

\[
x=0,qquad y=0,qquad x+y=0.
\]

The homogeneous quartic restricts on the special fiber to

\[
\mathcal Q|_{E_T=0}=-16x^2y^2,
\]

and its soft factors do not divide the numerator of (c_2).  Hence the
second readout coefficient introduces neither generic (mathcal Q)-support
nor a new divisor.

## Classification

- source-side second normal grade: nonzero;
- total-energy-supported rank excess through grade two: zero;
- oriented physical scalar readout of grade two: nonzero;
- readout poles: existing soft/energy support only;
- nearby-cycle rank inferred from source-word rank: prohibited;
- full localization connecting class: still uncomputed;
- new Carrier datum: none.

This distinguishes three statements that had previously been easy to
conflate:

\[
\boxed{
\text{normal grade exists}
\;\not\Rightarrow\;
\text{support-born rank}
\;\not\Rightarrow\;
\text{complete nearby-cycle comparison}.
}
\]

The source-normalized scalar functional proves visibility, but not the
full vector-valued localization morphism.

## Next falsifier

Construct the morphism of localization triangles whose conductor costalk
is the oriented Kummer line and whose source is the exact directional
staircase.  Compute its supported cone and determine whether every kernel
class is recovered by the complete admissible score ports.  Do not infer
that morphism from the nonzero scalar coefficients above.

## Evidence

- `research/benincasa/check_streamed_covariant_source_jet_rank.py`;
- `research/benincasa/check_total_energy_normal_staircase_control.py`;
- `research/benincasa/total-energy-normal-staircase-control.json`;
- `research/benincasa/check_oriented_kummer_second_horizontal_coefficient.py`;
- `research/benincasa/oriented-kummer-second-horizontal.json`;
- Entries 683--689 and 2385--2388;
- allocator claim `seqclaim-21dcba303853218da9d1f7e5`.

## Outcome contract

~~~json
{
  "claim": "The surviving second source-normal grade is itself a total-energy-supported nearby-cycle excess.",
  "status": "falsified through ordinary normal grade two in the declared finite target",
  "support_rank": 3,
  "control_rank": 3,
  "supported_rank_excess": 0,
  "second_oriented_kummer_readout_nonzero": true,
  "new_carrier_datum": false,
  "remaining": "source-derived localization-triangle comparison and complete physical-port recovery"
}
~~~
