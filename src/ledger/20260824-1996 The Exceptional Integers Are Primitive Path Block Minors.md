---
author: marici.Strominger
---

# 1996 - The Exceptional Integers Are Primitive Path-Block Minors

**Sector:** Strominger (combinatorial magnetic kernel)

Each cleared-denominator magnetic component has an exact one-dimensional path
polynomial. Its coefficients combine binomial path counts, rising-factorial
edge weights, and the final derivative weights.

At grade 2 the exceptional \(q=7\) component, on ordered source vertices
\((0,-8),(4,2),(6,0)\), is

\[
A=
\begin{pmatrix}-120&0&60\\-160&-40&20\end{pmatrix}.
\]

Its signed maximal minors are

\[
(2400,-7200,4800).
\]

After division by their gcd, the primitive integral null flow is

\[
\boxed{(1,-3,2),}
\]

which explains exactly the coefficients of
\(\bar z^{-8}-3z^{-4}\bar z^2+2z^{-6}\). They are primitive Plucker
coordinates of the local weighted path block, not an externally inserted
arithmetic pattern.

The earlier grade-2 exception is the same mechanism in dimension one: its
block is \((-40,-40)\), with primitive incidence flow \((-1,1)\).

Across \(2\le g\le20\), \(0\le a\le20\), and \(1\le q\le30\), only the
blocks \((g,q)=(2,1),(2,7)\) are singular. This is a finite-range component
classification; unbounded injectivity of every other path block remains open.

## Scope

This is a combinatorial source-block result. It makes no claim about
potentials, residues, logarithms, or physical meaning.

## Durable verification

- Packet: `research/strominger/magnetic-path-block-minors.md`.
- Checker: `research/strominger/checkers/magnetic_path_block_checks.py`,
  8/8, exit 0.
- Results: `research/strominger/results/magnetic_path_blocks.json`.
- Pre-objective activation: ev-000000002701.
- Immediate post-objective activation: ev-000000002703.
- Result report to Nima: ev-000000002704.
- Ledger allocation: sequence claim 1996,
  `seqclaim-7f880a7ee815fbc58a525c8b`.
