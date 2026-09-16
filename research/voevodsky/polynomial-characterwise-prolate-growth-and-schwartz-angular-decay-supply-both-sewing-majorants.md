# Polynomial characterwise prolate growth and Schwartz angular decay supply both sewing majorants

## Counting hypothesis

Choose a length function \(|\chi|\) on the discrete angular dual. Assume shell counting

\[
\#\{\chi:n\le|\chi|<n+1\}
\le
C_{ang}(1+n)^{q-1}.
\]

Here \(q\) is the polynomial growth dimension of the angular dual.

## Prolate hypothesis

Assume the characterwise transition mass satisfies

\[
\mathfrak p_{\Lambda,S}(\chi)
\le
C_S(1+L)(1+|\chi|)^d,
\qquad
L=\log\Lambda.
\]

Smooth observer packets supply, for every \(M\), a uniform angular estimate

\[
w_G(\chi)
\le
C_{G,M}(1+|\chi|)^{-M}.
\]

## Strong-feature majorant

A Hilbert--Schmidt leg controlled by the square root of transition mass has bound

\[
M_G^{str}(\chi)
\le
C(1+L)^{1/2}
(1+|\chi|)^{d/2-M}.
\]

Its square satisfies

\[
(M_G^{str}(\chi))^2
\le
C^2(1+L)
(1+|\chi|)^{d-2M}.
\]

The shell sum converges when

\[
q-1+d-2M<-1,
\]

that is,

\[
\boxed{2M>d+q.}
\]

Thus the strong-feature route obtains a square-summable angular majorant from any Schwartz order satisfying this inequality.

## Minimal-product majorant

For the trace-class product, a direct transition estimate gives

\[
N_G^{prod}(\chi)
\le
C(1+L)
(1+|\chi|)^{d-M}.
\]

The angular sum converges when

\[
q-1+d-M<-1,
\]

or

\[
\boxed{M>d+q.}
\]

This supplies the summable \(L^1\) majorant required by the minimal-product route.

## Tail bounds

Let

\[
r_{str}=2M-d-q>0.
\]

Then the strong angular tail beyond shell \(N\) obeys

\[
\sum_{|\chi|>N}
(M_G^{str}(\chi))^2
\le
C'(1+L)(1+N)^{-r_{str}}.
\]

Similarly, with

\[
r_{prod}=M-d-q>0,
\]

one has

\[
\sum_{|\chi|>N}
N_G^{prod}(\chi)
\le
C''(1+L)(1+N)^{-r_{prod}}.
\]

These bounds make removal of the finite angular projection quantitative.

## Regulator dependence

The factor \(1+L\) belongs to radial prolate growth. For a completed sewing limit, one needs either:

1. recentered leg convergence that removes this growth before taking \(L\to\infty\); or
2. a correlated angular cutoff \(N(L)\) whose tail bounds dominate the radial factor.

For example, the strong tail vanishes if

\[
(1+L)(1+N(L))^{-r_{str}}
\longrightarrow0.
\]

The product route has the analogous condition with \(r_{prod}\).

## Consequence

Once the characterwise prolate exponent \(d\) is established, smooth observer packets automatically supply both angular majorants:

- choose \(M>(d+q)/2\) for the strong route;
- choose \(M>d+q\) for the product route.

The remaining source estimate is therefore the localized characterwise Hankel bound determining \(d\), together with radial recentering that controls the factor \(1+L\).
