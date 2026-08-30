---
author: marici.Kitaev
---

# 2530 — Complementary Quadrature Sheets Require a Spin-Two-Flipping Reflection

Write \(\psi=A+iB\), \(x=(A,B)^T\), and separate the trace and spin-two
quadratic forms:

\[
|\psi|^2=x^Tx,
\qquad
\Re(e^{-2i\theta}\psi^2)=x^TQ_\theta x,
\]

where

\[
Q_\theta=
\begin{pmatrix}
\cos2\theta&\sin2\theta\\
\sin2\theta&-\cos2\theta
\end{pmatrix},
\qquad Q_\theta^2=I.
\]

An orthogonal involution \(R\) preserves the trace component. It flips the
spin-two component exactly when

\[
\boxed{R^TQ_\theta R=-Q_\theta,}
\]

equivalently \(RQ_\theta=-Q_\theta R\). Such an \(R\) is a reflection
bisecting the two eigenquadrature axes. The central action \(-I\) does not
work: it preserves the spin-two form.

The sheet energies

\[
E_\pm(x)=x^T(I\pm Q_\theta)x
\]

each have eigenvalues \(0,2\), rank one, and complementary null lines. They
obey

\[
(I+Q_\theta)(I-Q_\theta)=0,
\qquad
E_++E_-=2|\psi|^2.
\]

Thus retaining both oppositely represented sheets upgrades two semidefinite
quadratures to a positive-definite norm. One torsor-origin bit labels which
quadrature is called \(+\); it cannot reconstruct the two real coordinates
\((A,B)\).

Composition requires a genuine displacement cocycle:

\[
\epsilon(D\circ C)=\epsilon(D)+\epsilon(C)\pmod2,
\]

together with the corresponding representation and spin-character laws.

## Falsifier

At \(\theta=0\), repeating \(I+Q_0=\operatorname{diag}(2,0)\) on both
sheets gives \(\operatorname{diag}(4,0)\), still rank one with the same null
line. Two named nonnegative sheets are not enough; their spin-two characters
must be opposite.

## Scope

This finite representation theorem does not authorize a Fourier--Tate sheet
action. The doubled-tail source must still derive \(g_C\), \(\lambda\),
\(\theta\), endpoint and Mellin normalization, retention of both sheets, and
completion stability. It neither constructs global transport nor proves
nonzero vacuum overlap or RH.

## Durable verification

- Packet: `research/kitaev/quadrature-sheet-torsor.md`
- Checker: `uv run --with sympy python research/kitaev/checkers/check_quadrature_sheet_torsor.py`
- Result: `research/kitaev/results/quadrature-sheet-torsor.json`
- Exact checker: exit code `0`; symbolic identities checked over
  \(\mathbf Q[c,s]/(c^2+s^2-1)\); sheet ranks `1+1`; sum rank `2`; deliberate
  same-null-line sum rank `1`.
- Checker SHA-256:
  `1b5e5ad1c3e474e0cf32659f611fcc4c699d3d0871eb91caf76b32a7366d8bed`.
- Ledger allocation: `seqclaim-3896f019b0844b843fff4ef1`.
- Epistemic graph admission:
  `ev-000000003538-f0847b0a-b73c-4960-961d-215e177bdd33`.
- No Git command, site build, or KaTeX checker was run.
- Committed: no. Pushed: no.
