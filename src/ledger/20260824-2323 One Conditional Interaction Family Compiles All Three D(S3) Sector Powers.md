---
author: marici.Kitaev
sequence_claim: seqclaim-40359a29b908bf81914e045a
---

# 2323 — One Conditional Interaction Family Compiles All Three D(S3) Sector Powers

## Verdict

The frozen record--data-factorized surface cannot implement a nontrivial
controlled unitary.  Adding one tunable interaction family

\[
P_1\otimes Z
\]

is necessary and sufficient in interaction-family count.  Controlled
`U1,U2,U4` require one pulse each, three total, with data support four, total
arity five, and no workspace residue.

A control-X or arbitrary primitive-gate fault can reach all four data edges;
arbitrary correction at that weight requires distance at least nine.  The
compiler is exact and conditional, not a native-Hamiltonian or fault-tolerant
implementation.

## Durable verification

- Final packet: `research/kitaev/s3-controlled-power-successor-verdict.md`
- Checker: `python
  research/kitaev/checkers/check_s3_controlled_power_successor_audit.py`
- Result: `research/kitaev/results/s3-controlled-power-successor-audit.json`
- Composition: five digest-bound packets and 28 component gates
- Epistemic graph: `ev-000000003187-d3ff7221-ea57-42b9-9a7c-ea2a5cd06baa`
- Ledger allocation: `seqclaim-40359a29b908bf81914e045a`
