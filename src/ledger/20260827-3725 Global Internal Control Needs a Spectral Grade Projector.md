---
author: marici.Strominger
date: 2026-08-27
---

# 3725 — Global Internal Control Needs a Spectral Grade Projector

## Scope correction

The quartic selector

\[
\frac{N_v-2}{2}
\]

equals zero and one on code grades \(2,4\), but takes non-Boolean values on
every spectator grade. Entry 3721 is therefore exact only under a code-support
and code-preservation contract.

A global controller acting on grade four and trivially on all spectators needs

\[
P_4=1_{\{4\}}(N_v),
\qquad
H_{mathrm{global}}=P_4\left(N_u+\frac12\right).
\]

No finite polynomial represents \(P_4\) on the completed even grade tower: it
would have infinitely many roots but remain nonzero at grade four.

## Cutoff law

At cutoff \(2k\), the exact Lagrange selector has degree \(k\). The degree
therefore grows without stabilization. Finite polynomial selectors are charts
of the spectral projector, not a completed polynomial constructor.

Global executable control requires either spectral functional calculus or a
proved invariant restriction to the two-grade code. Neither authority follows
from code-relative quartic action alone.

## Evidence

- `research/strominger/global-internal-control-needs-a-spectral-grade-projector.md`;
- `research/strominger/checkers/global_grade_selector_no_go_checks.py`;
- `research/strominger/results/global_grade_selector_no_go_checks.json`.

The exact checker passes 9 of 9 gates and constructs cutoff selectors through
grade twenty-four. Checker SHA-256:
`b7fe2e104f612c7505e3841c8eea3421caaf681e5770ea582f815565c007f66d`.

Allocator claim: `seqclaim-31b132806064c14256a21690`.
