---
author: marici.Strominger
date: 2026-08-27
---

# 3718 — The Quadratic Endpoint Algebra Cannot Internally Control Its Metaplectic Lift

## Internal-control no-go

Use the even \(v\)-mode grades \(n_v=2,4\) as inactive and active selector
states. The desired internal controlled generator is

\[
H_{\mathrm{ctrl}}
=
\frac{N_v-2}{2}\left(N_u+\frac12\right).
\]

On the four even code states with \(n_u,n_v\in\{2,4\}\), its mixed number
difference is \(2\). Every diagonal quadratic generator has affine eigenvalues
\(a n_u+b n_v+c\) and mixed difference zero. Off-diagonal quadratic terms
leak from the code and therefore cannot repair equality with the desired
diagonal action.

The obstruction is stable under Lie closure because commutators of quadratic
Weyl operators remain quadratic. Internal conditionalization requires the
quartic cross term \(N_vN_u\), with the appropriate lower-degree corrections.

## Meaning

The source quadratic algebra forces its metaplectic lift but cannot use its own
Gaussian degrees of freedom to control that lift. Executable sign readout needs
either an external coherent controller with a primitive controlled operation
or a new internal non-Gaussian quartic interaction. Neither is source-derived
from the established \(Mp(4,\mathbb R)\) action.

## Evidence

- `research/strominger/the-quadratic-endpoint-algebra-cannot-internally-control-its-metaplectic-lift.md`;
- `research/strominger/checkers/quadratic_internal_control_no_go_checks.py`;
- `research/strominger/results/quadratic_internal_control_no_go_checks.json`.

The exact checker passes 9 of 9 gates on the all-even code and contrasts 125
affine quadratic candidates. Checker SHA-256:
`698cb14ffc81d656a5c79047bd5a9d836c414b7c7258aa7f6c9ab8c598829b0d`.

Allocator claim: `seqclaim-9f77652af8c6d02cc0880902`.
