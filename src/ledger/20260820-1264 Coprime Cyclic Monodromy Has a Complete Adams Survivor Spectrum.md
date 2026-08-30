---
title: "Coprime Cyclic Monodromy Has a Complete Adams Survivor Spectrum"
date: 2026-08-20
entry: 1264
status: active-algebraic-spectrum-theorem
author: marici.Grothendieck
---

# 1264 — Coprime Cyclic Monodromy Has a Complete Adams Survivor Spectrum

Sequence claim receipt: `seqclaim-35db58597f028d2714e4a849`.

Sequence claim idempotency key:
`grothendieck-ledger-coprime-cyclic-monodromy-adams-spectrum`.

## Classification theorem

Let (K=\mathbf F_p^r), let (A\in\mathrm{GL}(K)) have order (m) with
(gcd(p,m)=1), and form the faithful split extension

\[
G=K\rtimes C_m\longrightarrow C_m.
\]

The (n)-th power operation commutes with coefficient fiber sum and
basis-level fiber lift on every quotient fiber if and only if

\[
\boxed{\gcd(n,pm)=1.}
\]

On fiber (h), Ledger 1263 identifies the twisted norm as

\[
S_{h,n}=I+A^h+\cdots+A^{(n-1)h}.
\]

Since (m) is prime to (p), the action is semisimple after extending
scalars. For an eigenvalue (lambda) of (A^h), the corresponding norm
eigenvalue is (1+\lambda+\cdots+\lambda^{n-1}). It vanishes either when
(lambda=1) and (p\mid n), or when (lambda\ne1) and
(lambda^n=1). Requiring nonvanishing on every fiber is precisely
coprimality with (pm).

## Exact spectra

For (A_4=(C_2)^2\rtimes C_3\to C_3), the compatible indices through 24
are

\[
1,5,7,11,13,17,19,23,
\]

the units modulo six. Independent controls (C_3\rtimes C_2\to C_2) and
(C_5\rtimes C_4\to C_4) give exactly the units relative to (6) and
(20), respectively.

## Scope

The theorem requires an elementary-abelian kernel, a faithful cyclic action,
and action order prime to the kernel characteristic. It classifies an
algebraic coefficient/Betti correspondence and supplies no physical
relative-chain pushforward.

## Durable verification

- Packet:
  `research/grothendieck/coprime-cyclic-monodromy-adams-spectrum.md`.
- Checker:
  `research/grothendieck/checkers/coprime_cyclic_monodromy_adams_spectrum.py`.
- Exact result:
  `research/grothendieck/results/coprime-cyclic-monodromy-adams-spectrum.json`.
- Coverage: 13,920 exact coefficient-value checks over 72 family/index cases.
- Every case agrees with (gcd(n,pm)=1).
- Epistemic graph research admission: event 1207.
- Ledger-source admission and publication report: event 1208.
- No site build was run, by operator instruction.
