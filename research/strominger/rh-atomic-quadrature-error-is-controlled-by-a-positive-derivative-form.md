# Atomic quadrature error is controlled by a positive derivative form

## Question

Can the scalar sum--integral error be upgraded to an inequality on every polynomial quadratic form, preserving positivity before Gram inversion?

## Discrete and continuous forms

Fix \(x_0=\log3\), \(a>0\), and \(0<\beta<1/2\). For a polynomial \(p\), define

\[
Q_{\rm at}(p)=
\sum_{n\ge3}
\frac{|p(\log n)|^2}{n e^{2a(\log n)^\beta}}
\]

and

\[
Q_{\rm cont}(p)=
\int_{x_0}^\infty |p(x)|^2e^{-2ax^\beta}dx.
\]

Put \(F(x)=|p(x)|^2e^{-2ax^\beta}\) and \(h(t)=F(\log t)/t\). Then \(Q_{\rm at}(p)=\sum_{n\ge3}h(n)\) and \(Q_{\rm cont}(p)=\int_3^\infty h(t)dt\).

## Euler remainder

The first-order sum--integral formula gives the safe bound

\[
|Q_{\rm at}(p)-Q_{\rm cont}(p)|
\leq h(3)+\int_3^\infty|h'(t)|dt.
\]

After \(t=e^x\),

\[
\int_3^\infty|h'(t)|dt
=
\int_{x_0}^\infty e^{-x}|F'(x)-F(x)|dx.
\]

Since \(x_0>1\), one has \(x^{\beta-1}\leq1\). Using

\[
2|p(x)p'(x)|\leq |p(x)|^2+|p'(x)|^2
\]

gives

\[
|F'-F|
\leq e^{-2ax^\beta}
\left(|p'|^2+(2+2a\beta)|p|^2\right).
\]

Therefore define the positive quadratic form

\[
R(p)=
\frac{|p(x_0)|^2e^{-2ax_0^\beta}}{3}
+
\int_{x_0}^\infty e^{-x-2ax^\beta}
\left(|p'(x)|^2+(2+2a\beta)|p(x)|^2\right)dx.
\]

Then

\[
Q_{\rm cont}(p)-R(p)
\leq Q_{\rm at}(p)
\leq Q_{\rm cont}(p)+R(p).
\]

This is a quadratic-form inequality, so its finite-degree matrix representation is a genuine Loewner bound. It does not choose Hankel-entry errors independently.

## Remaining coercivity gate

The lower bound is useful only if \(R\) is relatively bounded by \(Q_{\rm cont}\) with degree-dependent constant strictly below one on the polynomial subspace relevant to the Christoffel problem. The derivative term may grow with degree. Establishing or falsifying

\[
R(p)\leq\eta_K Q_{\rm cont}(p),
\qquad \eta_K<1,
\]

is the next matrix-level test.

## Disposition

The atomic quadrature error has been converted into a positive derivative form. Matrix positivity is preserved. No inverse bound or flat-vector conclusion is claimed until relative coercivity is tested.
