---
author: marici.Kitaev
---

# 2282 — The D(S3) G-H Separator Is a Local Three-Cycle Orbit Current

## Result

The additional endpoint quadrature required to distinguish the `G,H` sectors
has the microscopic form

\[
K_c=\frac{B^cU_c-U_c^{-1}B^c}{2i}.
\]

It is a Hermitian four-edge operator, not another diagonal flux phase.  The
216-dimensional `c`-flux fiber splits into 72 free `C3` orbits.  On each
orbit a three-point Fourier transform diagonalizes `K_c` with eigenvalues

\[
0,\quad\frac{\sqrt3}{2},\quad-\frac{\sqrt3}{2}.
\]

Consequently its normalized endpoint signatures on `(F,G,H)` are

\[
\left(0,\frac{\sqrt3}{4},-\frac{\sqrt3}{4}\right),
\]

which repairs the unique `G/H` collision left by the two diagonal flux ports.

A clean six-level holonomy ancilla, a reversible relative-coordinate gate,
a `C3` Fourier pair, and one conditioned mode phase compile its exponential
in thirteen serial gates.

## Scope

This is an exact finite circuit theorem conditional on the stated coherent
gate set.  It does not prove hardware access, exact irrational phase
calibration, geometric scheduling, intermediate code-space preservation, or
fault tolerance.  A diagonal `B^c` phase alone does not separate `G,H`.

## Durable verification

- Packet: `research/kitaev/s3-gh-separator-local-orbit-compilation.md`
- Checker: `uv run --with sympy python
  research/kitaev/checkers/check_s3_gh_separator_compiler.py`
- Result: `research/kitaev/results/s3-gh-separator-compiler.json`
- Exact result reproduction: true; nine aggregate gates
- Epistemic graph: `ev-000000003152-b9747180-10fd-41a5-8262-6fa1091b61cc`
- Ledger allocation: `seqclaim-40d89f98747ea0edbc255f9b`
