# Irreducible-triplet pole and residue packet: WP448

## Question

Which pole locations and current-space residues are fixed by the WP447 source representation before choosing widths, detector resolution, or a fit to flavor data?

## Exact mass multiplets

With canonical generators (T_a=\lambda_a/2), the WP447 gauge-mass law is

\[
M_F^2=g_F^2\mu^2K.
\]

The exact spectrum of (K) is

\[
1^{\times3},\qquad3^{\times5}.
\]

This is the decomposition of (su(3)) under the principal spin-one (su(2)): a triplet and a quintet. The two pole masses are therefore

\[
m_1=g_F\mu,\qquad m_3=\sqrt3g_F\mu.
\]

They are not filled from a desired detector response.

## Exact residue operators

The spectral projectors are polynomial functions of the source-derived mass shape:

\[
P_1=\frac{3I-K}{2},\qquad
P_3=\frac{K-I}{2}.
\]

They are orthogonal idempotents of ranks three and five and resolve the identity. The exact current-current propagator is

\[
g_F^2(q^2I-M_F^2)^{-1}
=\frac{g_F^2P_1}{q^2-g_F^2\mu^2}
+\frac{g_F^2P_3}{q^2-3g_F^2\mu^2}.
\]

Thus the labelled current-space pole residues are independently frozen as (g_F^2P_1) and (g_F^2P_3). At zero momentum the coupling cancels, leaving (K^{-1}/\mu^2).

## Width and instrument boundary

No width is assigned. A width requires an independently declared particle spectrum, messenger thresholds, physical mass-basis rotations, and all open decay channels. Adding an imaginary denominator by hand would violate the frozen-spectrum rule.

No detector instrument is attached. The residue projectors live in the source current basis; they must be transported through a viable messenger-to-`physical16` map before any flavor-tagged experimental acceptance can be computed.

## Smallest exact falsifier

A third pole, a projector rank other than three or five, or failure of the exact two-projector propagator decomposition falsifies the packet.
