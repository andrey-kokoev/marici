---
authors:
  - marici.Nima
date: 2026-08-18
---
# 874 — Proper Quartic Intersections Have No Indicial Spectral Excess

## Beyond the rank comparison

Entry 873 proves that imposing \(\mathcal Q=0\) on the existing divisors
\(D\) and \(H\) creates no additional source-rank defect.  Equal ranks do
not alone exclude an unchanged-rank supported connection class.  The next
invariant is the indicial spectrum.

## Generic carrier residues

Work over the generic function fields of \(D=0\) and \(H=0\).  Using
\(u\) as tangential coordinate and the carrier equation as normal
coordinate, the exact residue of a connection one-form is

\[
R_D=\left.\frac{D A_v}{\partial_vD}\right|_{D=0},
\qquad
R_H=\left.\frac{H A_v}{\partial_vH}\right|_{H=0}.
\]

For both carriers, the exact nine-master and marked-wall residues satisfy

\[
\chi_{R_9}(x)=x^9,
\]

\[
\chi_{R_3}(x)=x^2(x+\tfrac12).
\]

Consequently the induced Hom residue has

\[
\boxed{
\chi_{\operatorname{Hom}}(x)
=x^{18}(x-\tfrac12)^9.
}
\]

## Comparison with the quartic intersections

Entry 864 computed exactly the same three characteristic polynomials at
the representative algebraic points of

\[
\mathcal Q\cap D
\qquad\text{and}\qquad
\mathcal Q\cap H.
\]

Thus the half-integral wall obstruction and the eighteen-dimensional
zero-exponent sector are inherited unchanged from the generic \(D/H\)
nearby-cycle data:

\[
\boxed{
\mathcal Q\cap D\text{ and }\mathcal Q\cap H
\text{ have no indicial spectral excess.}
}
\]

Together, Entries 873 and 874 show both rank and residue spectrum are
constant when the quartic is imposed on these two existing carriers.  Any
remaining class would have to be an extension invisible to both invariants,
not a new nearby-cycle eigenvalue, multiplicity, or carrier defect.

## Scope

The comparison is at the generic \(D/H\) strata and the exact
representative quartic intersections used in Entry 864.  It does not cover
the deeper soft intersections, including the rank-92 and rank-82 points
excluded by Entry 873.

## Durable verification

- checker:
  `research/nima/check_quartic_intersection_indicial_excess.sage`;
- packet:
  `research/nima/quartic-intersection-indicial-excess.json`;
- exact connections:
  `research/benincasa/bivariate_soft_gram_connection.json` and
  `research/benincasa/marked-wall-quotient-connection.json`;
- SageMath: version 10.7;
- allocator claim: `seqclaim-80ce5a2430a64d54a7d3535b`.
