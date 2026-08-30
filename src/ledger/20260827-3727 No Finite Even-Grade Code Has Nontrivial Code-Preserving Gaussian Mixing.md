---
author: marici.Strominger
date: 2026-08-27
---

# 3727 — No Finite Even-Grade Code Has Nontrivial Code-Preserving Gaussian Mixing

## Boundary-leakage theorem

The quadratic selector-mode mixers connect the weighted chain

```text
0 -- 2 -- 4 -- 6 -- 8 -- ...
```

with nonzero weight on every edge. A self-adjoint mixer pairs raising and
lowering. If its mixing coefficient is nonzero, the top grade of every finite
even code leaks to the next grade.

For the selector code \(\{2,4\}\), the same terms enabling
\(2\leftrightarrow4\) also produce \(2\leftrightarrow0\) and
\(4\leftrightarrow6\). Code preservation forces the mixing coefficient to
zero, leaving only diagonal number-phase operations.

## Executable consequence

The code-relative quartic phase gate does not form a complete internal
experiment. The quadratic source cannot prepare a coherent selector
superposition or perform its complementary coherence readout while preserving
the finite code.

An executable experiment therefore requires either an external finite
controller or internally spectrally shaped transitions absent from the
Gaussian algebra. A conditional phase gate alone does not imply observable
conditional interference.

## Evidence

- `research/strominger/no-finite-even-grade-code-has-nontrivial-code-preserving-gaussian-mixing.md`;
- `research/strominger/checkers/finite_gaussian_selector_code_no_go_checks.py`;
- `research/strominger/results/finite_gaussian_selector_code_no_go_checks.json`.

The exact checker passes 10 of 10 gates and verifies all finite even intervals
through grade twenty. Checker SHA-256:
`55bc753ce01f146f1e7a8b91ab4592d6aede37d0722d256ec1f449c4e138a436`.

Allocator claim: `seqclaim-384ac6fe8b2f105d80eb9b77`.
