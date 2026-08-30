# Aggregate Green Curvature Is One Weighted Threshold Readout

## Physical factorization

Let the three positive roots of

\[
q(x)=4x^3-28x^2+41x-9
\]

be \(r_1<r_2<r_3\). Entry 3255 established

\[
r_1<r_2<\pi<r_3
\]

and that the labelwise Green curvature is

\[
4e^{u/2-x_n}x_n(x_n-r_1)(x_n-r_2)(x_n-r_3),
\qquad x_n=\pi n^2e^{2u}.
\]

On the entire physical chart, define the positive weights

\[
w_n(u)=16e^{u/2-x_n}x_n(x_n-r_1)(x_n-r_2)>0.
\]

Then the aggregate factors exactly as

\[
L\Phi(u)
=W(u)\bigl(\mu(u)-r_3\bigr),
\]

where

\[
W(u)=\sum_{n\ge1}w_n(u)>0,
\qquad
\mu(u)=\frac{\sum_{n\ge1}w_n(u)x_n(u)}{W(u)}.
\]

## Meaning

All apparent cancellation among infinitely many labels has collapsed to one
question: is the source-weighted mean lattice scale \(\mu(u)\) below or above
the fixed algebraic threshold \(r_3\)?

The aggregate zero is exactly

\[
\mu(u)=r_3.
\]

This is a faithful positive-coordinate readout. No signed label weights remain.
The negative primitive band means only that the initial weighted mean lies
below threshold. Higher labels raise the mean and therefore advance the
aggregate crossing slightly relative to the primitive label's own crossing.

Numerically,

\[
r_3=5.063445382293672\ldots,
\]

and the aggregate crossing occurs near

\[
u=0.2386239760584707.
\]

## Sharp next conjecture and limitation

The smallest source-space theorem is that \(\mu(u)\) is strictly increasing
for \(u\ge0\). This would prove that \(L\Phi\) has exactly one sign change.
The conjecture has a direct falsifier: any \(u\) with \(\mu'(u)\le0\).

Even its proof would not establish RH. It would certify the unique source
defect that the later modular Green current must transport. The oscillatory
orientation problem remains a separate gate.
