---
authors:
  - marici.Benincasa
date: 2026-08-17
---
# The Two-Cut Koszul Determinant Is Not Source Realized

## Question

Entry 361 excluded ordinary nearby cycles and the ordinary Euler class as
sources of the missing overlap retraction. The remaining source-native
candidate was the ordered two-normal Koszul determinant. The hard-to-vary
claim tested here is

\[
\boxed{
\text{the frozen singly polar source realizes the top class of the }
(q_{\mathcal G_{12}},q_{\mathcal G_{23}})\text{ Cousin complex}.
}
\]

No joint pole, product of source summands, secondary kernel, or support cell
is inserted.

## Completed normal grammar

Put

\[
u=q_{\mathcal G_{12}},
\qquad
v=q_{\mathcal G_{23}}.
\]

On the generic common open, all lower denominators and the Cayley--Menger
coefficient are units in the completed normal ring. Their Taylor expansions
contain only nonnegative powers of (u,v). The frozen physical source is
therefore locally of the form

\[
\frac{A(u,v)}u+\frac{B(u,v)}v+C(u,v),
\]

with (A,B,C\in R[[u,v]]). Its negative Laurent support is contained in

\[
\{(-1,0),(0,-1)\}.
\]

## Top Cousin projection

For the regular sequence ((u,v)), the top local-cohomology quotient is

\[
H^2_{(u,v)}(R)
\simeq
R[u^{-1},v^{-1}]Big/
\left(R[u^{-1}]+R[v^{-1}]\right).
\]

Only Laurent monomials negative in both variables survive. The primitive
ordered determinant class is represented by

\[
\frac1{uv},
\]

with support ((-1,-1)).

Both singly polar source terms map to zero in this quotient. Addition and
the linear Cousin differential do not multiply them. Hence

\[
\boxed{
\operatorname{pr}_{H^2_{(u,v)}}
\left(\frac Au+\frac Bv+C\right)=0.
}
\]

The geometric Koszul determinant exists, but the frozen physical coefficient
form does not realize it.

## Verdict

The tested claim is falsified. Producing the determinant requires either

\[
\frac1{q_{\mathcal G_{12}}q_{\mathcal G_{23}}}
\]

or an independently derived secondary correspondence kernel with the same
top Cousin grade. The first changes the source pole grammar; the second has
not been derived. Neither is admissible as a repair.

Combined with Entries 357--361, this closes the frozen pairwise descent
attack:

\[
\boxed{
\text{the physical three-site source supplies a common supported cospan but
no cross-sector descent transition.}
}
\]

## Classification

| Datum | Classification |
|---|---|
| regular sequence ((u,v)) | existing carrier normal geometry |
| ((uv)^{-1}) | geometric top Koszul/Cousin class |
| singly polar source support | sector-specific coefficient form |
| top Cousin projection | zero |
| missing determinant coefficient | absent secondary coefficient datum |
| new carrier stratum | none |

## Consequence for the cosmology architecture

This does not falsify H2. H2 permits sector-specific coefficient objects and
does not require their physical summands to satisfy Čech descent. It does
falsify the stronger proposal that the three marked-Cut rank-twelve modules
are glued by pairwise overlap transitions already present in the frozen
six-term integrand.

The positive global structure should therefore be sought in the Cousin
degree where the source actually lives: a cyclic sum of singly supported
classes on the union of the three marked-Cut divisors, with zero pairwise top
residue—not as a degree-zero sheaf assembled by overlap isomorphisms.

## Evidence

- `research/benincasa/marici-gm/src/bin/two_cut_cousin_determinant_gate.rs`;
- `research/benincasa/two-cut-cousin-determinant-gate-certificate.json`;
- Entries 229 and 357--361.

## Next falsifier

Construct the full three-divisor Cousin complex for

\[
D_{\rm Cut}
=D_{12}\cup D_{23}\cup D_{31}
\]

using the six frozen source occurrences. Place each singly marked summand in
Cousin degree one, retain its lower-denominator occurrence label, and compute
the differential to all three pairwise intersections and the triple
intersection.

Test whether the all-positive cyclic source is a canonical nonzero
degree-one cocycle with vanishing higher residues. If so, this identifies its
global home without inventing transition maps. If it is exact or develops a
nonzero higher residue after the full lower-boundary data are retained, the
equivariant direct-sum interpretation must be revised.
