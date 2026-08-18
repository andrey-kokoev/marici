---
id: 454
date: 2026-08-17
title: The Exceptional Cartier Layer Has a Canonical Rank-Two Pushforward
---

# The Exceptional Cartier Layer Has a Canonical Rank-Two Pushforward

Entry 453 globalized the common factor (H).  On the complementary chart the
exceptional divisor and its doubled section have coordinate ring

\[
\mathcal O_{2D}
=\mathbb Q[b,a,\psi]/(a^2,\psi^2),
\qquad
\psi=t+\frac12(1-b^2).
\]

Because (psi) is monic in (t), it remains a nonzerodivisor before imposing
(psi^2), even though the exceptional divisor itself retains (a^2=0).
Consequently there is a canonical Cartier exact sequence

\[
0\longrightarrow (\psi)/(\psi^2)
\longrightarrow\mathcal O_{2D}
\longrightarrow\mathcal O_D
\longrightarrow0,
\]

with

\[
(\psi)/(\psi^2)\simeq\mathcal O_D,
\qquad
\mathcal O_D\simeq\mathbb Q[b,a]/(a^2).
\]

Entry 452 showed that the exceptional exact image lands in the first term.
Thus its canonical residual target is the last term, not a quotient selected
from a truncated matrix.

Let (D\to\mathbb A^1_b) be the projection.  Since the whole section (D) is
contained in this chart, its direct image is explicitly

\[
\pi_*\mathcal O_D
\simeq\mathbb Q[b]\langle1,a\rangle,
\qquad a^2=0.
\]

It is free of rank two over the (b)-axis, including at (b=\pm1), where the
fiber is (mathbb Q[a]/(a^2)).  This supplies a geometric rank-two coefficient
object whose length agrees with the Euler-resonance plane of Benincasa Entry
449.  It does **not** yet identify the two objects: the filtered degrees of
(1,a) have not been matched to the exact-cokernel representatives
([a^4]) and ([a^{11}(b+1)]).

Nor is (mathcal O_D) automatically the nearby-cycle object.  It is the
canonical zeroth Cartier layer of the doubled exceptional support.  A
nearby-cycle claim requires the specialization morphism and monodromy (or an
equivalent local-cohomology comparison).

The next gate is to compute the inherited grading of (1,a), including the
sector shifts from Entry 452, and test whether it matches the two Euler
resonance degrees.

The executable audit is
research/voevodsky/check_soft_axis_exceptional_cartier_layer.py.
