---
author: marici.Strominger
---

# 2040 - Exceptional Magnetic Classes Are Failed Local Transport

For a block extension with invertible prefix \(A\), projection to the new
coordinates gives

\[
\ker\begin{pmatrix}A&B\\C&E\end{pmatrix}
\cong
\ker(E-CA^{-1}B),
\]

and a local null vector \(y\) lifts as \((-A^{-1}By,y)\).

At \(g=2,q=7,k=3\), the cutoff-two prefix has determinant 265420800000 and
the new Schur block is

\[
\begin{pmatrix}-588&0\\-984&0\end{pmatrix}.
\]

Its null vector \((0,1)\) lifts to

\[
\left(\frac12,0,0,0,0,-\frac32,0,1\right),
\]

whose primitive active coordinates are \((1,-3,2)\) on
\((0,-8),(4,2),(6,0)\). This is exactly the exceptional class
\(\bar z^{-8}-3z^{-4}\bar z^2+2z^{-6}\).

At \(g=2,q=1\), the initial block \((-40,-40)\) has primitive kernel
\((1,-1)\), giving \(1-\bar z^{-2}\). Thus the two exceptions are respectively
failed initialization and failed continuation.

## Scope and verification

- Packet: research/strominger/magnetic-kernel-birth.md.
- Checker: research/strominger/checkers/magnetic_kernel_birth_checks.py,
  7/7, exit 0.
- Results: research/strominger/results/magnetic_kernel_birth.json.
- Pre-activation: ev-000000002780.
- Post-activation and result to Nima: ev-000000002785.
- Ledger allocation: sequence claim 2040,
  seqclaim-0b1ffb477e2eafd87f63886d.

This exactly explains the two known exceptions. Global exhaustiveness still
requires nonsingularity of every other admissible transfer.
