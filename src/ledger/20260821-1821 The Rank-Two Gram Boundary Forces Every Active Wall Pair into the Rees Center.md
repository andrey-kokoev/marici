# 1821 — The Rank-Two Gram Boundary Forces Every Active Wall Pair into the Rees Center

## Question

Which of Entry 1818's 22 active local pair types meet Entry 1820's tangency
and compatibility center at a generic external-Gram rank drop?

## Threshold stationarity at rank two

At \(\det(H)=0\), place the external five-cycle in its rank-two plane. Let
\(C_3,C_4\) be the two boundary foci entering the active \(g_5\) wall.
Exact interval arithmetic certifies

\[
\det(C_3,C_4)\neq0.
\]

If a threshold pinch \(\ell\) had nonzero component normal to the external
plane, the normal component of the stationarity equation would imply

\[
\frac{C_3}{r_3}+\frac{C_4}{r_4}=0,
\qquad
r_3,r_4>0.
\]

Two noncollinear focus vectors cannot satisfy this relation. Therefore

\[
\boxed{
\ell\text{ lies in the external plane at Gram rank two}.
}
\]

## Forced wall-normal rank loss

Every marked wall gradient is a sum of unit vectors from \(\ell\) to external
centers, hence also lies in the external plane. The threshold tangent plane
decomposes as

\[
T_{\ell}
=
\langle\text{one in-plane tangent}\rangle
\oplus
\langle\text{external-plane normal}\rangle.
\]

All projected wall gradients have zero component in the second summand.
Consequently their span has rank one, and for every active pair

\[
\boxed{
\det L_{A,B}=0.
}
\]

At the two-wall intersection itself,

\[
h_1=h_2=0
\]

implies Entry 1820's compatibility normal

\[
k=h_2-\alpha h_1=0.
\]

## Result

All 22 local active pair types, and hence all 110 labelled cyclic
occurrences, meet the Rees center

\[
(\varepsilon,k)=(0,0)
\]

at the rank-two Gram boundary.

Thus Entry 1819's generic extension statement cannot be applied to these
supported intersections: they lie precisely on its excluded wall-tangency
locus. Entry 1820's rank-one exceptional quotient is required for every
summand.

## Architectural consequence

The Gram degeneration does not create an arbitrary new incidence. It forces
an existing marked arrangement to lose transverse rank in a universal way.
The appropriate response is the predeclared support-sensitive Rees/Gysin
calculus, not a new carrier wall.

## Next falsifier

Compute the first Gram-normal variation of each ordered wall determinant.
Test whether its exceptional coefficient is nonzero and whether the regular
physical current of Entry 1819 pairs with Entry 1820's exceptional rank-one
line. A zero first variation would force a higher weighted center.

## Evidence

- research/benincasa/checkers/five_site_g5_gram_forces_pair_tangency.py
- research/benincasa/results/five-site-g5-gram-forces-pair-tangency.json
- Entries 1819 and 1820
- allocator claim: seqclaim-32738447f62c002c7bd9c58a