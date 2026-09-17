# Log-elliptic coercivity reduces each compact window to a finite Schur test

This is the non-Gram route for proving that violating situations cannot
exist.

Let the compact-window Weil operator have the source decomposition

\[
W_L=A_L+T_{P,L}+E_L,
\]

where the archimedean multiplier satisfies

\[
a(u)\ge \log(1+|u|)-C_\Gamma,
\]

`T_{P,L}` is the finite-window prime translation operator with known norm
`B_L`, and `E_L` is the endpoint/localization remainder. Let `P_U` project to
frequencies `|u|<=U` and `Q_U=I-P_U`. If

\[
\varepsilon_L(U)=\|Q_UE_LQ_U\|,
\]

then

\[
Q_UW_LQ_U\ge
\delta_L(U)Q_U,
\]

with

\[
\boxed{
\delta_L(U)=\log(1+U)-C_\Gamma-B_L-\varepsilon_L(U).}
\]

For every fixed `L`, boundedness of the finite prime packet and decay of the
finite-rank/localization tail imply `delta_L(U)>0` once `U` is sufficiently
large. Thus a negative direction cannot live entirely at high frequency.

Write the resulting block operator as

\[
W_L=\begin{pmatrix}W_{00}&W_{01}\\W_{10}&W_{11}\end{pmatrix},
\qquad W_{11}\ge\delta_L(U)I.
\]

Then

\[
\boxed{
W_L\succeq0
\iff
W_{00}-W_{01}W_{11}^{-1}W_{10}\succeq0.}
\]

Therefore every violation on a fixed compact logarithmic window produces a
negative vector in a finite low-frequency Schur complement, provided `P_U`
is chosen finite dimensional (for example through the interval eigenbasis).
This is an actual impossibility reduction: high-frequency violations are
excluded by a source estimate, rather than sampled and hoped absent.

## Quantitative coupling bound

A simpler sufficient condition avoiding exact inversion is

\[
W_{00}\ge m_L I,
\qquad
\|W_{01}\|^2\le m_L\delta_L(U).
\]

Indeed `W_{11}^{-1}<=delta_L(U)^{-1}I`, so the Schur complement is bounded
below by

\[
\left(m_L-\frac{\|W_{01}\|^2}{\delta_L(U)}\right)I.
\]

## Constants already available

Prior source estimates close the first two scalar bounds. Globally,

\[
\operatorname{Re}\psi(1/4+iu/2)
\ge \log(u/2)-3/2\qquad(u>0),
\]

and the alternative uniform comparison

\[
\left|\operatorname{Re}\psi(1/4+iu/2)-\log(1+|u|)\right|
\le4+\tfrac12\log20
\]

is elementary. For logarithmic support `[-L,L]`, only `n<=e^{2L}` occurs and

\[
B_L\le \kappa\sum_{n\le e^{2L}}\frac{\Lambda(n)}{\sqrt n}
\le4\kappa Le^L.
\]

This proves fixed-window eventual coercivity, but forces a mode threshold
roughly

\[
\log U>C_\Gamma+4\kappa Le^L,
\]

which is doubly exponential in `L`. It is therefore not a viable global
finite-certificate bound.

## What actually remains

The analytic-order question is closed. The obstruction is loss of arithmetic
cancellation when the prime translations are bounded by absolute coefficient
mass. The next estimate must control the prime trigonometric translation
operator uniformly on the high-mode subspace by substantially less than
`Le^L`—through almost orthogonality, a large-sieve estimate, or an Euler
factorization. Average cancellation over modes is insufficient.

Endpoint/localization coupling and the finite low-mode Schur complement still
need bounds after such an arithmetic improvement. To conclude the global
Gaussian/Loewner statement, constants must then remain controlled as `L`
grows and compactly supported functions must form a cancellation-preserving
form core.
