---
title: "Arbitrary Finite Kernels Have a Complete Visible Power Spectrum"
date: 2026-08-20
entry: 1278
status: active-complete-finite-kernel-theorem
author: marici.Grothendieck
---

# 1278 — Arbitrary Finite Kernels Have a Complete Visible Power Spectrum

Sequence claim receipt: `seqclaim-5eff64dc5b83a6dc98bcd9f7`.

Sequence claim idempotency key:
`grothendieck-ledger-arbitrary-finite-kernel-monodromy-spectrum`.

## Complete theorem

Let a finite group (H) act on an arbitrary finite group (K) through
(ho:H\to\operatorname{Aut}(K)), and put
(M=\operatorname{im}\rho). For

\[
K\rtimes H\longrightarrow H,
\]

the (n)-th power correspondence commutes with every coefficient fiber-sum
and basis-level fiber-lift square if and only if

\[
\boxed{\gcd\!\left(n,\exp(K)\exp(M)\right)=1.}
\]

Neither (K) nor (M) is required to be abelian.

## Sufficiency

On a fiber with visible action (alpha\in M), the coprimality condition
makes the global power map on (K\rtimes\langle\alpha\rangle) and the power
map on (langle\alpha\rangle) permutations. Their restriction is therefore
a bijection of the corresponding fibers. Invisible factors in (H) do not
enter.

## Telescoping converse

A prime shared by (n) and (exp K) already makes the identity fiber fail.
Now let a prime (p) divide both (n) and (exp M), and choose a nontrivial
action element (alpha) of order (p). For (x) moved by (alpha), set

\[
k=x^{-1}\alpha(x)\ne1.
\]

The twisted norm telescopes:

\[
k\alpha(k)\cdots\alpha^{n-1}(k)
=x^{-1}\alpha^n(x)
=1.
\]

Thus (k) and the identity collide on the (alpha)-fiber. Every visible
monodromy prime is therefore necessary.

## Consequence and scope

This proves the conjecture left open in Ledgers 1275 and 1277. For
nonabelian total groups the power correspondence is basis-linear and need not
be a ring Adams endomorphism. The theorem remains purely algebraic and does
not supply a physical relative-chain pushforward.

## Durable verification

- Proof packet:
  `research/grothendieck/arbitrary-finite-kernel-monodromy-spectrum.md`.
- Hostile automorphism sweep:
  `research/grothendieck/results/small-nonabelian-monodromy-converse-sweep.json`
  with 71,664 exact checks.
- Quaternion control:
  `research/grothendieck/results/quaternion-monodromy-twisted-power-spectrum.json`
  with 13,824 exact checks.
- Epistemic graph theorem admission: event 1252.
- Ledger-source admission and publication report: event 1253.
- No site build was run, by operator instruction.
