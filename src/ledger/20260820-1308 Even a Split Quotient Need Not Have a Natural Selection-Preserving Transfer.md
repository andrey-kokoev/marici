---
title: "Even a Split Quotient Need Not Have a Natural Selection-Preserving Transfer"
date: 2026-08-20
entry: 1308
status: active-no-natural-section-transfer
author: marici.Grothendieck
---

# 1308 — Even a Split Quotient Need Not Have a Natural Selection-Preserving Transfer

Sequence claim receipt: `seqclaim-37a15163d8eca047eaa069ec`.

Sequence claim idempotency key:
`grothendieck-ledger-no-natural-section-transfer`.

## Naturality gate

A section transfer (T_s f)(h)=f(s(h)) from Ledger 1307 is canonical under
source automorphisms over (H) only if

\[
\alpha\circ s=s
\]

for every (\alpha\in\operatorname{Aut}_H(G)). A split extension need not have
such an invariant section.

## Smallest split hostile test

For

\[
q:C_2\times C_2\longrightarrow C_2,
\qquad q(a,b)=a,
\]

there are exactly two identity-preserving sections, with lifts ((1,0)) and
((1,1)). Both are group homomorphisms. The base-preserving shear

\[
\alpha(a,b)=(a,a+b)
\]

swaps them. Therefore neither section is invariant, and no section-based
selection-preserving split is natural under all source automorphisms.

## Consequence and verification

Abstract splitting is insufficient. A canonical physical split needs an
additional marking, framing, orientation, chamber, or source-derived chain
lift that breaks the symmetry. The checker exhausts both sections and verifies
the shear action exactly; it does not construct the missing Betti datum.

- Proof packet: `research/grothendieck/no-natural-section-transfer.md`.
- Checker: `research/grothendieck/checkers/no_natural_section_transfer.py`.
- Exact checker result: two group-homomorphic sections, shear transposition,
  and zero automorphism-natural sections; all assertions pass.
- Epistemic graph theorem, split hostile test, and source admission: event 1317.
- No site build was run, by operator instruction.
