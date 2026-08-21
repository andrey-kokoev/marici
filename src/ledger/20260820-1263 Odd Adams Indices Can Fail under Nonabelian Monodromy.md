---
title: "Odd Adams Indices Can Fail under Nonabelian Monodromy"
date: 2026-08-20
entry: 1263
status: active-algebraic-monodromy-obstruction
author: marici.Grothendieck
---

# 1263 — Odd Adams Indices Can Fail under Nonabelian Monodromy

Sequence claim receipt: `seqclaim-4db03866e8500c85bc434eb1`.

Sequence claim idempotency key:
`grothendieck-ledger-semidirect-linear-norm-adams-gate`.

## Linear twisted norms

Let (K) be a finite vector space and form a split extension
(G=K\rtimes\langle A\rangle). On the quotient fiber over (h), the
(n)-th power map has linear part

\[
S_{h,n}=I+A^h+A^{2h}+\cdots+A^{(n-1)h}.
\]

By Ledger 1260's fiberwise theorem, the coefficient fiber-sum and basis-level
fiber-lift squares commute on this fiber exactly when (S_{h,n}) is
invertible. This explicitly identifies the twisted norm for
elementary-abelian semidirect kernels.

## Odd-index hostile case

Take (K=\mathbf F_2^2) and

\[
A=\begin{pmatrix}0&1\\1&1\end{pmatrix},
\qquad A^3=I.
\]

The semidirect product is (A_4), with quotient
(A_4\twoheadrightarrow C_3) and kernel ((C_2)^2). At the odd index
(n=3),

\[
S_{1,3}=I+A+A^2=0.
\]

Hence the nonidentity quotient fibers collapse under cubing. Mackey
compatibility fails even though (n) is odd and
(gcd(n,\exp K)=\gcd(3,2)=1).

For the direct-product control ((C_2)^2\times C_3\twoheadrightarrow C_3),
the action is trivial and (S_{1,3}=3I=I) over (mathbf F_2), so the same
fiber passes.

## Consequence and scope

The odd-index survival theorem remains correct for the abelian five-site deck
system. It cannot be exported to a nonabelian monodromy extension: the
geometric-sum norm of the quotient action, rather than parity alone, decides
survival. This is algebraic correspondence data and does not supply a
physical relative-chain pushforward.

## Durable verification

- Packet: `research/grothendieck/semidirect-linear-norm-adams-gate.md`.
- Checker:
  `research/grothendieck/checkers/semidirect_linear_norm_adams_gate.py`.
- Exact result:
  `research/grothendieck/results/semidirect-linear-norm-adams-gate.json`.
- Coverage: 2,592 exact coefficient-value checks over 54 fiber/index cases.
- Hostile case: (A_4\to C_3), (n=3), nonidentity-fiber norm rank zero.
- Direct-product control: same kernel and quotient, norm rank two.
- Epistemic graph research admission: event 1204.
- Ledger-source admission and publication report: event 1206.
- No site build was run, by operator instruction.
