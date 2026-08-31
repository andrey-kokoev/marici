# A source-fixed low-frequency window removes theta division but not exponential-sum conditioning

## Question

Can the completed-theta factor be divided out on a fixed Fourier window without inspecting arithmetic coefficients or spectral zeros?

## Claim boundary

Yes. A nonzero zeroth Fourier moment and one finite absolute first moment give an explicit source-fixed interval on which the completed-theta transform is bounded away from zero. Division on that interval is continuous. This eliminates theta zeros as the local obstruction, but it does not yet provide continuous recovery of infinitely many nonuniform exponential frequencies from one bounded interval.

## Moment hypothesis supplied by the theta atom

Let the full-line completed-theta atom satisfy

\[
\Phi\in L^1(\mathbb R),
\qquad
u_1:=\int_{\mathbb R}|t\Phi(t)|\,dt<\infty,
\]

and define

\[
m_0:=\widehat\Phi(0)
=\int_{\mathbb R}\Phi(t)\,dt.
\]

For the source precursor

\[
h(t)=\frac12e^{t/2}\vartheta(e^{2t}),
\qquad
\Phi=(\partial_t^2-\tfrac14)h,
\]

the rapid endpoint decay makes the integrations by parts legitimate and gives

\[
m_0=-\frac14\int_{\mathbb R}h(t)\,dt\ne0.
\]

Only nonvanishing is needed below; no numerical approximation is used.

## Explicit window

For real \(\xi\),

\[
|\widehat\Phi(\xi)-m_0|
\le
\int_{\mathbb R}|e^{-i\xi t}-1|\,|\Phi(t)|\,dt
\le |\xi|\nu_1.
\]

Hence, if

\[
r_0=\frac{|m_0|}{2\nu_1}
\]

when \(\nu_1>0\), then every \(|\xi|\le r_0\) satisfies

\[
|\widehat\Phi(\xi)|\ge\frac{|m_0|}{2}.
\]

If \(\nu_1=0\), the atom is concentrated at the origin in the measure sense and the present smooth nonzero theta atom is not in that case.

The interval \([-r_0,r_0]\) depends only on the declared theta source. It is independent of the coefficient packet, prime cutoff, Xi divisor, and G4 realization.

## Continuous local division

For a synthesized common history

\[
\widehat h_c(\xi)=\widehat\Phi(\xi)F_c(\xi),
\]

one may recover on the fixed window

\[
F_c(\xi)=\frac{\widehat h_c(\xi)}{\widehat\Phi(\xi)}.
\]

The multiplier obeys

\[
\left\|\frac1{\widehat\Phi}\right\|_{L^\infty([-r_0,r_0])}
\le\frac2{|m_0|}.
\]

Derivatives of the quotient are also controlled on a slightly smaller fixed interval because \(\widehat\Phi\) is smooth and remains separated from zero there. Thus theta deconvolution is continuous in every fixed finite-order compact-window seminorm.

## What remains open

The arithmetic exponential sum is

\[
F_c(\xi)=
\sum_\lambda a_\lambda
\left(c_\lambda^+e^{i\xi L_\lambda}
+c_\lambda^-e^{-i\xi L_\lambda}\right).
\]

Knowing this entire function on a real interval determines it algebraically, but analytic continuation from a bounded interval is not automatically continuous. Near-colliding frequencies permit high-order cancellations on that interval. The one-exponential-order nearest-neighbour estimate controls a local two-frequency separation cost; it does not bound simultaneous interpolation for an unbounded number of frequencies.

Therefore the remaining theorem must estimate the inverse of the restricted exponential synthesis

\[
c\longmapsto F_c|_{[-r_0,r_0]}
\]

between the declared projective coefficient topology and an observer topology strong enough to retain all derivatives or an equivalent entire-function growth family. A finite-order compact-window norm cannot be assumed sufficient.

## Direction rescore

- Source-fixed theta deconvolution window: completed.
- Theta zeros as a local obstruction: eliminated.
- Two-frequency spacing cost: completed separately.
- Infinite restricted exponential interpolation in a finite-order norm: 1/10 and likely false.
- Recovery from the full derivative/entire observer topology: 9/10.

## Disposition

The completed-theta factor can be removed continuously near zero by a source-only estimate. The depth-first frontier is now precisely the topology of restricted exponential interpolation: determine whether the complete derivative jet on the fixed window controls every projective coefficient seminorm with a finite seminorm shift. No RH or Hilbert coercivity conclusion is authorized.
