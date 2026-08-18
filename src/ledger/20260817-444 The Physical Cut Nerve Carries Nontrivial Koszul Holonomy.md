---
id: 444
date: 2026-08-17
title: The Physical Cut Nerve Carries Nontrivial Koszul Holonomy
---

# The Physical Cut Nerve Carries Nontrivial Koszul Holonomy

Entry 443 replaces the nonexistent codimension-three stratum by the global
cycle problem on the physical Cut compatibility graph. That graph is not the
three-cube. It is the eight-vertex Moebius ladder (the Wagner graph): an
eight-cycle together with the matching between opposite vertices.

Entry 442 assigns the comparison sign \(-1\) to every compatibility edge,
because reversing two normal contractions is Koszul odd. For a deterministic
spanning tree, the five chord cycles have lengths
\[
(5,4,5,5,4).
\]
Their signed holonomies are therefore
\[
(-1,+1,-1,-1,+1).
\]
In particular three basis generators detect nontrivial holonomy.

Equivalently, the constant edge one-cochain with value \(-1\) could be removed
by vertexwise sign changes precisely if the compatibility graph were
bipartite. Its five-cycles show that it is not. The Koszul comparison data thus
define a nonzero class in
\[
H^1(N_{\mathrm{Cut}};\mathbb Z/2).
\]

This is a genuine global descent obstruction, not a failure of any local Cut
square. The local codimension-two theorem remains exact, but the eight local
Cut objects cannot be glued with untwisted scalar identifications. The next
gate is to determine whether the normalization-sheet/conductor/Thom package
already carries a compensating orientation local system. If it does not, that
local system must be added explicitly; otherwise global Cut descent is false
in the untwisted category.

The executable audit is
research/voevodsky/check_n8_cut_nerve_signed_holonomy.py.
