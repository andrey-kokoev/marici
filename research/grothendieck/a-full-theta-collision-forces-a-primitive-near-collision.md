# A Full Theta Collision Forces a Primitive Near-Collision

## Primitive--tail split

On the positive chamber, write

\[
\Phi(u)=\phi_1(u)+\tau(u),
\]

with the uniform pointwise estimate

\[
0<\tau(u)<\delta\phi_1(u),
\qquad
\delta=0.006001.
\]

For a support endpoint \(L>0\), define primitive masses

\[
Z_0(L)=\int_0^L\phi_1(u)\,du,
\qquad
Z_1(L)=\int_0^L u\phi_1(u)\,du.
\]

Define the primitive collision coordinates

\[
C_1(L,x)=\int_0^L\phi_1(u)\cos(xu)\,du,
\]

\[
M_1(L,x)=\int_0^L u\phi_1(u)\sin(xu)\,du.
\]

The corresponding tail coordinates are \(C_\tau\) and \(M_\tau\).

## Exact perturbation bounds

Pointwise dominance gives

\[
|C_\tau(L,x)|
\le
\int_0^L\tau(u)\,du
<
\delta Z_0(L),
\]

and

\[
|M_\tau(L,x)|
\le
\int_0^L u\tau(u)\,du
<
\delta Z_1(L).
\]

These estimates are uniform in \(L\) and \(x\). They make no
order-preservation claim for oscillatory transforms.

## Collision localization theorem

A double-zero collision of the full truncated theta transform satisfies

\[
C_1+C_\tau=0,
\qquad
M_1+M_\tau=0.
\]

Therefore every full collision must obey both inequalities

\[
\frac{|C_1(L,x)|}{Z_0(L)}<\delta,
\qquad
\frac{|M_1(L,x)|}{Z_1(L)}<\delta.
\]

Thus the infinite winding-label problem has been localized to a simultaneous
\(0.6001\%\) near-collision of one explicit primitive
polynomial--Gaussian transform.

Equivalently, define the normalized primitive reserve

\[
\varepsilon_1(L,x)
=
\max\left\{
\frac{|C_1(L,x)|}{Z_0(L)},
\frac{|M_1(L,x)|}{Z_1(L)}
\right\}.
\]

Then

\[
\varepsilon_1(L,x)\ge\delta
\]

excludes a full theta collision at \((L,x)\).

## Incomplete-gamma form

Put

\[
b=\pi e^{2L},
\qquad
a=\frac54+\frac{ix}{2}.
\]

The primitive half-transform is

\[
H_{1,L}(x)
=
\pi^{-1/4-ix/2}
\int_\pi^b
t^{a-1}(2t-3)e^{-t}\,dt.
\]

Using incomplete-gamma recurrence,

\[
\int_\pi^b
t^{a-1}(2t-3)e^{-t}\,dt
=
(2a-3)\left(\gamma(a,b)-\gamma(a,\pi)\right)
-
2\left(b^ae^{-b}-\pi^ae^{-\pi}\right).
\]

Moreover,

\[
C_1(L,x)=\operatorname{Re}H_{1,L}(x),
\qquad
M_1(L,x)=-\operatorname{Re}\partial_xH_{1,L}(x).
\]

The remaining collision search is therefore a two-coordinate
incomplete-gamma reserve problem, not an infinite theta-label problem.

## What remains

A global bound \(\varepsilon_1\ge\delta\) cannot be asserted without further
analysis: both primitive transform coordinates decay along high-frequency
sequences. The correct proof must combine:

1. compact-region control of the normalized incomplete-gamma reserve;
2. endpoint asymptotics at high frequency;
3. a uniform transition between those regimes as \(L\) varies.

The smallest falsifier is an \((L,x)\) satisfying both normalized primitive
bounds. Such a point is not yet a full theta collision, but it defeats any
proof relying only on the uniform pointwise tail estimate.
