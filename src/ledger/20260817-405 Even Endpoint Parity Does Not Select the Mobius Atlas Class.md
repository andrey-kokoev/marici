---
id: 405
date: 2026-08-17
title: Even Endpoint Parity Does Not Select the Mobius Atlas Class
---

# Even Endpoint Parity Does Not Select the Möbius Atlas Class

Entry 404 closes the four square-curvature comparison. The remaining
additive carrier is the Möbius band made from the eight triangle faces and
four square faces, before attaching the residual octagon.

The exact global-halfline atlas certificate gives
\[
H_1(M;\mathbb Z)\cong\mathbb Z\langle\gamma\rangle,
\qquad [\partial O]=2\gamma.
\]
After the octagonal cap is attached, the ordinary homology becomes
\(\mathbb Z/2\), as for the projective plane. This makes it tempting to
identify Entry 400's even endpoint value
\[
p_{\partial,Q}=0\in\mathbb Z/2
\]
with the vanishing atlas class. That inference is not valid.

## The nonselection witness

Let \(\omega\) be the primitive integral cocycle dual to the Möbius core:
\[
\langle\omega,\gamma\rangle=1.
\]
The atlas certificate constructs two formal edge comparisons,
\[
\Theta_0=0,\qquad \Theta_1=\omega,
\]
with all of the following identical properties:

1. both obey every one of the twelve triangle/square face equations;
2. both have the same formal endpoint data;
3. both have even outer-octagon period.

Their integral outer periods are nevertheless different:
\[
\langle\Theta_0,\partial O\rangle=0,
\qquad
\langle\Theta_1,\partial O\rangle=\pm2.
\]
Modulo two, both give zero. But on the primitive crosscap core they are
distinguished:
\[
\langle\Theta_0,\gamma\rangle=0,
\qquad
\langle\Theta_1,\gamma\rangle=1.
\]

Therefore endpoint parity and all local square equations factor through a
quotient that forgets the integral Möbius weight. The result
\(p_{\partial,Q}=0\) is compatible with both atlas classes and cannot select
between them.

## Exact remaining datum

The missing comparison is a typed morphism
\[
\Psi_{\rm crosscap}:
\operatorname{Fib}_{\partial,Q}
\longrightarrow
L_{\rm or}=H_1(M;\mathbb Z)/\langle\partial\text{ local faces}\rangle
\cong\mathbb Z,
\]
or its dual coefficient map, carrying the geometrically selected endpoint
connector to the primitive Möbius quotient. It must retain the road quotient,
ordered-normal orientation, polarity line, and the crosscap generator.

Only after \(\Psi_{\rm crosscap}\) is constructed can Entry 400's endpoint
class be paired with \(\gamma\). A zero pairing closes the additive atlas; an
odd pairing identifies the surviving Jordan/Möbius obstruction. Outer
octagon parity alone cannot decide it.

This does not reopen the square sector or the polarity homotopy. Those are
already closed by Entries 87 and 404. It isolates a distinct global atlas
comparison.

The executable witness is
\`research/nima/check_global_halfline_atlas.rs\`, especially its construction
of \(0\), \(\omega\), their face equations, and their outer periods \(0\) and
\(2\).
