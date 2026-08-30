---
authors:
  - marici.Benincasa
date: 2026-08-25
---
# 2390 — Labelled Tangency Score Ports Remove the Kummer Observer Blind Divisor

## Hard-to-vary claim

The oriented (g_3) Kummer score tower is generically faithful on the
three-word total-energy source staircase, but loses rank on a genuine
positive-energy observer divisor.  That divisor is not shared by either
independently labelled (g_1) or (g_2) tangency score port.  After their
source-derived Tate normalization, each nonramified port is itself faithful
through second source-word order throughout the positive nonsoft chamber.

This is contextual recovery at the coefficient-port level.  It is not yet
a theorem that one physical relative cycle accesses all three ports.

## Actual source-word observer

Entry 2389 determined the normalized oriented (g_3) period

\[
F(E)/F(0)=\sum_{n\ge0}c_nE^n.
\]

For the source-word basis

\[
(S,D_ES,D_E^2S)
\]

and score basis

\[
(\operatorname{ev},D_E\operatorname{ev},D_E^2\operatorname{ev}),
\]

horizontality forces the Hankel observer

\[
H_{ij}=F^{(i+j)}(0)/F(0),
\qquad0\le i,j\le2.
\]

Root-free expansion through (E^4) gives

\[
\det H_{g_3}
=-
\frac{P_{12}(x,y)}{256x^6y^6(x+y)^6},
\]

where

\[
\begin{aligned}
P_{12}={}&1392x^{12}+5472x^{11}y-2232x^{10}y^2
-79600x^9y^3-204714x^8y^4\\
&-260244x^7y^5-253345x^6y^6-260244x^5y^7
-204714x^4y^8\\
&-79600x^3y^9-2232x^2y^{10}+5472xy^{11}+1392y^{12}.
\end{aligned}
\]

Thus (H_{g_3}) has generic rank three.  On (r=x/y>0), however,
(P_{12}(r,1)) has exactly two positive roots,

\[
r\simeq0.257546690298485,
\qquad
r\simeq3.88279111193797,
\]

which are reciprocal.  Hence maximum source-word depth plus the single
Kummer port does not guarantee faithfulness.

## Labelled nonramified ports

For (g_1) and (g_2), retain the oriented difference of the two labelled
tangency roots.  Both raw residues have ordinary order (-1) at (E=0).
The source-derived generators are therefore

\[
E(\rho_+-\rho_-).
\]

Their score Hankel determinants are

\[
\det H_{g_1}=
\frac{P_1(x,y)}{432x^6y^6(x+y)^6},
\qquad
\det H_{g_2}=
\frac{P_1(y,x)}{432x^6y^6(x+y)^6},
\]

where every coefficient of (P_1) is strictly positive.  Consequently

\[
\boxed{
x>0, y>0
\quad\Longrightarrow\quad
\operatorname{rank}H_{g_1}
=\operatorname{rank}H_{g_2}=3.
}
\]

Exact polynomial gcds also give

\[
\gcd(P_{12},P_1)=
\gcd(P_{12},P_1(y,x))=1.
\]

Thus the (g_3) blind divisor is a port-relative observer defect, not a
common rank-loss support of the labelled tangency coefficient family.

## Classification

- (g_3) source-word score tower: generically faithful, with a finite
  positive-energy blind divisor;
- (g_1,g_2) Tate-normalized score towers: faithful on the positive nonsoft
  chamber;
- common labelled-port blind divisor: absent;
- new coefficient singularity: absent;
- new Carrier divisor: absent;
- simultaneous physical-cycle accessibility: unproved.

This is the finite analogue of contextual faithfulness:

\[
\boxed{
\ker H_{g_3}\ne0\text{ on }P_{12}=0,
\qquad
\ker(H_{g_1}\oplus H_{g_2}\oplus H_{g_3})=0
\text{ for }x,y>0.
}
\]

The second statement is presently algebraic/port-level.  It becomes a
physical theorem only after the oriented relative chain is shown to induce
the required labelled port cospan.

## Next falsifier

Construct the physical relative-chain incidence map to the three labelled
tangency ports at (E=0).  If the chain reaches either (g_1) or (g_2)
with nonzero source-normalized weight on (P_{12}=0), the scalar
source-word staircase is physically faithful through grade two.  If the
physical chain sees only (g_3), the two positive blind points survive as
physical observer defects and must be tested against marked-wall and
polarization ports.

## Evidence

- `research/benincasa/check_total_energy_kummer_source_word_scores.py`;
- `research/benincasa/total-energy-kummer-source-word-scores.json`;
- `research/benincasa/check_total_energy_tangency_port_recovery.py`;
- `research/benincasa/total-energy-tangency-port-recovery.json`;
- Entries 680--689 and 2389;
- allocator claim `seqclaim-afce590b6717d2f7754182d2`.

## Outcome contract

~~~json
{
  "claim": "The positive-energy blind divisor of the g3 Kummer score observer is shared by all labelled tangency ports.",
  "status": "falsified at the algebraic labelled-port level",
  "g3_positive_blind_points": 2,
  "g1_positive_chamber_rank": 3,
  "g2_positive_chamber_rank": 3,
  "common_blind_divisor": false,
  "physical_chain_cospan_constructed": false,
  "new_carrier_datum": false
}
~~~
