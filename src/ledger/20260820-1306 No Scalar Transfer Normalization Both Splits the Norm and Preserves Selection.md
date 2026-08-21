---
title: "No Scalar Transfer Normalization Both Splits the Norm and Preserves Selection"
date: 2026-08-20
entry: 1306
status: active-transfer-normalization-selector-nogo
author: marici.Grothendieck
---

# 1306 — No Scalar Transfer Normalization Both Splits the Norm and Preserves Selection

Sequence claim receipt: `seqclaim-b7e451e300f2450f107040c4`.

Sequence claim idempotency key:
`grothendieck-ledger-transfer-normalization-selector-nogo`.

## Scalar normalization no-go

Let (q:G\twoheadrightarrow H) have degree (d>1), and work in characteristic
zero with (d) invertible. For a scalar-normalized transfer (T=a q_!),

\[
Tq^*=\operatorname{id}
\quad\Longrightarrow\quad a=\frac1d,
\]

because (q_!q^*=d\operatorname{id}). But

\[
T\delta_{0,G}=\delta_{0,H}
\quad\Longrightarrow\quad a=1,
\]

because unnormalized transfer already satisfies
(q_!\delta_{0,G}=\delta_{0,H}). The two requirements are incompatible for
every nontrivial quotient.

## What averaging actually does

After degree localization,

\[
P=\frac1d q^*q_!
\]

is an idempotent projector onto fiber-constant coefficient functions. Yet

\[
P\delta_{0,G}=\frac1d1_{\ker q},
\]

so it does not preserve the frozen identity selector. For (C_4\to C_2),
the image is ((1/2,0,1/2,0)).

## Scope and verification

Exact rational arithmetic verifies the incompatibility for degrees two,
three, and four and verifies the (C_4\to C_2) averaging projector is
idempotent. This excludes scalar normalization only. A geometrically weighted
physical transfer would require new source data and the missing Betti map.

- Proof packet:
  `research/grothendieck/transfer-normalization-selector-nogo.md`.
- Checker:
  `research/grothendieck/checkers/transfer_normalization_selector_nogo.py`.
- Exact checker result: incompatible scales for degrees (2,3,4), normalized
  selector ((1/2,0,1/2,0)), and idempotent averaging projector; all
  assertions pass.
- Epistemic graph theorem, normalization controls, and source admission:
  event 1315.
- No site build was run, by operator instruction.
