---
id: 429
date: 2026-08-17
title: Generic Localization Preserves the Logarithmic Thom Unit
---

# Generic Localization Preserves the Logarithmic Thom Unit

Entry 428 reduced the remaining comparison to the generic radial chart. Flat
base change from
\[
C=A[X,u^{\pm1}]
\quad\text{to}\quad
D=C[X^{-1}]
\]
preserves the relative interval complex, its primitive class
\([I]=e_1-e_D\), and the pairing \(\operatorname{tr}([I])=1\). The only
possible ambiguity is the change from the Kato normal coordinate \(u\) to the
raw DNC coordinate \(t=u/X\).

For ordinary additive differentials one has
\[
du=X\,dt+t\,dX.
\]
Relative to the occurrence base this becomes \(du=X,dt\), so an additive
Thom generator would acquire the unit \(X\). A claim of literal unit
preservation for the ordinary additive dualizing line would therefore be
false.

The connector, however, carries the logarithmic normal-circle orientation.
On the generic chart,
\[
d\log u=d\log X+d\log t.
\]
Passing to relative logarithmic differentials over the occurrence base kills
\(d\log X\), and hence
\[
\boxed{d\log u=d\log t\quad\text{relatively}.}
\]
The logarithmic orientation determinant is exactly \(+1\), not merely a unit.
Consequently localization sends the Kato Thom trace to the raw generic
log-DNC trace with
\[
\boxed{\operatorname{tr}_{\rm log}([I])=+1.}
\]

Reflection exchanges the interval endpoints and reverses the log orientation;
the two signs again cancel. Thus the comparison is compatible with the marked
orientation and introduces neither a scalar nor an occurrence monomial.

This closes the generic logarithmic trace comparison. It does not identify
the additive canonical modules, whose coordinate bases differ by \(X\), and it
does not yet construct the complete global algebraic correspondence span.
The remaining task is to assemble the three rotated Artin/Kato charts with
the normalization-sheet source and identify both global projections, rather
than only their finite and generic local models.

The executable audit is
`research/voevodsky/check_generic_log_dnc_thom_trace.py`.
