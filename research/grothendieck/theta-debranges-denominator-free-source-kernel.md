# A canonical de Branges kernel removes the logarithmic denominator

Status: exact source reduction and RH-equivalent positivity target; no RH claim

Use the real entire critical-line parametrization

\[
 X(z)=\xi\!\left(\frac12+iz\right),
 \qquad X(\bar z)=\overline{X(z)}.                    \tag{1}
\]

The theta source supplies `X` and every derivative on the same fixed real
contour.  Define, without factoring `X`,

\[
 E(z)=X(z)+iX'(z),
 \qquad E^*(z)=\overline{E(\bar z)}=X(z)-iX'(z).      \tag{2}
\]

## Exact equivalence to the Weyl sign

Where `X(z)` is nonzero, put `M(z)=-X'(z)/X(z)`.  Direct algebra gives

\[
 |E(z)|^2-|E^*(z)|^2
 =4|X(z)|^2\operatorname{Im}M(z).                    \tag{3}
\]

Thus the Hermite--Biehler inequality

\[
 |E(z)|>|E^*(z)|,\qquad \operatorname{Im}z>0,        \tag{4}
\]

is exactly the Nevanlinna sign of the completed logarithmic derivative.  In
the completed Xi analytic class this is equivalent to all zeros of `X` being
real, hence to RH.  Possible common real factors caused by multiple real
zeros are boundary factors and must be retained in the multiplicity audit;
they do not license assuming simplicity.

## Denominator-free coupled kernel

The associated de Branges kernel is

\[
 \mathcal D(z,w)=
 \frac{E(z)\overline{E(w)}-E^*(z)\overline{E^*(w)}}
 {2\pi i(\bar w-z)}.                                  \tag{5}
\]

Substituting (2) cancels the quadratic self-terms and leaves the Bezoutian

\[
 \boxed{
 \mathcal D(z,w)=
 \frac{X'(z)\overline{X(w)}-X(z)\overline{X'(w)}}
 {\pi(\bar w-z)}.
 }                                                     \tag{6}
\]

No logarithmic division remains.  Positivity of this kernel for every finite
set of upper-half-plane points is equivalent to (4), and therefore to RH.

## Exact pullback to the fixed theta source

Under the fixed Fourier convention write

\[
 X(z)=\int_0^\infty\Phi(u)\cos(zu)\,du,
 \qquad
 X'(z)=-\int_0^\infty u\Phi(u)\sin(zu)\,du.          \tag{7}
\]

Equations (6)--(7) give the two-copy source identity

\[
 \boxed{
 \mathcal D(z,w)=\frac1{\pi(\bar w-z)}
 \int_0^\infty\!\!\int_0^\infty
 \Phi(u)\Phi(v)
 \left[
 v\cos(zu)\sin(\bar wv)
 -u\sin(zu)\cos(\bar wv)
 \right]du\,dv.
 }                                                     \tag{8}
\]

This is the desired nonlinear bridge in denominator-free form.  Divisor
extraction has not disappeared; it has been encoded as a two-copy Wronskian
of the source transform.  Unlike an abstract Herglotz realization, every
quantity in (8) is source-defined before any zero is named.

## A manifestly positive anchor ray

The diagonal kernel is already source-positive on the purely imaginary
`z`-ray.  For `z=iy`, `y>0`, define

\[
 A_y=\int_0^\infty\Phi(u)\cosh(yu)\,du,
 \qquad
 B_y=\int_0^\infty u\Phi(u)\sinh(yu)\,du.            \tag{9}
\]

Both are strictly positive because the completed theta kernel is positive.
Moreover `X(iy)=A_y` and `X'(iy)=-iB_y`.  Substitution in (6) gives the exact
identity

\[
 \boxed{
 \mathcal D(iy,iy)=\frac{A_yB_y}{\pi y}>0.
 }                                                     \tag{10}
\]

At `y=0` the removable limit is likewise positive and is determined by the
second theta moment.  Thus failure, if any, cannot originate at the
nonoscillatory anchor.  It can arise only when continuation in `Re z`
introduces cancellation between the sine and cosine channels.

