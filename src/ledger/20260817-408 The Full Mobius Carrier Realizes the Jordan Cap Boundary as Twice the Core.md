---
id: 408
date: 2026-08-17
title: The Full Mobius Carrier Realizes the Jordan Cap Boundary as Twice the Core
---

# The Full Möbius Carrier Realizes the Jordan Cap Boundary as Twice the Core

Entry 407 identified the reduced connecting matrix \([2]\). We now verify
that this is not an artifact of retracting the carrier to one cell.

The occurrence-resolved carrier has twelve vertices, twenty-four edges,
eight triangular faces, and four square faces. Its integral cellular
matrices have ranks eleven and twelve, with \(H_1\cong\mathbb Z\).
The free-face collapse gives a unimodular twelve-by-twelve minor of
\(\partial_2\), and the remaining graph gives a primitive core \(\gamma\)
and dual cocycle \(\omega\).

For the labelled outer octagon \(b_O\), the checker constructs an explicit
integral two-chain \(H_O\) on the twelve actual faces such that
\[
\boxed{b_O-2\gamma=\partial H_O}
\]
up to outer orientation. This is stronger than merely pairing with
\(\omega\): it is a chain-level witness in the full incidence complex.

For every one of the sixteen \(D_8\) transports \(g\), the checker
independently verifies
\[
g b_O-\langle\omega,g b_O\rangle\gamma=\partial H_g,
\qquad
\left|\langle\omega,g b_O\rangle\right|=2.
\]
Thus the cap attachment has no denominator, residual square correction, or
dihedral anomaly. Reflections may reverse the sign but not the multiplicity.

Combining Entries 406--408 gives
\[
\langle\omega,\gamma\rangle=1,\quad
[\partial O]=2[\gamma],\quad
\langle\omega,\partial O\rangle=2,\quad
2\bmod2=0.
\]

This closes the additive cellular cap comparison. It does not convert the
residue/Gysin cospans into invertible atlas transitions. Any multiplicative
holonomy construction must first supply those typed equivalences.

The executable audit is
\`research/nima/check_global_halfline_atlas.rs\`.
