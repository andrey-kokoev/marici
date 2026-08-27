# The RH moving seam and spectral height have a Weyl curvature

Author: `marici.Nima`

Date: 2026-08-26

Status: exact source transport square

## Two native transports

The source carries two independent continuous operations.

Spectral height acts by modulation:

\[
(M_xf)(u)=e^{ixu}f(u).
\]

Moving the seam by \(q\) acts on the retained tail by translation:

\[
(T_qf)(u)=f(u+q).
\]

When the complete seam history is retained, translation extends to the exact
tail--seam isometry. The following algebra is already visible on its tail
component and survives as a typed phase on the complete cut correspondence.

## Exact Weyl relation

Direct substitution gives

\[
T_qM_x=e^{ixq}M_xT_q.
\]

Therefore the transport square has central holonomy

\[
T_qM_xT_q^{-1}M_x^{-1}=e^{ixq}I.
\]

Infinitesimally, multiplication by \(u\) and differentiation in \(u\) obey
the Heisenberg commutator. The relative connection on the two-parameter
spectral--seam plane is not flat; its curvature is the central identity
channel with the source-fixed normalization above.

For a prime seam displacement \(q=\log p\), the holonomy is

\[
e^{ix\log p}=p^{ix}.
\]

Thus the Euler phase is the holonomy of the source transport square between
spectral modulation and prime-scale resegmentation.

## Why this coherencer is genuine

The phase is not declared after comparing two routes. It follows from the
definitions of the two source actions. Deleting the seam displacement or the
spectral modulation makes the square commute; retaining both forces the
central residual.

This is the first nontrivial coherencer in the present categorical sweep that
is derived directly from source operations rather than from an abstract
associator law.

It also gives a concrete meaning to ordered composition. Applying spectral
phase before moving the arithmetic boundary is not the same operation as
moving the boundary first. Their difference is a measurable route effect.

## What it explains

The Weyl curvature explains:

- why no static pointed cone can be invariant under spectral transport;
- why prime labels and spectral height form conjugate coordinates;
- why order-sensitive operator transport contains information absent from
  scalar additive bookkeeping;
- why the moving seam is part of the physical state rather than a removable
  correction;
- why prime phases naturally enter as holonomies rather than independent
  positive ports.

It also gives the relative connection a source genesis. One component is
spectral modulation and the other is seam translation; their curvature is
fixed before theta scalar projection.

## What it does not explain

The Weyl holonomy is central and unitary. It controls phase but not the
smallest generalized singular value of the full \(GL(3)\) transport. By
itself it cannot exclude a cross-chiral orthogonality or a Maslov crossing.

The determinant-line connection sees this phase, while the traceless
\(\mathfrak{sl}_3\) connection carries shear, squeeze, and wall incidence.
The completed source law must couple both the central Weyl curvature and the
traceless frame curvature.

The first is now exact. The second requires the completed operator lift of
the dual wall incidence and the typed arithmetic currents.

## New finite audit

For every finite prime block, the operator compiler should compare the two
ordered composites

\[
T_{\log p}M_x,
\qquad
M_xT_{\log p}.
\]

on the complete tail--seam state. The residual must be exactly the central
phase \(p^{ix}\) and must act trivially on support typing. Any additional
bulk or boundary residual identifies missing incidence in the proposed lift.

For two primes, the corresponding squares must compose according to
\(\log(pq)=\log p+\log q\). This tests the coherencer before determinant
aggregation.

## Verification

The checker constructs an exact four-state clock-and-shift representation.
It verifies the Weyl commutation relation, the nontrivial central square
holonomy, multiplicativity of successive seam displacements, and failure of a
flat commuting model.
