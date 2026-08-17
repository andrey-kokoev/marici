---
id: 430
date: 2026-08-17
title: Separated Normalization Sheets Cannot Be the Left Leg of the Span
---

# Separated Normalization Sheets Cannot Be the Left Leg of the Span

Entry 429 completed the generic logarithmic trace comparison. Attempting to
assemble the three local models into an ordinary global span exposes a
topological obstruction on a single marked exceptional fiber.

The source fiber is the connected V-poset
\[
h<r_D,\qquad h<r_1.
\]
The normalized source has two separated sheet points \(e_-\) and \(e_+\), an
antichain. Any order-preserving map from the V-poset to this antichain must be
constant: comparability of \(h\) with each ray forces all three images to be
equal. But Entry 400's uniquely forced endpoint comparison requires
\[
r_D\longmapsto e_-,
\qquad
r_1\longmapsto e_+.
\]
Therefore no continuous finite-space map, and hence no ordinary projection
\(p\) in a span with separated normalization as target, realizes the already
proved endpoint matrix.

The minimal repair is canonical. Adjoin the conductor point \(c\) with
\[
c<e_-,\qquad c<e_+.
\]
There is then exactly one order-preserving extension of the endpoint data:
\[
h\mapsto c,qquad r_D\mapsto e_-,qquad r_1\mapsto e_+.
\]
Reflection fixes \(c\) and exchanges both pairs of rays and sheets, so this
map is equivariant. No extra choice or scalar is introduced.

Thus the sought global geometry is not an ordinary correspondence
\[
\mathcal S^{\rm norm}_{\rm sh}\leftarrow Z\to\mathfrak P_{\rm PC}.
\]
It must retain the normalization–conductor cospan, or equivalently use the
mixed-variance kernel anticipated in Entries 144 and 146. Passing prematurely
to the separated normalization deletes the central image needed to connect
the two forced endpoint branches.

This is not a setback in the finite connector: its V-fiber already contains
the missing conductor point. It precisely identifies the global left target
that must now be constructed. The next gate is to assemble the three rotated
maps into the normalization–conductor finite/log cospan and verify its overlap
and projection properties. Only after applying the appropriate recollement
functor may one extract the separated-sheet source object.

The executable audit is
`research/voevodsky/check_global_normalization_projection_no_go.py`.
