---
authors:
  - marici.Nima
date: 2026-08-18
---
# The Unsplit Physical Residue Pair Has Zero Occurrence-Exceptional Residue

## Source-defined pair

Entry 590 types the physical (q_{G_{12}}) residue as the labelled sum of
the (g_{23}) and (g_{31}) four-pole families.  Near their positive
occurrence collision use the source-derived weighted chart

\[
E=\tau^2,qquad
a=y+\tau^2r,qquad
b=x-\tau^2r+\tau^3n.
\]

The two occurrence denominators become

\[
q_{g_{31}}=\tau^2r,
\qquad
q_{g_{23}}=\tau^2(-r+\tau n),
\]

while their sum is

\[
q_{g_{31}}+q_{g_{23}}=\tau^3n.
\]

Therefore the source-prescribed unsplit combination satisfies

\[
\frac1{q_{g_{23}}}+\frac1{q_{g_{31}}}
=
\frac{q_{g_{23}}+q_{g_{31}}}{q_{g_{23}}q_{g_{31}}}
\]

and gains one exceptional valuation relative to either individual summand.

## Exact exceptional grade

Including the shared (q_{g_3}^{-1}) factor, each individual full term has
weight (-4), whereas the unsplit pair has weight (-3).  Its leading
two-form is

\[
-\frac{n}{4xyr^2},dr\wedge dn
=
d\left(\frac{n}{4xyr},dn\right).
\]

Hence

\[
\boxed{
\operatorname{Res}_{r=0}^{\rm simple}
(\text{unsplit physical pair})=0.
}
\]

The committed exact checker verifies the weighted denominator identities at
179,685 integer points and the cleared differential identity independently.

## Consequence for the source-master map

The two individual occurrence-wall currents are not canonical, but their
source-weighted sum is canonical and has no simple class on the occurrence
exceptional divisor.  Thus the missing map to the elliptic coefficient block
cannot be supplied by assigning separate Gysin residues to (a=y) and
(b=x), nor by their canonical unsplit exceptional grade.

This does **not** prove that the full residue pair has zero infinity-Gysin
image.  A global contribution may still arise from the shared

\[
\{q_{g_1},q_{g_2},q_{g_3}\}
\]

core or from the physical relative chain away from the occurrence collision.
The next calculation must therefore push the common three-pole core into the
nine-master module and test its infinity restriction; the occurrence walls
should enter only through the already trivialized exact pair.

## Evidence

- `research/benincasa/check_unsplit_occurrence_pair.rs`;
- `research/benincasa/unsplit-occurrence-pair.json`;
- Entries 545, 589, and 590.

## Outcome contract

~~~json
{
  "claim": "The source-prescribed sum of the two physical q_G12 residue summands carries a nonzero simple Gysin class on the occurrence exceptional divisor.",
  "status": "falsified",
  "exact_weighted_points": 179685,
  "individual_weight": -4,
  "unsplit_pair_weight": -3,
  "leading_exceptional_form_exact": true,
  "simple_occurrence_residue": 0,
  "global_infinity_gysin_image_determined": false,
  "next_experiment": "Map the shared g1-g2-g3 residue core into the nine-master module and compute its infinity-Gysin image."
}
~~~
