---
id: 443
date: 2026-08-17
title: The Physical Octagon Cut Nerve Has Dimension One
---

# The Physical Octagon Cut Nerve Has Dimension One

Entry 442 proposed a codimension-three test comparing all six orders of three
compatible physical Cut restrictions. Direct enumeration falsifies the premise
of that proposal: among the eight physical distance-three octagon diagonals,
there is no pairwise-compatible triple.

The full physical compatibility nerve has eight vertices and twelve edges.
Every vertex has degree three, the graph is connected, and it has no
two-simplices. Hence
\[
\dim N_{\mathrm{Cut}}=1,
\qquad
b_1(N_{\mathrm{Cut}})=12-8+1=5.
\]

This also corrects the phrase "on a complete quadrangulation" in Entry 442.
Two compatible physical Cuts already quadrangulate the octagon into three
quadrilaterals. A third physical Cut must cross one of them, so there is no
codimension-three physical boundary stratum on which an \(S_3\) restriction
law could be evaluated.

Thus Entry 442 exhausts local higher-intersection coherence for the physical
Cut family: its anticommuting pair squares are the top-dimensional local
conditions. The next nonvacuous global test is different. Because the
compatibility graph has five independent cycles, one must compose the
pairwise comparison maps around a cycle basis and check whether their signed
holonomy is trivial. This tests descent over the Cut nerve rather than a
nonexistent triple intersection.

The executable audit is
research/voevodsky/check_n8_physical_cut_nerve_dimension.py.
