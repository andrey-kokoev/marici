---
id: 438
date: 2026-08-17
title: The Loaded Octagon Carrier Contains the Forced Cut Boundary
---

# The Loaded Octagon Carrier Contains the Forced Cut Boundary

Entry 437 fixed the right-hand side of the first eight-point Cut-naturality
square. We now construct the smallest ambient combinatorial object in which
its left-hand side could live: the loaded noncrossing-diagonal carrier of the
octagon.

The octagon has 20 diagonals. Its noncrossing face counts are
\[
(1,20,120,300,330,132).
\]
Loading a face \(F\) by every subset \(H\subseteq F\) produces 12,425 cells.
With degree \(5-|F|+|H|\), the chain ranks are
\[
(132,990,2940,4320,3140,903).
\]

For the cut \(D_{05}\), the Entry-437 carrier embeds by
\[
(F,H)\longmapsto(F\cup\{D_{05}\},H).
\]
The Cut divisor is adjoined but left unmarked. This gives exactly 1,075
distinct octagon cells and preserves every degree. It is precisely the closed
\(D_{05}\) boundary facet, not merely an abstract carrier with matching size.

Contracting the native octagon orientation along \(D_{05}\), with the
mandatory normal-suspension factor \((-1)^{|F|}\), gives the boundary
orientation. Omitting that factor reverses every radial arrow. With it, the
checker verifies all 369 radial face incidences, equivalently all 1,735 loaded
radial arrows after accounting for markings.

There is a second 1,075-cell copy in which \(D_{05}\) is marked. It is disjoint
from the boundary image and shifted by one degree. This is the normal direction
to the Cut divisor. Its existence explains why the unmarked inclusion is
canonical and identifies the data an extension differential must control.

Thus there is no carrier-level extension obstruction: the forced six-by-four
boundary sits functorially and orientation-compatibly inside the full
eight-point carrier. The next gate is genuinely algebraic. One must place the
conductor/Thom kernel on the 12,425 cells and determine whether the primitive
boundary line has a cycle representative whose differential in the
marked-normal copy vanishes.

The executable audit is
research/voevodsky/check_n8_loaded_octagon_carrier.py.
