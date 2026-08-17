---
id: 394
date: 2026-08-17
title: The Literal Q Boundary Has the Right First Coefficient but Zero Second Transgression
---

# The Literal Q Boundary Has the Right First Coefficient but Zero Second Transgression

Entry 393 left one support attachment between the expanded logarithmic path
and the absolute quotient generator. The absolute cellular complex already
contains a tempting candidate. Let
\[
 q_{03}^{Q}=\{D03\}\in F_2/F_1,\qquad
 E_{D3}=\{D03,x_3\}\in F_1/F_0.
\]
The universal occurrence differential adds a diagonal with its occurrence
variable. Since \(D03=(0,3)<x_3=(3,5)\), the established lexicographic
incidence convention gives
\[
 d q_{03}^{Q}\supset -X_3E_{D3}.
\]
Thus the literal absolute boundary has exactly the required \(x_3\)
occurrence degree and coefficient, up to the forced orientation of the target
basis. The first attachment is not missing.

## The obstruction occurs one step later

Every absolute cellular boundary term starting on a face containing \(D03\)
still contains \(D03\): radial boundaries add diagonals, and normal-circle
boundaries do not change the face. Consequently the full image of the literal
road lies in the strict subcomplex
\[
 G_{03}=\langle(S,H):D03\in S\rangle\subset F_1,
\]
while
\[
 G_{03}\cap F_0=0
\]
because \(v_+=\{x_1,x_3,x_5\}\) does not contain \(D03\). Hence the
second connecting morphism of the literal attachment vanishes:
\[
 q_{03}^{Q}\longrightarrow G_{03}[1]
   \longrightarrow F_0[2]=0.
\]
This recovers the earlier zero Yoneda pullback, now while retaining the useful
information that its first leg has the correct coefficient.

The log-expanded carrier behaves differently:
\[
 C_{\log}=X_1E_{13}+X_{D03}E_{D3},qquad
 dC_{\log}=X_{D03}X_0c-X_1X_5v_+.
\]
Its \(E_{D3}\) component is compatible with the literal absolute first leg,
but its nonzero \(v_+\) endpoint exists only after passing through the
log-expanded central-flip geometry. Removing \(D03\) is not an incidence in
the absolute face poset.

## Sharpened frontier

The remaining datum is therefore not an arbitrary attachment and not another
coefficient. It is a comparison morphism from the expanded logarithmic
carrier to the absolute support filtration which simultaneously:

1. identifies the \(E_{D3}\) leg with
   \(d q_{03}^{Q}=-X_3E_{D3}\);
2. sends the expanded endpoint to the actual \(F_0\) generator \(v_+\);
3. intertwines the logarithmic Cartier residue with the target localization
   triangle.

Entry 393 proves that the coefficient square of such a comparison would
commute. The present result proves that the comparison cannot be replaced by
the literal absolute inclusion: its second transgression is identically zero.
Connector existence remains open, but the search space has narrowed to a
single cross-category comparison across the log expansion.

The executable audit is
research/voevodsky/check_d03_literal_q_boundary_gate.py.
