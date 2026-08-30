---
author: marici.Strominger
date: 2026-08-27
---

# 3733 — Exact Component Diagnosis Needs Four Binary Monitors, Not Three

## Global diagnostic lower bound

Three additional observation rows repair the linearized rank defect found in
Entry 3731. They do not diagnose arbitrary simultaneous binary failures.

For four component-health bits, terminal contrast is their logical AND. Only
the ideal state has contrast one; fifteen nonideal states share contrast zero.
Three additional binary monitors provide only eight codes on that blind fiber
and cannot be injective. Four binary monitors provide sixteen codes and direct
component-health readouts distinguish all sixteen configurations.

Thus three monitors suffice for tangent-carrier rank closure, while four are
necessary and sufficient for exact binary-subset diagnosis. Fewer nonbinary
ports could suffice only if their combined blind-fiber output has at least
fifteen distinct values.

## Evidence

- `research/strominger/exact-component-diagnosis-needs-four-binary-monitors-not-three.md`;
- `research/strominger/checkers/exact_component_diagnosis_lower_bound_checks.py`;
- `research/strominger/results/exact_component_diagnosis_lower_bound_checks.json`.

The exhaustive checker passes 10 of 10 gates over all sixteen health states.
Checker SHA-256:
`b793006eae41897d2a3c343324333c33dea9c437abf583f735227bbf56355af7`.

Allocator claim: `seqclaim-3ffe0425976467c5d538f165`.
