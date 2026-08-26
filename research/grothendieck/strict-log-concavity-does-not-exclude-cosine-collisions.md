# Strict log-concavity does not exclude cosine collisions

## Question

The exact step-source hostile rules out monotonicity and minimum phase.  Can
smooth strict log-concavity exclude stationary imaginary-axis crossings?

## Exponential collision family

On the fixed interval \([0,1]\), take

\[
f_A(u)=e^{-Au},
\qquad
A>0,
\]

and let \(y>0\) denote frequency.  Direct integration gives

\[
C_A(y)
=
\int_0^1e^{-Au}\cos(yu)\,du
=
\frac{A+e^{-A}(-A\cos y+y\sin y)}{A^2+y^2}.
\]

At a zero of the numerator, the derivative condition \(C_A'(y)=0\) is
equivalent to the derivative of that numerator vanishing.  The collision
system is therefore

\[
(A+1)\sin y+y\cos y=0,
\]

\[
Ae^A-A\cos y+y\sin y=0.
\]

## Existence in the fourth trigonometric quadrant

On

\[
\frac{3\pi}2<y<2\pi,
\]

the first equation determines

\[
A(y)=-1-y\cot y.
\]

Substitution into the second equation gives a continuous scalar function.
Direct interval evaluation at \(y=5.1\) and \(y=5.2\) gives opposite signs,
with approximate values

\[
-1.94
,\qquad
4.78.
\]

The margins are large enough for elementary directed bounds on sine, cosine,
and exponential.  The intermediate value theorem yields an exact collision
inside that interval.  Newton refinement, used only to display its location,
gives

\[
A_0\approx1.35340345194012,
\qquad
y_0\approx5.14163979500253.
\]

No zeta zero data enter this construction.

## Transverse parameter Jacobian

Let the two collision equations be \(F_1=0\) and \(F_2=0\).  At a solution,
the lower-right Jacobian entry equals \(F_1\) and hence vanishes.  The other
two relevant entries are

\[
\partial_yF_1
=(A+2)\cos y-y\sin y>0,
\]

\[
\partial_AF_2
=(A+1)e^A-\cos y>0
\]

throughout the chosen quadrant.  Consequently

\[
\det D_{A,y}(F_1,F_2)<0.
\]

The collision is transverse in the two external parameters.

## Strictly log-concave continuation

Now introduce

\[
f_{A,\varepsilon}(u)
=e^{-Au-\varepsilon u^2}.
\]

The two collision integrals depend smoothly on \((A,y,\varepsilon)\).  The
nonzero Jacobian above lets the implicit-function theorem continue the exact
collision to functions \(A(\varepsilon)\) and \(y(\varepsilon)\) for all
sufficiently small \(\varepsilon\).

For every sufficiently small \(\varepsilon>0\), the continued hostile source
is:

- smooth;
- strictly positive;
- strictly decreasing;
- strictly log-concave, since

  \[
  (\log f_{A,\varepsilon})''=-2\varepsilon<0;
  \]

- minimum-phase by the positive layer-cake factorization;
- tangent to the imaginary axis at a nonzero half-transform value.

Thus smooth strict log-concavity does not exclude the remaining cosine
collision.

## Consequence for the theta programme

The following source properties are now all insufficient:

- positivity;
- smoothness;
- strict decrease;
- strict log-concavity;
- minimum phase;
- positive real-axis sine orientation;
- finite-support endpoint retention.

The surviving distinction cannot be an unlabelled shape constraint on the
aggregate density.  It must involve structure absent from the exponential
family, most plausibly:

- the integral winding-label decomposition;
- Poisson/modular coherence among those labels;
- an arithmetic restriction on which current redistributions are authorized;
- a nonlocal theta identity stronger than pointwise curvature.

This agrees with the earlier all-order sign-regularity theorem: the labelled
integral carrier has rigid square separation, while scalar aggregation can
erase that protection.

## Deutsch--Popper revision

The conjecture should no longer say that a positive, decreasing, or strictly
log-concave source has transverse half-transform crossings.  All three claims
are false.

The hard-to-vary conjecture is:

> The labelled modular theta constructor forbids the specific current
> redistribution required for a multiple real zero, even though the same
> aggregate shape properties permit it in hostile sources.

The next task is to express the collision equations before label summation and
identify the coherence residual that the exponential hostile cannot satisfy.

## Result

Strict log-concavity is not the missing RH force.  A smooth family of
positive strictly decreasing strictly log-concave sources contains exact
tangent cosine zeros.  The remaining programme must return to labelled
modular coherence rather than strengthen scalar source curvature.
