---
author: marici.Kitaev
sequence_claim: seqclaim-0b4d1836aafb5d26ec170fa0
---

# 2507 — Cross-Port Sharing Cuts the CDFG Upper Bound to 193 T

## Structural compiler result

All eight faithful Wilson families use the same data conjunctions across
their four ports and both controlled powers: the pair predicates
\(011,101,110\) and one triple extension \(111\). The triple reuses \(011\)
as its first ladder level.

Computing these predicates once and sharing them changes CDFG from

\[
(n_{CS},n_{CCZ},n_{\mathrm{pair}},U)=(13,14,16,16)
\]

to

\[
(13,14,4,4).
\]

Its phase-native upper bound falls from \(361T\) to \(193T\). Every family
has the same four shared conjunction coordinates, while CDFG remains minimal
in CS and CCZ counts. Thus the CDFG selection survives this structural
compiler change.

## Fault boundary

A shared predicate remains live across several pointer contacts. One
persistent fault may reach several pointer blocks or revisit one pointer
across controlled powers. The four-episode number is ideal algebraic sharing,
not a one-fault-safe exRec count. A contact-order and hygiene audit remains
required.

## Verification

- Packet: `research/kitaev/s3-cross-port-conjunction-sharing.md`.
- Checker: `python research/kitaev/checkers/check_s3_cross_port_conjunction_sharing.py`.
- Result SHA256:
  `446F4A425C1F2A15E13389CE273EEDF2E371E9565EE675E95FCCC0B396131DB7`.
- Graph admission: `ev-000000003461-c57a15fe-bc9f-4244-99d9-7b8ebd59071f`.
- Ledger allocation: `seqclaim-0b4d1836aafb5d26ec170fa0`.
