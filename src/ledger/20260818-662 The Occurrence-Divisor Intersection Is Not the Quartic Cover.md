---
authors:
  - marici.Benincasa
date: 2026-08-18
---
# 662 — The Occurrence-Divisor Intersection Is Not the Quartic Cover

## Hard-to-vary claim

The two physical occurrence denominators define two marked divisors on the
post-\(q_{G_{12}}\) residue surface, not one distinguished endpoint ratio.
Moreover, their algebraic intersection does not generate the quartic
\(\mathcal Q\): the Cayley--Menger branch value at that intersection has
different generic support.

## Frozen residue data

The source denominators restrict exactly as

\[
q_{g_{23}}|_{G_{12}}=b-x,
\qquad
q_{g_{31}}|_{G_{12}}=a-y.
\]

Thus the unsplit physical source carries the union

\[
D_{\rm occ}=\{b=x\}\cup\{a=y\},
\]

with one occurrence divisor in each source summand. It does not select their
intersection as a relative-chain endpoint.

Entry 661 supplies the literal Cayley--Menger polynomial

\[
\begin{aligned}
K_E(a,b)={}&x^2a^4-(x^2+y^2-z^2)a^2b^2+y^2b^4\\
&+\left[x^2(x^2-y^2-z^2)+E^2(y^2-x^2-z^2)\right]a^2\\
&+\left[y^2(y^2-x^2-z^2)+E^2(x^2-y^2-z^2)\right]b^2\\
&+z^2E^4+E^2z^2(z^2-x^2-y^2)+z^2x^2y^2,
\end{aligned}
\]

where \(E=x+y+z\).

## Direct intersection test

The two occurrence divisors meet at

\[
(a,b)=(y,x).
\]

Direct substitution and factorization give

\[
\boxed{
K_E(y,x)
=
E^3\left[2z^3+(x-y)^2(x+y-z)\right].
}
\]

The source quartic is instead

\[
\mathcal Q
=-16x^2y^2-8xyE^2+8(x+y)E^3-5E^4.
\]

These polynomials are neither associates nor do they have the same generic
zero locus. In particular, the intersection branch value has a cubic
total-energy factor, whereas

\[
\mathcal Q|_{E=0}=-16x^2y^2
\]

is nonzero away from soft support.

Therefore

\[
\boxed{
\mathcal Q
\ne
\text{the branch value at }
\{q_{g_{23}}=q_{g_{31}}=0\}.
}
\]

## Typing consequence

Even before this polynomial mismatch, choosing the intersection would have
been inadmissible: the physical form is a sum of two four-mark relative
classes. Replacing that union by the codimension-two intersection introduces
a new operation not supplied by the source integration chain.

The direct mismatch now also falsifies the candidate numerically and
algebraically. No choice of normalization by a source-fixed unit can turn
\(K_E(y,x)\) into \(\mathcal Q\), because their behavior at \(E=0\)
differs generically.

## Relation to parallel work

This calculation uses Entry 661's literal residue polynomial but does not
duplicate its rank-twenty reduction or horizontal-saturation program. It
tests only one candidate home for \(\mathcal Q\) inside the marked
post-residue geometry.

## Classification

- existing carrier: unchanged;
- physical marked data: the union \(\{b=x\}\cup\{a=y\}\);
- rejected coefficient support: their codimension-two intersection;
- new carrier datum: none.

## Surviving frontier

Entry 660's Källén double cover remains an ambient source-compiled candidate,
but it is not obtained by intersecting the two occurrence sections.

The next admissible test is separate restriction:

\[
K_E(a,x)
\quad\text{and}\quad
K_E(y,b).
\]

Compute each branch polynomial and its discriminant in the remaining fiber
coordinate. Then test whether \(\mathcal Q\) occurs as a canonical factor
for either individual physical summand. This preserves the source's
occurrence decomposition and does not invoke the rank-thirty-five extension.

## Evidence

- primary-source denominator residue recorded in
  research/benincasa/physical_five_pole_g12_residue.py;
- literal \(K_E\) in Entry 661 and
  research/benincasa/physical_four_mark_residue_twisted_derham.py;
- research/benincasa/physical-occurrence-intersection-q-gate.json.
- epistemic event ev-000000000265-b868219e-ae6a-4b0c-bcbb-d4a396e043d7.

## Outcome contract

~~~json
{
  "claim": "The quartic Q is the Cayley-Menger branch value at the intersection of the two physical occurrence divisors.",
  "status": "falsified",
  "occurrence_intersection": "(a,b)=(y,x)",
  "intersection_branch_value": "E^3*(2*z^3+(x-y)^2*(x+y-z))",
  "generic_support_equals_Q": false,
  "source_selects_intersection": false,
  "new_carrier_datum": false,
  "next_experiment": "Compute the discriminants of K_E(a,x) and K_E(y,b) separately."
}
~~~
