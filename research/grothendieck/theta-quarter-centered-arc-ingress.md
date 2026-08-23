# Quarter-centered characteristic arcs and critical-axis ingress

## Exact arc classification

The square map

\[
w=z^2
\]

sends the open first \(z\)-quadrant bijectively to the open upper
\(w\)-half-plane. The energy-flow characteristics are therefore the upper
semicircles

\[
w(\vartheta)=\frac14+Re^{i\vartheta},
\qquad 0<\vartheta<\pi.
\]

The cone field moves clockwise, from \(\vartheta=\pi\) to
\(\vartheta=0\). The right endpoint always lifts to

\[
z_+(R)=\sqrt{\frac14+R}>0.
\]

The left endpoint has three regimes:

\[
z_-(R)=
\begin{cases}
\sqrt{\frac14-R},&0<R<\frac14,\\
0,&R=\frac14,\\
i\sqrt{R-\frac14},&R>\frac14.
\end{cases}
\]

Thus the inner arcs connect two positive-real source points, while every
outer arc enters from the critical axis and exits on the positive real axis.
The exact dividing characteristic passes through the origin.

Because

\[
Q=-2\partial_\vartheta\mathcal E,
\qquad
\mathcal E(w)=|B(\sqrt w)|^2,
\]

the global target is strict clockwise energy growth on each of these arcs.

## Outer ingress is tangent

Fix \(R>1/4\), put

\[
\gamma=\sqrt{R-\frac14},
\]

and parametrize clockwise distance from the left endpoint by

\[
\varepsilon=\pi-\vartheta.
\]

Then

\[
z(0)=i\gamma,
\qquad
z'(0)=p:=\frac{R}{2\gamma}>0,
\]

and

\[
z''(0)=iq,
\qquad
q:=\frac{R(1/4-\gamma^2)}{4\gamma^3}.
\]

The completed even source is real on the critical axis. Write

\[
X(\gamma)=B(i\gamma)\in\mathbb R.
\]

Then

\[
B'(i\gamma)=-iX'(\gamma),
\qquad
B''(i\gamma)=-X''(\gamma).
\]

Critical-axis symmetry forces

\[
\left.\frac{d}{d\varepsilon}|B(z(\varepsilon))|^2
\right|_{\varepsilon=0}=0.
\]

So positive flux cannot be supplied by a first-order boundary derivative.
It must emerge from the ingress curvature.

## Exact ingress-curvature identity

Taylor expansion gives

\[
\boxed{
\frac12\left.\frac{d^2}{d\varepsilon^2}
|B(z(\varepsilon))|^2\right|_{0}
=p^2\bigl(X'^2-XX''\bigr)+qXX'.
}
\]

The first term is the classical Laguerre expression of the critical-line
function. The second is an unavoidable drift caused by the curvature of the
lifted quarter-centered circle.

At a simple critical-line zero, \(X=0\) and the expression reduces to

\[
p^2X'^2>0.
\]

Thus a simple zero is locally compatible with strict clockwise energy growth:
the energy rises quadratically away from its zero boundary value. A zero is
not itself a local falsifier of the ingress mechanism.

At a nonzero critical point of \(X\), where \(X'=0\), the condition reduces
to

\[
-p^2XX''>0.
\]

It therefore asks that every nonzero critical-line extremum be an extremum of
\(|X|\) in the expected direction.

## Interpretation

The phrase "control the critical-axis boundary" must not hide an RH-strength
premise. The exact local requirement is

\[
\boxed{
p^2(X'^2-XX'')+qXX'>0.
}

Proving only the Laguerre inequality may be insufficient because the drift
term changes sign at \(\gamma=1/2\). Conversely, the weighted combination
could conceivably be easier than global Laguerre positivity because its
coefficient is dictated by the characteristic geometry.

This identity gives the first local hostile test for the energy-flow
explanation: evaluate the weighted ingress curvature along the critical axis
without assuming zero locations. Failure at any \(\gamma\) kills
boundary-generated monotonicity on the corresponding arc, even if the energy
later recovers.

## Remaining global gap

Positive ingress curvature is only local. A proof still needs to exclude an
interior turning point of \(\mathcal E\) on every upper semicircle. The
correct sequence is:

1. establish or falsify the exact ingress-curvature inequality;
2. derive an evolution law for \(-\partial_\vartheta\mathcal E=Q/2\);
3. prove that positive flux cannot cross back through zero before the
   positive-real endpoint.

No step may infer the required sign from RH or from an assumed real-zero
factorization.

The normalized clockwise current is now identified with the imaginary part
of the analytic function
\((w-1/4)C'(w)/C(w)\). Thus the global target is a precise Herglotz property.
Its conditional zero expansion explains why critical-axis zeros contribute
with the correct sign, while also exposing the circularity of assuming those
pole locations. See `theta-angular-current-herglotz-gate.md`.
