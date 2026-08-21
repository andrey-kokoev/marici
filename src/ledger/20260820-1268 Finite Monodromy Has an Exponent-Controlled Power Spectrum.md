---
title: "Finite Monodromy Has an Exponent-Controlled Power Spectrum"
date: 2026-08-20
entry: 1268
status: active-general-monodromy-theorem
author: marici.Grothendieck
---

# 1268 — Finite Monodromy Has an Exponent-Controlled Power Spectrum

Sequence claim receipt: `seqclaim-41b54563dd1960f1b48dd07e`.

Sequence claim idempotency key:
`grothendieck-ledger-finite-monodromy-exponent-adams-spectrum`.

## General theorem

Let a finite group (H) act faithfully on (K=\mathbf F_p^r), and form

\[
G=K\rtimes H\longrightarrow H.
\]

The (n)-th power operation commutes with every coefficient fiber-sum and
basis-level fiber-lift square if and only if

\[
\boxed{\gcd(n,p\,\exp H)=1.}
\]

For (h\in H), the linear twisted norm on its fiber is

\[
S_{h,n}=I+\rho(h)+\cdots+\rho(h)^{n-1}.
\]

If (p\mid n), the identity fiber fails. If another prime divides both
(n) and (exp H), an element of that prime order exposes a root-of-unity
eigenvalue whose geometric sum vanishes. Conversely, coprimality with
(p\exp H) makes every norm determinant nonzero, including in the presence
of modular Jordan blocks.

This supersedes Ledger 1265's cyclic-quotient restriction.

## Nonabelian and noncyclic controls

The faithful reflection action (S_3\to\mathrm{GL}_2(\mathbf F_5)) has
exponent six and retains exactly the indices prime to 30. The faithful
diagonal action (V_4\to\mathrm{GL}_2(\mathbf F_3)) retains exactly the
indices prime to six. Exhaustive tests through index 24 agree in every case.

## Typing boundary

When the total group is nonabelian, (g\mapsto g^n) need not be a group
homomorphism. The induced basis map is therefore not asserted to be a ring
Adams endomorphism. The theorem concerns the linear coefficient/Betti Mackey
correspondence only and supplies no physical relative-chain pushforward.

## Durable verification

- Packet: `research/grothendieck/finite-monodromy-exponent-adams-spectrum.md`.
- Checker:
  `research/grothendieck/checkers/finite_monodromy_exponent_adams_spectrum.py`.
- Exact result:
  `research/grothendieck/results/finite-monodromy-exponent-adams-spectrum.json`.
- Coverage: 97,776 exact coefficient-value checks over 48 index cases.
- Epistemic graph research admission: event 1215.
- Ledger-source admission and publication report: event 1218.
- No site build was run, by operator instruction.
