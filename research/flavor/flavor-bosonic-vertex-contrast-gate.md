# Bosonic vertex contrast gate: WP712

## Minimal candidate completion

Add one heavy real boson (chi) with source-declared field-dependent mass

\[
m_\chi^2=M^2+g_n|n|^2+g_m|m|^2.
\]

The positive bosonic one-loop supertrace channel contributes, up to its common
positive normalization (kappa),

\[
\kappa(g_n|n|^2+g_m|m|^2)^2.
\]

In the WP709 beta packet this gives

\[
N=\kappa g_n^2,
\qquad
M=\kappa g_m^2,
\qquad
X=2\kappa g_ng_m,
\qquad
C=0.
\]

The stability-opening combination is the exact positive Gram contrast

\[
N+M-X=\kappa(g_n-g_m)^2.
\]

It is strictly positive precisely when the bosonic source couples differently
to the two labelled triplets.

## Complete signed competition

Including the admitted WP711 disjoint Dirac chains gives

\[
N+M-X
=\kappa(g_n-g_m)^2-8(F_n+F_m).
\]

The regular WP708 ray moves into radial stability at first order exactly when

\[
\kappa(g_n-g_m)^2>8(F_n+F_m).
\]

Exchange-symmetric bosonic coupling, (g_n=g_m), is blind to the needed
contrast and cannot oppose any nonzero fermion erosion.

## Typing limits

This packet is a conditional existence constructor, not evidence that the
boson belongs to the flavor source. The action, representation, multiplicity,
self-coupling, thresholds, and loop normalization must be frozen independently
of the desired inequality. The raw one-loop polynomial must also be isolated
through the correctly derived counterterm channel; its sign cannot be fitted
from the target stability margin.

Even after the inequality holds, the operation selects no numerical coupling:
an open continuum of ((g_n,g_m,F_n,F_m,kappa)) gives the same contrast. It
opens an admissible stability region and distinguishes labelled mediator
routes, but source identification and physical readout remain nonfaithful.

## Disposition

WP712 supplies the first algebraically progressive signed vertex mechanism:
a positive source Gram can overcome the known fermion destabilizer. Selector
authority remains conditional on deriving this boson from a completed flavor
action and proving the displaced ray's full transverse basin, decoupling, and
finite-scale portal prediction.

The smallest exact falsifier is (g_n=g_m) with any
(F_n+F_m>0), for which the total correction is strictly negative.

Reproduce with: uv run --with sympy python research/flavor/checkers/wp712_bosonic_vertex_contrast_gate.py

Generated result: results/wp712_bosonic_vertex_contrast_gate.json.
