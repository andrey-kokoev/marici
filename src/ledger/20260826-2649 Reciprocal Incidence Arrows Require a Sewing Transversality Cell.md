---
author: marici.Kitaev
---

# 2649 — Reciprocal Incidence Arrows Require a Sewing Transversality Cell

The direct sector arrow \(p:F_+\to Y_+\) and reciprocal sector arrow
\(q:Y_-\to F_-\) cannot compose until source-derived sewing maps

\[
U:Y_+\to Y_- ,\qquad V:F_+\to F_-
\]

are supplied. Their closed incidence is

\[
\kappa_{U,V}=pV^{-1}qU.
\]

Nonzero \(p,q\) do not imply \(\kappa\ne0\). Identity and swap sewing applied
to identical rank-one arrows give \(\kappa=1\) and \(0\), respectively.
Coherent basis changes preserve \(\kappa\), but changing the sewing map or sheet
phase changes it.

Uniformly bounded invertible sewing maps also do not ensure completion-stable
closure: an exact family has \(\kappa_N=1/N\to0\) while both sewing matrices
remain uniformly bounded.

## Scope

This is a finite sewing and completion compiler theorem. It does not derive
Fourier–Tate sewing, a theta sheet frame, signed arithmetic current, uniform
transversality, conservative realization, zero orientation, or RH.

## Durable verification

- Packet: `research/kitaev/reciprocal-incidence-arrows-require-a-sewing-transversality-cell.md`
- Checker: `research/kitaev/checkers/check_reciprocal_incidence_sewing.py`
- Results: `research/kitaev/results/reciprocal-incidence-sewing.json`
- Sequence authority: `seqclaim-716e3e26c38abf32b9aa063a`
- Epistemic graph event: `ev-000000004014-e446bbac-aab1-4a37-a35e-ef17c8a2acc7`

The research state is coherent but uncommitted. No commit or push was
authorized.
