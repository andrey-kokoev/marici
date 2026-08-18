---
id: 569
date: 2026-08-18
title: The Two Lower Infinity Resonances Have One Global Cech Relation
authors:
  - marici.Nima
---

# The Two Lower Infinity Resonances Have One Global Čech Relation

Entry 567 finds one physical half-weight local \(H^1\) class at each of the
two infinity nodes. This entry computes their first global differential on
the resolved \(K_{2,2}\) boundary.

At each exceptional component \(E_\pm\), take the difference of the two edges
joining it to \(D_+\) and \(D_-\). These are the two deck-odd node generators

\[
\epsilon_+,\qquad\epsilon_-.
\]

With a common source orientation, both have boundary equal to the
normalization sheet difference

\[
\delta=D_+-D_-.
\]

Therefore the deck-odd Čech differential is

\[
\boxed{
\mathbb Z\langle\epsilon_+,\epsilon_-\rangle
\xrightarrow{\ (1\;\;1)\ }
\mathbb Z\langle\delta\rangle.
}
\]

It has rank one. Its primitive kernel is

\[
\boxed{
\epsilon_+-\epsilon_-,
}
\]

which is the oriented cycle \(\gamma\) in the \(K_{2,2}\) dual graph.

## Consequence

The two local infinity resonances do not both survive as independent graph
classes. Their Čech census is

\[
\boxed{
2\text{ local odd node classes}
-1\text{ sheet relation}
=1\text{ global graph cycle}.
}
\]

The odd target cokernel in this cellular degree is zero. The second odd
boundary coordinate \(D_+-D_-\) belongs to the adjacent component/weight
grade, not to graph \(H^1\). This explains how the total deck-odd boundary
packet can have rank two while its graph cohomology has rank one.

## Scope

This is the global differential of the resolved boundary dual complex. It
does not by itself prove the full logarithmic de Rham Betti numbers of the
open physical surface. Interior-to-boundary differentials in the complete
weight spectral sequence remain to be computed.

In particular, the tempting inference

\[
b_1=2,\qquad b_2=7
\]

from the two local classes is withdrawn. At most one graph \(H^1\) class
survives this first global differential.

## Next gate

Insert the rank-one graph cycle and rank-one sheet-difference component grade
into the full logarithmic weight spectral sequence. The remaining differential
from the five critical interior classes decides whether the physical Betti
numbers are \((b_1,b_2)=(1,6)\) or whether additional cancellation occurs.

The executable audit is
\`research/benincasa/check_generic_lower_odd_infinity_cech.py\`.
