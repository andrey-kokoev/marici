---
author: marici.Figueiredo
---

# 3411 — Rank and Index Form a Faithful Relational Two-Port Readout

## Claim

For endpoint ranks \((n_0,n_\pi)\), aggregate rank and oriented index have joint
response

\[
\begin{pmatrix}T\\I\end{pmatrix}
=
\begin{pmatrix}1&1\\1&-1\end{pmatrix}
\begin{pmatrix}n_0\\n_\pi\end{pmatrix}.
\]

The determinant is \(-2\), so the pair is faithful on its parity-compatible
integer image. Either scalar probe alone has rank one. Same-index and same-rank
hostile pairs prove that both are necessary.

## Classification

Separately labelling the endpoints replaces the endpoint-swap quotient by the
stabilizer of the labels. The result is a faithful relational readout and
rigidifier, not a source selector. Physical authority requires two
source-derived, commonly calibrated endpoint couplings and their threshold and
detector response.

## Durable verification

- Packet: research/flavor/flavor-endpoint-rank-index-two-port-readout.md
- Checker:
  research/flavor/checkers/wp763_endpoint_rank_index_two_port_readout.py
- Generated result:
  research/flavor/results/wp763_endpoint_rank_index_two_port_readout.json
- Exact checker outcome: 11/11 PASS.
- Sequence authority: seqclaim-560d294f752de1bc5c6a672d.
- Epistemic-graph admission:
  ev-000000007307-5916e3ce-972a-4b0d-a49b-e3eb2badec56.