This converts the global problem into an angular-propagation theorem: prove
that the source-positive diagonal and its coupled polarization remain
positive while moving horizontally through the upper half-plane.  Any such
proof must retain the full two-copy phase; replacing it by absolute values
loses precisely the continuation information at issue.

## Exact sum--difference transport reduction

The diagonal current admits a more revealing real formula.  Write
`z=x+iy`, with `y>0`, and set

\[
 J(x,y)=\operatorname{Im}\left(X(z)\overline{X'(z)}\right),
 \qquad \mathcal D(z,z)=\frac{J(x,y)}{\pi y}.          \tag{11}
\]

Expanding (7), symmetrizing the two source variables, and using product-to-sum
identities gives

\[
 \begin{aligned}
 J(x,y)=\frac14\int_0^\infty\!\!\int_0^\infty
 \Phi(u)\Phi(v)\big[&
 (u+v)\sinh(y(u+v))\cos(x(u-v))\\
 &+(u-v)\sinh(y(u-v))\cos(x(u+v))
 \big]du\,dv.                                        \tag{12}
 \end{aligned}
\]

Both nonoscillatory coefficients are nonnegative because
`r sinh(yr)>=0` for real `r`.  All possible negativity is confined to the two
cosine readouts.

Now set

\[
 S=u+v,\qquad D=u-v,qquad S\ge0,\quad |D|\le S,       \tag{13}
\]

and

\[
 W(S,D)=
 \Phi\!\left(\frac{S+D}{2}\right)
 \Phi\!\left(\frac{S-D}{2}\right).                  \tag{14}
\]

Including the Jacobian, (12) becomes

\[
 \boxed{
 J(x,y)=\frac18
 \int_0^\infty\int_{-S}^{S}W(S,D)
 \left[
 S\sinh(yS)\cos(xD)
 +D\sinh(yD)\cos(xS)
 \right]dD\,dS.
 }                                                     \tag{15}
\]

This is not a new numerical representation.  It identifies the exact
geometry of the positivity problem:

\[
 \text{positive labelled two-copy theta transport}
 \longrightarrow
 \text{two reciprocal cosine band systems}
 \longrightarrow J(x,y).                              \tag{16}
\]

The first channel oscillates only in the difference coordinate `D`, weighted
by the positive sum response `S sinh(yS)`.  The second oscillates in `S`,
weighted by the positive even difference response `D sinh(yD)`.  Their
exchange under sum--difference duality explains why a one-channel or
absolute-value argument cannot close.

This is the correct re-entry point for the earlier adjacent-band transport
program.  Its task is no longer to justify an auxiliary quadrant readout: it
must prove that canonical consecutive cosine bands in the two reciprocal
channels compensate under the *same* source density `W`.  A pairing chosen
independently in the two channels is inadmissible because it breaks their
common two-copy origin.

The sharp analytic falsifier is a canonical adjacent band pair for which the
source-normalized transported negative mass exceeds the corresponding
positive mass in the sum of both channels.  The proof target is a
variation-diminishing theorem for (15), uniform in `x in R` and `y>0`.

## Bilateral contour removes the apparent second channel

Formula (15) is correct, but its two-channel appearance is an artifact of
folding the even source to the half-line too early.  On the faithful fixed
contour use

\[
 X(z)=\frac12\int_{\mathbb R}\Phi(u)e^{izu}\,du.      \tag{17}
\]

Now `u,v` range independently over the real line, so the same variables
`S=u+v`, `D=u-v` range over all of `R^2`.  The density

\[
 W(S,D)=\Phi((S+D)/2)\Phi((S-D)/2)                    \tag{18}
\]

is even separately in `S` and `D`.  Symmetry in `D` replaces
`v=(S-D)/2` by `S/2`; pairing `S` with `-S` then yields

\[
 \boxed{
 J(x,y)=\frac18\int_0^\infty S\sinh(yS)
 \left[
 \int_{\mathbb R}W(S,D)\cos(xD)\,dD
 \right]dS.
 }                                                     \tag{19}
\]

Thus the reciprocal `cos(xS)` channel in (15) is not independent physical
data.  It is the correction required when the bilateral source is represented
in the folded wedge.  On the faithful contour the RH-equivalent diagonal
current has only one oscillatory coordinate.

Define the fixed-sum autocorrelation transform

\[
 \widehat W_S(x)=\int_{\mathbb R}
 \Phi((S+D)/2)\Phi((S-D)/2)\cos(xD)\,dD.             \tag{20}
\]

The live theorem is now

\[
 \boxed{
 \int_0^\infty S\sinh(yS)\widehat W_S(x)\,dS>0
 \quad(x\in\mathbb R,\ y>0).
 }                                                     \tag{21}
\]

This is strictly sharper than attempting two separately chosen band
pairings.  A sufficient—but potentially stronger than necessary—source
theorem would be

\[
 \widehat W_S(x)\ge0\qquad(S>0,\ x\in\mathbb R),      \tag{22}
\]

meaning that every fixed-sum slice is positive definite in its difference
coordinate.  Its first analytic test is not numerical: determine whether the
slice

\[
 D\longmapsto
 \Phi((S+D)/2)\Phi((S-D)/2)                            \tag{23}
\]

belongs to a Fourier-positive class forced by the modular theta source.
Failure of (22) would not falsify RH; it would show that positivity occurs
only after the canonical positive `S sinh(yS)` mixture in (21).

## Hudson rigidity falsifies slice-wise positivity

The stronger sufficient condition (22) is analytically impossible.  With

\[
 q=S/2,
\]

the slice transform (20) is, up to the harmless Fourier normalization, the
Wigner distribution of the pure state `Phi`:

\[
 \widehat W_S(x)
 =\int_{\mathbb R}
 \Phi(q+D/2)\Phi(q-D/2)\cos(xD)\,dD.                 \tag{24}
\]

Because `Phi` is real and even, nonnegativity for every `S>0` and real `x`
would extend by reflection and continuity to nonnegativity of its Wigner
distribution on the whole phase plane.  Hudson's theorem then forces `Phi`
to be Gaussian (up to the standard phase-space symmetries).

The completed theta kernel is not Gaussian: its tails contain the
superexponential scale `exp(-pi exp(2|u|))` multiplied by elementary
exponentials, rather than `exp(-a u^2)`.  Hence

\[
 \boxed{
 \widehat W_S(x)\text{ must be negative somewhere.}
 }                                                     \tag{25}
\]

This is a mechanism theorem, not an RH falsifier.  It proves that the
positive `S sinh(yS)` mixture in (21) is essential.  The Carrier is therefore
quasiprobabilistic at each fixed sum slice but conjecturally positive after
the source-prescribed hyperbolic marginal.  Any proof that demands positivity
before that marginal has discarded indispensable coherence.

Reference: R. L. Hudson, “When is the Wigner quasi-probability density
non-negative?”, *Reports on Mathematical Physics* 6 (1974), 249--252,
https://doi.org/10.1016/0034-4877(74)90007-X.

## The hyperbolic marginal is normal modulus flow

The mixture (21) is not an invented smoothing.  Direct differentiation gives

\[
 \boxed{
 \partial_y|X(x+iy)|^2=2J(x,y).
 }                                                     \tag{26}
\]

Indeed `partial_y X=iX'`, so the identity follows before using any integral
representation.  Combining it with (19) gives

\[
 \partial_y|X(x+iy)|^2
 =\frac14\int_0^\infty S\sinh(yS)\widehat W_S(x)\,dS. \tag{27}
\]

The sharp Deutsch--Popperian conjecture is therefore

\[
 \boxed{
 \partial_y|X(x+iy)|^2>0
 \quad\text{for every }x\in\mathbb R, y>0.
 }                                                     \tag{28}
\]

Within the completed Xi class, (28) is equivalent to RH.  It excludes an
upper-half-plane zero because the derivative would vanish there; under RH,
the real-zero canonical product makes the outward logarithmic derivative a
strictly positive sum of Poisson/Cauchy atoms.

Its explanatory content is geometric: the real spectral axis is the strict
normal-modulus valley of the completed source.  The Wigner slices are
necessarily signed, but reciprocal-scale coherence selects exactly the
hyperbolic marginal whose normal current is positive.

The falsifier is local and unforgiving: one pair `(x,y)` with a negative
exact value in (27) disproves the conjecture and RH.  Conversely, no finite
collection of positive points proves it.  The analytic attack must explain
why the signed Wigner distribution has a positive normal marginal for every
hyperbolic weight, rather than trying to make the quasidistribution itself
positive.

## Only the half-strip is unknown

The classical critical-strip theorem places every zero `a` of `X` in

\[
 |\operatorname{Im}a|<\frac12.                        \tag{29}
\]

Pair the canonical product using the even symmetry `a <-> -a`.  For
`z=x+iy` with `y>=1/2`, the normal derivative contributed by each zero in the
pair is

\[
 \frac{y-\operatorname{Im}a}{|z-a|^2}
 +\frac{y+\operatorname{Im}a}{|z+a|^2}>0.             \tag{30}
\]

The paired product has no residual exponential drift because `X` is even.
Symmetric convergence therefore gives unconditionally

\[
 \boxed{
 \partial_y\log|X(x+iy)|>0
 \qquad(y\ge1/2).
 }                                                     \tag{31}
\]

Accordingly the RH-equivalent unknown domain is only

\[
 \boxed{x\in\mathbb R,qquad0<y<1/2.}                 \tag{32}
\]

The vertical Carrier depth is compact; the unbounded difficulty is entirely
the horizontal oscillatory frequency `x`.  This also explains why the Euler
and far-ray arguments can succeed without approaching the central theorem:
they live outside the only unresolved strip.

At the lower boundary, evenness in `y` gives zero normal current.  Its first
inward coefficient is the classical Laguerre form

\[
 \partial_y|X(x+iy)|^2
 =2y\left(X'(x)^2-X(x)X''(x)\right)+O(y^3).           \tag{33}
\]

Thus the immediate analytic subproblem is a uniform boundary-layer theorem
for the first Laguerre form plus controlled higher terms on `0<y<1/2`.
Proving only the first form is insufficient globally, but a failure of it at
one real `x` would already falsify RH.

This reduction reinforces the faithful-coordinate rule: the folded
half-line presentation created an apparent extra cancellation mechanism that
disappears on the original bilateral Carrier.

## What remains

Positivity of `Phi` alone does not fix the sign of the oscillatory Bezoutian
in (8).  The next theorem must use a special order property of the completed
theta source to factor the *fully integrated* kernel:

\[
 \mathcal D(z,w)=\langle R_z,R_w\rangle_{\mathcal H_\Phi}.       \tag{34}
\]

This is the same missing positivity as the squared-coordinate Loewner
kernel, but (8) improves the attack surface in three ways:

1. it stays on the natural unsquared spectral coordinate;
2. it uses only `X` and one contour derivative;
3. it identifies the canonical Hilbert-space candidate `E=X+iX'` rather
   than guessing an operator spectrum.

The Gaussian Carrier kernel is a heat-smoothed presentation of the same
positive divisor measure.  It is not an independent route: (5) is the
Cauchy-feature presentation, while the Gaussian kernel uses Gaussian
features.  Their universal positivity carries the same content once the
respective feature families are dense.

## Sharp falsifier

A single finite packet `z_1,...,z_N` and coefficients `c_j` for which

\[
 \sum_{j,k}c_j\bar c_k\mathcal D(z_j,z_k)<0            \tag{35}
\]

falsifies the proposed source Gram theorem (and would falsify RH if evaluated
exactly for the completed source).  Positive finite packets cannot prove the
universal statement.  Accordingly the live work is analytic factorization
of (8), not scouting its minors.
