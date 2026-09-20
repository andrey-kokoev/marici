# Higher-coherence topology iteration 15: spectral-shift topology types the boundary current, but its phase is oscillatory, not monotone

## Candidate topology

Replace norm convergence of full-line resolvents by relative scattering data.
For a suitable self-adjoint pair `(H_1,H_0)`, encode the boundary defect through
the spectral-shift function `xi` and Birman--Krein determinant

\[
\det\mathcal S(t)=e^{-2\pi i\xi(t)}.
\]

This topology is adapted to continuous spectrum: stable left/right charts and
their boundary phase remain meaningful even when the full-line pencil is not
Fredholm.

## Exact arithmetic phase

For one prime,

\[
J_p(t)
=
\frac{L_p(1/2-it)}{L_p(1/2+it)},
\qquad
\xi_p(t)
=-\frac1{2\pi i}\log J_p(t).
\]

The source calculation gives

\[
\xi_p(t)
=-\frac1\pi
\sum_{k\ge1}\frac{p^{-k/2}}{k}
\sin(kt\log p),
\]

and

\[
\xi_p'(t)
=-\frac{\log p}{\pi}
\sum_{k\ge1}p^{-k/2}\cos(kt\log p).
\]

Thus the Weil prime current is exactly the spectral-shift density.

## Sign test

The function `xi_p` is periodic, odd, and nonzero. It takes both signs. Its
derivative also changes sign. Finite prime sums remain almost-periodic and no
source-level monotonicity follows.

Therefore Krein's trace formula

\[
\operatorname{Tr}(f(H_1)-f(H_0))
=\int f'(t)\xi(t)\,dt
\]

reproduces the signed arithmetic current but does not make it positive.

## Endpoint and matrix structure

Endpoint crossings contribute integer jumps to scalar spectral shift. But the
source endpoint packet has positive and negative parity channels, so one scalar
jump cannot retain the full Green matrix. A matrix-valued or Pontryagin-space
scattering system is needed. That returns to the indefinite-topology issue:
positivity requires an independently selected physical cone.

## Missing scattering bridge

The arithmetic phase belongs to the dual/canonical pairing, while the positive
prolate/Halmos dilation belongs to a different operator pair. Their
identification would require

\[
\det_{\rm rel}\mathcal S_{\rm prolate,S}(t)
=
J_\infty(t)\prod_{p\in S}J_p(t).
\]

This relative determinant identity is not currently constructed. Even if it
were, determinant equality would give the same oscillatory signed phase, not a
positive boundary square.

## Relation to repeated cones

Successive scattering channels may absorb boundary residuals as phase shifts,
resonance jumps, and higher channel matrices. Their total phase composes
additively. But additive phase cancellation is weaker than equality of route
energies. A zero total phase can coexist with nontrivial channelwise positive
energy.

## Verdict for topology 15

Spectral-shift/scattering topology is well matched to the Xi seam and gives an
exact realization of the arithmetic boundary current. Its explicit phase is
oscillatory, so the hoped-for monotonicity unlock fails. Higher scattering
cones organize signed currents but do not force the relative-Haar energy cycle.

The next nonredundant topology to test is an ordered Banach lattice or
operator-system topology, where positivity is encoded by a cone rather than by
norm or trace and higher fillers must be completely positive.