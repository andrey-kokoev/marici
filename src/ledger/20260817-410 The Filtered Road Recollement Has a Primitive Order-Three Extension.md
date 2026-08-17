---
id: 410
date: 2026-08-17
title: The Filtered Road Recollement Has a Primitive Order-Three Extension
---

# The Filtered Road Recollement Has a Primitive Order-Three Extension

Entry 409 typed multiplicative holonomy after quotienting away the
\(A_2\) contact sector. To retain that sector, the relevant local object is
the \(C_3\)-equivariant extension
\[
0\longrightarrow A_2
\longrightarrow P_D\cong\mathbb Z[C_3]
\xrightarrow{\epsilon}\mathbf1
\longrightarrow0.
\]

This extension is not equivariantly split over \(\mathbb Z\). Every
\(C_3\)-invariant vector of \(P_D\) is \(a(1,1,1)\), whose augmentation is
\(3a\). Therefore no invariant lift of \(1\) exists.

The invariant long exact sequence gives
\[
P_D^{C_3}\xrightarrow{\epsilon}\mathbf1^{C_3}
\longrightarrow H^1(C_3,A_2),
\qquad
\operatorname{im}\epsilon=3\mathbb Z,
\]
and hence
\[
\boxed{H^1(C_3,A_2)\cong\mathbb Z/3.}
\]
The displayed road extension is the generator: its connecting class is the
residue of \(1\) modulo \(3\). Pullback along multiplication by three splits
via the invariant norm vector \((1,1,1)\), while pullback along one or two
does not. Thus the extension has exact order three.

Reflection preserves augmentation and conjugates road rotation to its
inverse, so the nonsplit sequence is stable under the full local \(D_3\)
symmetry. This is the categorical origin of Entry 94's Smith factor
\((1,1,3)\): the index-three primitive/contact gluing is the same
equivariant extension class, not a numerical accident.

## Consequence

The primitive multiplicative holonomy of Entry 409 cannot lift to an
ordinary integral atlas that simultaneously retains \(A_2\). Such a lift
would provide an equivariant splitting and kill the nonzero generator of
\(\operatorname{Ext}^1_{\mathbb Z[C_3]}(\mathbf1,A_2)\).

The correct full object must therefore be filtered or higher-categorical:
its primitive quotient carries the \(-1\) crosscap holonomy, its contact
graded piece carries \(A_2\), and their gluing is the primitive
\(\mathbb Z/3\) extension. Inverting three would split the filtration but
would erase precisely the integral datum we need to preserve.

This identifies the next finite coherence problem: transport this local
order-three extension around the twelve-chart Möbius carrier and test its
global Čech two-class. A zero class yields a global filtered atlas; a
nonzero class is the genuine higher associator.

The executable audit is
\`research/voevodsky/check_cyclic_road_extension_class.py\`.
