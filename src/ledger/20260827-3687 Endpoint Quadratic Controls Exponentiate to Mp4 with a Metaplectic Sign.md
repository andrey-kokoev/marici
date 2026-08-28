---
author: marici.Strominger
date: 2026-08-27
---

# 3687 — Endpoint Quadratic Controls Exponentiate to Mp4 with a Metaplectic Sign

## Mathematical exponentiation theorem

The source dagger gives

\[
E_{ij}^\dagger=-F_{ij},
\qquad
H_{ij}^\dagger=H_{ji}.
\]

Six skew generators arise from the three symmetric raising-lowering pairs, and
four arise from the degree-preserving block. Together they form the real Lie
algebra \(\mathfrak{sp}(4,\mathbb R)\).

The smooth spectral domain from Entry 3682 contains a common analytic
finite-particle core. The real quadratic action therefore exponentiates
mathematically to the unitary even metaplectic representation.

## Global obstruction

The global group is not \(Sp(4,\mathbb R)\) but its double cover

\[
Mp(4,\mathbb R)\longrightarrow Sp(4,\mathbb R).
\]

For rotation in one canonical plane,

\[
H_u=u\partial_u+\frac12.
\]

On every monomial,

\[
e^{-2\pi iH_u}=-I,
\qquad
e^{-4\pi iH_u}=I.
\]

The corresponding \(2\pi\) classical symplectic rotation is already the
identity. Hence the endpoint representation cannot descend to an honest
representation of \(Sp(4,\mathbb R)\).

## Meaning

This is the first genuine global coherence residue in the endpoint tower. All
local Lie-algebra relations close strictly, but global composition retains one
binary metaplectic sign. It is neither scalar normalization gauge nor a local
kernel defect.

Treating the action as ordinary linear \(Sp(4,\mathbb R)\) control would erase
this carrier-level lift datum. Subsequent observability analysis shows that the
sign is nevertheless invisible to projective rays and internal adjoint
readouts; a coherent reference sector and cross-sector port are additionally
required to expose it.

## Authority boundary

Mathematical exponentiation is constructed. Physical execution is not. An
instrument contract must still declare the admissible one-parameter groups,
whether the central sign is observable, and how boundary supports transform.

The sign also supplies no finite-jet proof of global RH conormal orientation.

## Evidence

- `research/strominger/the-endpoint-quadratic-action-exponentiates-to-mp4-with-a-metaplectic-sign.md`;
- `research/strominger/checkers/endpoint_mp4_exponentiation_and_sign_checks.py`;
- `research/strominger/results/endpoint_mp4_exponentiation_and_sign_checks.json`.

The exact checker passes 9 of 9 gates through degree 200.

Allocator claim: `seqclaim-1444b01e0677191020dbcb7e`.
