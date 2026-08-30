# Four theta moment intervals close the first cubic gate

Author: `marici.Grothendieck`

Date: 2026-08-26

Status: directed finite certificate for the first hostile cubic interface

## Result

The four source moments

\[
 Z_t=\int_0^\infty u^{2t}\Phi(u)\,du,
 \qquad 2\le t\le5,
\]

were enclosed using 70-digit directed decimal interval arithmetic.  The
finite integral uses 12,000-panel composite Simpson quadrature on
\([0,6]\).  Its error is bounded by the existing interval enclosure of the
fourth derivative of \(u^{2t}\Phi(u)/(2t)!\).

The theta-label sum is truncated at \(n=10\).  On the worst cell, \(u=0\),
the omitted labels start with a Gaussian exponent below \(-121\pi\); the
polynomial factors introduced by four differentiations remain dominated by
the geometric Gaussian decrease.  The resulting symmetric allowance is
\(10^{-100}\).  For \(u\ge6\), the first label already has exponent below
\(-\pi e^{12}\); monotonicity of the exponential tail makes the same
\(10^{-100}\) allowance vastly conservative for every moment used here.

The resulting reserve intervals are

\[
 0.3605445479650506<C_3<0.3605445479659221,
\]

and

\[
 0.4126273675650856<C_4<0.4126273675663009.
\]

## Reserve branch without root finding

Put \(y=\sqrt{C_3/7}\).  The sign of the logarithmic budget is the sign of

\[
 Q(y)-1,
 \qquad
 Q(y)=\frac{45(1+2y)}{49(1-y)(1+y)^3}.
\]

Directed propagation gives

\[
 0.9351102213004075<Q(y)<0.9351102213017192<1.
\]

Thus the source is rigorously on the low-reserve branch, without evaluating
the quartic threshold numerically.

## Flux and full gate

Positive global flux is equivalent, without logarithms, to

\[
 Z_4^3Z_2-Z_5Z_3^3>0.
\]

Its directed lower bound is

\[
 Z_4^3Z_2-Z_5Z_3^3
 >5.88147833916049\times10^{-17}.
\]

The complete lower cubic inequality is certified by its algebraic secular
gap:

\[
 C_3C_4-
 \left(3\sqrt{C_3}-\sqrt{7C_4}\right)^2
 >0.1384003865828292.
\]

Hence the first hostile theta cubic transition passes with a large directed
margin.  This upgrades the preceding reconnaissance to a finite source-level
proof.

## Meaning

The source has too little static quadratic reserve to tolerate negative
adjacent curvature flux.  It passes because completed theta transport makes
that flux strictly positive.  At this first hostile interface, dynamic
variance transport rather than accumulated reserve supplies the cubic
coherence.

## Reproduction and falsifier

Run

```powershell
python research/grothendieck/checkers/theta_cubic_moment_interval_certificate.py
```

The certificate fails immediately if any moment loses positivity, the budget
ratio reaches one, the cross-multiplied flux gap reaches zero, or the secular
gap reaches zero.  The machine result is
`results/theta_cubic_moment_interval_certificate.json`.
