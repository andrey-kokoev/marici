---
id: 535
date: 2026-08-18
title: The Carrier Differential Reduces Cut Cech Ambiguity to Five Top Cycles
---

# The Carrier Differential Reduces Cut Cech Ambiguity to Five Top Cycles

Entry 534 found (157) integral cycle directions on the cellwise Čech page.
This entry computes the differential induced on that page by every radial and
normal arrow of the loaded Cut carriers.

For each induced Cut graph, choose a spanning forest.  Its non-tree edges give
an integral basis of the graph-incidence cokernel.  Project each carrier arrow
to the target graph and reduce it against the target forest.  This constructs
the induced matrices without choosing a quotient after seeing their ranks.

The chain groups, in internal degrees zero through four, have ranks

\[
(0,4,32,72,49).
\]

The four differentials have rational ranks

\[
(0,4,28,44),
\]

and their consecutive products vanish exactly.  Therefore the rational
homology is

\[
\boxed{(0,0,0,0,5)}.
\]

Thus (152) of the (157) cellwise Čech directions are removed by the
ordinary loaded-carrier differential.  Only five top-degree directions
survive.  Projection of the top kernel to the five Wagner-cycle coordinates
of the empty loaded label has full rank five.  The survivors are therefore
not a new bulk family: rationally they are the transported form of the five
global cycles already present in the physical Cut nerve.

This result still does not prove uniqueness of the descended physical line.
It instead isolates the exact residual ambiguity:

\[
\boxed{H_{m carrier}(H^1_{\check C})\otimes\mathbb Q
       \cong\mathbb Q^5\text{ in top degree}.}
\]

The remaining integral test has two parts.  First compute Smith data for the
induced matrices and their kernel/image quotients to exclude finite torsion or
nonprimitive projection onto the Wagner lattice.  Then evaluate the physical
line's edge comparison on those five cycles.  If all five evaluations vanish,
the physical section is unique despite ambient derived (H^1); otherwise it
forms a torsor over the detected cycle lattice.

The executable audit is
`research/voevodsky/check_n8_cut_cech_h1_carrier_homology.py`.
