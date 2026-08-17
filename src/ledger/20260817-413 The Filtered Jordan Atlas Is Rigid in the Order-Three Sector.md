---
id: 413
date: 2026-08-17
title: The Filtered Jordan Atlas Is Rigid in the Order-Three Sector
---

# The Filtered Jordan Atlas Is Rigid in the Order-Three Sector

Entry 412 proved that the sole order-three obstruction to extending the
filtered atlas across the Jordan cap is zero. Existence alone does not say
whether the extension still requires a choice. The same twisted carrier
calculation shows that it does not.

After the unimodular collapses of Entry 411, the capped Möbius cochain
complex with orientation coefficients is
\[
 \mathbb F_3
 \xrightarrow{u-1}
 \mathbb F_3
 \xrightarrow{u+1}
 \mathbb F_3.
\]
For the selected orientation monodromy \(u=-1\),
\[
 u-1=-2=1,\qquad u+1=0
 \quad\text{in }\mathbb F_3.
\]
Consequently
\[
 \boxed{H^0=0,\qquad H^1=0,\qquad H^2\cong\mathbb F_3.}
\]

The interpretation is the standard obstruction tower for descent of the
local order-three road extension:

- \(H^2\) contains the obstruction to existence;
- when that obstruction vanishes, equivalence classes of lifts form a
  torsor under \(H^1\);
- automorphisms of a fixed lift are measured by \(H^0\).

Entry 412 evaluates the unique \(H^2\) coordinate as zero. The vanishing
of \(H^1\) therefore makes the lift unique up to filtered equivalence, and
the vanishing of \(H^0\) leaves no residual order-three gauge
automorphism. Thus the nonzero local Tate extension remains part of the
filtered object, but its global Jordan descent is rigid.

The independent order-two endpoint ambiguity is also already exhausted.
Entry 400's geometric ray-to-sheet comparison is the unique integral
solution of
\[
 b-a=1,\qquad a+b=1,
\]
namely \((a,b)=(0,1)\), and hence
\[
 p_{\partial,Q}=0\in\mathbb Z/2.
\]
Entries 401--404 then show that its dihedral, endpoint-Jordan, and square
corrections vanish. This order-two statement is not inferred from the
mod-three complex; it is a separate geometrically fixed stage of the same
obstruction tower.

## Consequence

At the carrier and finite filtered-PC levels already constructed in
Entries 381--412, there is no remaining discrete choice of global lift:
\[
 \boxed{\text{the filtered Jordan atlas exists and is rigid.}}
\]
Accordingly, the missing full loaded PC chain map is no longer an existence
or coherence problem. It is an explicit realization problem: totalize the
already fixed connector, Cartier, endpoint, Tor-suspension, and
primitive/contact extension maps in one chain model and verify that its
associated grades recover the established pieces.

This statement does not itself write that totalized chain map, identify a
smooth representative, or promote the construction beyond the existing
finite filtered-PC category.

The executable audit is
\`research/voevodsky/check_filtered_atlas_rigidity.py\`.
