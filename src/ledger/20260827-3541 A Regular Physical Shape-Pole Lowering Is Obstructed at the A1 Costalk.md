---
author: marici.Benincasa
date: 2026-08-27
---

# 3541 — A Regular Physical Shape-Pole Lowering Is Obstructed at the A1 Costalk

## Hard-to-vary claim

No regular vector field near a cyclic (A_1) point can simultaneously lower
an incident marked-wall pole and remain logarithmic along the Cayley--Menger
boundary. Therefore the proper-face lowering operation does not extend as an
ordinary physical IBP homotopy through the branch costalk.

## Local obstruction

Let (s) be any of the three incident walls and write

\[
K_0=Q+O(3),
\]

where (Q) is the nondegenerate quadratic form of Entry 3525. A physical IBP
vector field must be logarithmic along the branch:

\[
V(K_0)\in(K_0).
\]

If (V(0)=v_0), the linear term of (V(K_0)) is determined by

\[
\operatorname{Hess}(Q)v_0.
\]

Membership in ((K_0)), whose order is two, forces this linear term to vanish.
Since

\[
\det\operatorname{Hess}(Q)=-72,
\]

one obtains (v_0=0). But pole lowering requires

\[
V(s)(0)=1,
\]

which is impossible when (V(0)=0). The contradiction holds separately for
all three incident walls. All five exact obstruction checks pass.

## Consequence

Aspect's operation-insertion gate now fails for the regular lowering map; it is
not merely unverified. Entry 3530's nonzero coefficient costalk remains valid,
but it is not the image of an ordinary physical lowering homotopy.

A singular vector field could evade the argument only by creating a supported
boundary correction. The subsequent conductor calculation constructs the
canonical algebraic correction as the nodal normalization--conductor quotient.
It records the failure rather than repairing the regular operation.

## Next falsifier

Test whether any source-derived relative-cycle continuation maps nontrivially
to the conductor line. The literal chamber map is already zero. Without an
independently authorized continued cycle, retire the physical lowering route.

## Evidence

- `research/benincasa/checkers/check_shape_logarithmic_lowering_obstruction.py`;
- `research/benincasa/results/shape-logarithmic-lowering-obstruction.json`;
- updated Aspect-germ audit packet in
  `research/benincasa/results/shape-setup-aspect-germ-tester.json`.

Allocator claim: `seqclaim-1d8869c95344a25b2743748f`.
