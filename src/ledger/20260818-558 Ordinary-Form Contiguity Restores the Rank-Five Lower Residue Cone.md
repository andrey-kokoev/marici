---
id: 558
date: 2026-08-18
title: Ordinary-Form Contiguity Restores the Rank-Five Lower Residue Cone
authors:
  - marici.Benincasa
---

# Ordinary-Form Contiguity Restores the Rank-Five Lower Residue Cone

Entry 553 constructs the correct integer-contiguity chain map but declares its
normal cone acyclic by replacing the local cone with
\([k\xrightarrow{17}k]\). That replacement silently gives the source a
logarithmic one-form generator. The actual source lies on the space containing
the wall and therefore uses ordinary forms. This entry computes the resulting
cone degree-by-degree.

## Exact local map

Let \(q=q_{g1}\), let \(n=17\), and consider

\[
(\mathcal O,d)
\longrightarrow
(\mathcal O(*0),d+n\,dq/q),
\qquad
\omega\longmapsto q^{-n}\omega.
\]

In degree zero the image contains \(q^m\) for \(m\geq-n\). In degree one,
ordinary source forms map as

\[
q^k dq\longmapsto q^{k-n}dq,
\]

so the image contains \(q^m dq\) only for \(m\geq-n\). It does **not** contain

\[
q^{-n-1}dq=q^{-n}\frac{dq}{q}.
\]

On the quotient, the target differential is

\[
q^m\longmapsto(m+n)q^{m-1}dq.
\]

Every quotient one-form is hit except \(q^{-n-1}dq\). No quotient function is
closed. Therefore

\[
\boxed{
H^0(C_n)=0,
\qquad
H^1(C_n)=
k\left\langle q^{-n}\frac{dq}{q}\right\rangle.
}
\]

Finite Laurent truncations at cutoffs \(20,24,32,48\) all give the same
one-dimensional cohomology.

## Source-type control

If the source is enlarged to \(\Omega^1(\log q)\), its image does contain
\(q^{-n}dq/q\), and the quotient becomes acyclic. Thus Entry 553's result is
correct only for a logarithmic source lattice, not for the ordinary de Rham
source appearing in its own contiguity map.

## Global rank consequence

Entry 557 independently computes the unmarked tangential wall rank as five.
Tensoring it with the one-dimensional normal residue gives

\[
\boxed{
\operatorname{rank}
\operatorname{Cone}(\text{integer contiguity})
=5.
}
\]

This restores a canonically typed rank-five residue cone at the frozen integer
coefficient. It is not obtained by subtracting ranks: the map comes from
integer contiguity, the normal class from the ordinary/meromorphic lattice
quotient, and the tangential rank from the independent wall calculation.

Entries 552--554 remain relevant to a formal Kummer-parameter family, but they
do not replace this fixed-integer lattice calculation. Entry 553's claim that
integer contiguity trivializes the ordinary-source residue cone is retracted.
Entry 555's positive-chain disjointness also remains valid: a nonzero
cohomological residue object need not pair with the literal generic positive
chain.

The next test is now a genuine comparison: map this rank-five contiguity
residue object to Entry 549's resolved rank-five boundary packet and verify
the regulator connection and pair-residue incidences.

The executable audit is
`research/benincasa/marici-gm/src/bin/generic_lower_integer_contiguity_cone.rs`.
