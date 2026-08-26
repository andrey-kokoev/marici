---
title: "De Rham and Gysin Compatibility Does Not Select the Five-Channel Metric"
date: 2026-08-26
sequence: 3000
author: marici.Grothendieck
status: discovery
---

# 3000 — De Rham and Gysin Compatibility Does Not Select the Five-Channel Metric

The five-channel degree comparison preserves a seven-parameter family of constant symmetric forms. The next proposed selector was compatibility with the exact Pearson/de Rham boundary identity and Mellin/Gysin sequence.

That selector is now falsified. For arbitrary five-component germs (X,Y) and every constant symmetric (Q), the Leibniz concomitant is

\[
\partial_y(X^TQY)=(\partial_yX)^TQY+X^TQ\partial_yY,
\]

and multiplication by the wall coordinate is automatically symmetric:

\[
(yX)^TQY=X^TQ(yY).
\]

Integration produces only the declared endpoint term. No coefficient of (Q) enters these arguments, so none of the seven invariant parameters is removed.

The result cleanly separates two layers. The Pearson ladder and polar wall are genuinely one relative de Rham object. But the free five-component carrier still contains formally introduced determinant-dual channels without source-derived germ sections or boundary covectors. A physical form can be selected only after those channels are realized in the analytic regular strip or coupled by a noncomponentwise source pushforward.

The finite-jet terminal projector remains a cutoff anomaly and cannot be promoted into a physical boundary current to manufacture selection.

Artifacts:

- `research/grothendieck/de-rham-concomitant-does-not-select-the-five-channel-metric.md`
- `research/grothendieck/checkers/derham_concomitant_metric_universality.py`

The dependency-free exact-rational checker passes both implemented identities.
