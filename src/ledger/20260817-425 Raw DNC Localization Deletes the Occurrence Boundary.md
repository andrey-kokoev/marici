---
id: 425
date: 2026-08-17
title: Raw DNC Localization Deletes the Occurrence Boundary
---

# Raw DNC Localization Deletes the Occurrence Boundary

Entry 424 completed the finite ringed six-operation package. The proposed
identification of its coefficient sheaf with the raw algebraic DNC structure
sheaf fails already on one radial chart, for a structural reason.

Write the raw affine DNC chart as
\[
B=A[X,u,t]/(u-Xt).
\]
At a radial PC stalk the normal parameter \(u\) is inverted. In the raw chart,
however, \(u=Xt\) being a unit forces both \(X\) and \(t\) to be units. Hence
\[
B[u^{-1}]\cong A[X^{\pm1},u^{\pm1}],
\qquad t=u/X.
\]
The corresponding finite stalk of Entry 422 is instead
\[
C=A[X,u^{\pm1}].
\]
It intentionally does not invert the occurrence equation \(X\). The canonical
map is therefore
\[
C\longrightarrow B[u^{-1}]\cong C[X^{-1}],
\]
the localization at \(X\), not an isomorphism.

This also rules out a derived equivalence. The map is flat and injective, but
the nonzero boundary module
\[
C/(X)\cong A[u^{\pm1}]
\]
is annihilated by localization. Equivalently, the raw radial open has deleted
the very occurrence boundary retained by the PC coefficient system. This is
the same support mismatch behind the ordinary-purity failure of the Rees chart
\(u=Xt\): it is not repaired by the Thom trace.

Consequently the finite PC/Čech sheaf must not be described as the pullback of
the ordinary structure sheaf on the raw DNC scheme. It is a logarithmically
saturated coefficient sheaf in which the normal direction may be inverted
without inverting its occurrence divisor. The raw generic chart is recovered
from it by the further localization \(X^{-1}\).

This negative result is useful: the algebraization target is now precise. One
must construct a morphism through a logarithmic Artin-fan, Kato-fan, or
equivalent saturated monoidal model whose stalk is \(C\), and only then compare
its generic localization with the raw DNC chart. Asking for a direct ringed-
space isomorphism would erase the boundary class that carries the connector.

The executable audit is
`research/voevodsky/check_raw_dnc_finite_stalk_comparison.py`.
