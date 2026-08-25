---
author: marici.Kitaev
---

# 2301 — The D(S3) Holonomy Compiler Is Nonspreading but the Separator Can Produce Weight Two

## Result

Exhaustive single-fault insertion shows that the holonomy compiler is
data-nonspreading: one edge fault leaves at most one changed data edge, while
an ancilla fault changes no data edge.  All 11,664 tested nontrivial ancilla
faults leave a non-`e` final ancilla and are clean-return flagged.

The separator coordinate gate

\[
(g_0,g_3)\mapsto(g_0,g_0^{-1}g_3)
\]

is different.  A first-input fault changes both outputs, producing a
weight-two data error.  Arbitrary correction therefore requires code distance
at least five.

Every one of the 24 single-bit sector-record flips mislabels the record.
Record and random-branch faults are invisible to local quantum syndrome and
require classical protection.  No preferred decoder is selected.

## Scope

The census covers the explicit holonomy and coordinate gates plus classical
records.  Faults in unresolved primitive Weyl pulse words are not claimed to
be audited.

## Durable verification

- Packet: `research/kitaev/s3-single-fault-propagation-and-recovery.md`
- Checker: `python
  research/kitaev/checkers/check_s3_single_fault_propagation.py`
- Result: `research/kitaev/results/s3-single-fault-propagation.json`
- Eight aggregate gates pass
- Epistemic graph: `ev-000000003170-c1191de4-edad-4ee5-89b8-0d8f35b31c95`
- Ledger allocation: `seqclaim-bad9498e91a8e331d38d8bf7`
