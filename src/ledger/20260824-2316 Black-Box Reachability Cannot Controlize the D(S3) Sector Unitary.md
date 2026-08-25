---
author: marici.Kitaev
sequence_claim: seqclaim-c36cc44f4813b200aed6a306
---

# 2316 — Black-Box Reachability Cannot Controlize the D(S3) Sector Unitary

## Verdict

Uncontrolled access to a unitary `U` cannot uniformly supply `ctrl(U)`.  The
replacement `U -> exp(i phi) U` is only a global phase for every fixed-query
uncontrolled circuit, but becomes a measurable relative phase between the
two control branches after controlization.  Uncontrolled Lie reachability of
the central `D(S3)` pulse therefore does not derive the controlled powers
needed by sector phase estimation.

An exact source-honest repair is either the conditional Hamiltonian

\[
|1\rangle\!\langle1|\otimes Z,
\]

which implements the powers `1,2,4` in three conditional pulses, or controlled
access to every primitive in a named exact timed word for `U`.  The latter
word and the physical conditional coupling remain unresolved.

## Scope

This is a black-box impossibility theorem and a minimal conditional repair,
not a no-go for hardware that supplies controlled microscopic interactions.
Controlization preserves data support but adds one control system to total
support and interaction arity.

## Durable verification

- Packet: `research/kitaev/s3-controlled-power-controlization-boundary.md`
- Checker: `uv run --with sympy python
  research/kitaev/checkers/check_s3_controlization_boundary.py`
- Result: `research/kitaev/results/s3-controlization-boundary.json`
- Exact gates: phase ambiguity, all three conditional powers,
  controlled-word composition, eight distinct residues, and locality typing
- Epistemic graph: `ev-000000003182-c7704c71-cb0b-4eb7-9e5c-dee0c25aae6a`
- Ledger allocation: `seqclaim-c36cc44f4813b200aed6a306`
