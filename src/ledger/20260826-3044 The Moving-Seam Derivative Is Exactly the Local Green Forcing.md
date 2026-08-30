---
title: "The Moving-Seam Derivative Is Exactly the Local Green Forcing"
date: 2026-08-26
sequence: 3044
author: marici.Grothendieck
status: exact-theorem
---

# 3044 — The Moving-Seam Derivative Is Exactly the Local Green Forcing

For the finite autocorrelation window

\[
W_L(d)=2\int_0^L\Phi(q)\Phi(q+d)\,dq,
\]

its odd separation transform obeys

\[
\partial_L\mathcal K_{W_L}(z)
=\Phi(L)(H_+(L,z)-H_-(L,z)).
\]

The right side is precisely the local doubled Green forcing density. The full
forcing is therefore the accumulated moving-seam boundary variation from zero
to infinity.

The remaining obstruction is arithmetic sampling: prime recursions expose
only (L=k\log p), not the continuous scale axis. A source-derived quadrature
or incidence theorem must reconstruct the full current from those samples and
the archimedean remainder. Without it, “telescoping over primes” is not yet a
defined operation.

## Durable verification

- Packet: `research/grothendieck/the-moving-seam-derivative-is-exactly-the-local-green-forcing.md`
- Checker: `research/grothendieck/checkers/moving_seam_derivative_is_forcing.py`
- Result: `research/grothendieck/results/moving_seam_derivative_is_forcing.json`
- Graph event: `ev-000000006038-159f6136-9cf6-4da0-b801-1a8561f1edaa`
- No build was run because the operator's standing prohibition remains active.
