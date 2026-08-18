---
id: 534
date: 2026-08-18
title: The Full Cut Cech Page Has 157 Cycle Directions
---

# The Full Cut Cech Page Has 157 Cycle Directions

Entry 533 constructs the full Thom-twisted Čech totalization on the eight
loaded Cut charts.  Existence of its primitive constant section does not imply
uniqueness.  This entry computes the Čech-direction cohomology before taking
the internal carrier differential.

Because every chart-to-overlap map is a coordinate quotient, the Čech complex
splits by loaded cell label.  For a label ((F,H)), let (Gamma_{F,H}) be the
induced subgraph of the physical Wagner graph on the Cuts whose charts contain
that label.  Its integral incidence complex has

\[
\operatorname{rk}H^0=c(Gamma_{F,H}),
\qquad
\operatorname{rk}H^1=|E|-|V|+c(Gamma_{F,H}),
\]

and no torsion.

There are (4985) distinct loaded labels.  By internal chain degree their
counts are

\[
(168,900,1800,1592,525).
\]

The resulting Čech ranks are

\[
\operatorname{rk}H^0=(224,1252,2600,2376,805),
\]

and

\[
\boxed{\operatorname{rk}H^1=(0,4,32,72,49)},
\qquad
\boxed{\operatorname{rk}H^1_{m total}=157}.
\]

Exactly (137) labels carry a cycle, while (2192) labels have disconnected
eligible-Cut graphs.  The latter contribute (2272) extra (H^0) component
directions beyond one per label.  The largest graph is the original Wagner
graph and occurs only for the empty loaded label; it contributes its familiar
five cycles.  Smaller labels contribute the remaining (152) directions.

This is not yet hypercohomology of the full total complex.  The internal
radial and normal differential acts between these cellwise graph homology
groups and may kill most or all of the (157) directions.  Therefore the
correct conclusion is narrow:

\[
\boxed{\text{full-chart uniqueness does not follow from Čech descent alone}.}
\]

The next admissible calculation is the induced carrier differential on the
cellwise (H^1) lattice, followed by its integral homology.  Only that page
can decide whether the primitive physical section is unique in the totalized
derived object.

The executable audit is
`research/voevodsky/check_n8_full_cut_cech_cellwise_cohomology.py`.
