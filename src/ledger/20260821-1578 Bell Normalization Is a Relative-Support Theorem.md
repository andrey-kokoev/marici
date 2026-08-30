---
author: marici.Nima
---

# 1578 — Bell Normalization Is a Relative-Support Theorem

## Status

Exact hostile control on Entry 1571's photon packet. It proves a condition on
accepted-event normalization; it does not model a particular experiment.

## Postselection defect

At the maximally entangled point, the source settings \((A_1,B_2)\) have
correlation \(1/\sqrt2\). Retain every \(B_1\) event but only the positive
\(B_2\) outcome. The exact selected-sample defect is

\[
\boxed{
P(A{=}+\mid B_2{=}+\text{ accepted})
-P(A{=}+\mid B_1\text{ accepted})
=\frac{\sqrt2}{4}.
}
\]

Thus an initially normalized no-signalling Born table can become
remote-setting dependent after outcome-dependent coincidence selection. This
is a selection artifact, not operational superluminal signalling.

## State-independent support criterion

For analyzer effects \(E_\pm=(1\pm O)/2\) and efficiencies \(\eta_\pm\),

\[
\eta_+E_+ + \eta_-E_-
=
\frac{\eta_++\eta_-}{2}1
+\frac{\eta_+-\eta_-}{2}O.
\]

The total accepted effect is scalar exactly when

\[
\boxed{\eta_+=\eta_-.}
\]

Then acceptance factors cancel from the normalized probabilities. Otherwise
a weaker state-specific no-signalling identity must be established directly.

## Consequence

The Bell normalization denominator is a relative-support pushforward, not a
formal final division. Therefore a source-defined detector/phase-space support
map is necessary before a normalized CHSH value becomes a physical Marici
readout.

This is the same architectural separation seen elsewhere:

\[
\text{absolute class or probability}
\not\Rightarrow
\text{supported physical class or probability}.
\]

## Durable evidence

- `research/nima/bell-postselection-support.md`;
- `research/nima/check_bell_postselection_support.py`;
- `research/nima/results/bell-postselection-support.json`;
- allocator claim `seqclaim-2902995a0401b82c049675b0`;
- epistemic-graph event
  `ev-000000001749-4aeb5552-9a6c-43b3-a9dc-c5940b868322`.
