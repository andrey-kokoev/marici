# The Two Weighted Quadratures Are One Harmonic Gradient and RH Forbids Its Interior Critical Points

Define the source primitive

\[
Y(z)=\int_0^\infty f(q)\frac{\sinh(zq)}q\,dq.
\]

Then `Y'(z)=X(z)/2`. Writing `Y=U+iV`, the weighted quadratures satisfy

\[
\partial_aU=C_a,
\qquad
\partial_tU=-S_a.
\]

Hence a Riemann zero is exactly a critical point of the harmonic potential
`U`. The seam is a constant-potential boundary because `U(0,t)=0`; its
tangential derivative vanishes identically, and seam zeros occur when the
normal derivative also vanishes. Off the seam, a zero would be an interior
harmonic saddle.

At a simple puncture the two-channel Jacobian is

\[
\det D(C,S)=\frac14|X'(z)|^2>0.
\]

Thus RH is equivalent to absence of interior critical points of this
source-derived relationship field.

Research packet:
`research/grothendieck/the-two-weighted-quadratures-are-one-harmonic-gradient-and-rh-forbids-its-interior-critical-points.md`

Checker:
`research/grothendieck/checkers/check_theta_harmonic_gradient_zero_equivalence.py`

The checker passes 6/6 gates.
