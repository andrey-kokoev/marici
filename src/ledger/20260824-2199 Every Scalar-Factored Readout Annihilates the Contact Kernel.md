---
authors:
  - marici.Benincasa
date: 2026-08-24
---
# 2199 — Every Scalar-Factored Readout Annihilates the Contact Kernel

## Factorization theorem

Let

\[
V_{\rm ct}\xrightarrow{\epsilon_{\rm ct}}R_{\rm ct}
\]

be Entry 2196's frozen contact augmentation, and let

\[
K_{\rm ct}=\ker\epsilon_{\rm ct}.
\]

Any further observable constructed only from the summed correlator has the
form

\[
V_{\rm ct}\xrightarrow{\epsilon_{\rm ct}}R_{\rm ct}
\xrightarrow{\phi}O.
\]

For every such \(\phi\),

\[
\boxed{(\phi\epsilon_{\rm ct})|_{K_{\rm ct}}=0.}
\]

This is independent of whether \(\phi\) is linear, differential, integral,
or a supported restriction, provided it genuinely factors through the
ordinary correlator object.

## Consequence

No post-processing of the scalar correlator can recover the hidden route
packet. A successful physical activation must fail to factor through
\(R_{\rm ct}\): it must retain, mark, condition on, or otherwise resolve a
route before aggregation.

Thus the missing physical datum is not a more ingenious scalar functional.
It is a lift of the physical readout to the labelled-port object.

## Evidence

- Entries 2194 and 2196–2198
- `research/benincasa/checkers/scalar_readout_factorization_no_go.rs`

