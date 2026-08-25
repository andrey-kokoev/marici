# Four Wilson interfaces require a joint selector and fault contract

Owner: `marici.Kitaev`

## Bounded question

Does a realizable or costed interface for each of the CDFG pointers imply a
realizable and costed four-pointer interface?

## Exact joint-image gate

Give each port (C,D,F,G) a binary native/binary interface state. Independent
switching has (2^4=16) joint configurations and therefore needs at least
four selector bits. A single shared bit has complete marginals at every port
but reaches only

\[
0000,\qquad1111,
\]

leaving fourteen joint configurations unreachable. If independent port
choice is required, this is exactly
`joint_selector_correlation_deficit`.

## Lockstep alternative

The two-state diagonal is sufficient if a source-authorized coherence law
requires all four ports to switch in lockstep. That option does not restore
fault independence: one selector authority and fault root spans four pointer
blocks. It must carry a common-cause set, epoch/replay identity, and a
four-block one-fault output contract.

## Resource consequence

The earlier hybrid comparison leaves a total interface allowance below
(83T)-equivalent units. Per-interface marginal costs cannot simply be added
into that allowance until the joint constructor is fixed: independent and
lockstep constructors have different selector state spaces and fault
contracts. This packet derives no numerical switch cost.

## Assumptions

- CDFG uses four distinct coherent pointer blocks.
- Each interface has two abstract states, native and digit-exposed binary.
- A selector state is counted only when its joint image is operationally
  reachable.

## Falsifiers

- One shared bit reaches any non-diagonal four-port configuration.
- The task requires only lockstep operation and an admitted shared-fault
  contract already proves the four-block one-fault condition.
- A direct native factory eliminates digit-interface switching entirely.
- An independently verified joint interface supplies a different state space
  and resource census.

## Unresolved typing

- Whether Wilson extraction requires independent, staged, or lockstep port
  switching.
- Physical selector authority, epoch, replay, and fault domains.
- Numerical joint code-switch cost and exRec.

## Artifacts

- Checker: `checkers/check_s3_joint_interface_selector_fault_gate.py`
- Result: `results/s3-joint-interface-selector-fault-gate.json`
- Result SHA256:
  `B65015EEB8F4F34AE3D7F101B370485B3BDFFD583D46DA50A0E739460988B4BC`
- Graph admission: `ev-000000003487-81e23905-a72f-4b31-9ae9-4497f8321dbc`
- Ledger: entry 2518, `seqclaim-2490badb2465aaf42a6602f8`
