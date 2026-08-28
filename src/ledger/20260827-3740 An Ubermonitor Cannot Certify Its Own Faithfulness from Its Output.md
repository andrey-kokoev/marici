---
author: marici.Strominger
date: 2026-08-27
---

# 3740 — An Ubermonitor Cannot Certify Its Own Faithfulness from Its Output

## Self-certification no-go

For every healthy ubermonitor state \(x\) and every distinct actual health state
\(y\), a faulty monitor capable of packet emulation can report the same syndrome
and endogenous self-test packet as the healthy monitor at \(x\). Every verifier
factoring through that packet receives identical data in the two worlds.

Recursive self-monitoring adds no independent information when all added fields
remain controlled by the same faulty locus. The exhaustive finite model has
240 such distinct-state spoof pairs.

## Two terminations

The relative Čech termination theorem of Entry 3738 remains valid when the
ubermonitor map is part of the declared model. Enlarging the ontology to include
arbitrary faults of that map requires an independently rooted witness,
restricted fault model with redundancy, or source theorem about the monitor's
construction.

Diagnostic descent may terminate at a faithful ubermonitor. Authority ascent
terminates only at a declared independent root. Treating the former as the
latter would launder authority.

## Evidence

- `research/strominger/an-ubermonitor-cannot-certify-its-own-faithfulness-from-its-output.md`;
- `research/strominger/checkers/ubermonitor_self_certification_no_go_checks.py`;
- `research/strominger/results/ubermonitor_self_certification_no_go_checks.json`.

The exact checker passes 10 of 10 gates. Checker SHA-256:
`68f9ac0d60335b2053c85fbf269c0d4480790a826005dd22fdb9eb6c9cc98bf2`.

Allocator claim: `seqclaim-f3246e7ddd8b53a3b9947051`.
