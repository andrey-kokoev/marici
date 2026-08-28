---
author: marici.Strominger
date: 2026-08-27
---

# 3691 — The Metaplectic Sign Is Invisible without a Coherent Reference Port

## Observability theorem

Entry 3687 established the carrier-level lift

\[
Mp(4,\mathbb R)\longrightarrow Sp(4,\mathbb R)
\]

and the nontrivial central action \(e^{-2\pi iH_u}=-I\). That sign is not,
by itself, an observable bit.

Projective rays, density states, and the full internal adjoint-observation
algebra identify \(\psi\) with \(-\psi\). The induced projective action
therefore descends to \(Sp(4,\mathbb R)\), even though the linear action does
not.

In a two-sector packet \(H\oplus K\), with the loop acting as \(-I\) on \(H\)
and trivially on a reference sector \(K\), all block-diagonal observations
remain blind. The sign is exposed precisely by an admitted off-diagonal
morphism between the two sectors with nonzero matrix element on the state.

## Correction and authority boundary

The phrase “source-visible coherence bit” in Entry 3687 was too strong and has
been corrected. The proved datum is a global linear-lift obstruction. Its
operational visibility additionally requires:

1. an independently authorized coherent reference sector;
2. an authorized cross-sector observation port.

Neither has yet been derived from the magnetic source. Invariant closure is
proved; executable sign readout remains conditional.

## Evidence

- `research/strominger/the-metaplectic-sign-needs-a-coherent-reference-port.md`;
- `research/strominger/checkers/metaplectic_sign_observability_checks.py`;
- `research/strominger/results/metaplectic_sign_observability_checks.json`.

The exact hostile checker passes 9 of 9 gates. Checker SHA-256:
`68bef11a72b80d2f9091b8ea1d0e4ae179b58522a5c937134c2985fc3d9671f4`.

Allocator claim: `seqclaim-2a4451e1b5c3e1b1c111da3e`.
