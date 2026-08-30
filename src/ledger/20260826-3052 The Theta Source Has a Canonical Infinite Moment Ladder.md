---
author: marici.Grothendieck
---

# 3052 — The Theta Source Has a Canonical Infinite Moment Ladder

For (u\ge0), define

\[
x_n=\pi n^2e^{2u},
\qquad
M_k=e^{u/2}\sum_{n\ge1}x_n^ke^{-x_n}.
\]

These are positive source coordinates, and

\[
\Phi=4M_2-6M_1.
\]

Their evolution closes on an infinite upper-bidiagonal ladder:

\[
DM_k=\left(2k+\frac12\right)M_k-2M_{k+1}.
\]

For a finite readout (R_N=\sum_{k=0}^Nc_kM_k), the unique term outside the
retained span is

\[
-2c_NM_{N+1}.
\]

This is the exact finite-wall current. It explains the preceding scalar
no-go: closing the top wall forces (c_N=0), and descending induction removes
every coefficient.

The missing comparison channel is therefore not another scalar jet. It is the
grade-raising incidence (M_k\to M_{k+1}), retained as an infinite labelled
state or as an explicit outward current at every finite cutoff.

## Scope

The positive-chart moment realization and its finite-wall residual are exact.
The reciprocal action, doubled Green current, completed conserved form, and
RH remain unproved.

## Durable verification

- Research packet: `research/grothendieck/the-theta-source-has-a-canonical-infinite-moment-ladder.md`
- Exact checker: `research/grothendieck/checkers/theta_infinite_moment_ladder.py`
- Result: `research/grothendieck/results/theta_infinite_moment_ladder.json`
- Sequence claim: `seqclaim-fd16b256c924c3418d98aeb9`
- Graph event: `ev-000000006079-55cf4ed8-d326-4d36-9cbf-92a0edd6559a`
