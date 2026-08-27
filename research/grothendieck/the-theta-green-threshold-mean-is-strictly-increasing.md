# The Theta Green Threshold Mean Is Strictly Increasing

## Statement

Let \(X=\pi e^{2u}\), let \(a_n=n^2\), and use the positive weights from
entry 3260. Their weighted mean

\[
\mu(X)=\frac{\sum_n w_n(X)a_nX}{\sum_nw_n(X)}
\]

is strictly increasing for \(X\ge\pi\). Consequently the aggregate Green
curvature \(L\Phi\) has exactly one zero on \(u\ge0\), and changes sign there
from negative to positive.

## Primitive-relative coordinates

Put \(r_n=w_n/w_1\), \(R=\sum_{n\ge2}r_n\), and

\[
C=\sum_{n\ge2}(a_n-1)r_n.
\]

Then

\[
\mu(X)=X\left(1+\frac{C}{1+R}\right).
\]

For either subphysical root \(r_i\),

\[
\frac{a}{aX-r_i}<\frac1{X-r_i}.
\]

It follows directly that every logarithmic ratio derivative is negative:

\[
\frac{d}{dX}\log r_n<-(a_n-1)<0.
\]

Differentiating the mean and retaining the favorable term from \(R'<0\)
gives

\[
\mu'(X)\ge1-X|C'(X)|.
\]

## Uniform tail bound

On \(X\ge\pi\), the two subphysical factors give

\[
r_n(X)
\le
\frac73a_n^3e^{-(a_n-1)X}.
\]

The logarithmic derivative also satisfies

\[
-\frac{d}{dX}\log r_n<a_n+1.
\]

Therefore

\[
X|C'(X)|
<
\frac{7X}{3}
\sum_{n\ge2}(a_n^2-1)a_n^3e^{-(a_n-1)X}.
\]

Every summand decreases for \(X\ge\pi\). Evaluation at the endpoint, with
the \(n=2\) term separated and the remaining Gaussian tail bounded by its
first term and a geometric majorant, gives

\[
X|C'(X)|<0.568.
\]

Hence

\[
\mu'(X)>0.432.
\]

The initial mean is below \(r_3\), while \(\mu(X)\sim X\) as
\(X\to\infty\). Strict monotonicity therefore gives a unique threshold
crossing. Its numerical location is

\[
u_0=0.2386239760584707\ldots.
\]

## Explanatory content and boundary

The one-fold source geometry is now a theorem, not reconnaissance. Its force
comes from primitive dominance plus exponentially suppressed positive repair,
not pairwise total positivity: the raw two-label derivative brackets can be
negative.

This still does not orient the oscillatory transform required for RH. It
proves that modular Green transport receives exactly one canonical defect
band and no hidden later defects.

