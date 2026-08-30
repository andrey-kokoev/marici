# 1803 — Nine Region-Wall Families Produce Kummer Quotients and Six Are Source-Absent

## Question

Do non-singleton region walls create higher tangencies or new coefficient
types at the physical five-site threshold?

## Geometric census

For the representative \(g_5\)-\(G^-_{e_{12}}\) threshold, the frozen
five-cycle packet contains fifteen non-singleton region-wall labels. On both
reflected physical sheets, exact rational interval arithmetic proves that
every wall has nonzero tangential gradient on the \(q_e\)-residue sphere.

Thus all thirty labelled-sheet germs are linear–Morse, not higher tangent.

## Source-support partition

The source packet divides the fifteen labels into two classes.

Six labels never occur in a term containing \(G^-_{e_{12}}\):

\[
g_{12},\ g_{123},\ g_{1234},\
g_{1235},\ g_{1245},\ g_{125}.
\]

Their carrier intersections exist, but the corresponding wall-residue
quotient is absent from the frozen source.

Nine labels do co-occur:

\[
g_{1345},\ g_{145},\ g_{15},\
g_{23},\ g_{234},\ g_{2345},\
g_{34},\ g_{345},\ g_{45}.
\]

For each label and both reflected sheets, impose the wall with a
source-energy deformation preserving the threshold point. Between six and
twelve source terms contribute. Exact interval arithmetic certifies every
remaining wall and every complete residue coefficient as nonzero.

## Coefficient quotient

Each supported germ reduces to

\[
\int
\frac{du\,dv}
{(\tau+u^2+v^2)(h+\lambda u)},
\qquad
\lambda\neq0.
\]

Hence its added-wall residue is a rank-one Kummer line on

\[
h^2+\lambda^2\tau=0,
\]

with

\[
T_s=-1,
\qquad
N=0.
\]

## Cyclic assembly

Each of the nine relative labels generates a free \(C_5\)-orbit. Therefore
the assembled object has

\[
\boxed{
\operatorname{rank}=45,
\qquad
\chi=(45,0,0,0,0).
}
\]

## Architectural result

\[
\boxed{
15\text{ carrier incidences}
=
9\text{ source-supported Kummer families}
+
6\text{ source-absent families}.
}
\]

No higher tangency and no new carrier generator appear. The distinction
between carrier incidence and coefficient activation is determined exactly
by source occurrence data.

## Next falsifier

Study intersections among two added supported region walls. Their two
restricted gradients may be independent or collinear; the collinear cases
are the first candidates for a genuinely higher coefficient collision.

## Evidence

- research/benincasa/checkers/five_site_g5_region_wall_tangent_census.py
- research/benincasa/results/five-site-g5-region-wall-tangent-census.json
- research/benincasa/checkers/five_site_g5_region_wall_source_coefficients.py
- research/benincasa/results/five-site-g5-region-wall-source-coefficients.json
- research/benincasa/checkers/five_site_g5_region_wall_kummer_quotients.py
- research/benincasa/results/five-site-g5-region-wall-kummer-quotients.json
- allocator claim: seqclaim-1c150238936814cda7c49e88
