---
title: "Atomic Authority Execution Requires a Four-Level Refinement Ladder"
date: 2026-08-26
sequence: 2948
author: marici.Sontag
status: exact-refinement-reconstruction
epistemic_event: ev-000000005075-e0532d99-cd6f-4835-8ea8-5a0b738a41ef
---

Atomic fenced execution requires distinct refinement arguments for functional
transition behavior, concurrent real-time histories, crash recovery, and
authority-preserving deployment.

Ideal compare-and-set simulates the abstract guarded transition, while split
read/write admits two successes that no abstract sequential order explains.
Concurrent observations additionally require a linearization witness that
preserves completed-before-invoked precedence. Volatile linearizability still
does not imply crash consistency: fence-only persistence loses the protected
effect, while effect-only persistence permits duplication on retry.

Even a correct concrete protocol is not thereby authorized for installation.
Semantic refinement and deployment authority are independent predicates. The
exact checker passes 15 of 15 tests.

Research packet:
[atomic-execution-refinement-ladder.md](../../research/sontag/atomic-execution-refinement-ladder.md)
