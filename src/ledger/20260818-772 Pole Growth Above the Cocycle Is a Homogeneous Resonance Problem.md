---
authors:
  - marici.Nima
date: 2026-08-18
---
# 772 — Pole Growth Above the Cocycle Is a Homogeneous Resonance Problem

## Splitting equation

In an adapted extension frame, a splitting section (X) obeys

\[
dX+A_E X-XA_T=-C.
\]

Entry 762 computed the complete denominator vector simultaneously for
(A_T,A_E), and (C).  Suppose a rational solution has pole order (m) on
a support component (f=0), with (m) strictly larger than the local pole
order already present in (C).

Then the highest negative power of (f) on the left has no inhomogeneous
counterpart on the right.  Its coefficient must vanish in the homogeneous
Hom connection:

\[
\nabla_{\rm Hom}X=dX+A_EX-XA_T.
\]

For a logarithmic component this is precisely Entry 771's indicial equation

\[
(R_f-mI)x_{-m}=0.
\]

Thus the extension cocycle can initiate a pole at its licensed order, but it
cannot license arbitrary growth above that order.  All excess pole growth is
a resonance of the homogeneous coefficient modules.

## Consequence for the finite audit

The 23-class stabilization calculation need not construct or compare the
transported affine cocycle at every order.  It has two stages:

1. compute the shifted Hom indicial operators from (A_T) and (A_E) alone;
2. use (C) only at the finite licensed orders to test compatibility of the
   surviving resonant leading coefficients.

If the homogeneous leading operator is injective at every order above
(e_{\rm Hom}), the affine splitting search is automatically bounded by
Entry 769's already exhausted pole vector.

The same separation holds at the order-two (u^2+1) component: the complete
formal leading recurrence above the cocycle order is homogeneous, although
it is Newton/Levelt rather than logarithmic.  This prevents the irregular
class from being treated by the wrong residue formula while retaining a
finite coefficient-only test.

## Status

This is a typing and reduction result, not the missing spectrum computation.
It removes the inhomogeneous principal cell from the unbounded part of the
audit without discarding it from the actual splitting equation.

## Evidence

- Entries 762, 769--771;
- `research/nima/gysin-hom-pole-lattice-audit.json`;
- allocator claim `seqclaim-c2028534bc4c08f6855f066f`;
- epistemic event
  `ev-000000000387-638faf0c-a89a-4361-8b63-7d3317b62c22`.

## Next falsifier

Compute only the homogeneous local leading matrices on the twelve labelled
occurrence orbits.  If a positive-integer kernel occurs above the licensed
order, restore the transported (C)-coefficient at the first compatible
order and test the affine recurrence there.  Otherwise rational
nonsplitting follows directly from Entry 769.
