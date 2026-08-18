---
authors:
  - marici.Benincasa
date: 2026-08-18
---
# 672 — The Complete Logarithmic Syzygy Module Has Constant Rank on Tested Quartic Fibers

## Hard-to-vary claim

If the algebraic quartic

\[
\mathcal Q
=
-16p^2-8pE^2+8sE^3-5E^4
\]

is the Fitting support of the complete minimal source-logarithmic primitive
module, then the degree-seven syzygy dimension must jump at a generic
nonsoft point of \(\mathcal Q=0\).

This is distinct from Entries 526--528. Those entries tested a fitted
quotient line. Here the frozen object is the full degree-seven module

\[
\operatorname{Der}_{\leq 7}
\bigl(-\log(K_Eq_{g1}q_{g2}q_{g3}q_{g23}q_{g31})\bigr)
\]

from Entry 652, with all five source poles retained.

## Frozen finite-field construction

Work over

\[
\mathbb F_{2305843009213693951}.
\]

A source-independent parameterization of quartic-zero fibers is obtained by
choosing \(E,t\) and setting

\[
s=\frac{t^2/E+E}{2},
\qquad
p=-\frac{E^2}{4}+\frac{Et}{2}.
\]

Then

\[
E(2s-E)=t^2,
\]

and direct substitution gives \(\mathcal Q=0\).  Solving

\[
X^2-sX+p=0
\]

produces the two ordered branches \((x,y)\); \(z=E-s\).  Two independent
families were used,

\[
(E,t)=(2,3),\qquad (3,2),
\]

and both ordered branches were retained.  All arithmetic, including the
Cayley--Menger polynomial and the five-wall syzygy matrix, was performed
modulo the field prime.

## Result

At all four quartic-zero samples,

\[
\dim
\operatorname{Der}_{\leq 7}(-\log D)
=3.
\]

For each sample, the two transverse comparison fibers obtained by replacing
\(E\) by \(E-1\) and \(E+1\), while retaining \(x,y\) and updating
\(z=E-x-y\), also have dimension three.  Thus the census is

\[
\begin{array}{c|c|c}
\text{locus} & \text{samples} & \text{degree-seven nullity}\\ \hline
\mathcal Q=0 & 4 & 3\\
\text{transverse neighbors} & 8 & 3.
\end{array}
\]

No rank jump is detected.

Therefore the tested claim is falsified:

\[
\boxed{
\mathcal Q
\text{ is not Fitting support of the complete minimal logarithmic-syzygy module
on the tested generic fibers.}
}
\]

## Interpretation

This removes another possible home of \(\mathcal Q\).  The quartic is not
detected by:

- the pure elliptic infinity-Gysin quotient;
- the rank-seven algebraic kernel;
- the fitted conic line;
- ordinary wall/conductor support;
- the unsplit numerator-zero divisor; or now
- the rank of the complete minimal source-logarithmic primitive module.

The surviving location remains secondary data: a supported relative-chain
pairing, a Gysin/extension class, or an apparent singularity of a chosen
scalar presentation.  This result does not distinguish those alternatives.

## Classification

- existing carrier: \(K_E=0\) and the five frozen marked walls;
- coefficient support tested: Fitting support of the minimal logarithmic
  syzygy module;
- result: \(\mathcal Q\) is absent in the tested fibers;
- new carrier datum: none.

## Scope

This is an exact finite-field generic-fiber falsifier, not a symbolic global
Fitting-ideal theorem.  It proves neither flatness on every point of
\(\mathcal Q\) nor compatibility with the physical integration chain.

## Next falsifier

Do not repeat absolute rank tests.  Construct a source-derived supported
pairing of the three minimal primitive directions with the physical relative
chain, then ask whether its determinant or extension class has
\(\mathcal Q\)-support.  If no such source-derived pairing exists, record
that absence rather than fitting one.

## Evidence

- \`research/benincasa/check_q_zero_log_syzygy_rank.rs\`;
- \`research/benincasa/q-zero-log-syzygy-rank.json\`;
- Entries 652, 526--528, 667--669.

## Outcome contract

~~~json
{
  "claim": "The complete degree-seven logarithmic-syzygy module jumps in rank on generic Q=0 fibers.",
  "status": "falsified_in_tested_fibers",
  "q_zero_samples": 4,
  "transverse_neighbor_samples": 8,
  "q_zero_nullity": 3,
  "neighbor_nullity": 3,
  "rank_jump_detected": false,
  "classification": "not tested Fitting support; no new carrier datum",
  "next_experiment": "Compute a source-derived supported physical-chain pairing before testing Q in secondary extension data."
}
~~~
