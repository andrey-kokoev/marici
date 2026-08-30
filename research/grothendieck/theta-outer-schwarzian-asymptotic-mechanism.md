# Large-source asymptotic mechanism for the outer Schwarzian

## Completed logarithmic derivative

Put

\[
r=\sqrt x,
\qquad
s=\frac12+r.
\]

Then

\[
H(x)=\frac{s(s-1)}{2s-1}\frac{\xi'(s)}{\xi(s)}
=\left(\frac r2-\frac1{8r}\right)\frac{\xi'(s)}{\xi(s)}.
\]

For \(s>1\),

\[
\frac{\xi'}{\xi}(s)
=\frac1s+\frac1{s-1}
-\frac12\log\pi
+\frac12\psi(s/2)
-\sum_{n\ge2}\frac{\Lambda(n)}{n^s}.
\]

The prime-power series is absolutely convergent. Stirling expansion of the
digamma term gives the leading behavior

\[
\frac{\xi'}{\xi}(s)
=\frac12\log\frac r{2\pi}+O(r^{-1}),
\]

and therefore

\[
\boxed{
H(x)=\frac r4\log\frac r{2\pi}+O(\log r).
}
\]

## Exact completion cancellation

The apparent rational remainder is actually absent. If

\[
A(s)=\frac{s(s-1)}{2s-1}=\frac r2-\frac1{8r},
\]

then

\[
A(s)\left(\frac1s+\frac1{s-1}\right)=1.
\]

Hence, with

\[
g(s)=\frac12\left(\psi(s/2)-\log\pi\right),
\qquad
P(s)=\sum_{n\ge2}\frac{\Lambda(n)}{n^s},
\]

the completed response has the exact decomposition

\[
\boxed{
H(x)=1+A(s)g(s)-A(s)P(s).
}
\]

Thus constants aside, the outer geometry is exactly

\[
\text{completed-gamma geometry}
\;-
\text{prime-power perturbation}.
\]

This changes the proof architecture. Define

\[
H_\Gamma(x)=1+A(s)g(s),
\qquad
H_{\mathbb P}(x)=-A(s)P(s).
\]

Rather than bounding a mixed rational--Stirling--prime remainder around the
coarse leading model, one can first attack the exact polygamma statement

\[
\mathcal N(H_\Gamma)(x)>0
\]

on a ray, and then dominate the exponentially small derivatives of
\(H_{\mathbb P}\). The quarter-centered prefactor is therefore doing more
than locating the critical boundary: it algebraically absorbs both completed
poles.

## Hostile baseline falsifier

The exact gamma baseline is not globally positive. A dependency-free scan,
using recurrence to digamma argument at least (24) followed by an eight-term
differentiated Bernoulli expansion, found:

- (H_\Gamma'<0) near the critical edge, with its last sampled nonpositive
  value between (x=6.5466) and (x=6.6096);
- \(\mathcal N(H_\Gamma)<0\) on an intermediate window, reaching about
  \(-8.67\times10^{-4}\) near \(x=2.14\); and
- the last sampled Schwarzian sign transition between \(x=89.91\) and
  \(x=90.78\), after which the logarithmic scan through \(10^8\) stayed
  positive.

These are reconnaissance brackets, not certified roots or intervals. They
falsify any claim that gamma geometry alone explains the complete outer ray.
In particular, the completed theta response has positive sampled Schwarzian
at \(x=10\), where the isolated gamma baseline is negative: the prime-power
sector is not merely an error term on the intermediate ray. It participates
constructively in the completed sign before becoming a perturbation in the
far regime.

This produces a sharper division of labor:

\[
\begin{array}{c|c}
\text{compact/intermediate ray} & \text{inseparable gamma--prime coupling}\\
\text{far ray} & \text{positive gamma baseline plus small prime perturbation}
\end{array}
\]

The derivative form of the remainder must be bounded through third
\(x\)-derivative before this becomes a proof of the Schwarzian sign.

## Exact leading Schwarzian

Let

\[
h_0(x)=\frac r4L,
\qquad
L=\log\frac r{2\pi}.
\]

Since \(\partial_x=(2r)^{-1}\partial_r\),

\[
h_0'=\frac{L+1}{8r},
\]

\[
h_0''=-\frac{L}{16r^3},
\]

and

\[
h_0'''=\frac{3L-1}{32r^5}.
\]

Consequently

\[
\boxed{
2h_0'h_0'''-3h_0''^2
=\frac{3L^2+4L-2}{256r^6}
=\frac{3L^2+4L-2}{256x^3}.
}
\]

The numerator polynomial is positive when

\[
L>\frac{-2+\sqrt{10}}3.
\]

Equivalently,

\[
\boxed{
x>x_0:=
4\pi^2\exp\!\left(\frac{2(-2+\sqrt{10})}{3}\right)
\approx85.7.
}
\]

Thus the leading completed-gamma geometry has strictly positive Schwarzian
throughout the far outer ray.

## Comparison with reconnaissance

At \(x=300\), the leading expression is approximately the full observed
Schwarzian numerator \(7.44\times10^{-10}\). This explains why the margin
decays like \(x^{-3}\) times a logarithmic polynomial and why the far ray was
the weakest sampled region.

Near \(x=100\), the leading polynomial has only recently become positive, so
algebraic completion corrections remain quantitatively important. The
asymptotic theorem should therefore begin at a conservatively larger explicit
threshold, leaving a compact interval for separate certification.

## Required remainder theorem

Write

\[
H=h_0+E.
\]

The exact Schwarzian numerator decomposes as

\[
\begin{aligned}
\mathcal N(H)={}&\mathcal N(h_0)
+2h_0'E'''+2E'h_0'''+2E'E'''\\
&-6h_0''E''-3E''^2.
\end{aligned}
\]

A sufficient far-ray theorem is therefore

\[
\mathcal N(h_0)
>
2|h_0'E'''|+2|E'h_0'''|+2|E'E'''|
+6|h_0''E''|+3|E''|^2.
\]

Before the exact cancellation above is used, the coarse remainder appears to
have three source sectors:

1. rational completion terms from \(1/s+1/(s-1)\) and
   \(r/2-1/(8r)\);
2. the directed Stirling remainder of \(\psi(s/2)\); and
3. the prime-power tail and its derivatives, bounded absolutely by the
   leading \(2^{-s}\) scale.

The first sector cancels identically in the exact completed decomposition.
This gives a finite proof contract: derive explicit bounds for
\(E',E'',E'''\) and close the displayed inequality beyond one chosen
threshold \(x_1\). No zero locations occur.

## Eventual positivity theorem

Standard differentiated Stirling asymptotics give, with \(r=\sqrt x\),

\[
E'=O(r^{-2}\log r),
\qquad
E''=O(r^{-4}\log r),
\qquad
E'''=O(r^{-6}\log r).
\]

These deliberately loose bounds include the rational completion terms. The
prime-power sector is much smaller. For every fixed \(k\),

\[
\left|
\frac{d^k}{ds^k}\frac{\zeta'}{\zeta}(s)
\right|
\le
\sum_{n\ge2}\frac{(\log n)^{k+1}}{n^s}
=O_k(2^{-s})
\qquad(s\to+\infty).
\]

After conversion by

\[
\partial_x=\frac1{2r}\partial_s,
\]

this remains exponentially smaller than every displayed algebraic term.

Substitution into the exact remainder expansion yields

\[
\boxed{
\mathcal N(H)
=\frac{3L^2+4L-2}{256r^6}
+O\!\left(\frac{(1+L)^2}{r^7}\right)
+O\!\left(2^{-r}r^M\right)
}
\]

for some fixed harmless integer \(M\). Since the leading numerator is
asymptotic to \(3L^2/(256r^6)>0\), there exists a finite source-derived
\(x_1\) such that

\[
\boxed{
2H'(x)H'''(x)-3H''(x)^2>0
\qquad(x\ge x_1).
}
\]

This proves eventual outer rank-two positivity without RH or zero locations.
It is an asymptotic theorem, not yet an explicit numerical certificate: the
big-\(O\) constants must be made directed to state a concrete \(x_1\).

## Explicit prime-tail bound template

For a directed version, use \(\Lambda(n)\le\log n\). When
\(s>m/\log2\), the function \((\log t)^m t^{-s}\) decreases for \(t\ge2\),
and

\[
\sum_{n\ge2}\frac{(\log n)^m}{n^s}
\le
\frac{(\log2)^m}{2^s}
+\int_2^\infty\frac{(\log t)^m}{t^s}\,dt.
\]

Writing \(a=s-1\), the integral is elementary:

\[
\boxed{
\int_2^\infty\frac{(\log t)^m}{t^s}\,dt
=2^{1-s}
\sum_{j=0}^m
\frac{m!}{(m-j)!}
\frac{(\log2)^{m-j}}{(s-1)^{j+1}}.
}
\]

This bounds every prime derivative required by \(E',E'',E'''\) using only
rational operations, \(\log2\), and \(2^{-s}\). The remaining explicit work
is a directed Stirling remainder through the corresponding digamma order.

For the sharpened decomposition, no chain-rule ambiguity remains. The needed
prefactor derivatives are

\[
A'=\frac1{4r}+\frac1{16r^3},
\quad
A''=-\frac1{8r^3}-\frac3{32r^5},
\quad
A'''=\frac3{16r^5}+\frac{15}{64r^7},
\]

while, writing \(P_j=d^jP/ds^j\),

\[
P_x=\frac{P_1}{2r},
\]

\[
P_{xx}=\frac{P_2}{4r^2}-\frac{P_1}{4r^3},
\]

and

\[
P_{xxx}
=\frac{P_3}{8r^3}-\frac{3P_2}{8r^4}
+\frac{3P_1}{8r^5}.
\]

Leibniz's rule now turns the elementary prime-tail bounds into explicit
bounds for all three derivatives of \(H_{\mathbb P}=-AP\). The remaining
non-elementary sign question is isolated entirely in the exact polygamma
baseline \(H_\Gamma\).

## Directed Binet remainder

The polygamma baseline can be enclosed without a formally differentiated
asymptotic series. For \(q>0\), Binet's formula gives

\[
\psi(q)=\log q-\frac1{2q}+R(q),
\]

where

\[
R(q)
=-2\int_0^\infty
\frac{t}{t^2+q^2}\,
\frac{dt}{e^{2\pi t}-1}.
\]

Writing

\[
\frac1{t^2+q^2}
=\frac1{(q-it)(q+it)},
\]

Leibniz differentiation and \(|q\pm it|\ge q\) give

\[
\left|
\frac{d^m}{dq^m}\frac1{t^2+q^2}
\right|
\le
\frac{m!(m+1)}{q^{m+2}}.
\]

Since

\[
\int_0^\infty\frac{t}{e^{2\pi t}-1}\,dt
=\frac1{24},
\]

we obtain the directed all-order estimate

\[
\boxed{
|R^{(m)}(q)|
\le
\frac{m!(m+1)}{12q^{m+2}}.
}
\]

In the completed-gamma response,

\[
q=\frac s2=\frac{r+1/2}{2},
\qquad
g(s)=\frac12\left(\psi(q)-\log\pi\right).
\]

Split

\[
g=g_0+\rho,
\qquad
g_0=\frac12\left(\log\frac q\pi-\frac1{2q}\right),
\qquad
\rho=\frac12R(q).
\]

Because \(dq/ds=1/2\),

\[
\boxed{
\left|\frac{d^m\rho}{ds^m}\right|
\le
\frac{m!(m+1)}{24\,2^m q^{m+2}}
\qquad(m=0,1,2,3).
}
\]

Converting these bounds by

\[
\partial_x=\frac1{2r}\partial_s
\]

and applying Leibniz's rule to \(A(s)\rho(s)\) gives explicit bounds
for its first three \(x\)-derivatives. No Bernoulli truncation, numerical
differentiation, or zero data enters.

## Revised explicit far-ray certificate

Let

\[
H_0(x)=1+A(s)g_0(s),
\qquad
E(x)=A(s)\rho(s)-A(s)P(s).
\]

Then \(H=H_0+E\), where \(H_0\) and its first three derivatives are
elementary rational--logarithmic expressions. The Binet bounds direct the
gamma part of \(E',E'',E'''\), and the prime-tail formula directs the prime
part.

The exact sufficient inequality is

\[
\mathcal N(H_0)
>
2|H_0'E'''|
+2|E'H_0'''|
+2|E'E'''|
+6|H_0''E''|
+3|E''|^2.
\]

Every term is now bounded by elementary expressions in \(r\), \(q\),
\(\log(q/\pi)\), and \(2^{-s}\). The remaining task is a one-variable
inequality on a chosen ray \(r\ge r_1\), rather than a special-function
remainder problem.

## Directed-budget reconnaissance

The companion checker evaluates the exact elementary baseline and the
directed Binet-plus-prime error budget at selected radii. It finds:

\[
\begin{array}{c|c|c|c}
r & \mathcal N(H_0) & \text{error budget} & \text{safety factor}\\ \hline
10 & 1.0924\times10^{-9} & 1.4511\times10^{-8} & 0.075\\
20 & 4.0263\times10^{-10} & 2.2273\times10^{-11} & 18.08\\
32 & 4.5262\times10^{-11} & 6.4331\times10^{-13} & 70.36\\
50 & 4.7991\times10^{-12} & 2.2188\times10^{-14} & 216.3\\
100 & 1.2517\times10^{-13} & 1.1117\times10^{-16} & 1125.9
\end{array}
\]

The point \(r=20\), equivalently \(x=400\), is therefore the first
conservative candidate threshold in this scan. The prime contribution is
already much smaller than the gamma remainder there and becomes negligible
rapidly.

Each error formula is a directed analytic bound, but the displayed baseline
and comparison use ordinary floating arithmetic at isolated points.
Accordingly this is threshold reconnaissance, not a continuum certificate.
The exact remaining theorem is:

\[
\boxed{
\mathcal N(H_0)(r)-\mathcal E(r)>0
\qquad(r\ge20).
}
\]

A monotonic-ratio proof or a directed interval enclosure on a finite initial
segment followed by monotonic domination would turn \(x_1=400\) into an
explicit far-ray theorem.

A 10,000-point logarithmic scan on \(20\le r\le10^4\) finds the safety factor
strictly increasing at every sampled step. Its sampled logarithmic slope

\[
\frac{d\log(\mathcal N(H_0)/\mathcal E)}{d\log r}
\]

stays between approximately \(2.1276\) and \(3.5396\). Thus even the rescaled
quantity

\[
r^{-2}\frac{\mathcal N(H_0)}{\mathcal E}
\]

is increasing throughout the reconnaissance grid. This suggests a robust
two-part continuum proof:

1. direct the short initial interval \(20\le r\le32\), where the endpoint
   safety factors are already \(18.08\) and \(70.36\); and
2. prove a coarse lower bound of logarithmic slope \(2\) for \(r\ge32\).

This sampled slope is diagnostic only. It predeclares the monotonicity target
and makes any future interval proof hostile: a single nonpositive derivative
box falsifies the proposed continuum closure.

## Exact elementary baseline theorem on \(r\ge20\)

The elementary baseline simplifies exactly to

\[
\boxed{
H_0(r)
=\frac34+\frac1{8r}
+\left(\frac r4-\frac1{16r}\right)L,
\qquad
L=\log\frac{2r+1}{4\pi}.
}
\]

Its Schwarzian numerator is

\[
\mathcal N(H_0)
=c_0(r)+c_1(r)L+c_2(r)L^2,
\]

with rational coefficients. Using the common positive denominator
\(4096r^{10}(r+1/2)^2\), the first two numerators are

\[
\begin{aligned}
p_0(r)={}&
3+18r+15r^2-164r^3-364r^4-64r^5-32r^6,\\
p_1(r)={}&
-3-15r-48r^2-104r^3-128r^4+16r^5+64r^6,
\end{aligned}
\]

while

\[
c_2(r)
=\frac{3+72r^2+48r^4}{4096r^{10}}>0.
\]

For \(r\ge20\), \(p_1(r)>0\): each of its five negative monomials is
bounded in magnitude by one copy of \(r^6\), while its leading term is
\(64r^6\). Hence \(c_1,c_2>0\), so the quadratic is strictly increasing for
\(L\ge0\).

Moreover \(L>1\) on this ray. Indeed, using
\(\pi<22/7\) and \(e<3\),

\[
4\pi e<\frac{264}{7}<41\le2r+1.
\]

It therefore suffices to evaluate at \(L=1\). Exact reduction gives

\[
\left.\mathcal N(H_0)\right|_{L=1}
=
\frac{
3+24r-48r^2-784r^3-1632r^4+320r^6
}{
16384r^{10}(r+1/2)^2
}.
\]

For \(r\ge20\), the three negative terms are bounded respectively by
\(r^6,r^6,5r^6\). Consequently the numerator is at least

\[
(320-7)r^6+24r+3>0.
\]

Thus

\[
\boxed{
\mathcal N(H_0)(r)>0
\qquad(r\ge20).
}
\]

This is an exact continuum theorem for the elementary archimedean baseline.
The remaining \(x\ge400\) task is only to dominate the directed Binet and
prime perturbation budgets uniformly by this positive rational--logarithmic
margin.

## Uniform perturbation closure on the far ray

The perturbation task also closes with deliberately rounded constants.  Put

\[
H=H_0+E,
\]

where \(E\) is the sum of the Binet remainder and the prime-power term.  Direct
substitution of

\[
|\partial_s^m\rho|
\le \frac{m!(m+1)}{24\,2^m q^{m+2}},
\qquad q=\frac{r+1/2}{2},
\]

and of the geometric majorant for \((-\zeta'/\zeta)^{(m)}(s)\), followed by
the chain rule \(d/dx=(2r)^{-1}d/dr\), gives, for \(r\ge20\),

\[
\boxed{
|E'|\le\frac1{8r^3},\qquad
|E''|\le\frac9{32r^5},\qquad
|E'''|\le\frac7{8r^7}.
}
\]

These are termwise bounds: no cancellation between gamma and prime sectors
is used.  For the prime majorant one uses \(\log2<1\),
\((s-1)^{-1}\le40/(39r)\), and the fact that every needed
\(r^k2^{-r}\) is decreasing from \(r=20\) onward.  The exact affine-in-\(L\)
jet extraction for \(H_0\), recorded by the companion checker, similarly
gives

\[
\boxed{
|H_0'|\le\frac{L}{4r},\qquad
|H_0''|\le\frac{L}{16r^3},\qquad
|H_0'''|\le\frac{3L}{32r^5}.
}
\]

Here the constant terms are absorbed using \(L>1\).  Each displayed estimate
reduces, after clearing the positive denominators, to domination of lower
monomials by the leading monomial at \(r=20\).

Consequently the full Schwarzian-numerator perturbation satisfies

\[
\begin{aligned}
|\mathcal N(H)-\mathcal N(H_0)|
&\le
2|H_0'E'''|+2|E'H_0'''|+2|E'E'''|
+6|H_0''E''|+3|E''|^2\\
&\le \frac{145L}{256r^8}+\frac{467}{1024r^{10}}.
\end{aligned}
\]

The logarithm obeys \(L\le r/16\) on this ray: the inequality holds at
\(r=20\), and the derivative of
\(r/16-\log((2r+1)/(4\pi))\) is positive there and thereafter.  Hence

\[
|\mathcal N(H)-\mathcal N(H_0)|
\le \frac{145}{4096r^7}+\frac{467}{1024r^{10}}.
\]

On the other hand, the preceding exact baseline proof and
\((r+1/2)^2\le(41r/40)^2\) give

\[
\mathcal N(H_0)
\ge
\frac{313\cdot1600}{16384\cdot1681}\frac1{r^6}.
\]

At \(r=20\) the coefficient on the last lower bound exceeds the two error
coefficients after conversion to \(r^{-6}\), and the discrepancy only grows
with \(r\).  Therefore

\[
\boxed{
\mathcal N(H)(x)>0
\qquad (x=r^2\ge400).
}
\]

This is the explicit far-ray rank-two theorem.  It is not RH: the compact
interval \(1/4<x<400\), and then the passage from rank two to all Loewner
ranks, remain open.

Exact extraction artifacts:

- checkers/theta_far_schwarzian_exact_log_quadratic.py
- results/theta-far-schwarzian-exact-log-quadratic.json

Artifacts:

- checkers/theta_far_schwarzian_directed_budget.py
- results/theta-far-schwarzian-directed-budget.json

## Revised global rank-two architecture

1. Prove the exact polygamma baseline \(\mathcal N(H_\Gamma)>0\) on a far
   ray, then dominate the prime-power perturbation by directed exponential
   bounds. The rational completion sector is already gone exactly.
2. Certify the compact interval \([1/4,x_1]\) directly from the completed
   theta source.
3. Use Schwarzian nonnegativity and the concave-length theorem to obtain every
   separated rank-two Loewner determinant on \((1/4,\infty)\).

This proves rank two only; it does not prove full Loewner positivity or RH.
