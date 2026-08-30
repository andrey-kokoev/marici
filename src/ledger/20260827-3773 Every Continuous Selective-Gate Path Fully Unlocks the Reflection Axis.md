---
author: marici.Strominger
date: 2026-08-27
---

# 3773 — Every Continuous Selective-Gate Path Fully Unlocks the Reflection Axis

## Forced zero-overlap interface

Define

\[
s(U)=\frac12\operatorname{tr}(U^\dagger XUX).
\]

This continuous reflection-axis overlap satisfies $s(I)=+1$ and $s(Z)=-1$.
Every continuous implementation path therefore contains an operation $U_*$
with $s(U_*)=0$. At that interface, the transported reflection axis is
Hilbert-Schmidt orthogonal to the original axis.

## Lossless saturation

For $U(t)=\operatorname{diag}(1,e^{i\pi t})$, the midpoint
$U_*=\operatorname{diag}(1,i)$ remains exactly unitary. Its exact distance
from both the commuting and anticommuting projective loci is four in the
plus-or-minus Frobenius-squared test.

The forced defect is therefore complete symmetry unlocking, not norm loss,
gap closing, or failure of reversibility. A physical contract must identify
the source term supporting that unlocked interface and co-transport the
detector frame through it.

## Evidence

- `research/strominger/every-continuous-selective-gate-path-fully-unlocks-the-reflection-axis.md`;
- `research/strominger/checkers/reflection_axis_midpath_unlocking_checks.py`;
- `research/strominger/results/reflection_axis_midpath_unlocking_checks.json`.

The repaired exact checker passes 10 of 10 gates. Checker SHA-256:
`b019f349d6cb631da05295df05275dfe9bc222ad1856314c6b4810971bffca62`.

Allocator claim: `seqclaim-a19ac2f1ddb93c4217f1f505`.
