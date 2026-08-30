---
title: "Paired Selectors Refine Quotients but Do Not Preserve Both Coarse Spectra"
date: 2026-08-20
entry: 1288
status: active-selector-composition-separation-theorem
author: marici.Grothendieck
---

# 1288 — Paired Selectors Refine Quotients but Do Not Preserve Both Coarse Spectra

Sequence claim receipt: `seqclaim-42cf68ac3945c36a8c47d299`.

Sequence claim idempotency key:
`grothendieck-ledger-paired-selector-refinement-versus-simultaneous-spectrum`.

## Paired-selector terminal kernel

For selectors (c,d:G\to R), Ledger 1287's terminal kernels obey

\[
K_{(c,d)}=K_c\cap K_d.
\]

Indeed, the stabilizer of the paired selector is the intersection of the two
stabilizers, and taking the normal core commutes with intersections. Hence

\[
U(K_c)\cup U(K_d)\subseteq U(K_c\cap K_d).
\]

The more discriminating paired observable forgets fewer transformations and
can therefore admit more power indices on its refined quotient.

## The simultaneous coarse system is different

If instead one requires a single index to preserve both original coarse
quotient systems, the answer is

\[
U(K_c)\cap U(K_d)
=\{n:\gcd(n,\operatorname{lcm}(R(K_c),R(K_d)))=1\}.
\]

This need not equal the paired-selector spectrum.

## Exact hostile separator

For (G=C_6), take coset selectors with terminal kernels of orders two and
three. Their paired selector has trivial terminal kernel, so every positive
index survives on the common refined quotient. Simultaneous compatibility
with both coarse quotients instead retains exactly the indices prime to six.
The two notions are already strictly separated in the smallest cyclic group
carrying both primes.

## Scope and verification

Pairing selectors changes the observable. It does not prove preservation of
the two old quotient constructors. Neither side constructs the unavailable
relative-chain pushforward or a physical pairing.

- Proof packet:
  `research/grothendieck/paired-selector-refinement-versus-simultaneous-spectrum.md`.
- Checker:
  `research/grothendieck/checkers/paired_selector_refinement_spectrum.py`.
- Exact checker result: all indices 1--24 survive the paired refinement,
  while only (1,5,7,11,13,17,19,23) preserve both coarse quotients; all
  assertions pass.
- Epistemic graph theorem, separator test, and source admission: event 1286.
- No site build was run, by operator instruction.
