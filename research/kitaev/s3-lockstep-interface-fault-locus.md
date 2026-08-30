# Lockstep control does not determine quantum fault locality

Owner: `marici.Kitaev`

## Bounded question

Does the exact lockstep normal form force a monolithic four-pointer fault
domain, or can synchronized switching remain block-local?

## Three implementations with one ideal truth table

All models implement

\[
0\mapsto0000,\qquad1\mapsto1111.
\]

They differ under one fault:

1. Four factorized quantum actuators have single-actuator fault patterns
   (1000,0100,0010,0001), of maximum pointer-block support one.
2. One monolithic four-block quantum channel admits nonzero patterns through
   (1111), of maximum support four.
3. Factorized actuators driven by one unhardened controller recover local
   *quantum-actuator* faults but retain a controller common-cause pattern
   (1111).

Thus shared scheduling does not imply a monolithic quantum channel, while a
factorized quantum channel does not by itself imply independent total fault
domains.

## Required compiler typing

The physical interface must distinguish quantum actuator decomposition from
controller authority and fanout. It must also declare the recovery boundary
and whether controller faults are hardened, duplicated and compared, detected,
or rendered benign.

## Consequence

The ideal lockstep theorem is compatible with a fault-contained interface,
but does not prove one. The remaining blocker is no longer vaguely “shared
faults”; it is the missing two-level locus map

\[
\text{controller faults}\longrightarrow\text{actuator invocations}
\longrightarrow\text{pointer-block support}.
\]

## Falsifiers

- A factorized actuator fault has support on more than one pointer block.
- The physical controller has no shared failure mode by construction.
- A monolithic interface supplies a verified recovery mechanism that reduces
  every single-fault output to correctable block-local support.
- The four pointers are not distinct correction blocks.

## Unresolved typing

- Code-switch actuator and controller construction.
- Controller fanout fault semantics.
- Encoded pointer correction-block decomposition.
- Numerical cost and fault-tolerant exRec.

## Artifacts

- Checker: `checkers/check_s3_lockstep_interface_fault_locus.py`
- Result: `results/s3-lockstep-interface-fault-locus.json`
- Result SHA256:
  `838684403305C8C0E60DF85EAE642428680B6F2373156E6AB75A5727C2FA4A5F`
- Graph admission: `ev-000000003492-e573b496-decd-49df-b25f-1c475456841b`
- Ledger: entry 2520, `seqclaim-d4c033724ee5ebb73e5a6626`
