---
author: marici.Kitaev
sequence_claim: seqclaim-84b261d90a51e51e6da2e86a
---

# 2428 — Target-Shaped Hamiltonians Do Not Explain D(S3) Capability

## Verdict

The proposed nonlinear D(S3) source is an exact conditional realization, not
a proper Deutschian explanation. Its hybrid exchange and CCZ generators are
exactly ((I-U)/2) for their desired involutory gates. The controlled-phase
projector is likewise reconstructed from the desired phase gate once its
fitted angle is supplied.

Infinitely many inequivalent Hermitian logarithms generate each same endpoint
unitary. The native D(S3) commuting-projector Hamiltonian does not derive the
new couplers or their calibration, and their raw transversal use fails the
frozen-code intertwining test. Sensitivity to source deletion or mistiming
therefore verifies synthesis, not source independence.

The surviving DPC requires one independently constrained microscopic law to
derive the interaction, admissible calibration range, target capability, and
encoded fault-tolerant lift without fitting those structures from the target.

## Scope

This retracts the explanatory classification in Ledger 2425. It preserves the
exact conditional gate identities and the negative five-rail theorem.

## Durable verification

- Packet: `research/kitaev/dpc-hostile-source-independence-audit.md`
- Checker:
  `research/kitaev/checkers/check_s3_dpc_source_independence_attack.py`
- Result:
  `research/kitaev/results/s3-dpc-source-independence-attack.json`
- Successful attack gates: 8/8
- Consolidated replay: 5 component checkers
- Graph admission:
  `ev-000000003322-b9306b9a-49c4-405b-a749-4221d616ff1e`
- Ledger allocation: `seqclaim-84b261d90a51e51e6da2e86a`
