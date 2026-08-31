# The resolved window tail is strictly positive by symmetric-unimodal autocorrelation

## Claim

For every prime label \(p\), with \(L=\log p>0\),

\[
 g_p=\langle BW_L,BW_{2L}\rangle>0.
\]

This uses the resolved-tail metric only.  It does not identify that metric with
the endpoint Stieltjes metric or with the oriented linking polarization.

## Source factors

The preceding exact reduction gives

\[
g_p=2\bigl(C_F(L)-C_F(3L)\bigr),
\qquad
F=K_+*\rho,
\]

where

\[
K(r)=\int_r^\infty\Phi(s)\,ds\quad(r\ge0),
\qquad
K_+(r)=\mathbf1_{[0,\infty)}(r)K(r),
\]

and the Gaussian front has

\[
\rho(q)=e^{-\pi q^2}.
\]

The completed theta kernel is positive on the open half-line.  Consequently
\(K\) is positive and strictly decreasing there.

For a real function \(h\), write

\[
A_h(a):=(h*\widetilde h)(a),
\qquad
\widetilde h(x)=h(-x).
\]

Then \(C_F=A_F\), and convolution associativity gives

\[
A_F=A_{K_+}*A_\rho.
\]

## The one-sided-tail autocorrelation is decreasing

For \(a\ge0\),

\[
A_{K_+}(a)=\int_0^\infty K(x)K(x+a)\,dx.
\]

It is even.  If \(0\le a<b\), strict decrease of \(K\) gives

\[
K(x+a)>K(x+b)
\]

for every \(x\ge0\).  Since \(K(x)>0\), integration yields

\[
A_{K_+}(a)>A_{K_+}(b).
\]

Thus \(A_{K_+}\) is nonnegative, even, and strictly decreasing on the positive
half-line.

The Gaussian autocorrelation is explicitly

\[
A_\rho(a)=2^{-1/2}e^{-\pi a^2/2},
\]

so it too is positive, even, and strictly decreasing for \(a>0\).

## Convolution preserves symmetric decrease

If \(u,v\ge0\) are even and nonincreasing on \([0,\infty)\), then \(u*v\)
is even and nonincreasing there.  One direct proof uses layer cake: every such
function is a positive superposition of centered interval indicators, and

\[
\mathbf1_{[-r,r]}*\mathbf1_{[-s,s]}
\]

is an even trapezoid nonincreasing with distance from the origin.

Strictness in the present case can be checked without invoking a general
strict-convolution theorem.  Put

\[
\gamma(a)=A_\rho(a)=2^{-1/2}e^{-\pi a^2/2}.
\]

For every centered interval of positive radius,

\[
(\mathbf1_{[-r,r]}*\gamma)(a)
 =\int_{a-r}^{a+r}\gamma(z)\,dz,
\]

and, for \(a>0\),

\[
\frac d{da}(\mathbf1_{[-r,r]}*\gamma)(a)
 =\gamma(a+r)-\gamma(a-r)<0.
\]

Here evenness interprets \(\gamma(a-r)=\gamma(|a-r|)\), and
\(|a-r|<a+r\).  The layer-cake representation of the nonzero function
\(A_{K_+}\) has positive mass on centered intervals of positive radius.
Integrating the strict inequality over those layers proves

\[
C_F=A_{K_+}*A_\rho
\]

is strictly decreasing on \((0,\infty)\).

Since \(0<L<3L\),

\[
C_F(L)>C_F(3L),
\]

and therefore

\[
\boxed{g_p>0.}
\]

## Scope

This closes the sign, but not a closed theta-series value, of the mixed
resolved window-tail scalar.  Also, because \(C_F(a)\to0\),

\[
g_p\to0\qquad(p\to\infty).
\]

Thus the mixed entry is positive but supplies no prime-uniform positive lower
bound by itself.  Arithmetic calibration of the independently oriented
boundary-Stokes block, radical descent, and full-pushout closed range remain
open.  No RH conclusion is authorized.
