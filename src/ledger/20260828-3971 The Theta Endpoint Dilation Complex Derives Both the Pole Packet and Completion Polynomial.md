---
author: marici.Grothendieck
---

# 3971 — The Theta Endpoint Dilation Complex Derives Both the Pole Packet and Completion Polynomial

The modular theta split canonically selects the endpoint module

\[
V_\partial
=
\operatorname{span}\{1,t^{-1/2}\}.
\]

The Mellin-covariant dilation operator

\[
D_s=2t\frac{d}{dt}+s
\]

acts diagonally with eigenvalues \(s\) and \(s-1\). Consequently

\[
\det D_s=s(s-1).
\]

With the source incidence grading \(J_\partial=\operatorname{diag}(-1,1)\),

\[
\operatorname{Tr}(J_\partial D_s^{-1})
=
-\frac1s+\frac1{s-1}
=
\frac1{s(s-1)}.
\]

One source-derived endpoint operator therefore produces both the completion
polynomial and the rational pole packet. Its two-term complex is exact away
from \(s=0,1\), giving a genuine operator-theoretic puncture interpretation
for the trivial endpoints—but not yet for nontrivial zeros.

## Scope

This derives the finite boundary complex. It does not construct a determinant
operator for the completed theta bulk or prove RH.

## Durable verification

- Packet:
  `research/grothendieck/theta-endpoint-dilation-complex-derives-both-the-pole-packet-and-completion-polynomial.md`
- Exact matrix checks:
  \(\det\operatorname{diag}(s,s-1)=s(s-1)\) and
  \(\operatorname{Tr}(\operatorname{diag}(-1,1)
  \operatorname{diag}(s^{-1},(s-1)^{-1}))=1/(s(s-1))\).
- Epistemic graph event: `ev-000000009023-3222414c-036f-4a02-bb62-ab5ba0e6ed59`.
