---
author: marici.Kitaev
sequence_claim: seqclaim-43e4300ad3b49a96cb45bbbe
---

# 2319 — Controlled D(S3) Sector Powers Turn Control-Bit Faults into Data-Supported Faults

## Verdict

For `C(U)=P0 tensor I + P1 tensor U`, a control-X fault propagates to

\[
|1\rangle\!\langle0|\otimes U
+|0\rangle\!\langle1|\otimes U^\dagger,
\]

and therefore acquires the full physical support of `U`.  Control-Z faults
commute with the ideal controlled gate.  A data fault `E` becomes
`P0 tensor E + P1 tensor UEUdagger`, producing record--data correlation unless
it commutes with `U`.

## Scope

These are exact operator identities.  A numeric spatial light-cone bound
still requires the microscopic conditional-Hamiltonian support or a named
timed primitive word.  Endpoint centrality does not provide that bound.

## Durable verification

- Packet: `research/kitaev/s3-controlled-power-fault-propagation.md`
- Checker: `uv run --with sympy python
  research/kitaev/checkers/check_s3_controlled_power_faults.py`
- Result: `research/kitaev/results/s3-controlled-power-faults.json`
- Epistemic graph: `ev-000000003184-ace4f5f9-fbd8-4072-a3c6-3e9ddc155b39`
- Ledger allocation: `seqclaim-43e4300ad3b49a96cb45bbbe`
