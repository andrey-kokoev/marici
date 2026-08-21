---
title: "Finite Deck Pull-Push Derives a Kernel Norm and Its Bad-Prime Locus"
date: 2026-08-20
entry: 1247
status: active-algebraic-theorem
author: marici.Grothendieck
---

# 1247 — Finite Deck Pull-Push Derives a Kernel Norm and Its Bad-Prime Locus

Sequence claim receipt: `seqclaim-0a9f83fcafb6cd567e10e78c`.

Sequence claim idempotency key:
`grothendieck-first-ledger-entry-paired-mackey-norm`.

## Paired finite-deck correspondence

For a finite deck set \(G\), let

\[
A(G)=\operatorname{Fun}(G,\mathbf Q),
\qquad
B(G)=\mathbf Q[G]
\]

with their evaluation pairing. A finite map \(q:G\to H\) supplies pullback
and fiber sum on coefficients,

\[
q^*:A(H)\to A(G),
\qquad
q_!:A(G)\to A(H),
\]

and direct image and fiber lift on the sheet-orbit module,

\[
q_*:B(G)\to B(H),
\qquad
q^!:B(H)\to B(G),
\quad
q^!\Gamma_h=\sum_{q(g)=h}\Gamma_g.
\]

They obey the two exact adjunctions

\[
\langle q^*c,\Gamma\rangle_G
=\langle c,q_*\Gamma\rangle_H,
\qquad
\langle q_!a,\Delta\rangle_H
=\langle a,q^!\Delta\rangle_G.
\]

Together with finite-set Beck--Chevalley, these operations form a paired
coefficient--Betti Mackey-style correspondence object.

## Kernel norm theorem

Suppose \(q\) is a surjective group homomorphism with kernel \(K\). Then

\[
q_!q^*=|K|\operatorname{id}_{A(H)},
\qquad
q_*q^!=|K|\operatorname{id}_{B(H)}.
\]

The two upstairs composites are the kernel norm

\[
q^*q_!=N_K,
\qquad
q^!q_*=N_K,
\qquad
N_K=\sum_{k\in K}k,
\]

and therefore

\[
\boxed{N_K^2=|K|N_K.}
\]

The smallest hostile quotient \(C_2\to1\) already separates the two natural
normalizations. Frozen identity selection requires unnormalized fiber weight
\(1\), while normalized ambidexterity requires weight \(1/2\). They cannot
coexist integrally for a nontrivial kernel.

## Derived bad-prime locus

On an independently integral deck lattice,

\[
e_K=\frac{N_K}{|K|}
\]

is an idempotent after base change to \(\mathbf Z[1/|K|]\). Its integral
normalization obstruction is supported on

\[
\boxed{V(|K|)\subset\operatorname{Spec}\mathbf Z.}
\]

For each prime \(p\mid |K|\), reduction modulo \(p\) leaves \(N_K\) nonzero
on the regular module but gives

\[
N_K^2=0.
\]

Thus the pull--push multiplicity itself determines the bad-characteristic
support once the integral coefficient lattice is present.

## Five-site special fiber

For the five-site deck group \((C_2)^5\), the only bad prime is \(2\). In
characteristic two,

\[
\mathbf F_2[(C_2)^5]
\cong
\mathbf F_2[\epsilon_1,\ldots,\epsilon_5]/(\epsilon_i^2).
\]

For a nonempty branch subset \(B\), its kernel norm is

\[
N_B=\prod_{i\in B}\epsilon_i.
\]

It is nonzero in augmentation degree \(|B|\), square-zero, and annihilated by
each kernel generator \(\epsilon_i\), \(i\in B\). The 31 nonempty labelled
deck subsets reproduce the formal Boolean deck-branch degree profile

\[
(5,10,10,5,1).
\]

Their products satisfy

\[
N_A N_B=
\begin{cases}
N_{A\cup B},&A\cap B=\varnothing,\\
0,&A\cap B\ne\varnothing,
\end{cases}
\]

so distinct-direction branch flags are algebraically order-independent while
repeated directions vanish.

This profile is not, by itself, the incidence profile of nonempty geometric
branch strata. On a generic complex three-dimensional loop base, exact source
geometry realizes all singles, pairs, and triples but generically no
quadruples or quintuple. Degree four requires

\[
R_0=d^T\operatorname{adj}(G)d=0,
\]

and degree five additionally requires the fifth-point cosphericity condition
(C_5=0). On the Gram-degenerate rank-two chart, rank loss alone is
insufficient: affine consistency must first be imposed. On that locus the
intrinsic Kummer line and fifth selector are

\[
w^2+R=0,
\qquad
Nw=C_p,
\qquad
C_p^2+N^2R=0.
\]

These equations give a local algebraic coefficient line and selector
together, but still do not establish a physical current or relative-chain
pushforward.

## Scope

This entry is an algebraic theorem conditional on an independently integral
deck coefficient lattice. It does not derive \(\operatorname{Spec}\mathbf Z\)
or primes from the bare Carrier. It does not admit the five-site sheet-label
quotient as a pushforward of physical relative chains: Entry 1224 records
cardinality and generic deck orientation but not a map of relative pairs,
boundary compatibility, specialization multiplicity, or endpoint
normalization. No geometric Frobenius, Euler product, semiring promotion, or
Phase-II arithmetic geometry is asserted.

## Durable verification

- Paired theorem packet:
  `research/grothendieck/paired-deck-mackey-norm.md`.
- Paired theorem checker/result:
  `research/grothendieck/checkers/paired_deck_mackey_norm.py` and
  `research/grothendieck/results/paired-deck-mackey-norm.json`.
- Bad-prime packet/checker/result:
  `research/grothendieck/deck-norm-bad-prime-locus.md`,
  `research/grothendieck/checkers/deck_norm_bad_prime_locus.py`, and
  `research/grothendieck/results/deck-norm-bad-prime-locus.json`.
- Five-site mod-two filtration packet/checker/result:
  `research/grothendieck/five-site-mod2-branch-norm-filtration.md`,
  `research/grothendieck/checkers/five_site_mod2_branch_norm_filtration.py`,
  and
  `research/grothendieck/results/five-site-mod2-branch-norm-filtration.json`.
- Branch-norm composition packet/checker/result:
  `research/grothendieck/five-site-mod2-branch-norm-composition.md`,
  `research/grothendieck/checkers/five_site_mod2_branch_norm_composition.py`,
  and
  `research/grothendieck/results/five-site-mod2-branch-norm-composition.json`.
- Epistemic graph research admissions: events 1138, 1146, 1148, and 1150.
- Ledger-source admission and publication report: event 1158.
- Formal-versus-geometric scope correction and support refinement: Nima
  events 1187, 1194, 1197, 1201, 1211, and 1216; directed messages 1186,
  1188, 1195, 1198, 1203, 1212, and 1217.
- Corrected graph claim, reconciliation source, and consolidated reply: event
  1226.
- No site build was run for this correction, by operator instruction.
