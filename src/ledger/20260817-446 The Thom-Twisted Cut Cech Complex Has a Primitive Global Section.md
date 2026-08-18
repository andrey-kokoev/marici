---
id: 446
date: 2026-08-17
title: The Thom-Twisted Cut Cech Complex Has a Primitive Global Section
---

# The Thom-Twisted Cut Cech Complex Has a Primitive Global Section

Entry 445 cancels the Cut-nerve sign holonomy. The integral Cech complex makes
the arithmetic consequence explicit. The physical nerve has eight vertex
charts and twelve pair overlaps, so its coefficient complex is
\[
\mathbb Z^8\longrightarrow\mathbb Z^{12}.
\]

After forgetting the odd Thom-normal line, transport on every edge is \(-1\).
The differential is the signless incidence matrix. It has rank eight and the
greatest common divisor of its maximal minors is two. Consequently
\[
H^0_{\mathrm{scalar}}=0,
\qquad
H^1_{\mathrm{scalar}}\cong\mathbb Z^4\oplus\mathbb Z/2.
\]
The \(\mathbb Z/2\) summand is the integral shadow of Entry 444's odd-cycle
holonomy.

With the native marked-normal Thom line included, the two minus signs cancel.
The differential becomes the ordinary oriented incidence matrix. It has rank
seven and a unit maximal minor, hence saturated image. Therefore
\[
H^0_{\mathrm{Thom}}\cong\mathbb Z,
\qquad
H^1_{\mathrm{Thom}}\cong\mathbb Z^5,
\]
with no integral torsion. The generator of \(H^0\) is the constant vector
\((1,\ldots,1)\), which is primitive and matches the eight positive physical
Cut coefficients of Entry 441.

Thus the rank-one integral twisted Cech totalization exists and carries the
required global class. The next gate is to lift this coefficient-line
calculation to the full eight-chart system of 1,075-cell Cut objects and their
125-cell pair overlaps, checking the total differential cell by cell.

The executable audit is
research/voevodsky/check_n8_twisted_cut_cech_totalization.py.
