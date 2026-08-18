---
id: 464
date: 2026-08-17
title: The Two Resonances Have Unequal Cartier Thickness
---

# The Two Resonances Have Unequal Cartier Thickness

Entry 462 leaves visible powers of (u) in the first Cartier symbols.  The
degreewise Rees shifts of Entry 460 cancel them exactly.  For

\[
a^I=u^{\lfloor I/2\rfloor}a^{I\bmod2}t^{\lfloor I/2\rfloor},
\]

the normalized (q)-symbol at the odd resonance ((I,J)=(7,1)) is

\[
-6a t^3(b+1).
\]

This is precisely the source-derived odd lattice generator with boundary
divisor

\[
3[b=1]+4[b=-1].
\]

It is reached independently from sectors ((s_a,s_b)=(1,1)) and ((1,0)),
using source monomials (a^5) and (a^4), respectively.  The coefficient
(-6) is a unit, so the first Cartier symbol is surjective on the odd
resonant block.

The even resonance ((0,0)) has no possible source: every normalized
(p)-symbol has target (a)-degree at least one, and every normalized
(q)-symbol has degree at least two.  Its first Cartier symbol is zero.

Let (R=\mathbb Q[z]/(z^2)) denote the doubled carrier direction.  Locally on
the resonant blocks, the transformed exact image has the form (zA).  Hence:

- at ((0,0)), (A=0), so the block remains (R), of Cartier length two;
- at ((7,1)), (A) is surjective, so the block is (R/(z)), of length one.

The complete resonant associated object therefore has total Cartier length
three but reduced rank two.  This is compatible with Benincasa Entry 463: the
two reduced nearby-cycle characters survive with monodromy (+1) and (-1),
while only the invariant class retains a nilpotent Cartier thickening.

This is not yet the global specialization theorem.  The calculation is on the
normalized exceptional blocks; the specialization map from the full exact
cokernel must still be constructed and checked at (b=\pm1).  Its predicted
target is now precise: a length-two invariant block plus a reduced
anti-invariant block.

The executable audit is
research/voevodsky/check_soft_axis_normalized_cartier_resonance.py.
