---
authors:
  - marici.Benincasa
date: 2026-08-18
---
# The Generic Lower-Family Rank 34 Is a Deletion-Closed Critical Count

## Record

This entry returns to the generic multi-external-leg lower family of
arXiv:2408.16386 with independent site energies and momentum resultants,
\(X_i\ne P_i\). It adds no denominator, numerator divisor, support summand,
normalization, or carrier cell.

## Deutsch--Popperian conjecture tested

The hard-to-vary claim was

\[
\boxed{
\text{the source number }34\text{ is not the deletion-closed twisted
critical rank of the frozen four-denominator family.}
}
\]

The finite falsifier was exact rank \(34\) at two independent good primes
and two independent generic six-scale points.

## Frozen object

Set \((c,a,b)=(y_{12},y_{23},y_{31})\). The denominator support is

\[
q_{g_1}=c+b+X_1,qquad
q_{g_2}=c+a+X_2,
\]

\[
q_{g_3}=a+b+X_3,qquad
q_{g_{23}}=c+b+X_2+X_3.
\]

The Cayley--Menger twist is the generic polynomial \(K(c,a,b;P_1,P_2,P_3)\)
of Entry 185. For each selected support \(S\), the logarithmic critical
ideal is saturated by

\[
uK\prod_{q\in S}q-1.
\]

The polynomial loop-measure numerators are not promoted to twist divisors.
Generic pairwise-distinct regulator exponents are used only to avoid
resonance in the critical count.

## Exact rank theorem

At

\[
\mathbf F_{32003},qquad
(X_1,X_2,X_3)=(2,3,4),qquad
(P_1,P_2,P_3)=(5,7,11),
\]

the exact sparse Gröbner quotient gives

\[
r_{\varnothing}=7,
\qquad
r_{\{q_{g_1}\}}=12,
\]

\[
r_{\{q_{g_1},q_{g_2}\}}=18,
\qquad
r_{\{q_{g_1},q_{g_{23}}\}}=17,
\]

and

\[
\boxed{
r_{\{q_{g_1},q_{g_2},q_{g_3},q_{g_{23}}\}}=34.
}
\]

The first pair is a finite branch--pole collision and the second is the
source-parallel pair. Thus the tested proper increments are

\[
12-7=5,
\]

\[
18-12-12+7=1,
\]

\[
17-12-12+7=0.
\]

This matches the independent geometry of Entry 185: finite pairs carry one
collision grade, while the parallel pair carries no proper intersection
grade.

The full rank replicates at

\[
\mathbf F_{65521},qquad
(X_1,X_2,X_3)=(3,5,6),qquad
(P_1,P_2,P_3)=(7,11,13),
\]

again with

\[
\boxed{r_{\rm full}=34.}
\]

Both full runs produce Gröbner bases of size \(223\).

## Verdict

The conjecture is falsified:

\[
\boxed{
34=
\operatorname{rank}
\mathcal M^{\rm closed}_{g_1g_2g_3g_{23}}
}
\]

for the frozen generic lower family at two independent exact generic fibers.

This types the source statement more sharply. Rank \(34\) is:

- the deletion-closed rank of the complete four-denominator generic lower
  coefficient module;
- not a homogeneous-system rank;
- equipped with proper full-support grade zero after complete Möbius inversion;
- not evidence for a new carrier stratum.

The complete deletion cube, in binary mask order
\((q_{g_1},q_{g_2},q_{g_3},q_{g_{23}})\), is

\[
\boxed{
r_S=(7,12,12,18,12,18,18,26,12,17,18,24,18,24,26,34).
}
\]

Möbius inversion gives

\[
\boxed{
m_S=(7,5,5,1,5,1,1,1,5,0,1,0,1,0,1,0).
}
\]

Thus every single pole has proper grade five; all five finite pairs have
proper grade one; the parallel pair has grade zero; exactly the two triple
supports of Entry 185 have grade one; the other triples and the full
fourfold support have grade zero. Denominator deletion therefore reproduces
the frozen collision-incidence census at coefficient-rank level.

## Classification

\[
\boxed{
\text{unchanged generic Cayley--Menger/denominator carrier}
+
\text{rank-34 filtered lower-sector coefficient module}.
}
\]

The algebraic letters of Entries 185--196 remain coefficient/relative-period
support. No new carrier datum appears.

## Scope boundary

Established:

- the complete sixteen-face Boolean deletion cube at one exact generic fiber;
- all proper support grades by Möbius inversion;
- full-family rank \(34\) at two independent exact fibers;
- exact agreement between nonzero pair/triple grades and the collision
  supports of Entry 185.

Not established:

- a canonical 34-master basis;
- deletion, residue, or extension morphisms;
- physical-chain monodromy beyond the already closed radical census.

## Next finite falsifier

Construct geometric representatives for the rank-five single-pole grades,
the five rank-one finite-pair grades, and the two rank-one triple grades.
Then compute their deletion/Gysin connecting maps and test whether the
resulting filtered coefficient object is realized by the frozen logarithmic
denominator/Cayley--Menger incidence, with no fitted splitting.

A proper grade requiring a singular support or incidence morphism outside
that frozen geometry would falsify H2. Rank growth alone remains
sector-specific coefficient complexity.

## Evidence

- `research/benincasa/marici-gm/src/bin/generic_lower_sector_groebner_rank.rs`;
- `research/benincasa/generic-lower-sector-groebner-rank.json`;
- Entry 185 for the frozen six-scale Cayley--Menger and denominator geometry.

## Outcome contract

~~~json
{
  "claim": "The source rank 34 is not the deletion-closed critical rank of the frozen generic four-denominator lower family.",
  "status": "falsified",
  "full_deletion_closed_rank": 34,
  "independent_exact_full_runs": 2,
  "full_groebner_basis_size": 223,
  "deletion_closed_ranks": [7, 12, 12, 18, 12, 18, 18, 26, 12, 17, 18, 24, 18, 24, 26, 34],
  "proper_support_grades": [7, 5, 5, 1, 5, 1, 1, 1, 5, 0, 1, 0, 1, 0, 1, 0],
  "complete_deletion_cube": true,
  "proper_full_support_grade": 0,
  "new_carrier_datum": false,
  "next_experiment": "Construct geometric representatives and connecting maps for every nonzero proper support grade."
}
~~~
