# Minimum-phase monotone sources can have tangent cosine zeros

## Question

Does positivity, monotone decrease, and upper-half-plane zero-freeness of the
half-transform suffice to exclude the remaining stationary imaginary-axis
crossing?

## Exact decreasing hostile source

Set

\[
a=\frac\pi2,
\qquad
L=\frac{3\pi}2,
\]

and define the positive nonincreasing source

\[
f(u)=
\begin{cases}
2,&0\le u\le a,\\
1,&a<u\le L.
\end{cases}
\]

Its half-transform is

\[
H(x)=\int_0^L f(u)e^{ixu}\,du
=C(x)+iS(x).
\]

At \(x=1\), direct integration gives

\[
C(1)
=2\int_0^{\pi/2}\cos u\,du
+\int_{\pi/2}^{3\pi/2}\cos u\,du
=2-2=0.
\]

The position-weighted sine integral is

\[
M(1)
=2\int_0^{\pi/2}u\sin u\,du
+\int_{\pi/2}^{3\pi/2}u\sin u\,du
=2-2=0.
\]

Therefore

\[
C(1)=C'(1)=0.
\]

But

\[
S(1)
=2\int_0^{\pi/2}\sin u\,du
+\int_{\pi/2}^{3\pi/2}\sin u\,du
=2>0.
\]

Thus \(H(1)=2i\ne0\).  The half-transform curve does not pass through the
origin; it touches the imaginary axis tangentially.

## Positive layer-cake form

The source is the tail of the positive measure

\[
\mu=\delta_{\pi/2}+\delta_{3\pi/2}.
\]

Indeed,

\[
f(u)=\mu([u,L]),
\]

and

\[
izH(z)=\int(e^{izt}-1)\,d\mu(t).
\]

Consequently the same positive-increment argument makes \(H\) zero-free in
the upper half-plane.  The hostile source therefore satisfies exactly the
minimum-phase architecture proved from theta monotonicity.

In the current variable,

\[
g(x)=\int\sin(xt)\,d\mu(t)=xC(x).
\]

At \(x=1\), both atoms sit at odd sine extrema with opposite signs:

\[
g(1)=1-1=0,
\qquad
g'(1)=0+0=0.
\]

The collision is a multiple real zero of the positive current's sine
transform.

## Consequence

The following data do not exclude a finite cosine collision:

- positivity of the source;
- monotone decrease of its density;
- a positive layer-cake measure;
- upper-half-plane zero-freeness of the half-transform;
- strict positivity of the real-axis sine component;
- retention of the endpoint boundary atom.

Therefore the completed-theta collision theorem must use a stronger property
than monotonicity or minimum phase.  Candidate extra structure includes strict
log-concavity, smooth modular sewing, and the integral winding-label
decomposition.  None may be replaced by the properties already falsified.

## What the hostile geometry says

Tangency occurs because two separated current atoms land at opposite sine
extrema while both cosine velocities vanish.  The source-specific theorem must
forbid this exact balance.  In signed-band language, it must prevent separated
positive current mass from matching across opposite extrema after position
weighting.

This suggests that the relevant theta datum is not merely the order of the
current but its curvature or inter-band likelihood ratio.  Strict
log-concavity is a plausible input because the hostile step source has atomic
curvature and a flat plateau, but log-concavity has not yet been shown to imply
the required nonstationarity.

## Refined Deutsch--Popper conjecture

The completed theta current

\[
d\mu_L=-\Phi'(t)\,dt+\Phi(L)\delta_L
\]

admits no multiple positive real zero of its sine transform.  The explanation
must cite a theta property absent from the exact two-atom current above.

The immediate falsifier remains one \((L,x)\) satisfying the cosine collision
equations for the actual theta source.  A broader proposed theorem is rejected
if it also admits the explicit step source.

## Result

Minimum phase is not the missing RH force.  A positive monotone source can
have a nonzero half-transform that touches the imaginary axis tangentially.
The remaining obstacle is genuinely a theta-current curvature or labelled
coherence theorem.
