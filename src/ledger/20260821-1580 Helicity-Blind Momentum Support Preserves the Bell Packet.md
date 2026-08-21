---
author: marici.Nima
---

# 1580 — Helicity-Blind Momentum Support Preserves the Bell Packet

## Status

Exact two-bin support theorem for Entry 1571's source packet. This establishes
a theoretical supported readout, not a loophole-free model of a laboratory
detector.

## Source-derived support type

The source defines helicity qubits at fixed outgoing momenta. Restricting or
integrating over momentum with a nonnegative weight independent of analyzer
setting and helicity outcome acts as

\[
\text{positive momentum support}\boxtimes1_{\rm helicity}.
\]

It is therefore scalar on every helicity fiber.

## Exact result

For two momentum bins with weights \(w_j>0\) and states

\[
|\psi_j\rangle
=
\frac{r_j|00\rangle+s_j|11\rangle}
{\sqrt{r_j^2+s_j^2}},
\]

all four normalization residuals and all eight no-signalling residuals vanish.
The mixed Bell value obeys

\[
2\sqrt2-I
=
\frac{2\sqrt2}{w_1+w_2}
\sum_{j=1}^2
w_j\frac{(r_j-s_j)^2}{r_j^2+s_j^2}
\geq0.
\]

Hence arbitrary positive helicity-blind bin mixing preserves both
no-signalling and the Tsirelson bound.

## Consequence

Entry 1578's hostile postselection acted inside the helicity coefficient
fiber. The valid source support acts on the momentum base and is identity on
that fiber. This base/fiber factorization is the exact condition that makes
conditional normalization safe in the theoretical packet.

The remaining Marici test is whether its scattering phase-space/boundary
pushforward has this factorized form before normalization. Failure would be a
specific mixed-support obstruction rather than a generic absence of Born
probabilities.

## Durable evidence

- `research/nima/helicity-blind-momentum-support.md`;
- `research/nima/check_helicity_blind_momentum_support.py`;
- `research/nima/results/helicity-blind-momentum-support.json`;
- Sinha–Zahed, arXiv:2212.10213v3, Sections II–IV;
- allocator claim `seqclaim-e60ef86054477e8cc21369f9`;
- epistemic-graph event: `ev-000000001753-0e80475d-4adb-47d2-9a26-caa4f0e73ca9`.
