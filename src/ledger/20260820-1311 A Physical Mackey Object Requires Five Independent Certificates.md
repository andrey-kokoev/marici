---
title: "A Physical Mackey Object Requires Five Independent Certificates"
date: 2026-08-20
entry: 1311
status: active-paired-mackey-certificate-stack
author: marici.Grothendieck
---

# 1311 — A Physical Mackey Object Requires Five Independent Certificates

Sequence claim receipt: `seqclaim-fb86fa561f7e66a61312db56`.

Sequence claim idempotency key:
`grothendieck-ledger-paired-mackey-five-gate-obstruction-stack`.

## Five certificates

A paired physical Mackey/correspondence object requires five separately typed
certificates:

1. contravariant frozen-selector descent through the quotient;
2. basis-level power--Mackey compatibility at the chosen index;
3. a covariant transfer with the declared norm and selection normalization;
4. naturality/coherence under source automorphisms and composition;
5. a physical relative-chain pushforward with boundary, orientation,
   multiplicity, and exact pairing compatibility.

The first four are now algebraically classified by Ledgers 1281--1309. None
implies the next.

## Exact independence witnesses

- Five-site (\delta_0) fails selector descent for every nontrivial kernel,
  although odd indices pass the algebraic resonance sieve.
- (A_4\to C_3) passes quotient-selector admission but fails the index-three
  power--Mackey square, even after degree localization.
- (C_4\to C_2) averaging is equivariant and split but rescales selection;
  a section repairs selection only by breaking symmetry.
- (C_2\times C_2\to C_2) is split but has no automorphism-natural section.
- The five-site formal deck quotient still has no source-derived relative-chain
  pushforward, so the physical certificate remains unavailable.

## Algebraic object versus physical extension

The completed coefficient half is the resonance-enriched surjection category
with arrow bidegree

\[
(|\ker q|,R_G(\ker q)),
\]

selector terminal costs, contravariant pullback, and unnormalized covariant
fiber-sum. A physical Mackey object is an extension by certificate five, not
an automatic interpretation of this algebra.

## Falsifier and scope

A falsifier is a canonical source-derived five-site chain map satisfying
boundary covariance, orientation and multiplicity normalization, strict
composition, and the exact coefficient--Betti pairing without the identified
lift data. No such map is currently present.

- Synthesis packet:
  `research/grothendieck/paired-mackey-five-certificate-stack.md`.
- Epistemic graph synthesis, falsifier, and source admission: event 1322.
- No site build was run, by operator instruction.
