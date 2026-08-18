---
id: 445
date: 2026-08-17
title: The Native Thom Normal Line Cancels Cut Holonomy
---

# The Native Thom Normal Line Cancels Cut Holonomy

Entry 444 detects a nonzero \(\mathbb Z/2\) holonomy class after scalarizing
the pairwise Cut comparisons. The question is whether cancellation requires a
new auxiliary twist or is already part of the transformed object.

Entry 438 supplies the answer at carrier level. Every Cut facet has a disjoint
marked-normal copy shifted by one degree. On a compatible pair overlap,
interchanging the two odd normal factors contributes the determinant-line
braiding sign \(-1\). This is the same edge local system as the raw
restriction-order sign found in Entry 442.

On the five fundamental cycles, both local systems have holonomy
\[
(-1,+1,-1,-1,+1).
\]
Their tensor product therefore has holonomy
\[
(+1,+1,+1,+1,+1).
\]
The cancellation occurs already on every one of the twelve edges, since
\((-1)(-1)=+1\).

The remaining transformed factors do not change this conclusion. Entries 440
and 441 give path-independent sheet localization, conductor base change,
primitive log Thom trace, and physical-line coefficient \(+1\). Thus the
compensating local system is precisely the native odd marked-normal Thom line;
it is not an ad hoc repair.

There are consequently two distinct statements. Untwisted scalar descent is
obstructed, as Entry 444 says. Descent in the native graded Thom category is
unobstructed at the sign level. The next gate is to build the integral twisted
Cech totalization over the Wagner graph and verify its differential and
primitive global class, rather than stopping at holonomy cancellation.

The executable audit is
research/voevodsky/check_n8_thom_orientation_local_system.py.
