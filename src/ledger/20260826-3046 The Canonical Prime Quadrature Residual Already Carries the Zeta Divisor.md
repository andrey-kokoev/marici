---
title: "The Canonical Prime Quadrature Residual Already Carries the Zeta Divisor"
date: 2026-08-26
sequence: 3046
author: marici.Grothendieck
status: exact-circularity-boundary
---

# 3046 — The Canonical Prime Quadrature Residual Already Carries the Zeta Divisor

The source-derived prime-power sampling measure

\[
d\nu_{\mathrm{arith}}(L)
=\sum_{n\ge2}\frac{\Lambda(n)}n\delta_{\log n}(dL)
\]

has Laplace transform

\[
-\frac{\zeta'}{\zeta}(s+1).
\]

Subtracting the continuous scale measure gives the exact quadrature residual

\[
-\frac{\zeta'}{\zeta}(s+1)-\frac1s.
\]

The pole at the zeta pole is removed, but every nontrivial zero (ho)
produces a pole at (s=\rho-1). Thus the missing arithmetic quadrature error
already carries the zeta divisor. Controlling it by scalar continuation or a
claimed sign would import the problem being solved.

The moving-seam route remains viable only through a pre-aggregation source
coboundary, an independent operator law, or exact quadrature on a separately
derived restricted theta function class.

## Durable verification

- Packet: `research/grothendieck/the-canonical-prime-quadrature-residual-already-carries-the-zeta-divisor.md`
- Checker: `research/grothendieck/checkers/prime_quadrature_residual_carries_divisor.py`
- Result: `research/grothendieck/results/prime_quadrature_residual_carries_divisor.json`
- Graph event: `ev-000000006039-bbfc6508-bcce-4d1a-9f90-ed0a0a659935`
- No build was run because the operator's standing prohibition remains active.
