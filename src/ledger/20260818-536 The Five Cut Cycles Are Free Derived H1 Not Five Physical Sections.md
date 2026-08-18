---
id: 536
date: 2026-08-18
title: The Five Cut Cycles Are Free Derived H1 Not Five Physical Sections
---

# The Five Cut Cycles Are Free Derived H1 Not Five Physical Sections

Entry 535 isolated five rational top-degree survivors of the carrier
differential on cellwise Cut-Čech (H^1).  This entry completes the integral
test and corrects the interpretation of that group.

Each of the four induced carrier matrices admits a complete reduction by
unimodular row and column operations using only (pm1) pivots.  The unit-pivot
counts equal the rational ranks

\[
(0,4,28,44).
\]

Consequently every nonzero Smith factor is one.  Images are primitive, all
intermediate zero rational homology groups vanish integrally, and the top
kernel is free:

\[
\boxed{H_{m carrier}(H^1_{\check C};\mathbb Z)
       \cong\mathbb Z^5}
\]

in top carrier degree, with zero homology in the other degrees.  There is no
finite torsion and no hidden index in the induced differentials.

## Interpretation correction

The five classes live in Čech degree one.  They are ambient derived
(H^1)-classes of the full loaded chart system, not five distinct global
physical sections.  The distinguished physical section constructed in
Entries 441, 446, and 533 lies in Čech degree zero.  Entry 445 already proves
that its combined sheet/conductor/log-Thom transport is (+1) on every edge
and hence (+1) around all five Wagner cycles.  Its additive edge cocycle is
therefore zero.

Thus the correct statement is

\[
\boxed{\text{the physical section has no cycle-holonomy obstruction, while
the ambient derived descent object retains a free }\mathbb Z^5.}
\]

Whether this (mathbb Z^5) acts as a deformation space requires a separately
typed shift or mapping-complex action.  It cannot be called a torsor of
physical sections merely because it is (H^1).  The next gate is to compute
the relative endomorphism/deformation complex of the framed physical line
inside the totalized Cut object.  Its degree-zero homology, with the eight
local boundary values fixed, is the actual uniqueness group.

The executable audit is
`research/voevodsky/check_n8_cut_cech_h1_carrier_homology.py`.
