# The first Laguerre form is exactly the defect of a two-channel phase-increment map

## Setup

Let

\[
F(x)=\int_0^\infty f(u)e^{ixu}\,du,
\qquad
X(x)=F(x)+F(-x),
\]

where \(f\) is positive. Define

\[
M_k=\int_0^\infty u^k f(u)\,du.
\]

The first completed Laguerre form is

\[
\mathcal L_1(x)=X'(x)^2-X(x)X''(x).
\]

## Same-sheet channel

The same-sheet logarithmic curvature is

\[
F(x)F''(x)-F'(x)^2
=
-\frac12
\iint
(u-v)^2f(u)f(v)e^{ix(u+v)}\,du\,dv.
\]

After adding the reflected sheet, its contribution to \(\mathcal L_1\) is

\[
\iint
(u-v)^2f(u)f(v)
\cos(x(u+v))\,du\,dv.
\]

Define the corresponding phase-increment energy

\[
R_-(x)=
\iint
(u-v)^2f(u)f(v)
[1-\cos(x(u+v))]\,du\,dv.
\]

## Opposite-sheet seam

The corrected seam contribution to \(XX''-(X')^2\) is

\[
-\iint
(u+v)^2f(u)f(v)e^{ix(u-v)}\,du\,dv.
\]

Its contribution to \(\mathcal L_1\) is therefore

\[
\iint
(u+v)^2f(u)f(v)
\cos(x(u-v))\,du\,dv.
\]

Define

\[
R_+(x)=
\iint
(u+v)^2f(u)f(v)
[1-\cos(x(u-v))]\,du\,dv.
\]

Both \(R_-\) and \(R_+\) are nonnegative.

## Exact defect identity

The two invariant trace masses satisfy

\[
\iint
\left[(u-v)^2+(u+v)^2\right]
f(u)f(v)\,du\,dv
=
4M_0M_2.
\]

Combining the same-sheet and seam channels gives

\[
\mathcal L_1(x)
=
4M_0M_2-R_-(x)-R_+(x).
\]

Thus first Laguerre positivity is exactly the contraction inequality

\[
R_-(x)+R_+(x)
\le
4M_0M_2.
\]

No oscillatory term remains outside the two phase-increment energies.

## Hilbert-space form

Using

\[
1-
\cos\theta
=
\frac12
|1-e^{i\theta}|^2,
\]

define

\[
r_-(u,v;x)=
\frac{u-v}{\sqrt2}
\sqrt{f(u)f(v)}
\left[1-e^{ix(u+v)}\right],
\]

\[
r_+(u,v;x)=
\frac{u+v}{\sqrt2}
\sqrt{f(u)f(v)}
\left[1-e^{ix(u-v)}\right].
\]

Then

\[
R_-(x)=\|r_-(x)\|_2^2,
\qquad
R_+(x)=\|r_+(x)\|_2^2.
\]

Consequently

\[
\mathcal L_1(x)
=
4M_0M_2
-
\left\|
\begin{pmatrix}
r_-(x)\\
r_+(x)
\end{pmatrix}
\right\|_2^2.
\]

This is the requested bulk-plus-seam recombination. It is an exact difference of a fixed invariant source mass and the norm of a source-defined two-channel phase-increment feature.

## Theta reconnaissance

The checker

`research/voevodsky/checkers/scout_first_laguerre_two_bulk_contraction.py`

samples the completed theta source for \(0\le x\le40\). All 161 sampled values satisfy the contraction inequality.

The smallest sampled Laguerre value occurs at \(x=40\):

\[
\mathcal L_1(40)
\approx
6.97218\times10^{-22}.
\]

The maximum sampled ratio is

\[
\frac{R_-(x)+R_+(x)}{4M_0M_2}
\approx
0.999999999999999999939.
\]

This near-saturation is expected because the Xi transform and its derivatives decay at large real frequency while the invariant source mass remains fixed.

Result:

`research/voevodsky/results/first-laguerre-two-bulk-contraction-scout.json`.

The scan is not interval certified.

## What was achieved

The trace surplus has not been discarded. It has been identified exactly as the budget from which the two phase-increment channels draw.

The first Laguerre problem is now a concrete norm bound for an explicit source map:

\[
f
\longmapsto
(r_-(x),r_+(x)).
\]

## Remaining issue

The identity does not yet prove that the map is contractive for the completed theta source. For a generic positive source, it need not be.

A constructive theta proof must derive

\[
\|r_-(x)\|_2^2+
\|r_+(x)\|_2^2
\le
4M_0M_2
\]

from modular sewing or a source operator identity.

Moreover, first Laguerre positivity alone is not sufficient for RH. The generating-level construction must replace \((u\pm v)^2\) by the complete even-power hierarchy while preserving one coherent contraction.

## Next target

Search for a unitary or partial-isometric modular sewing operator \(U_x\) on the two-copy theta carrier such that

\[
(r_-(x),r_+(x))
=
P_xU_xb,
\]

where \(b\) is a fixed bulk feature with

\[
\|b\|^2=4M_0M_2
\]

and \(P_x\) is an orthogonal projection. Such a factorization would prove the first contraction by construction and indicate how to lift it to symmetric powers.
