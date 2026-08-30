# The moving-endpoint theta flow couples radius and rapidity

## Labelled tails from one source atom

Let

\[
\rho_1(q)=2e^{q/2}e^{-\pi e^{2q}}.
\]

The (n)-th theta label obeys the exact translate law

\[
\rho_n(q)=n^{-1/2}\rho_1(q+\log n).
\]

Put (x=\log n). The reciprocal contributions of this label are samples of
the two moving-endpoint tails

\[
T_+(x,z)
=e^{-(1/2+z)x}\int_x^\infty\rho_1(v)e^{zv}\,dv,
\]

\[
T_-(x,z)
=e^{-(1/2-z)x}\int_x^\infty\rho_1(v)e^{-zv}\,dv.
\]

The full half-Mellin channels are obtained by sampling these tails at
(x=\log n) and summing the labels. Crucially, differentiating either tail
produces the same boundary forcing

\[
f(x)=e^{-x/2}\rho_1(x)>0:
\]

\[
\partial_xT_+=-\left(\frac12+z\right)T_+-f,
\qquad
\partial_xT_-=-\left(\frac12-z\right)T_--f.
\]

This common forcing is source-native. It is exactly what an independently
chosen radial gauge or rapidity shear would generally fail to preserve.

## The coupled Lorentz flow

Define the labelled symmetric and antisymmetric tails

\[
m=\frac{T_++T_-}{2},
\qquad
n=\frac{T_+-T_-}{2}.
\]

Their flow is the forced rank-two system

\[
\partial_xm=-\frac12m-zn-f,
\qquad
\partial_xn=-zm-\frac12n.
\]

The spectral parameter supplies the off-diagonal boost or rotation, while
the positive endpoint atom forces only the symmetric channel. This asymmetry
is not fitted to the scalar section; it follows from differentiating the
shared moving endpoint.

The labelled Lorentz radius

\[
Q=m^2-n^2=T_+T_-
\]

satisfies the exact balance law

\[
(\partial_x+1)Q=-2fm.
\]

Therefore radius and scalar component cannot evolve independently inside the
theta constructor. The common endpoint current is their coupling.

## Radial and rapidity equations

Where (Q\neq0), write

\[
m=R\cosh\chi,
\qquad
n=R\sinh\chi.
\]

The same rank-two flow becomes

\[
\frac{\partial_xR}{R}
=-\frac12-\frac{f}{R}\cosh\chi,
\]

\[
\partial_x\chi
=-z+\frac{f}{R}\sinh\chi.
\]

This is the first exact theta-source law that couples the two deformation
coordinates isolated in the preceding packet. A radial change alters the
rapidity equation through (f/R); a rapidity change alters the radial
equation through \(\cosh\chi\). Preserving the source requires preserving the
same forcing (f) in both equations.

## Scope of the advance

This does not yet prove zero confinement. The equations govern each labelled
moving-endpoint tail before the discrete sum, while the completed scalar zero
is a cancellation after aggregation and multiplication by (P(z)). The
remaining possible loss of meaning is therefore localized more sharply:

1. sampling the continuous tail flow at (x=\log n);
2. summing its labelled solutions;
3. adding the completion carrier;
4. intersecting the resulting global conic with (S=0).

The next theorem must show that the common-forcing balance survives these
four operations as a faithful global current. A scalar identity obtained only
after summing is insufficient; the forcing must remain typed by its moving
endpoint label.

## Hostile falsifier

Start with a reciprocal deformation

\[
T_+\mapsto he^gT_+,
\qquad
T_-\mapsto he^{-g}T_-.
\]

Substitute it into both tail equations. Unless the induced residuals are the
same source function in both equations and equal the translated Gaussian
endpoint current, the deformation is rejected before scalar aggregation.

The sharp hostile question is whether a nontrivial pair (h,g) can preserve
the common-forcing system at every sampled endpoint while changing the
completed divisor. If no such pair exists, the labelled tail flow supplies
canonical-section rigidity. If one exists, it is a direct counterexample to
this route.

## Operator stimulus

The operator's impossible-trajectory formulation led us to identify radius
and rapidity as independent abstract controls. Returning those controls to
the labelled theta source reveals why they are not independently executable:
both are driven by one moving-endpoint boundary atom.
