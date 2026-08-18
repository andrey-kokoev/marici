---
id: 555
date: 2026-08-18
title: The Positive Chain Selects No Lower Kummer Resonance Grade
authors:
  - marici.Nima
---

# The Positive Chain Selects No Lower Kummer Resonance Grade

Entry 554 proves that star/shriek variance alone cannot select one of the two
normal grades at the Kummer resonance \(\lambda=0\). The remaining
source-derived candidate is the physical integration-chain boundary. This
entry evaluates it using the frozen generic lower positive-chain census.

For the representative wall,

\[
q_{g1}=X_1+b+c.
\]

The literal Bunch--Davies chamber obeys

\[
X_1>0,\qquad b\geq0,\qquad c\geq0.
\]

Therefore

\[
\boxed{q_{g1}\geq X_1>0}
\]

everywhere on the chamber. Its closure at generic positive \(X_1\) is disjoint
from \(q_{g1}=0\). Consequently the chain has no normal boundary on this wall:

\[
\boxed{
\Gamma_{\rm BD}\cap V(q_{g1})=\varnothing,
\qquad
\partial_{q_{g1}}\Gamma_{\rm BD}=0.
}
\]

## Selection verdict

The physical chain therefore selects neither cohomological grade of

\[
[\,\mathbb Q\xrightarrow0\mathbb Q\,].
\]

It pairs trivially with the generic supported wall object. This agrees with
the earlier complete positive-chain census: all frozen marked-pole collision
strata are disjoint from the literal positive chamber and have zero physical
Picard--Lefschetz intersection.

Thus the current rank-five lower object is classified more narrowly as

\[
\boxed{
\text{generic logarithmic coefficient support}
\quad\text{with no literal positive-chain activation}.
}
\]

It is not a generic physical period block. A nonzero physical realization
would require additional source-derived data:

- analytic continuation to a boundary-value chamber meeting the wall;
- a soft or endpoint degeneration in which \(X_1\to0\);
- or a different relative-chain class.

None may be inferred from the critical rank.

## Consequence for H2

The support geometry and Kummer calculus remain valid, but the physical
functor kills this generic supported sector. This is exactly the separation

\[
\text{shared carrier/kernel calculus}
\quad+\quad
\text{sector- and chamber-specific coefficient pairing}.
\]

The next admissible frontier is the soft/endpoint limit \(X_1\to0\), where the
closure of the positive chain can first meet \(q_{g1}=0\). That degeneration
must be derived before assigning either resonant grade.

The executable audit is
\`research/benincasa/check_generic_lower_physical_kummer_selection.py\`.
