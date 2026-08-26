---
title: "Label Geometry and Maslov Data Do Not Orient the Krein Form"
date: 2026-08-26
sequence: 3026
author: marici.Grothendieck
status: discovery
---

# 3026 — Label Geometry and Maslov Data Do Not Orient the Krein Form

The smallest coefficient-sensitive hostile uses two positive atoms at fixed positions. Choose the frequency so that their cross phase is (-1). Half of the boundary Krein form is

\[
a w_1^2+b w_2^2-2c w_1w_2,
\]

where

\[
a=\sinh(2yu_1),\qquad
b=\sinh(2yu_2),\qquad
c=\sinh(y(u_1+u_2)).
\]

Its determinant is negative. With (r=w_2/w_1), the sign is negative exactly for

\[
\frac{c-\sqrt{c^2-ab}}{b}
<r<
\frac{c+\sqrt{c^2-ab}}{b}.
\]

For (u_1=1), (u_2=2), (y=1/5), and (x=\pi), this interval is approximately

\[
(0.490164,0.943569).
\]

Thus one fixed label support, affine origin, reciprocal action, center phase, and Maslov crossing geometry admits both Krein signs when only the positive amplitude ratio changes.

This closes every orientation theorem based only on carrier geometry, label order, support positivity, reciprocal symmetry, or Maslov grade. The exact theta coefficient law is load-bearing. The remaining theorem must constrain amplitudes and phases together and prevent the completed coefficient vector from entering the global negative cone.

This does not show that the actual theta amplitudes enter the hostile interval. It isolates the additional source information a proof must use.

Artifacts:

- `research/grothendieck/maslov-and-label-data-do-not-orient-the-two-atom-krein-form.md`
- `research/grothendieck/checkers/two_label_krein_amplitude_gate.py`

The dependency-free checker verifies the indefinite determinant, the exact negative-ratio interval, and positive-amplitude witnesses of both signs.
