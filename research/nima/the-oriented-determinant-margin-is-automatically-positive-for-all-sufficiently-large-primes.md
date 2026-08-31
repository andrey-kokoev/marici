# The oriented determinant margin is automatically positive for all sufficiently large primes

## Base-Gram domination

Put

\[
c=1+M_\Phi^2>0,
\qquad
u_L=(W_L,W_{2L}).
\]

The resolved Gram is the sum of two positive Gram matrices:

\[
G_L^{\mathrm{res}}
=c\,G_L^{(0)}+G_L^{(B)},
\]

where

\[
G_L^{(0)}=\operatorname{Gram}(W_L,W_{2L}),
\qquad
G_L^{(B)}=\operatorname{Gram}(BW_L,BW_{2L}).
\]

Hence, in Loewner order,

\[
G_L^{\mathrm{res}}\ge cG_L^{(0)}.
\]

For positive two-by-two matrices, eigenvalue monotonicity gives determinant
monotonicity. Therefore

\[
\boxed{
\Delta_L^{\mathrm{res}}
=\det G_L^{\mathrm{res}}
\ge c^2\det G_L^{(0)}.
}
\]

No resolved-tail estimate is needed for this lower bound.

## Ordinary window determinant

Since \(H'=-\rho\), with \(\rho(q)=e^{-\pi q^2}\),

\[
W_t(q)
=H(q+t)-H(q-t)
=-\int_{q-t}^{q+t}\rho(s)\,ds
=-(\mathbf1_{[-t,t]}*\rho)(q).
\]

The two windows are linearly independent for every \(L>0\).  Indeed, their
Fourier transforms contain respectively

\[
\frac{\sin(2\pi L\xi)}{\pi\xi}\widehat\rho(\xi)
\quad\text{and}\quad
\frac{\sin(4\pi L\xi)}{\pi\xi}\widehat\rho(\xi),
\]

and the two sine functions are not scalar multiples.  Thus

\[
D_0(L):=\det G_L^{(0)}>0
\qquad(L>0).
\]

The entries depend continuously on \(L\), so \(D_0\) is continuous.

## Large-window asymptotics

Gaussian smoothing changes each interval indicator only in boundary layers of
bounded width.  Equivalently, using the integrable Gaussian autocorrelation in
the double-integral formula for the window pairings gives

\[
\|W_t\|_2^2=2t+O(1),
\]

and, for the nested windows,

\[
\langle W_L,W_{2L}\rangle=2L+O(1).
\]

Therefore

\[
D_0(L)
=(2L+O(1))(4L+O(1))-(2L+O(1))^2
=4L^2+O(L).
\]

In particular,

\[
D_0(L)\to\infty
\qquad(L\to\infty).
\]

Hence there exist \(L_0>0\) and \(d_0>0\) such that

\[
\Delta_L^{\mathrm{res}}
\ge c^2D_0(L)\ge d_0L^2
\qquad(L\ge L_0).
\]

## Comparison with the oriented incidence

The arithmetic incidence satisfies

\[
|\kappa_p|
\le C(\log p)p^{-1/2}e^{-Bp^2}.
\]

Thus

\[
\frac{\kappa_p^2}{4}
=o((\log p)^2).
\]

Combining this with the determinant lower bound proves that, for all
sufficiently large primes,

\[
\boxed{
\Delta_p^{\mathrm{res}}-\frac{\kappa_p^2}{4}>0.
}
\]

Therefore no asymptotic prime sequence can violate the local oriented
positivity gate.  Any failure is confined to finitely many primes.

## Superseded finite gate and current scope

The finite scalar gate has since been closed analytically. The elementary
window bound gives \(\Delta_p^{\mathrm{res}}>0.25\), while the sampled
Euler--theta series gives \(\kappa_p^2/4<0.006\) for every prime. Thus the
conditional scalar margin exceeds \(0.244\) uniformly. See
`the-euler-theta-incidence-is-uniformly-too-small-to-exhaust-the-window-area.md`.

The non-proof hostile checker
`checkers/check_rh_first_adams_oriented_margin_numeric.py` evaluates the more
conservative inequality

\[
\det G_L^{(0)}>\frac{\kappa_p^2}{4},
\]

thereby discarding both the factor \((1+M_\Phi^2)^2\ge1\) and every positive
resolved-tail contribution. It passes all 168 primes through 1000. The
smallest sampled margin occurs at \(p=2\): the ordinary determinant is
approximately \(0.420126\), the oriented cost is
\(7.496\times10^{-4}\), and their difference is approximately
\(0.419376\). Independent quadrature agrees with the closed formula on ten
hostile labels from 2 through 997. These values are numerical evidence only,
not interval-certified finite-prime closure.

More importantly, this determinant calculation remains conditional on the
typed assembly theorem putting the resolved positive form and transported
Stokes/Wronskian linking form on the same carrier.  It does not repair the
dense nonclosed range of the isolated all-prime comparison in the declared
Köthe topology.  Radical descent and full-pushout closed range remain open.
No RH conclusion is authorized.
