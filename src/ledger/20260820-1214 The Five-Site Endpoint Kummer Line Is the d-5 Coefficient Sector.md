---
title: "The Five-Site Endpoint Kummer Line Is the d=5 Coefficient Sector"
date: 2026-08-20
entry: 1214
status: active-correction
sector: cosmology
---

# 1214 — The Five-Site Endpoint Kummer Line Is the \(d=5\) Coefficient Sector

Sequence claim: `seqclaim-2ac72d0355cf4e4ea1102090`.

## Primary-source measure gate

For a one-loop graph with \(n_e^{(1)}\) loop-edge weights, the source
Cayley--Menger measure in equation (3.10) of Benincasa--Vazao has exponent

\[
\frac{d-n_e^{(1)}-1}{2}.
\]

For the five-cycle,

\[
n_e^{(1)}=5,
\qquad
\boxed{\alpha_d=\frac{d-6}{2}}.
\]

The paper also states that when \(d<n_e^{(1)}\), not all loop-edge weights
are independent and the integral is only \(d\)-fold.

Primary source:
[Benincasa--Vazao, *The Asymptotic Structure of Cosmological Integrals*,
arXiv:2402.06558v3, equations (3.6)--(3.10)](https://arxiv.org/pdf/2402.06558).

## Correction to Entries 1211--1212

The local form used there was

\[
\frac{dz}{\sqrt{P(z)}}.
\]

This corresponds to

\[
\alpha_d=-\frac12
\quad\Longleftrightarrow\quad
\boxed{d=5}.
\]

Therefore Entries 1211--1212 correctly construct the square-root/Kummer
coefficient sector of the analytically continued \(d=5\) family, but they do
not yet construct the physical \(d=3\) five-site source current.

For \(d=3\),

\[
\boxed{\alpha_3=-\frac32},
\]

and only three of the five loop-edge variables are independent. The physical
cycle lies on the source rank-constrained locus and cannot be obtained by
simply pairing the unrestricted five-variable branch with the \(d=5\)
Kummer line.

## What survives unchanged

Entries 1207--1210 are algebraic statements about the generic radial branch,
its discriminant, endpoint Cartier structure, and normalization conductor.
They remain valid as coefficient geometry before choosing spatial dimension.

The corrected architecture is

\[
\boxed{
\begin{array}{c}
\text{generic five-edge CM coefficient family}\
\downarrow\ d=5
\text{square-root endpoint Kummer line}\
\downarrow\ d=3\ \text{is not ordinary pullback}\
\text{rank-constrained physical source current still unconstructed}.
\end{array}}
\]

## Narrow conclusion

No new carrier datum is indicated. The defect was a coefficient/physical
dimension mismatch:

\[
\text{generic coefficient continuation}
\not\Rightarrow
\text{physical-dimensional current}.
\]

This is another instance of the cross-sector warning that a valid coefficient
object need not be the physically selected object.

## Next falsifier

Derive the \(d=3\) five-site loop measure from the source Gram-rank
constraints, using three independent loop variables and retaining all five
labelled edge occurrences. Then compute its radial endpoint specialization.
Only that constrained current may be paired with the endpoint conductor or
used to decide whether a physical Kummer class survives.

## Artifact

- `research/benincasa/marici-gm/src/bin/five_site_cm_measure_dimension_gate.rs`
- `research/benincasa/results/five-site-cm-measure-dimension-gate.json`
