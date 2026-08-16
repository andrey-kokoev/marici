---
authors:
  - marici.Benincasa
date: 2026-08-15
---
# Cyclic Occurrence Sewing of the Exceptional Cut-Nearby Commutator

## Record

Status: the source-normalized exceptional Cut--nearby commutator of entry
226 has a unique cyclic sewing in the occurrence-resolved
\(q_{\mathcal G_{ij}}\)-only nine-master projections. All six source
occurrences have positive sign. Forgetting the lower-denominator occurrence
label produces multiplicity two at each marked Cut, not cancellation.

No denominator, carrier cell, support summand, projector, normalization, or
fitted sign is added.

## Deutsch--Popperian conjecture tested

The hard-to-vary claim was

\[
\boxed{
\text{the cyclic local commutators may fail to sew because their source
occurrence signs or nine-master permutations are incompatible.}
}
\]

The finite falsifier froze the literal source sum, occurrence labels,
integration orientation, equation-(58) master descriptors, and entry-226
normalization before exhausting the admissible sign/permutation grammar.

## Frozen source occurrences

The primary source writes

\[
\frac1{q_{\mathcal G_{12}}}
\left(
\frac1{q_{\mathfrak g_{23}}}
+
\frac1{q_{\mathfrak g_{31}}}
\right)
+
\operatorname{cyc}.
\]

Thus the six terms are

\[
(12|23),(12|31),(23|31),(23|12),(31|12),(31|23),
\]

all with coefficient \(+1\). Before occurrence identification they form
two cyclic orbits:

\[
(12|23)\to(23|31)\to(31|12)\to(12|23),
\]

\[
(12|31)\to(23|12)\to(31|23)\to(12|31).
\]

The two orbits were not collapsed before calculation.

## Residue orientations

Freeze the source volume order

\[
dy_{12}\wedge dy_{23}\wedge dy_{31}.
\]

The cyclic sector-local residue orders are

\[
\begin{aligned}
q_{\mathcal G_{12}}&:\quad
dq_{\mathcal G_{12}}\wedge dy_{23}\wedge dy_{31},\\
q_{\mathcal G_{23}}&:\quad
dq_{\mathcal G_{23}}\wedge dy_{31}\wedge dy_{12},\\
q_{\mathcal G_{31}}&:\quad
dq_{\mathcal G_{31}}\wedge dy_{12}\wedge dy_{23}.
\end{aligned}
\]

Since \(q_{\mathcal G_{ij}}=E+y_{ij}\), each normal derivative is
\(+1\). The three orders are even cyclic permutations. Therefore

\[
\boxed{\epsilon_{12}=\epsilon_{23}=\epsilon_{31}=+1.}
\]

No reflection is used. The odd \(C_2\) suspension cocycle of entry 228 is
a separate cross-sector datum and supplies no sign or shift here.

## Sectorwise master covariance

The supported equation-(58) descriptors in every sector-local basis are

\[
(e_3,e_5,e_6)
=
(\text{first remaining edge}\,\phi_{002},
\text{second remaining edge}\,\phi_{002},
\phi_{002}).
\]

Under \(\rho:(1,2,3)\mapsto(2,3,1)\), the remaining-edge orders obey

\[
(y_{23},y_{31})
\mapsto
(y_{31},y_{12})
\mapsto
(y_{12},y_{23}).
\]

Hence \(\rho:(e_3,e_5,e_6)\mapsto(e_3,e_5,e_6)\).

## Unique cyclic commutator

The three sector-local vectors are

\[
C_{12}
=
\left(
0,0,-\frac{2\pi^2}{X_1},0,-\frac{2\pi^2}{X_2},
-\frac{2\pi^2}{X_1X_2},0,0,0
\right),
\]

\[
C_{23}
=
\left(
0,0,-\frac{2\pi^2}{X_2},0,-\frac{2\pi^2}{X_3},
-\frac{2\pi^2}{X_2X_3},0,0,0
\right),
\]

\[
C_{31}
=
\left(
0,0,-\frac{2\pi^2}{X_3},0,-\frac{2\pi^2}{X_1},
-\frac{2\pi^2}{X_3X_1},0,0,0
\right).
\]

They satisfy

\[
\rho(C_{12})=C_{23},\qquad
\rho(C_{23})=C_{31},\qquad
\rho(C_{31})=C_{12}.
\]

The checker exhausted \(2^6\) occurrence-sign assignments and one
\(3!\) supported-master permutation in each rotated sector:

\[
2^6(3!)^2=2304.
\]

Exactly one candidate survived: all occurrence signs positive and both
master permutations the identity.

## Occurrence-forgetting projection

Let \(F\) forget which lower denominator accompanied a fixed marked Cut.
Then

\[
F(C_{12|23})=F(C_{12|31})=C_{12},
\]

and cyclically. Therefore

\[
\boxed{
F(C_{ij|jk}+C_{ij|ki})=2C_{ij}.
}
\]

The factor \(2\) is occurrence-identification multiplicity, not a new
coupling, incidence, or carrier generator.

## Verdict

The cyclic-sewing obstruction is falsified in the stated projection:

\[
\boxed{
\text{the source-normalized exceptional commutator sews uniquely and
cyclically, with no new carrier incidence.}
}
\]

The result remains in cyclic copies of the rank-seven algebraic
Tate/Kummer kernel and \(R_\infty(C_{ij})=0\). It has no elliptic Gysin
image, new elliptic monodromy, graph-homology component, or new stratum.

## Scope boundary

This is not yet the complete physical six-term assembly. Each source
occurrence carries an additional lower denominator
\(q_{\mathfrak g_{jk}}\) or \(q_{\mathfrak g_{ki}}\). This theorem
sews their common projection to the \(q_{\mathcal G_{ij}}\)-only
nine-master sector. Thus

\[
\text{cyclic sewing after projection}
\not\Rightarrow
\text{full four-pole occurrence-level sewing}.
\]

No equality of the two occurrence lifts is claimed before applying \(F\).

## Classification

- existing carrier: total-energy normal, three marked Cut divisors, cyclic
  occurrence labels, and frozen weighted marked-corner blowups;
- soft support: excluded;
- graph homology: none;
- Tate/Kummer coefficient data: all three commutators;
- elliptic Gauss--Manin data: zero image;
- occurrence multiplicity: \(2\) after forgetting the lower denominator;
- genuinely new carrier incidence: none.

## Exact evidence

- research/benincasa/check_cyclic_cut_nearby_sewing.rs;
- research/benincasa/cyclic-cut-nearby-sewing.json;
- rustfmt-clean warnings-denied optimized compilation;
- exact runtime assertions and 2,304 exhausted candidates;
- frozen primary-source equation eq:Triangle and denominator/master lists.

## Next finite falsifier

Lift each of the six occurrence-labelled classes from the common
nine-master projection to its literal source summand with
\(q_{\mathcal G_{ij}}\) and one of
\(q_{\mathfrak g_{jk}},q_{\mathfrak g_{ki}}\).

Compute the six lower-denominator boundary maps and test whether the two
cyclic occurrence orbits glue before applying \(F\).

Strong falsifier: if frozen four-pole relative geometry cannot produce one
lift without a new incidence stratum, the shared-carrier hypothesis fails
there. Failure of equality or cancellation inside existing coefficient
geometry falsifies full canonical assembly but not the carrier.
