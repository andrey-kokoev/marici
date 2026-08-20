---
title: "The Residual Gram-Kummer Grade Has a Nontrivial Elliptic Extension"
date: 2026-08-20
entry: 1196
status: active-generic-relative-extension
sector: cosmology
---

# 1196 — The Residual Gram-Kummer Grade Has a Nontrivial Elliptic Extension

Sequence claim: `seqclaim-8a6ba83c9d9c23dcf2fbeabb`.

## Relative-cohomology test

Entry 1195 identifies the rank-eight associated grade as two occurrence
copies of four Gram-Kummer lines. To test whether those lines split from the
elliptic pair systems, retain the three oriented faces of each source-labelled
residual triple.

For every one of the eight terms the exact profile is

\[
\boxed{2\text{ connected elliptic faces}+1\text{ split rational face}.}
\]

The split face supplies the (H^0_-) pair boundary already divided out in
Entry 1192. It contributes no new extension class.

## Two Abel--Jacobi components

On either connected elliptic face (C_{ij}), the off-branch triple lifts to
two distinct points (p_+,p_-). The relative-cohomology extension is the
oriented normal function

\[
\epsilon_{ij}\,operatorname{AJ}_{C_{ij}}
([p_+]-[p_-]),
\qquad
(\epsilon_{23},\epsilon_{13},\epsilon_{12})=(+,-,+).
\]

For a smooth genus-one curve the Abel map (C\to\operatorname{Pic}^1(C))
is injective. Therefore

\[
[p_+]-[p_-]=0\text{ in }\operatorname{Pic}^0(C)
\iff p_+=p_-.
\]

The retained triples are off branch, so both elliptic-face classes are
generically nonzero. Across the source packet this gives 16 labelled
nonzero extension components.

## Result

\[
\boxed{
\text{Gram-Kummer associated grade}
\not\simeq
\text{a canonically split summand of the marked-relative system}.}
\]

The full coefficient object is a nontrivial extension of the rank-one
Gram-Kummer quotient by existing elliptic (H^1) systems. This is precisely
the H2 architecture:

\[
\text{unchanged carrier and localization calculus}
+
\text{sector-specific nonsplit coefficient object}.
\]

## Scope

This is a generic fiberwise relative-cohomology nonsplitting statement. It
does not yet compute the complete Gauss--Manin off-diagonal matrices,
integral extension index, or physical-chain pairing.

## Next falsifier

For one representative of each (C_4) orbit, construct the two elliptic
curves with their labelled point pairs and calculate the normal-function
Gauss--Manin derivative. Quotient by regular triangular gauges and factor
its intrinsic singular support. The decisive question is whether all poles
lie on the already frozen branch/Gram/soft arrangement.

## Artifacts

- `research/benincasa/checkers/four_site_qg_residual_abel_jacobi_extension.py`
- `research/benincasa/results/four-site-qg-residual-abel-jacobi-extension.json`
