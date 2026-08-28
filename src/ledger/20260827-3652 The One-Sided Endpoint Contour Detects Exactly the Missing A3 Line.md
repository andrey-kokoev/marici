---
author: marici.Benincasa
date: 2026-08-27
---

# 3652 — The One-Sided Endpoint Contour Detects Exactly the Missing A3 Line

## Residue basis

At the infinity soft-signed corner, Entry 3648 gives the \(A_3\) Milnor basis

\[
1,qquad s,qquad s^2.
\]

On the source-selected central branch

\[
\bar W=ys^2,
\]

the associated residue forms are

\[
\alpha_j=\frac{s^jds}{\bar W}
=\frac1y s^{j-2}ds,
\qquad j=0,1,2.
\]

Their endpoint behaviors are

\[
\alpha_0=\frac{ds}{ys^2},
\qquad
\alpha_1=\frac{ds}{ys},
\qquad
\alpha_2=\frac{ds}{y}.
\]

Only \(\alpha_1\) has a logarithmic residue. The physical one-sided endpoint
contour therefore defines the row

\[
\operatorname{Res}_{s=0}^{\log}
=
\begin{pmatrix}
0&1/y&0
\end{pmatrix}
\]

on the ordered Milnor basis.

## Source normalization

The coordinate \(s=b/a=1/t\) is the frozen projective endpoint coordinate,
and its physical half-ray fixes the orientation. Under any nonzero tangential
rescaling \(s'=lambda s\),

\[
\frac{ds'}{s'}=\frac{ds}{s}.
\]

Thus the logarithmic coefficient is independent of tangential scale. No
regulator hierarchy or fitted normalization is required.

At the reciprocal finite endpoint, the same calculation gives

\[
\begin{pmatrix}
0&1/x&0
\end{pmatrix}.
\]

## Result

The reflection-odd Milnor line omitted by the algebraic deformation span in
Entry 3648 is detected exactly by the source physical relative readout.

This does not add a third deformation direction. It distinguishes two typed
operations:

- the source deformation map reaches the even plane
  \(\langle1,s^2\rangle\);
- the one-sided boundary residue reads the complementary line
  \(\langle s\rangle\).

Together they account for the full rank-three \(A_3\) coefficient germ using
existing soft, signed-energy, and marked-boundary operations. No new carrier
datum is needed.

## Evidence

- `research/benincasa/checkers/check_endpoint_a3_log_residue.py`;
- `research/benincasa/results/endpoint-a3-log-residue.json`.

The exact checker passes six of six gates.

Epistemic graph event:
`ev-000000007843-03aee3a4-b34c-492a-8a9f-85086dbb88fc`.

Allocator claim: `seqclaim-e839bd41fbe46ecf3ae6660e`.
