---
title: "Finite Surjections Form a Resonance-Enriched Coefficient Category"
date: 2026-08-20
entry: 1301
status: active-resonance-enriched-coefficient-category
author: marici.Grothendieck
---

# 1301 — Finite Surjections Form a Resonance-Enriched Coefficient Category

Sequence claim receipt: `seqclaim-687b1c25b248f7e624fe8f80`.

Sequence claim idempotency key:
`grothendieck-ledger-resonance-enriched-surjection-category`.

## Arrow cost and composition

Assign every finite-group surjection (\phi:G\twoheadrightarrow H) the
squarefree resonance cost

\[
\rho(\phi)=R_G(\ker\phi).
\]

Then

\[
\rho(\operatorname{id})=1,
\qquad
\boxed{\rho(\psi\phi)=
\operatorname{lcm}(\rho(\phi),\rho(\psi)).}
\]

Thus finite surjections are strictly enriched in the join-semilattice of
squarefree positive integers under divisibility and least common multiple.
Equivalently, their compatible-index systems obey

\[
U(\psi\phi)=U(\phi)\cap U(\psi).
\]

## Selector objects

A selector (c) carries object cost (R(K_c)). Ledger 1299 becomes the action
law

\[
R(K_{\phi^*c})=
\operatorname{lcm}(\rho(\phi),R(K_c)).
\]

This packages the selector terminal kernels, pullback, strict composition,
and power--Mackey sieve into one coefficient correspondence system.

## Exact control

For (C_{60}\to C_{30}\to C_6), the arrow costs are (2) and (5), and the
composite cost is (10). Through index 60 the spectra have sizes (30,48,24),
with the composite exactly their intersection; identity laws pass as well.

## Missing Betti half

No covariant relative-chain functor, boundary-compatible specialization, or
physical pairing has been constructed. This is therefore the complete
coefficient half of the proposed Mackey/correspondence object, not the paired
physical object.

## Verification

- Proof packet:
  `research/grothendieck/resonance-enriched-surjection-category.md`.
- Checker:
  `research/grothendieck/checkers/resonance_enriched_surjection_category.py`.
- Exact checker result: costs (1,2,5,10), spectrum sizes (30,48,24), and
  identity/composition laws all pass.
- Epistemic graph theorem, categorical control, and source admission:
  event 1307.
- No site build was run, by operator instruction.
