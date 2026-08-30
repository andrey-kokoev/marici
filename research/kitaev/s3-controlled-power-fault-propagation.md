# Fault propagation through the controlled central powers

Owner: `marici.Kitaev`

Status: exact operator identities; spatial support requires a microscopic
timed-word realization.

## Bounded question

What single-fault guarantees follow from an abstract controlled central power
`C(U)=P0 tensor I + P1 tensor U`?

For a control bit flip before the gate,

\[
C(U)(X\otimes I)C(U)^\dagger
=|1\rangle\!\langle0|\otimes U
 +|0\rangle\!\langle1|\otimes U^\dagger.
\]

Thus one control fault acquires the entire support of `U`; it is not a local
control-only error unless `U` is trivial.  By contrast,

\[
[C(U),Z\otimes I]=0,
\]

so a control dephasing fault does not spread to data through the ideal gate.

For a data fault `E`,

\[
C(U)(I\otimes E)C(U)^\dagger
=P_0\otimes E+P_1\otimes UEU^\dagger.
\]

It remains uncorrelated with the record qubit exactly when `E` commutes with
`U` (up to a common scalar action).  A sector-changing local error generally
does not commute with a central sector-phase unitary and therefore becomes a
record--data correlated fault.

## Consequence for the source audit

Endpoint centrality does not imply microscopic nonspreading.  A bound on the
data support of the propagated control fault requires either:

- a declared physical support for the conditional Hamiltonian
  `P1 tensor Z`; or
- a named primitive word and a gate-by-gate fault schedule.

The frozen source has neither.  Therefore the exact ideal controlled-power
repair closes algebraic controlization but does not close the fault-tolerance
obligation.  If a compiled word uses gates each spreading a fault by at most
`r` along an interaction graph, ordinary light-cone accounting can bound the
spread; Lie rank or endpoint dimension alone cannot.

The six-bit final-record code in the companion packet corrects a later
classical bit flip but does not repair these coherent acquisition faults.

## Verification and falsifiers

Run:

```text
uv run --with sympy python research/kitaev/checkers/check_s3_controlled_power_faults.py
```

The checker verifies the three conjugation identities for symbolic unitary
entries subject to exact inverse substitution, and exhibits commuting and
noncommuting data-fault witnesses.  Saved output:
`research/kitaev/results/s3-controlled-power-faults.json`.

Falsifiers are failure of an identity, data spreading from a control-Z fault,
or a source-derived microscopic compiler with a stronger verified light-cone
bound.  The last would supersede the unresolved-support disposition rather
than contradict the operator identities.

