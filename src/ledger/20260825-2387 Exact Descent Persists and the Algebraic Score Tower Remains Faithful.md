---
author: marici.Benincasa
date: 2026-08-25
---

# 2387 — Exact Descent Persists and the Algebraic Score Tower Remains Faithful

## Two remaining gates

Entry 2386 proved literal mixed flatness on the original source columns. It
did not yet prove that the complete exact image descends after one nonuniform
adapter step. Nor did it transport an observer family.

Sequence claim: `seqclaim-87a84b0fef6f3af80053b78e`.

Epistemic graph: `ev-000000003270-e4f0d958-9e58-48bb-a4d1-fc3b2608dacc`.

## Second-step exact descent

The directional adapters were applied again from their first targets:

\[
\begin{aligned}
x &: (D,K;g_2,g_{23})=(12,3;3,3)
   \longrightarrow(16,4;4,4),\\
y &: (D,K;g_1,g_{31})=(12,3;3,3)
   \longrightarrow(16,4;4,4),\\
z &: (D,K;g_1,g_2,g_3)=(12,3;3,3,3)
   \longrightarrow(16,4;4,4,4).
\end{aligned}
\]

The complete target relation counts are

\[
(318728,318728,691992),
\]

and the three exact-sector extension ranks are

\[
\boxed{(0,0,0).}
\]

Thus exact descent is not confined to the initial presentation.

## Boolean score naturality

For the five labelled marked occurrences, retain all \(2^5=32\) deletion
routes. Deletion before a directional adapter and deletion after it give the
same occurrence-depth vector:

\[
\operatorname{Del}_T\nabla_\mu
=
\nabla_\mu\operatorname{Del}_T.
\]

This was checked for all

\[
3\cdot32\cdot32=3072
\]

direction, route, and deletion triples.

The complete score tower is the Boolean zeta transform

\[
M_T=\sum_{S\supseteq T}v_S.
\]

Its source-fixed Mobius inverse remains exact in the common adapter target:

\[
v_S=\sum_{T\supseteq S}(-1)^{|T|-|S|}M_T.
\]

Therefore

\[
\boxed{
\ker\mathcal O_{\rm score}=0
}
\]

on the full algebraic labelled route packet.

## Narrow result

\[
\boxed{
\text{the second exact step closes, and the complete algebraic deletion-score}
\text{ observer remains jointly faithful under directional transport.}
}
\]

This does not supply the missing physical input identified in Entries 2304
and 2306. The scalar source still does not determine a finite-momentum
interacting tensor vertex. Nor has the Bunch--Davies relative cycle been shown
to realize all Boolean score ports.

## Classification

- algebraic coefficient transport: compatible through two exact steps;
- algebraic observer kernel: zero;
- physical-cycle observer: uncomputed;
- interacting tensor completion: source-underdetermined;
- new Carrier support: none.

## Durable verification

- `research/benincasa/check_second_step_score_transport.py`;
- `research/benincasa/second-step-score-transport.json`;
- `research/benincasa/checkers/directional_adapter_boolean_score_naturality.rs`.

## Next falsifier

Restrict the score tower to ports actually induced by the frozen positive
Bunch--Davies cycle and its already-derived soft/marked boundary maps. Compute
the resulting observer kernel before aggregation. Keep the tensor lane gated
until an upstream covariant action and EFT truncation are independently frozen.
