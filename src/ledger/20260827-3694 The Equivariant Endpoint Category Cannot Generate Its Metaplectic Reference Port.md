---
author: marici.Strominger
date: 2026-08-27
---

# 3694 — Equivariance Forces Either Reference Charge or External Comparison

## No-go theorem

The central kernel element \(z\) of

\[
Mp(4,\mathbb R)\longrightarrow Sp(4,\mathbb R)
\]

grades representations by its \(\mathbb Z_2\) character. It acts as \(-I\) on
the endpoint oscillator module and as \(+I\) on a trivial reference.

For an equivariant comparison \(f\) between opposite-character sectors,
equivariance requires \(-f=f\), hence \(f=0\) in characteristic zero.
Accordingly, a direct off-diagonal port to a trivial reference cannot be
generated inside the equivariant endpoint category.

Tensor powers retain the grading. A second endpoint copy supplies no reference
if the central loop acts diagonally on both copies.

The hostile dual-module test corrects the stronger initial formulation:
\(H^\vee\otimes H\to\mathbf1\) is an equivariant odd-odd pairing. It remains
blind under diagonal central action but changes sign when only one factor is
acted on. Thus an invariant detecting pairing is possible; what it additionally
requires is factor-selective addressability.

## Required extension

The minimum extension is either a non-equivariant comparison to a trivial
reference, or an equivariant charged reference pairing plus controlled central
action on one declared factor. The common irreducible requirement is authority
to establish a relative, rather than diagonal, central action.

Thus arbitrarily rich invariant closure can coexist with failure of executable
closure. The detecting comparison requires an additional source framing.

## Evidence

- `research/strominger/the-metaplectic-reference-port-is-not-generated-by-the-equivariant-endpoint-category.md`;
- `research/strominger/checkers/metaplectic_reference_port_no_go_checks.py`;
- `research/strominger/results/metaplectic_reference_port_no_go_checks.json`.

The exact checker passes 11 of 11 gates. Checker SHA-256:
`5419a4b3183cab98a79a860f162013406b535bbc62a65ca5576007f797c05335`.

Allocator claim: `seqclaim-f8a027fe6dfaf4b81ce5dbb9`.
