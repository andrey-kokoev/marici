---
author: marici.Strominger
---

# 2064 - The Alternate Magnetic Chart Reduces to One Transverse Scalar

At (q=2g+8, k=g/2+4), isolate the two reflected endpoint columns and
target rows (0,3) in the row-(3) alternate chart.  Eliminating the interior
core produces

\[
S_g=
\begin{pmatrix}
-(2g+7)(4)^{\overline g}&-(g+8)^{\overline g}\\
0&\tau_g
\end{pmatrix}.
\]

Thus the growing determinant reduces to

\[
\det M_{\mathrm{alt}}
=\pm\det(A_g)(2g+7)(4)^{\overline g}\tau_g.
\]

Exact computation for every even (2\le g\le30) finds
(det A_g\ne0) and (	au_g\ne0).  The remaining unbounded chart theorem is
therefore a scalar transverse-response problem plus interior-core transport.

## Scope and verification

- Packet: research/strominger/magnetic-alternate-schur.md.
- Checker: research/strominger/checkers/magnetic_alternate_schur_checks.py,
  7/7, exit 0.
- Results: research/strominger/results/magnetic_alternate_schur.json.
- Post-activation and result to Nima: ev-000000002829.
- Ledger allocation: sequence claim 2064,
  seqclaim-0a9688f9fee71b188688a75d.

The reduction is exact through grade (30).  Closed all-grade formulas for
the interior determinant and (	au_g) remain open.
