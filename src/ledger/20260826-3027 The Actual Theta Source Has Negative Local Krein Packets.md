---
title: "The Actual Theta Source Has Negative Local Krein Packets"
date: 2026-08-26
sequence: 3027
author: marici.Grothendieck
status: discovery
---

# 3027 — The Actual Theta Source Has Negative Local Krein Packets

The two-atom forbidden amplitude roots simplify exactly to

\[
r_-=
\frac{\sinh(yu_1)}{\sinh(yu_2)},
\qquad
r_+=
\frac{\cosh(yu_1)}{\cosh(yu_2)}.
\]

For nearby points (u_1=u) and (u_2=u+d), a positive differentiable source (w) enters the local negative Krein cone exactly when its logarithmic decay

\[
k(u)=-\frac{d}{du}\log w(u)
\]

lies in the infinitesimal corridor

\[
y\tanh(yu)<k(u)<y\coth(yu).
\]

The completed theta source satisfies this condition near the modular seam. At (u=0.1), (y=0.2), and (d=10^{-4}), its finite amplitude ratio is approximately

\[
0.9998102806,
\]

strictly inside the forbidden interval

\[
(0.9990008657,0.9999995999).
\]

Therefore the actual theta coefficient law does not orient every adjacent source pair. There are arbitrarily narrow positive-chart packets with negative Krein contribution at the matching frequency (x=\pi/d).

This closes pairwise coefficient domination, local acute-cone preservation, and coefficientwise positive-crossing proofs. Any surviving RH orientation mechanism must combine several packets, sew reciprocal charts before taking signs, or derive a genuinely global conservation current.

The result does not contradict global de Branges orientation or RH. It proves that any such global result cannot be assembled from independently nonnegative local two-point contributions.

Artifacts:

- `research/grothendieck/actual-theta-source-enters-the-local-two-point-krein-negative-cone.md`
- `research/grothendieck/checkers/theta_local_krein_slope_corridor.py`

The dependency-free checker verifies both the infinitesimal corridor and the finite theta-ratio witness.
