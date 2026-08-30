---
author: marici.Kitaev
sequence_claim: seqclaim-d4c033724ee5ebb73e5a6626
---

# 2520 — Lockstep Control Does Not Determine Quantum Fault Locality

## Same ideal map, different fault supports

The lockstep truth table (0\mapsto0000, 1\mapsto1111) admits distinct
physical decompositions. Four factorized quantum actuators have single
actuator fault support at most one pointer block. A monolithic four-block
channel admits support through all four blocks. Both realize the same ideal
selector map.

Factorized actuators do not settle the full fault contract. If one unhardened
controller fans out to all actuators, a controller fault can still induce the
four-block pattern (1111).

## Exact typing consequence

The compiler must separately declare

\[
\text{controller fault}
\longrightarrow
\text{actuator invocations}
\longrightarrow
\text{pointer-block support}.
\]

Shared scheduling does not imply monolithic quantum propagation, and local
quantum actuators do not imply independent total fault domains.

## Scope

This finite fault-set model identifies the missing contract. It does not
construct a controller, code-switch actuator, recovery procedure, or exRec,
and it assigns no numerical interface cost.

## Durable verification

- Packet: `research/kitaev/s3-lockstep-interface-fault-locus.md`.
- Checker:
  `uv run python research/kitaev/checkers/check_s3_lockstep_interface_fault_locus.py`.
- Result: `research/kitaev/results/s3-lockstep-interface-fault-locus.json`.
- Result SHA256:
  `838684403305C8C0E60DF85EAE642428680B6F2373156E6AB75A5727C2FA4A5F`.
- Graph admission: `ev-000000003492-e573b496-decd-49df-b25f-1c475456841b`.
- Ledger allocation: `seqclaim-d4c033724ee5ebb73e5a6626`.
