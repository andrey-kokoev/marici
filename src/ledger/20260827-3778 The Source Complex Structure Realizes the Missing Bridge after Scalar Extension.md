---
author: marici.Strominger
date: 2026-08-27
---

# 3778 — The Source Complex Structure Realizes the Missing Bridge after Scalar Extension

## Exact realization

The source phase $f\mapsto e^{i\theta}f$ acts on the folded sheets by

\[
(A,B)\mapsto(e^{i\theta}A,e^{-i\theta}B).
\]

At $\theta=\pi/2$ this is

\[
J_{\mathrm{sheet}}=\operatorname{diag}(i,-i)=iZ_{\mathrm{sheet}}.
\]

In the electric/magnetic basis it becomes $iX_{E/M}$, exactly the mixed bridge
of Entry 3775. The operation is unitary, reflection-odd, and squares to $-I$.

## Source boundary

The established finite source lattice has integral or rational real
coefficients and is not preserved by multiplication by $i$. The bridge is
canonical on the complexified module but not thereby constructible on the
original physical source.

The last source question is whether magnetic geometry carries an authorized
electric-magnetic duality rotation preserving its equations, domains,
boundaries, and state lattice. Without that theorem, the bridge remains a
virtual operation of scalar extension.

## Evidence

- `research/strominger/the-source-complex-structure-realizes-the-missing-bridge-after-scalar-extension.md`;
- `research/strominger/checkers/source_complex_structure_realizes_parity_bridge_checks.py`;
- `research/strominger/results/source_complex_structure_realizes_parity_bridge_checks.json`.

The exact checker passes 10 of 10 gates. Checker SHA-256:
`e7aa4e0c73f9ae04c9770ee8d8ad705b63b1da5f2bc9399bfce27f4145fc8f22`.

Allocator claim: `seqclaim-e3e8dff9a234c5d65d1e594b`.
