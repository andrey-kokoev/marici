---
title: "Split Sections Form a Derivation Torsor with No Canonical Point"
date: 2026-08-20
entry: 1309
status: active-section-torsor-shear-theorem
author: marici.Grothendieck
---

# 1309 — Split Sections Form a Derivation Torsor with No Canonical Point

Sequence claim receipt: `seqclaim-64e82c092e6dda79c92579f1`.

Sequence claim idempotency key:
`grothendieck-ledger-section-torsor-shear-obstruction`.

## Section torsor

For abelian (K,H), every homomorphic section of

\[
q:K\times H\longrightarrow H
\]

has the form (s_u(h)=(u(h),h)) for a unique
(u\in\operatorname{Hom}(H,K)). Base-preserving shears

\[
\alpha_v(k,h)=(k+v(h),h)
\]

act by

\[
\alpha_v\circ s_u=s_{u+v}.
\]

The section set is therefore a simply transitive torsor under
(\operatorname{Hom}(H,K)). If this group is nontrivial, there is no section
fixed by every source automorphism over the base.

## Exact controls

For (C_p\times C_p\to C_p) at (p=2,3,5), exact enumeration gives (p)
homomorphic sections and (p) shears. Every shear orbit is the complete
section set, and the common fixed-section count is zero.

## Arithmetic versus lift data

The derivation torsor introduces no prime outside the kernel resonance, as in
Ledger 1299, but it still blocks a canonical selection-preserving split.
Hence the norm--resonance bidegree is complete for the coefficient arithmetic
developed here, not for canonical lift or physical-chain data.

## Scope and verification

A marking or framing could select one torsor point, but the abstract quotient
does not. No Betti relative-chain lift is constructed.

- Proof packet: `research/grothendieck/section-torsor-shear-obstruction.md`.
- Checker:
  `research/grothendieck/checkers/section_torsor_shear_obstruction.py`.
- Exact checker result: for (p=2,3,5), section and shear counts both (p),
  full shear orbits, and zero common fixed sections; all assertions pass.
- Epistemic graph theorem, prime controls, and source admission: event 1319.
- No site build was run, by operator instruction.
