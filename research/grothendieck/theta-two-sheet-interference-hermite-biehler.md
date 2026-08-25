# Theta two-sheet interference and the Hermite--Biehler gate

Author: `marici.Grothendieck`

## 1. Spectral coordinate

Put

\[
X(z)=\xi\left(\frac12+iz\right).
\]

The functional equation and reality become

\[
X(-z)=X(z),
\qquad
X(\bar z)=\overline{X(z)}.
\]

The Riemann hypothesis is the assertion that every zero of `X` is real. In
the original `s`-plane, the real `z`-axis is precisely the critical line
`Re(s)=1/2`.

The points `s=0` and `s=1` are exchanged anchors of the functional equation,
not zeros of the completed xi function. Their midpoint produces the spectral
origin `z=0`.

## 2. Canonical two-sheet decomposition

With the completed positive even theta source `Phi`, define the positive-scale
half transform

\[
F(z)=\int_0^\infty\Phi(u)e^{izu}\,du.
\]

Evenness gives the exact decomposition

\[
\boxed{X(z)=F(z)+F(-z).}
\]

For an entire function, put

\[
F^\#(z)=\overline{F(\bar z)}.
\]

Because the source is real,

\[
F^\#(z)=F(-z).
\]

Thus

\[
\boxed{X=F+F^\#.}
\]

This is the precise two-sheet interference object. On the real spectral
axis, the two sheets are conjugate and

\[
X(x)=2\operatorname{Re}F(x).
\]

A critical-line zero is exactly a frequency at which the conjugate sheets
have equal amplitude and opposite phase.

## 3. Hermite--Biehler amplitude orientation

For `Im(z)>0`, the transform `F(z)` uses the damped factor `e^(-u Im(z))`,
whereas `F^#(z)=F(-z)` uses the growing factor. The source decays sufficiently
fast that both are entire.

Define the growing-sheet function

\[
E(z)=F(-z).
\]

Then `E^#=F` and

\[
X=E+E^\#.
\]

The sharp amplitude theorem is

\[
\boxed{
|E(z)|>|E^\#(z)|
\qquad(\operatorname{Im}z>0).
}
\]

This is the Hermite--Biehler orientation. Under the standard growth and
nondegeneracy hypotheses, it forces every real and imaginary part in the
de Branges family—including `E+E^#`—to have only real zeros. Hence it would
imply RH.

In interference language:

\[
\boxed{
\text{the two reciprocal sheets can have equal amplitude only on their
common spectral boundary.}
}
\]

This is stronger than functional-equation symmetry. Symmetry identifies the
boundary; Hermite--Biehler orientation confines complete cancellation to it.

## 4. Exact two-copy amplitude kernel

For `z=x+iy`, direct expansion gives

\[
\begin{aligned}
&|F(-z)|^2-|F(z)|^2\\
&\quad=2\int_0^\infty\int_0^\infty
\Phi(u)\Phi(v)
\sinh(y(u+v))
\cos(x(u-v))\,du\,dv.
\end{aligned}
\]

Using

\[
S=u+v,
\qquad
D=u-v,
\]

the domain is `S>0, |D|<S`, and the Jacobian magnitude is `1/2`. Therefore

\[
\boxed{
|F(-z)|^2-|F(z)|^2
=\int_0^\infty\sinh(yS)
\int_{-S}^{S}
\Phi\left(\frac{S+D}{2}\right)
\Phi\left(\frac{S-D}{2}\right)
\cos(xD)\,dD\,dS.
}
\]

Every factor except `cos(xD)` has a fixed positive sign. The entire RH
obstruction is the orientation of this finite-interval cosine transform.
This recovers, in exact two-sheet form, the oscillatory transport problem
encountered by the curvature and de Branges lanes.

## 5. Why symmetry alone does not work

A positive even source can have off-boundary destructive interference. The
atomic example

\[
\Phi_{a}(u)=w_0\delta_0
+\frac{w_1}{2}(\delta_a+\delta_{-a}),
\qquad w_0>w_1>0,
\]

has transform

\[
X_a(z)=w_0+w_1\cos(az).
\]

The equation

\[
\cos(az)=-\frac{w_0}{w_1}<-1
\]

has nonreal conjugate solutions. Thus positivity, evenness, the reciprocal
fold, and horizontal conjugation symmetry all coexist with off-line zeros.
Smooth positive even approximations preserve nearby nonreal zeros by ordinary
analytic stability.

The falsifier explains the missing datum: the central and displaced channels
can acquire equal amplitude away from the fixed boundary. A source-specific
amplitude orientation is indispensable.

## 6. Relation to the current arithmetic frontier

The all-prime rigidity theorem identifies the completed theta coefficient
packet uniquely among weighted integral-square sources. The interference
formula now states what that rigidity must accomplish analytically:

\[
\boxed{
\text{all-prime Euler coherence}
\quad\Longrightarrow\quad
\text{positive orientation of every }(S,D)\text{ cosine slice}.
}
\]

It need not make each fixed-`S` cosine transform positive; cancellation may
occur across `S`. But it must make their `sinh(yS)`-weighted total positive
for every `x` and every `y>0`.

## 7. Fixed-sum slice positivity is impossible

Define the even conditional density

\[
g_S(D)=
\Phi\left(\frac{S+D}{2}\right)
\Phi\left(\frac{S-D}{2}\right),
\qquad |D|\le S,
\]

and its cosine slice

\[
C_S(x)=\int_{-S}^{S}g_S(D)\cos(xD)\,dD.
\]

At the finite endpoints,

\[
g_S(S)=g_S(-S)=\Phi(S)\Phi(0)>0.
\]

One integration by parts gives

\[
C_S(x)
=\frac{2\Phi(S)\Phi(0)\sin(xS)}x
-\frac2x\int_0^Sg_S'(D)\sin(xD)\,dD.
\]

For smooth `Phi`, a second integration by parts bounds the remaining term by
`O(x^(-2))`. Hence

\[
\boxed{
C_S(x)=\frac{2\Phi(S)\Phi(0)\sin(xS)}x+O(x^{-2}).
}
\]

For every fixed `S>0`, this changes sign infinitely often. Therefore

\[
\boxed{
\text{no fixed-total-scale cosine slice is nonnegative for all frequencies.}
}
\]

This is an analytic no-go for a strong version of adjacent-band total
positivity. The Hermite--Biehler inequality, if true, is irreducibly an
`S`-transport theorem: negative oscillatory endpoint currents from one total
scale must be repaired by other total scales under the weight `sinh(yS)`.

The nonzero endpoint is also conceptually important. The defect occurs when
one source coordinate reaches the modular seam (`u=0`) while the other
remains at `S`. The completed two-dimensional integral may sew these boundary
currents across `S`, even though no individual conditional chart is positive.

## 8. Exact one-dimensional transported profile

Strict log-concavity of `Phi` implies that for `0<D<S`,

\[
\partial_D\log g_S(D)
=\frac12\left[
(\log\Phi)'\left(\frac{S+D}{2}\right)
-(\log\Phi)'\left(\frac{S-D}{2}\right)
\right]<0.
\]

Hence

\[
-\partial_Dg_S(D)>0.
\]

Insert the integration-by-parts identity for `C_S` into the full amplitude
difference and interchange the positive triangular integrals. For `x>0`, one
obtains

\[
\boxed{
|F(-z)|^2-|F(z)|^2
=\frac2x\int_0^\infty H_y(D)\sin(xD)\,dD,
}
\]

where

\[
\boxed{
\begin{aligned}
H_y(D)={}&
\sinh(yD)\Phi(D)\Phi(0)\\
&+\int_D^\infty\sinh(yS)
\bigl[-\partial_Dg_S(D)\bigr],dS.
\end{aligned}
}
\]

Every term defining `H_y` is nonnegative, and it is strictly positive for
`D>0`. The first line is the seam endpoint current; the second is the
transported interior current. They are not independent repairs but the two
boundary pieces of one integration-by-parts identity.

Thus the Hermite--Biehler problem has collapsed to a one-dimensional sine
orientation theorem:

\[
\boxed{
\int_0^\infty H_y(D)\sin(xD)\,dD>0
\qquad(x>0,y>0).
}
\]

This reduction uses only already-proved strict log-concavity to orient the
transport density. It does not assume the desired sine-transform sign.

## 9. A sharper Bernstein target

The profile satisfies `H_y(0)=0`; it rises from the origin and therefore
cannot be globally decreasing. The elementary decreasing-density criterion
for positive sine transforms is unavailable.

A stronger source-shaped sufficient condition is

\[
\boxed{
\frac{H_y(D)}D
=\int_0^\infty e^{-tD}\,d\nu_y(t),
\qquad d\nu_y\ge0.
}
\]

Indeed,

\[
\int_0^\infty De^{-tD}\sin(xD)\,dD
=\frac{2tx}{(t^2+x^2)^2}>0
\]

for `t,x>0`. Therefore complete monotonicity of `H_y(D)/D` would prove the
Hermite--Biehler amplitude inequality.

This is now a hard-to-vary conjecture with a local falsifier: find the first
derivative order and point for which

\[
(-1)^k\partial_D^k\left(\frac{H_y(D)}D\right)<0.
\]

Failure would not disprove RH or even sine positivity; it would sharply
reject the Bernstein explanation while leaving the exact one-dimensional
profile as the residual object.

## 10. The Bernstein target is structurally impossible

The local geometry at `D=0` decides the complete-monotonicity proposal. For
fixed `S`, evenness of `g_S` gives

\[
-\partial_Dg_S(D)=a_1(S)D+O(D^3),
\]

where strict log-concavity yields

\[
a_1(S)
=-\frac12\Phi(S/2)^2(\log\Phi)''(S/2)>0.
\]

Because the transported integral is weighted by `sinh(yS)`, its moving lower
endpoint contributes only at cubic order:

\[
\int_D^\infty\sinh(yS)
[-\partial_Dg_S(D)]\,dS
=c_yD+O(D^3).
\]

The seam term also has an odd expansion. Hence

\[
\boxed{H_y(D)=C_yD+O(D^3),\qquad C_y>0.}
\]

Therefore

\[
f_y(D):=\frac{H_y(D)}D
=C_y+O(D^2),
\qquad
f_y'(0+)=0.
\]

Suppose `f_y` were completely monotone. By Bernstein's theorem,

\[
f_y(D)=\int_0^\infty e^{-tD}\,d\nu_y(t),
\qquad \nu_y\ge0.
\]

The zero right derivative forces

\[
0=-f_y'(0+)=\int_0^\infty t\,d\nu_y(t).
\]

Thus `nu_y` is supported at `t=0`, and `f_y` must be constant. But the
super-exponential theta tail gives

\[
f_y(D)\longrightarrow0
\qquad(D\longrightarrow\infty),
\]

while `f_y(0+)=C_y>0`. This is impossible.

Consequently

\[
\boxed{
\frac{H_y(D)}D\text{ is not completely monotone for any }y>0.
}
\]

This is a clean structural falsifier. No derivative census is required. It
does not decide sine positivity; it proves only that the positive sine
transform, if true, belongs to a subtler class than positive mixtures of the
kernels `D exp(-tD)`.

## 11. Surviving one-dimensional target

The exact live theorem remains

\[
\int_0^\infty H_y(D)\sin(xD)\,dD>0
\qquad(x,y>0).
\]

The next admissible mechanism must tolerate a flat derivative at the origin
and non-monotone local shape. Candidate structures are:

1. a source-derived Pólya frequency representation after one additional
   differential transform;
2. alternating-band domination for the cumulative profile
   `int_D^infinity H_y(s) ds`;
3. an all-prime Euler recursion acting directly on `H_y`; or
4. a canonical-system energy whose boundary reduction is this sine
   transform but whose bulk is positive.

Any candidate claiming complete monotonicity of `H_y/D` is now excluded.

## 12. Corrected Gaussian--Bernstein target

The failed coordinate `D` suggests the source-natural correction. Put

\[
r=D^2,
\qquad
G_y(r)=\frac{H_y(\sqrt r)}{\sqrt r}.
\]

The odd germ of `H_y` makes `G_y` regular at `r=0`. Suppose

\[
\boxed{
G_y(r)=\int_0^\infty e^{-tr}\,d\mu_y(t),
\qquad d\mu_y\ge0.
}
\]

Equivalently, `G_y` is completely monotone in the squared-separation
coordinate. Then

\[
H_y(D)=D\int_0^\infty e^{-tD^2}\,d\mu_y(t).
\]

For every `t,x>0`,

\[
\int_0^\infty De^{-tD^2}\sin(xD)\,dD
=\frac{x\sqrt\pi}{4t^{3/2}}e^{-x^2/(4t)}>0.
\]

Therefore the Gaussian--Bernstein representation would prove the full
Hermite--Biehler amplitude inequality and hence RH, subject to the standard
analytic hypotheses already stated.

Unlike complete monotonicity in `D`, this conjecture is compatible with
`partial_D(H_y/D)|_(D=0)=0`. It also matches the primitive theta architecture:
the lattice source is assembled from Gaussian heat kernels in a squared
scale variable.

The exact local falsifier is now

\[
\exists k\ge0,r\ge0:
\qquad
(-1)^k\partial_r^kG_y(r)<0.
\]

At the origin, writing

\[
H_y(D)=C_yD+C_{y,3}D^3+O(D^5),
\]

the first new gate is

\[
\boxed{C_{y,3}\le0.}
\]

This coefficient can be derived directly from `Phi`, its seam jets, and the
transported log-curvature integral. It is the next smallest analytic attack;
failure at this first gate would reject the corrected explanation without
touching the broader sine-positivity conjecture.

## 13. Exact first Gaussian--Bernstein coefficient

Write

\[
\phi_0=\Phi(0),
\qquad
\phi_2=\Phi''(0),
\qquad
\ell=\log\Phi.
\]

For `a=S/2`, expansion of the transported density gives

\[
-\partial_Dg_S(D)
=a_1(S)D+a_3(S)D^3+O(D^5),
\]

with

\[
a_1(S)=-\frac12\Phi(a)^2\ell''(a),
\]

and

\[
\boxed{
a_3(S)
=-\Phi(a)^2
\left(
\frac{\ell''''(a)}{48}
+\frac{\ell''(a)^2}{8}
\right).
}
\]

The moving lower endpoint matters at cubic order. Since

\[
a_1(0)=-\frac12\phi_0\phi_2,
\]

one finds

\[
\boxed{
\begin{aligned}
C_{y,3}={}&
\frac34y\phi_0\phi_2
+\frac16y^3\phi_0^2\\
&-\int_0^\infty\sinh(yS)\Phi(S/2)^2
\left(
\frac{\ell''''(S/2)}{48}
+\frac{\ell''(S/2)^2}{8}
\right)dS.
\end{aligned}
}
\]

The first corrected Bernstein gate is exactly

\[
\boxed{C_{y,3}\le0\qquad(y>0).}
\]

Its three terms have distinct meanings:

1. `3y phi_0 phi_2/4` is the seam curvature contribution;
2. `y^3 phi_0^2/6` is the positive hyperbolic carrier contribution;
3. the integral is the completed fourth-log-curvature transport.

Strict log-concavity controls `ell''` but not the sign of `ell''''`; hence the
already-proved quadratic theorem does not decide this gate. Theta arithmetic
must orient the combined fourth-order expression.

## 14. Two-condition reduction of the first gate

Define

\[
\boxed{
Q(S)=\frac{\Phi(S/2)^2}{48}
\left[
\ell''''(S/2)+6\ell''(S/2)^2
\right].
}
\]

Then

\[
C_{y,3}
=\frac34y\phi_0\phi_2
+\frac16y^3\phi_0^2
-\int_0^\infty\sinh(yS)Q(S)\,dS.
\]

Because `Phi` is strictly even log-concave,

\[
\phi_2<0.
\]

Suppose the following two source inequalities hold:

\[
\boxed{Q(S)\ge0\qquad(S\ge0),}
\]

and

\[
\boxed{
\int_0^\infty S^3Q(S)\,dS\ge\phi_0^2.
}
\]

Since `sinh(yS)>=y^3S^3/6` for positive `y,S`, these imply

\[
\int_0^\infty\sinh(yS)Q(S)\,dS
\ge\frac16y^3\phi_0^2.
\]

The cubic carrier term is cancelled, while the seam-curvature term is
strictly negative. Therefore

\[
\boxed{C_{y,3}<0\qquad(y>0).}
\]

The first Gaussian--Bernstein derivative gate has thus reduced to one
pointwise fourth-curvature inequality and one normalized third-moment bound.

In terms of the potential `V=-log Phi`, the pointwise condition is

\[
\boxed{6V''(u)^2-V''''(u)\ge0.}
\]

This is substantially stronger than convexity of `V`, but it is a local
source statement rather than an oscillatory transform inequality.

## 15. Gaussian calibration

For the normalized Gaussian carrier `Phi_G(u)=exp(-u^2)`,

\[
\ell_G''=-2,
\qquad
\ell_G''''=0,
\]

and hence

\[
Q_G(S)=\frac12e^{-S^2/2}.
\]

Its third moment is

\[
\int_0^\infty S^3Q_G(S)\,dS=1=\Phi_G(0)^2.
\]

Thus the proposed moment inequality is exactly Gaussian-normalized and the
carrier saturates it. Theta must improve that equality while preserving the
pointwise fourth-curvature orientation.

This supplies an immediate hostile test for any source deformation: failure
of either `6V''^2-V''''>=0` or the normalized third moment rejects the first
Gaussian--Bernstein mechanism before any higher derivative is considered.

## 16. The moment gate is a weighted dilation gap

The fourth-curvature numerator has the denominator-free identity

\[
\boxed{
\Phi^2\left(\ell''''+6\ell''^2\right)
=\Phi\Phi''''-4\Phi'\Phi'''+3\Phi''^2.
}
\]

After the change `S=2u`,

\[
\int_0^\infty S^3Q(S)\,dS
=\frac13\int_0^\infty u^3
\left(
\Phi\Phi''''-4\Phi'\Phi'''+3\Phi''^2
\right)du.
\]

Three integrations by parts, using evenness at zero and rapid decay at
infinity, give the exact identity

\[
\boxed{
\begin{aligned}
\int_0^\infty S^3Q(S)\,dS
={}&\Phi(0)^2
-8\int_0^\infty u\Phi'(u)^2\,du\\
&+\frac83\int_0^\infty u^3\Phi''(u)^2\,du.
\end{aligned}
}
\]

Consequently the Gaussian-normalized moment gate is equivalent to

\[
\boxed{
\int_0^\infty u^3\Phi''(u)^2\,du
\ge
3\int_0^\infty u\Phi'(u)^2\,du.
}
\]

This is a weighted spectral-gap inequality for the dilation geometry of the
source. It is stronger than the generic weighted Hardy inequality, whose
unrestricted sharp constant is only one. The factor three must therefore
come from additional theta structure rather than boundary conditions alone.

For every Gaussian scale `exp(-a u^2)`, equality holds. Thus the theorem asks
whether the completed theta source lies on the stiff side of the Gaussian
under this dilation quotient.

The first Gaussian--Bernstein gate is now generated by two sharply typed
claims:

\[
\boxed{
\begin{cases}
\Phi\Phi''''-4\Phi'\Phi'''+3\Phi''^2\ge0,\\
\displaystyle
\int u^3\Phi''^2\ge3\int u\Phi'^2.
\end{cases}
}
\]

The first is local generalized-Laguerre orientation of the source; the
second is its global Gaussian-sharp dilation gap. Neither is implied by the
other, and both have direct analytic falsifiers.

## 17. Convex-power calibration separates the two gates

For

\[
\Phi_p(u)=e^{-u^{2p}},
\qquad p\ge1,
\]

gamma integration gives

\[
\int_0^\infty u\Phi_p'(u)^2\,du=\frac p2,
\]

and

\[
\int_0^\infty u^3\Phi_p''(u)^2\,du
=p^3+\frac p2.
\]

Therefore

\[
\boxed{
\frac{\int u^3\Phi_p''^2}{\int u\Phi_p'^2}
=2p^2+1.
}
\]

The Gaussian `p=1` saturates the required constant three, while every
strictly stiffer power improves the global dilation gap.

The local condition behaves differently. For `V_p=u^(2p)`,

\[
\begin{aligned}
6V_p''(u)^2-V_p''''(u)
={}&2p(2p-1)u^{2p-4}\\
&\times\left[
12p(2p-1)u^{2p}
-(2p-2)(2p-3)
\right].
\end{aligned}
\]

For `p>=2`, this is negative near the origin. Hence the convex-power source
passes the global gap but fails the local seam orientation.

This proves independence of the two gates and clarifies their meanings:

\[
\begin{array}{c|c}
\text{gate}&\text{what it controls}\\
\hline
\text{weighted dilation gap}&\text{global stiffness relative to Gaussian}\\
\text{fourth-curvature orientation}&\text{absence of an over-sharp seam}.
\end{array}
\]

Theta must satisfy both simultaneously.

This gives two exact falsifiers for any proposed proof:

1. a point `(x,y)` in the upper half-plane where the two sheet amplitudes are
   equal or reversed;
2. a completed Euler cluster whose contribution defeats the positive total
   after all modular partners are retained.

## 18. Scope

This packet makes the destructive-interference interpretation exact and
identifies its Hermite--Biehler theorem. It does not prove the amplitude
inequality and does not prove RH.
