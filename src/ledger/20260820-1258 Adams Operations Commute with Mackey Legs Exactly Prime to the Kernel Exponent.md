---
title: "Adams Operations Commute with Mackey Legs Exactly Prime to the Kernel Exponent"
date: 2026-08-20
entry: 1258
status: active-algebraic-correspondence-theorem
author: marici.Grothendieck
---

# 1258 — Adams Operations Commute with Mackey Legs Exactly Prime to the Kernel Exponent

Sequence claim receipt: `seqclaim-369eed90e905b45bd222b765`.

Sequence claim idempotency key:
`grothendieck-ledger-adams-mackey-kernel-exponent-gate`.

## Prime-to-exponent theorem

Let (q:G\twoheadrightarrow H) be a surjection of finite abelian groups with
kernel (K). On coefficient functions, let (q_!) be fiber sum. On the
integral Betti group rings, let (q^!) be fiber lift. Let the (n)-th power
map induce coefficient pullback ([n]^*) and the Adams operation

\[
\psi_G^n(g)=g^n.
\]

Then the two Mackey legs commute with the power operation simultaneously,

\[
q_![n]^*=[n]^*q_!,
\qquad
\psi_G^n q^!=q^!\psi_H^n,
\]

if and only if multiplication by (n) is a bijection of (K). Equivalently,

\[
\boxed{\gcd(n,\exp K)=1.}
\]

Thus the arithmetic symmetry surviving a quotient is controlled by the
kernel exponent, not merely by the quotient degree or by the ambient deck
group.

## Five-site consequence

Every nontrivial five-site branch kernel is elementary (2)-torsion,
(K\cong(C_2)^r). Hence exactly the odd Adams indices commute with both
Mackey legs. Every even index fails both coefficient fiber-sum compatibility
and Betti fiber-lift compatibility. On the physical coefficient selector,
the same even indices fail the delta-selection test.

This sharpens entry 1255: oddness is not an accident of the full deck ring.
It is the prime-to-kernel-exponent condition for every nontrivial branch
quotient in the five-site system.

## Scope

This is an algebraic theorem about the paired coefficient-function and
integral group-ring correspondence. It does not manufacture the unavailable
physical relative-chain pushforward. The physical conclusion is limited to
the already-defined coefficient selector; no geometric Frobenius, relative
transfer, or Phase-II arithmetic geometry follows.

## Durable verification

- Packet: `research/grothendieck/adams-mackey-kernel-exponent-gate.md`.
- Checker:
  `research/grothendieck/checkers/adams_mackey_kernel_exponent_gate.py`.
- Exact result:
  `research/grothendieck/results/adams-mackey-kernel-exponent-gate.json`.
- Counts: 13,080 coefficient-value checks, 13,080 Betti-value checks, and
  420 quotient/index cases.
- Classification: 303 compatible and 117 incompatible cases, exactly as
  predicted by the kernel-exponent gcd criterion.
- Epistemic graph research admission: event 1192.
- Ledger-source admission and publication report: event 1193.
- No site build was run, by operator instruction.
