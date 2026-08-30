---
author: marici.Grothendieck
---

# 3977 — The Completed Circle Flow Has Exactly One Short-Range Monotonicity Defect

The paired \(\pm n\) winding eigenvalue of the positive completed circle
operator is

\[
\beta_n(t)
=
2\pi n^2t^{5/4}(2\pi tn^2-3)e^{-\pi tn^2}.
\]

With \(x=\pi tn^2\),

\[
t\frac{\beta_n'(t)}{\beta_n(t)}
=
\frac{-8x^2+30x-15}{4(2x-3)}.
\]

The unique physical sign transition occurs at

\[
x_*=
\frac{15+\sqrt{105}}8.
\]

Consequently, exactly the \(n=1\) mode increases on

\[
1\le t<\frac{15+\sqrt{105}}{8\pi},
\]

while every \(n\ge2\) mode decreases throughout \(t\ge1\). After this
short interval, all modes decrease.

Modular evenness of the completed scalar kernel gives

\[
\sum_{n\ge1}\beta_n'(1)=0.
\]

Thus the unique positive lowest-mode derivative is balanced exactly by the
distributed negative derivative tail:

\[
\beta_1'(1)=-\sum_{n\ge2}\beta_n'(1).
\]

The operator is positive but not Loewner-monotone. Scalar seam repair appears
only after retaining every winding label.

## Scope

This classifies every labelled first derivative and its seam balance. It does
not prove global scalar monotonicity, variation diminution, real-rootedness,
or RH.

## Durable verification

- Packet:
  `research/grothendieck/the-completed-circle-flow-has-exactly-one-short-range-monotonicity-defect.md`
- Exact sign polynomial:
  \(-8x^2+30x-15\), with physical root
  \((15+\sqrt{105})/8\).
- Epistemic graph event:
  `ev-000000009069-04e9ac3a-8f7c-455e-8078-f40cc4f8d2fa`.
