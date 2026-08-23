# Angular monotonicity is a two-copy tilted-theta inequality

Use the even full-line theta measure and define

\[
 B(z)=\int_{\mathbb R}e^{zu}\,d\nu(u),\qquad z=a+ib.
\]

Let `nu_a` be its real exponential tilt and let `U,V` be independent with
law `nu_a`. Put

\[
 D=\mathbb E_a e^{ibU},\qquad
 N=\mathbb E_a[Ue^{ibU}],\qquad
 M=\frac ND=\frac{B'(a+ib)}{B(a+ib)}.
\]

For a quarter-centered arc, define

\[
 \alpha=2a-\frac{a}{2(a^2+b^2)},\qquad
 \beta=2b+\frac{b}{2(a^2+b^2)}.
\]

The Pick/angular target is

\[
 \beta\operatorname{Re}M+\alpha\operatorname{Im}M\ge0. \tag{1}
\]

Multiplying by `|D|^2` and symmetrizing two independent copies gives

\[
\boxed{
 \frac12\mathbb E_a\!\left[
 \beta(U+V)\cos(b(U-V))
 +\alpha(U-V)\sin(b(U-V))
 \right]\ge0.}                                         \tag{2}
\]

Indeed,

\[
 \operatorname{Re}(N\overline D)
 =\frac12\mathbb E[(U+V)\cos(b(U-V))],
\]

while

\[
 \operatorname{Im}(N\overline D)
 =\frac12\mathbb E[(U-V)\sin(b(U-V))].
\]

Equation (2) is denominator-free and contains no zero data.

It also has a one-line scalar interpretation. With
\(E(a,b)=|B(a+ib)|^2\), analyticity gives

\[
\boxed{
\text{left side of (2), with its positive normalization}
=\frac12(\beta\partial_a-\alpha\partial_b)E.
}
\]

The two-copy midpoint/relative-coordinate kernel is therefore the expanded
form of a directional energy flux. See
`theta-denominator-free-energy-flow.md`.

## Sign geometry

The unweighted relative-coordinate kernel is positive on the core band

\[
 |b(U-V)|\le\pi,
\]

because `(U-V)sin(b(U-V))>=0` there. It changes sign on later oscillatory
bands. Its coefficient `alpha` is nonnegative only when `a^2+b^2>=1/4`.
Inside that circle the core relative term is hostile, not favorable, and must
be dominated by the midpoint term. The midpoint term also oscillates through
the cosine, although the positive tilt biases `U+V` to the right.

This suggests a concrete source proof architecture:

1. split at `a^2+b^2=1/4`, where the relative-coordinate coefficient changes
   sign;
2. in the inner region, use the central complex Pick disk to quantify how the
   midpoint term pays for the hostile relative term;
3. in the outer region, certify the favorable central band, pair successive
   hostile sine/cosine bands, and dominate them by the super-exponential
   theta tail; and
4. preserve the coupling of both terms throughout instead of estimating them
   independently.

The condition is exact but remains equivalent to the global Pick/RH gate.
Generic positive even measures fail it, as the four-atom curvature falsifier
already demonstrates locally. RH is not proved.

## Quadrant--cone decomposition

Write `M=B'(z)/B(z)`. Reconnaissance suggests that the actual theta source has

\[
 \operatorname{Re}M\ge0,\qquad \operatorname{Im}M\ge0
 \quad(a,b>0).                                          \tag{3}
\]

If (3) holds, the entire outer region `a^2+b^2>=1/4` is immediate because
both `alpha` and `beta` are nonnegative. In the inner region, where
`alpha<0`, the remaining condition is the moving-cone bound

\[
 \boxed{
 \frac{\operatorname{Im}M}{\operatorname{Re}M}
 \le \frac{b}{a}\frac{1+4(a^2+b^2)}{1-4(a^2+b^2)}.}     \tag{4}
\]

Near the origin, evenness gives `M(z)=c z+O(z^3)` with `c>0`, so the left side
starts at `b/a`, strictly inside the widened cone on the right. This explains
the severe but positive cancellation observed there.

This is a sufficient decomposition, not a weakening of the global problem.
A global first-quadrant theorem for `B'/B` already excludes first-quadrant
zeros of `B` and is therefore itself RH-strength. Its value is architectural:
it separates the outer sign problem from the quantitatively sharper compact
inner cone problem.

A zero-free floating-point scan of the source formula found no violation of
(3), (4), or the full Pick inequality on its finite grid. This is
reconnaissance only, not a certificate.

The inner cone is now closed without relying on that scan. The directed
certificate `central-complex-pick-radius-seventeen-halves-certificate.md`
proves the full Pick inequality throughout `|t|<=17/2`. This contains the complete inner region
`a^2+b^2<=1/4` and an outer annulus. Beyond it `alpha,beta>=0`, so the
first-quadrant property (3) is a sufficient global completion target.

## Positive-boundary ingress is automatic

The outer first-quadrant target holds infinitesimally above every point of the
positive real `z` axis. At `b=0`,

\[
 M(a)=\frac{B'(a)}{B(a)}=\mathbb E_a U>0.
\]

Analytic differentiation gives

\[
 \left.\partial_b\operatorname{Im}M(a+ib)\right|_{b=0}
 =\left(\log B\right)''(a)
 =\operatorname{Var}_a(U)>0,                            \tag{5}
\]

while `partial_b Re M|_(b=0)=0`. Thus `M` enters the open first quadrant for
all sufficiently small positive `b` at each fixed `a>0`.

Consequently an outer-quadrant violation cannot emerge directly from the
positive real boundary. It must either form in the interior or enter through
the critical boundary `a=0`, where zeros of `B(ib)` are precisely the spectral
phenomenon under investigation. A uniform quantitative boundary strip and a
separate critical-boundary analysis are the next two proof components.

## Adjacent pointwise transport is retracted

The canonical label-preserving shift `(S,D)->(S,D+pi/b)` fails pointwise on
the faithful fiber `S=0`: its required density ratio tends to zero, while the
positive labelled theta ratio has a positive limit. See
`theta-adjacent-band-transport-first-falsifier.md`.

This does not alter the scalar gate. The surviving adjacent mechanism is the
separately stated conditional/block conjecture obtained by integrating `S|D`
with labels retained. Positive scalar expectation must not be read as
uniqueness of that or any other cancellation transport.

That conditional/block conjecture now also has a stable hostile failure on the
first asymmetric exchange orbit. At `a=1,b=11`, exact source-reflection
pairing followed by directed-binary64 box enclosure places the canonical
whole two-band block for `{(1,2),(2,1)}` strictly below zero. The enclosure is
conditional on stated transcendental-rounding, exact-pi-endpoint, and tail
closures, so it is not yet a fully formal interval proof. Its
initially proposed negative large-`b` obstruction is retracted: that leading
coefficient is diagnostically positive, so the failure is a finite-frequency
band interaction. See
`theta-adjacent-block-directed-box-certificate.md`.

Accordingly, labelwise adjacent variation diminution is no longer the leading
global mechanism. A canonical larger-block scan remains negative and
stabilizes for the same exchange orbit, so the live mechanism must permit
source-derived cancellation between distinct label orbits (or use a genuinely
different source order).

The first such coupled theorem is now available. If the pointwise higher-mode
theta tail is at most `rho` times the first mode, the full expectation is at
least `I_1-(2*rho+rho^2)A_1`, where `I_1` is the signed first-mode expectation
and `A_1` its absolute-kernel norm. The theta mode ratio is decreasing in its
source radius, so `rho` is fixed at radius zero. At `(a,b)=(1,11)` the
diagnostic lower margin remains positive, narrowly. See
`theta-first-mode-coupled-positivity-theorem.md`.

A fixed-physical-domain parameter scan shows that this absolute-norm criterion
cannot be uniform in the outer quadrant: `I_1/A_1` collapses rapidly at large
`b`. This isolates the lost information. The next coupled theorem must preserve
oscillatory phase and compare higher-mode transforms directly with the
first-mode transform; a pointwise density perturbation followed by `abs(K)` is
too coarse.

A signed-orbit scan then falsifies permanent first-mode privilege as well. The
subsequent exact one-copy factorization identifies the stronger source law:
the full infinite label sum cancels all odd folding jets at the modular sewing
point. Finite-mode estimates manufacture algebraic high-frequency tails that
are absent from the completed source. Stable factorized quadrature remains
positive through `b=40` and retracts the earlier two-dimensional `b=32` sign as
cancellation error. See `theta-modular-jet-sewing-mechanism.md`.

The completed Mellin coordinate now yields the source saddle equation
`x G'(x)/G(x)=-z/2` and a conditional thimble-convexity theorem. The physical
real saddle map is nondegenerate: the audited base curvature is
`V''(0)=18.7269...`, while the existing directed theorem gives `V'''>0` on the
positive half-line. The next local falsifier is therefore a genuinely complex
zero of `(log Phi)''` and its critical value under `z=-Phi'/Phi`. See
`theta-completed-mellin-thimble-gate.md`.

A dense complex-source Newton search locates the first observed outer saddle
degeneracy at `z=0.4799105+9.6245796i`, hence `|t|=|z|^2=92.86285...`.
No earlier open-quadrant candidate appeared, but the search is not a certified
root count and does not exclude an earlier Stokes transition. See
`theta-complex-saddle-critical-value-reconnaissance.md`.

Upward-flow tracing identifies an earlier Stokes jump on `z=1/2+ib` at
`b=5.98828528998...`, corresponding to `|t|=36.10956...`. The competitor
thimble acquires a real-contour intersection there. Its individual saddle cone
proxy is negative, but the canonical plus-paired proxy remains positive
(`1.201...`). Thus single-thimble positivity is falsified and coupled
two-thimble positivity is the next gate. See
`theta-first-stokes-jump-and-coupled-saddle-gate.md`.

## Durable verification

- Checker: `checkers/theta_two_copy_angular_contraction.py`
- Result: `results/theta-two-copy-angular-contraction.json`
- Diagnostic: `checkers/theta_log_derivative_cone_scan.py`
- Diagnostic result: `results/theta-log-derivative-cone-scan.json`
