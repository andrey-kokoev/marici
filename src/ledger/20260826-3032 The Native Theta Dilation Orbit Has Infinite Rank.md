---
title: "The Native Theta Dilation Orbit Has Infinite Rank"
date: 2026-08-26
sequence: 3032
author: marici.Grothendieck
status: finite-exact-theorem
---

# 3032 — The Native Theta Dilation Orbit Has Infinite Rank

For one theta label, set

\[
X=\pi n^2e^{2u}.
\]

After removing a nonzero label constant, its source atom is

\[
X^{1/4}e^{-X}(4X^2-6X).
\]

The native generator (\partial_u=2X\partial_X) acts on the residual polynomial by

\[
\mathcal DP
=2XP'(X)+(1/2-2X)P(X).
\]

Each application raises the polynomial degree by one and multiplies its leading coefficient by (-2). Therefore the (k)-th reduced derivative has degree (k+2) and leading coefficient

\[
4(-2)^k.
\]

The complete derivative orbit of every theta label is consequently linearly independent and infinite-dimensional. Primitive-label dominance at large positive scale transfers the constant-coefficient recurrence no-go to the completed theta source.

Thus the reciprocal-odd comparison tower cannot close as a finite-dimensional representation of native dilation. Any finite replacement must use genuinely nonlinear dynamics, transformed modular arguments, or independently derived variable coefficient fields.

Scope: this exact theorem rules out finite constant-coefficient differential closure. It does not rule out modular functional equations or nonlinear source identities.

## Durable verification

- Packet: `research/grothendieck/theta-native-dilation-orbit-has-infinite-rank.md`
- Exact checker: `research/grothendieck/checkers/theta_dilation_orbit_has_infinite_rank.py`
- Result: `research/grothendieck/results/theta_dilation_orbit_has_infinite_rank.json`
- Graph event: `ev-000000005938-033e25d9-d864-4d23-9c50-f89d69ab217e`
- No build was run because the operator's standing prohibition remains active.
