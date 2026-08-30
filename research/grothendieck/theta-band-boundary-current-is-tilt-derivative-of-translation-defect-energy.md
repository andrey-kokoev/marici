# Theta band boundary current is tilt derivative of translation-defect energy

## Bounded question

What invariant does the first surviving conditional adjacent-band requirement
actually measure after the complete labelled theta source is assembled?

## Aggregate correlation after labelled assembly

Let

\[
f_a(x)=e^{ax}\Phi(|x|),
\]

where the completed density is assembled from all retained arithmetic labels
before scalar evaluation. Define its translation correlation

\[
W_a(D)
=
\int_{\mathbb R}f_a(x)f_a(x-D)\,dx.
\]

This is the aggregate of the labelled conditional weights. Differentiation in
the tilt parameter gives the first-moment current

\[
J_a(D)=\partial_aW_a(D).
\]

The first boundary requirement from the conditional adjacent-band residual is

\[
J_a(0)\ge J_a(L),
\qquad
L=\frac{\pi}{b}.
\]

## Translation-defect identity

Define

\[
\mathcal C_a(D)
=
\frac12
\int_{\mathbb R}
\left|f_a(x)-f_a(x-D)\right|^2\,dx.
\]

Translation preserves the norm, so

\[
\mathcal C_a(D)=W_a(0)-W_a(D)\ge0.
\]

Consequently,

\[
J_a(0)-J_a(D)
=
\partial_a\mathcal C_a(D).
\]

Thus the required band-boundary orientation is exactly

\[
\partial_a\mathcal C_a(L)\ge0.
\]

## What Gram positivity does and does not prove

The correlation representation proves

\[
\mathcal C_a(D)\ge0
\]

for every source and every shift. But positivity of a function does not orient
its derivative in \(a\). The missing statement is monotonic growth of
translation distinguishability under the Mellin tilt.

Reflection of the even completed source gives

\[
\mathcal C_{-a}(D)=\mathcal C_a(D).
\]

Hence

\[
\partial_a\mathcal C_a(D)\big|_{a=0}=0.
\]

The desired outer-sector sign would follow from convexity of
\(\mathcal C_a(D)\) in \(a\), but that convexity is not supplied by the Gram
identity and must be derived or falsified from the theta source.

## Label-faithfulness boundary

The aggregate defect is formed only after the complete labelled Gram sum.
It does not prove the stronger labelwise inequalities

\[
J_{nm}(0)\ge J_{nm}(L).
\]

A successful scalar cancellation theorem may use the aggregate identity, but
any reconstruction or unique-pairing claim still requires the labelled
packet. No cross-label cancellation is being reinterpreted as labelwise
positivity.

## Result

The first surviving continuous-band gate is not an arbitrary conditional
moment inequality. It is the tilt derivative of a canonical translation-defect
energy.

This supplies a sharply typed next theorem:

\[
\partial_a
\left[
\frac12
\left\|
e^{a\cdot}\Phi(|\cdot|)
-
\tau_L\!\left(e^{a\cdot}\Phi(|\cdot|)\right)
\right\|_2^2
\right]
\ge0
\]

for \(a>0\) and \(L>0\), if true for the completed theta source.

The smallest hostile test is curvature at the symmetric point:

\[
\partial_a^2\mathcal C_a(L)\big|_{a=0}<0.
\]

Such a negative curvature would force the boundary current to have the wrong
sign for small positive tilt and close this route.

## Sharp falsifier

Find \(L>0\) and \(a>0\) for which

\[
\partial_a\mathcal C_a(L)<0.
\]

The special local falsifier is negative second derivative at \(a=0\).
