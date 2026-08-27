---
author: marici.Figueiredo
---

# 3377 — One Spurion Does Not Fix One Flavor Source Map

## Claim

For oppositely charged link multiplets and one supersymmetry-breaking spurion,
gauge symmetry separately permits the two diagonal Kähler operators with
Wilson coefficients \(c_+\) and \(c_-\). In the heavy-light link basis their
soft response is

\[
g^2v^2
\begin{pmatrix}
(c_++c_-)/2 & (c_+-c_-)/2\\
(c_+-c_-)/2 & (c_++c_-)/2
\end{pmatrix}.
\]

Without exchange symmetry, \(c_+-c_-\) mixes the nominal heavy and light
directions. The common spurion is then neither a threshold-channel rigidifier
nor a numerical selector.

## Exchange-symmetric residual

Exchange symmetry forces \(c_+=c_-=c\) and removes the mixing, but gives

\[
\epsilon=\frac{c}{2q^2+c},
\qquad
\Delta=\frac{g^2c}{2(2q^2+c)}.
\]

At \(q^2=1\), the equally admissible values \(c=1\) and \(c=3\) give
\(g^2/6\) and \(3g^2/10\), with exact residual \(2g^2/15\).

## Classification

One spurion does not define one source map. Exchange symmetry can rigidify the
channel but cannot normalize its surviving Wilson coefficient. A Deutschian
source principle must constrain the operator algebra itself: it must both
forbid the exchange-odd operator and normalize the exchange-even operator.

## Durable verification

- Packet:
  research/flavor/flavor-single-spurion-wilson-coefficient-dichotomy.md
- Checker:
  research/flavor/checkers/wp750_single_spurion_wilson_coefficient_dichotomy.py
- Generated result:
  research/flavor/results/wp750_single_spurion_wilson_coefficient_dichotomy.json
- Exact checker outcome: 13/13 PASS.
- Sequence authority: seqclaim-d9023d9c7491e8545e83aaf9.
- Epistemic-graph admission:
  ev-000000007238-a54e679a-f51c-4739-9cdf-a078ef7d593c.
