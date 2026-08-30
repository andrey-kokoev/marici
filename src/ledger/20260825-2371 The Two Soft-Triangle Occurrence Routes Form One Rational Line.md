---
author: marici.Benincasa
date: 2026-08-25
---

# 2371 — The Two Soft-Triangle Occurrence Routes Form One Rational Line

## Source relation

Entry 2370 retains the two occurrence routes instead of summing them.
Their coherence is not an ansatz. If \(e_{23}\) and \(e_{31}\) denote the
two source terms, then

\[
q_{\mathfrak g_{23}}e_{23}
-q_{\mathfrak g_{31}}e_{31}=0
\]

because both products equal the common three-wall term.

Sequence claim: seqclaim-13218ec3d3a781c4b87ff528.

## Weighted presentation

Let

\[
\eta=\frac{x}{p}.
\]

The exact normalized wall coefficients are

\[
\frac{q_{\mathfrak g_{23}}}{p}
=2+\eta\xi,
\]

\[
\frac{q_{\mathfrak g_{31}}}{p}
=t-1-\frac{\eta\kappa}{2}.
\]

Therefore the occurrence presentation is

\[
\boxed{
(2+\eta\xi)e_{23}
-\left(t-1-\frac{\eta\kappa}{2}\right)e_{31}=0.
}
\]

Its exceptional and first-normal symbols are respectively

\[
\begin{pmatrix}2&1-t\end{pmatrix},
\qquad
\begin{pmatrix}\xi&\kappa/2\end{pmatrix}.
\]

## Rational flatness

The coefficient \(2+\eta\xi\) is a unit over
\(\mathbb Q[[\eta]]\). Hence

\[
e_{23}
=
\frac{t-1-\eta\kappa/2}{2+\eta\xi}e_{31}.
\]

Thus the quotient is one free rational line:

\[
\boxed{
\mathcal R_{\rm occ,\mathbb Q}
\simeq\mathbb Q[[\eta,t,\kappa,\xi]]\,e_{31}.
}
\]

No rational route-difference node class survives.

## Integral residual

At every physical node \(t=1\) or \(t=3\), the specialized integral row
has greatest common divisor two:

\[
(2,0)
\quad\text{or}\quad
(2,-2).
\]

Therefore each integral node fiber has

\[
\mathbb Z\oplus\mathbb Z/2.
\]

The torsion is exactly the already established occurrence-identification
factor two. It is not a new prime or support generator.

## Result

The two source routes supply one rational coefficient line with a known
integral saturation defect. The unresolved local information must come from
the \(A_1\) vanishing-cycle/endpoint complex, not from an independent
occurrence-difference generator.

## Scope

This result classifies the occurrence presentation only. It does not compute
the \(A_1\) differential, integral saturation of the complete logarithmic
complex, or the physical period.

## Durable verification

- research/benincasa/check_soft_triangle_occurrence_coherence.py;
- research/benincasa/soft-triangle-occurrence-coherence.json;
- exact formal-unit section and all four integral node fibers;
- epistemic event
  ev-000000003249-1776c0b0-6f1d-4722-b517-b02de1e7170d.

## Next falsifier

Map the existing three-face endpoint cube into the one-line occurrence
coefficient at each \(A_1\) node. Compute the resulting local cone over
\(\mathbb Q\) and \(\mathbb Z\). Any rational survivor is a genuine
coefficient costalk; pure two-torsion remains occurrence saturation.
