---
id: 448
date: 2026-08-17
title: The First Soft-Axis Gauss-Manin Lift Is Necessarily Meromorphic
---

# The First Soft-Axis Gauss-Manin Lift Is Necessarily Meromorphic

Entry 447 constructs the full monic Cayley--Menger family and finds
\[
K_0=a^4,
\qquad
\partial_uK|_0=a^2(1-b^2).
\]
The first geometry-derived question is whether \(\partial_u\) admits a regular
vertical correction preserving the hypersurface relation.

At the soft fibre,
\[
(K_0,\partial_aK_0,\partial_bK_0)=(a^3).
\]
The Kodaira--Spencer class is therefore
\[
\kappa_{\rm soft}
= [a^2(1-b^2)]\in
\mathbb Q[a,b]/(a^3).
\]
It is nonzero and is annihilated by \(a\). A regular polynomial vector field
\(V\partial_a+W\partial_b\) cannot cancel it: the Jacobian contribution has
\(a\)-order at least three, while \(\kappa_{\rm soft}\) has order two.

The minimal first-order cancellation is instead
\[
V=\frac{b^2-1}{4a},
\qquad
\partial_uK+V\partial_aK=0
\quad (u=0).
\]
Thus the required Gauss--Manin lift is necessarily meromorphic with a simple
pole on \(a=0\). The obstruction vanishes at the two distinguished
coefficient directions \(b=\pm1\), but is nonzero generically.

This locates the missing correction geometrically. It cannot be supplied by
a regular connection on the naive quartic quotient, nor by copying the
Entry-446 cellular section. The natural next construction is the blowup of
the mixed ideal \((u,a)\), retaining its exceptional divisor, and a logarithmic
relative connection there. This is directly analogous in form—but not in
coefficients—to Benincasa's mixed-ideal blowup frontier.

No claim is made yet that the logarithmic lift exists globally, that it
identifies the filtered exact-form cokernel, or that its exceptional support
pushes forward to the physical target.

The executable audit is
research/voevodsky/check_soft_axis_gauss_manin_lift_obstruction.py.
