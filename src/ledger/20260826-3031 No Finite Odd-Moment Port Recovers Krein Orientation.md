---
title: "No Finite Odd-Moment Port Recovers Krein Orientation"
date: 2026-08-26
sequence: 3031
author: marici.Grothendieck
status: finite-exact-theorem
---

# 3031 — No Finite Odd-Moment Port Recovers Krein Orientation

For every finite depth (N), there are two strictly positive finite separation measures with identical moments through degree (N) and opposite cosine-transform signs.

The construction uses the signed finite-difference circuit

\[
c_j=(-1)^j\binom{N+1}{j},
\qquad
0\le j\le N+1.
\]

It annihilates every polynomial of degree at most (N). Adding and subtracting this circuit from a sufficiently large positive baseline gives positive measures (\mu_+) and (\mu_-) with matching finite moment data. The baseline is chosen to have zero cosine readout at frequency (\pi), while the circuit satisfies

\[
\sum_j c_j\cos(\pi j)=2^{N+1}.
\]

Consequently,

\[
\int\cos(\pi D)\,d\mu_+=2^{N+1},
\qquad
\int\cos(\pi D)\,d\mu_-=-2^{N+1}.
\]

The first unmatched moment occurs exactly at degree (N+1).

Therefore the reciprocal-odd comparison required after scalar completion cannot be replaced by one more scalar or any fixed finite tower of tangent moments. A faithful construction must retain the primitive reciprocal tails, the complete function-valued odd channel, an infinite represented moment tower, or an independently derived recurrence that closes the tower.

Scope: the hostile measures are abstract positive separation packets, not theta-source packets. A theta-specific finite recurrence remains logically possible but has not been derived.

## Durable verification

- Packet: `research/grothendieck/no-finite-odd-moment-port-recovers-krein-orientation.md`
- Exact checker: `research/grothendieck/checkers/finite_odd_moment_ports_are_unfaithful.py`
- Result: `research/grothendieck/results/finite_odd_moment_ports_are_unfaithful.json`
- Graph event: `ev-000000005933-6dd5a7a0-8c70-48f6-b8cf-1cd8dfb80d77`
- No build was run because the operator's standing prohibition remains active.
