---
authors:
  - marici.Benincasa
date: 2026-08-17
---
# Geometric Two-Cut Intersection Has No Source Iterated Residue

## Question

Entry 356 left open whether the frozen pre-residue integrand supplies a
genuine correspondence between the (q_{\mathcal G_{12}}) and
(q_{\mathcal G_{23}}) rank-twelve residue modules.

The hard-to-vary claim tested here is

\[
\boxed{
q_{\mathcal G_{12}}=q_{\mathcal G_{23}}=0
\text{ carries the source-defined iterated residue needed for an overlap arrow.}
}
\]

No denominator, zero map, carrier cell, support summand, or normalization is
added.

## Frozen common locus

Write

\[
x=X_1,\quad y=X_2,\quad z=X_3,\quad E=x+y+z,
\qquad (c,a,b)=(y_{12},y_{23},y_{31}).
\]

The two marked-Cut equations give

\[
q_{\mathcal G_{12}}=E+c=0,
\qquad q_{\mathcal G_{23}}=E+a=0,
\]

hence (c=a=-E), with (b) free. Restricting the exact source
Cayley--Menger polynomial gives the genuine one-dimensional double cover

\[
w^2=K_{12,23}(b)
=y^2b^4+y^2(y^2-x^2-z^2-2E^2)b^2+C_0,
\]

where

\[
C_0=E^2\!\left[x^2(x^2-y^2-z^2)+z^2(z^2-x^2-y^2)\right]
+y^2E^4+x^2y^2z^2.
\]

Thus the pairwise geometric intersection is nonempty at generic kinematics.

## Retained lower occurrences

The two source sectors restrict differently:

\[
\begin{array}{c|cc}
12 & q_{\mathfrak g_{23}}=b-x & q_{\mathfrak g_{31}}=-(x+2y+z)\\
23 & q_{\mathfrak g_{31}}=-(x+2y+z) & q_{\mathfrak g_{12}}=b-z.
\end{array}
\]

They share the (q_{\mathfrak g_{31}}) occurrence, which is generically a
nonzero parameter on the overlap, while their nonconstant marks are (b=x)
and (b=z). This is an exact restriction of the existing source divisors,
not a new carrier incidence.

## Orientation

The frozen source volume is

\[
dc\wedge da\wedge db.
\]

Consequently the two formal iterated-residue orientations induce (+db) and
(-db): they differ by the expected Koszul sign. The orientation itself is
therefore coherent.

## Source-form obstruction

The primary six-term numerator is

\[
\frac1{q_{\mathcal G_{12}}}
\left(\frac1{q_{\mathfrak g_{23}}}+\frac1{q_{\mathfrak g_{31}}}\right)
+\operatorname{cyc}.
\]

No summand contains

\[
\frac1{q_{\mathcal G_{12}}q_{\mathcal G_{23}}}.
\]

Therefore the frozen integration form has no joint marked-Cut polar
coefficient on the geometric intersection. Its proposed double Leray residue
is absent. Calling this an overlap zero map would add coefficient data not
provided by the source and remains prohibited.

The conjecture is falsified narrowly:

\[
\boxed{
\text{geometric two-Cut intersection}
\not\Rightarrow
\text{source iterated-residue correspondence}.
}
\]

## Classification

| Datum | Classification |
|---|---|
| (K_{12,23}(b)) | existing Cayley--Menger carrier restriction |
| (b=x,b=z) | existing marked coefficient divisors |
| opposite residue orders | shared derived/Koszul orientation |
| joint marked-Cut pole | absent from frozen coefficient form |
| cross-sector overlap arrow | not constructed; not zero |
| new carrier datum | none |

## Consequence

The result strengthens the distinction already forced by Entry 356. The
three sectors possess geometric pairwise intersections, but the physical
six-term form is a sum of singly marked residues, not a bicomplex with
double-marked coefficients. H2 survives in its local/equivariant form; global
Čech descent is not supported by this source object.

## Evidence

- `research/benincasa/marici-gm/src/bin/cross_sector_overlap.rs`;
- `research/benincasa/cross-sector-overlap-certificate.json`;
- Entries 188, 229, and 356.

## Next falsifier

Test the full relative pair rather than the physical six-term form: determine
whether the common curve (K_{12,23}(b)) defines a canonical Gysin
correspondence between the two marked residue surfaces using only the frozen
Cayley--Menger compactification and source boundary divisors. The map must be
derived from the pair geometry and must recover the Koszul sign above. If its
definition requires a double-marked coefficient or an added correspondence
cycle, the global descent hypothesis fails at the frozen three-site source.
