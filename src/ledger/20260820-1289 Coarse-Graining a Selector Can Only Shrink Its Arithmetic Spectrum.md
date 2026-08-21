---
title: "Coarse-Graining a Selector Can Only Shrink Its Arithmetic Spectrum"
date: 2026-08-20
entry: 1289
status: active-selector-data-processing-theorem
author: marici.Grothendieck
---

# 1289 — Coarse-Graining a Selector Can Only Shrink Its Arithmetic Spectrum

Sequence claim receipt: `seqclaim-2e62115375ff259877df282f`.

Sequence claim idempotency key:
`grothendieck-ledger-selector-data-processing-resonance-inequality`.

## Data-processing law

Let (c:G\to X) be a selector and let (d=f\circ c) be any deterministic
post-processing. Then

\[
\operatorname{Stab}_R(c)\subseteq\operatorname{Stab}_R(d),
\qquad K_c\subseteq K_d,
\]

where (K_c) and (K_d) are the normal-core terminal kernels of Ledger 1287.
Combining this with Ledger 1285 gives

\[
\boxed{R(K_c)\mid R(K_d),\qquad U(K_d)\subseteq U(K_c).}
\]

Deterministic coarse-graining can therefore only enlarge the invisible
quotient kernel and shrink the compatible power--Mackey spectrum. If (f) is
injective on the image of (c), equality holds throughout.

## Exact strict chain

For (G=C_6), take the fully labelled selector, post-process it to parity,
then to the constant selector. Their terminal kernel orders are

\[
1<3<6,
\]

their resonance radicals are (1\mid3\mid6), and their operation spectra are
all indices, indices prime to three, and indices prime to six. Exact testing
through index 24 makes both spectrum inclusions strict.

## Scope and verification

This is a coefficient-side data-processing inequality. A deterministic
post-processing is not thereby a source-authorized physical constructor, and
no Betti relative-chain map or physical pairing is supplied.

- Proof packet:
  `research/grothendieck/selector-data-processing-resonance.md`.
- Checker:
  `research/grothendieck/checkers/selector_data_processing_resonance.py`.
- Exact checker result: kernel orders (1,3,6), radical labels (1,3,6), and
  spectrum sizes (24,16,8) through index 24; all assertions pass.
- Epistemic graph theorem, strict control, and source admission: event 1289.
- No site build was run, by operator instruction.
