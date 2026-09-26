# Two-polarization shear selects area and parallel-frame transport

## Result

The preceding characteristic selection extends beyond fixed polarization.
A full positive, determinant-one transverse shape history C(u), corner area
and expansion, and an initial observer frame determine a local vacuum Rosen
plane wave and its parallel-frame transport before a caustic.

A rotating shape contributes to focusing even if its instantaneous eigenvalues
are constant. Ignoring this contribution produces a nonvacuum metric. An
explicit closed shape path also produces a nonzero comparison rotation of the
parallel frame relative to retained endpoint axes. This is not the earlier
four-sign eigenframe ambiguity and is not a closed spacetime-loop holonomy.

The complete shape history remains supplied characteristic data. This is an
Einstein-sector reconstruction theorem, not selection of that data by fibration.

## Full shape instead of one polarization scalar

Use Rosen coordinates with

    ds^2=-2du dV+gamma_ab(u)dX^a dX^b,
    gamma=r^2 C,    C=C^T>0, det C=1, r>0.

The symmetric determinant-one 2 by 2 matrix C carries two functional degrees
of freedom. Write M=C^-1 C'. Then tr M=0. M need not be symmetric in ordinary
coordinate components; it is self-adjoint in the C metric and similar to the
symmetric matrix C^-1/2 C' C^-1/2. Thus tr(M^2)>=0.

For a general Rosen transverse metric,

    Ric_uu=-(1/2)tr(gamma^-1 gamma'')
            +(1/4)tr(gamma^-1 gamma' gamma^-1 gamma'),

with all other Ricci components zero. Substituting gamma=r^2 C gives

    Ric_uu=-2r''/r-(1/4)tr(M^2).

Hence the vacuum focusing equation is

    r'' + [tr(M^2)/8] r=0.

For supplied C(u), r(u0)>0 and r'(u0), a linear ODE fixes r locally. Restrict
to r>0. The earlier polarized result follows from
C=diag(exp(2 beta),exp(-2 beta)), for which tr(M^2)=8 beta'^2.

The null shear endomorphism is M/2 and its squared norm is tr(M^2)/4. This is
the same affine, twist-free characteristic congruence as the previous Rosen
construction; fixing u and transverse labels remains part of the data.

## Observer transport is another determined equation

Along the central unit timelike geodesic X=Y=0, u=V=tau/sqrt(2), the transverse
connection in the coordinate basis is

    Gamma_u=(1/2)gamma^-1 gamma'.

Let F(u) have columns equal to the transverse observer frame vectors in Rosen
coordinates. Parallel transport is

    F'=-Gamma_u F,
    F(u0)^T gamma(u0) F(u0)=I.

Differentiating verifies F^T gamma F=I throughout the interval. Thus a specified
initial orthonormal frame determines the transported frame. This does not
require diagonalizing curvature at every instant and remains regular when
its eigenvalues cross, provided the metric/chart remains regular.

The coordinate curvature is

    R_uaub=-(1/2)gamma''+(1/4)gamma' gamma^-1 gamma'.

The unit observer's transverse tidal tensor in its parallel frame is

    E=(1/2) F^T [R_uaub] F.

The factor 1/2 is from du/dtau=1/sqrt(2). The longitudinal electric components
vanish. These equations keep coordinate components, orthonormal readouts and
observer normalization separate.

## A constant-anisotropy, rotating-shape example

Let

    D=diag(p^2,p^-2), p=6/5,
    R(u)=[[cos u,-sin u],[sin u,cos u]],
    C(u)=R(u) D R(u)^T.

Put

    s=(p^2-p^-2)/2=671/1800,
    c=(p^2+p^-2)/2=1921/1800.

Then c^2-s^2=1 and

    tr[(C^-1 C')^2]/8=s^2.

Although the eigenvalues of C are constant, its shear is not zero: the axes
rotate. With corner data r(0)=1, r'(0)=0,

    r(u)=cos(su).

Because 0<s<1/2, r stays positive over 0<=u<=pi. This produces an exact vacuum
solution over one complete shape loop without crossing a Rosen caustic.
Setting r=1 while retaining this rotating C gives Ric_uu=-2s^2, not vacuum.

## Closed shape and an explicit transport comparison

An instantaneous orthonormal shape-axis frame is

    B(u)=r(u)^-1 R(u) D^-1/2.

It is not parallel. Let J=[[0,-1],[1,0]]. A direct calculation gives

    B^-1(B'+Gamma_u B)=c J.

Consequently the parallel frame with F(0)=D^-1/2 is

    F(u)=B(u) R(-cu).

This formula solves the actual connection equation, rather than choosing a
rotation after seeing the endpoint. The shape closes at u=pi:

    C(pi)=C(0)=D.

Area does NOT close: r(pi)=cos(s pi), so the full metric gamma does not return.
Use the retained endpoint coordinate axes, orthonormalized at the new area,

    B_ref(pi)=r(pi)^-1 D^-1/2.

Then

    F(pi)=B_ref(pi) R((1-c)pi),
    (1-c)pi=-121*pi/1800.

The comparison rotation is nonzero and not just a V4 sign flip. It is meaningful
relative to the declared Rosen congruence/labels, endpoint reference and initial
frame. Without those retained identifications it is not an absolute comparison
of vectors at different events. Reframing the endpoint convention changes the
reported matrix, as expected.

Multiplying F by r removes the isotropic area factor. The normalized frame
obeys

    (rF)'=-(1/2)C^-1 C' (rF).

Thus the nonzero return can be described mathematically as transport around
a loop in SHAPE space using this connection. Its curvature is

    dA+A wedge A=-(1/4)(C^-1 dC) wedge (C^-1 dC),
    A=(1/2)C^-1 dC.

Noncommuting shape changes can therefore retain path information. This shape-
space holonomy must not be confused with a loop of spacetime events: the
observer follows an open timelike segment, and the scale changes along it.
Nor does the construction prove an asymptotic gravitational memory observable.
The isotropic limit p=1 gives c=1, s=0 and zero comparison rotation, as required.

## What is selected and what remains free

The reconstructed packet is

    full shape C(u), corner (r0,r1), gauge/normalization, initial frame
        -> area r(u), vacuum metric gamma(u), parallel frame F(u), tidal E(u).

It contains both polarizations within the plane-wave ansatz. The earlier
single-polarization scalar equation did not determine the missing rotating
shape data. A list of shape eigenvalues alone also fails: it omits the very
axis rotation that contributes to the focusing coefficient and transport.

Thus the physical selector is the complete boundary geometry, not just its
spectrum. The law determines the response to that geometry, not which boundary
history nature supplies. No measure on histories, matter-to-radiation map or
derivation of Einstein's equation has been added.

## Verification

Run:

    python research/voevodsky/check_two_polarization_characteristic_selection.py

All 45 exact rational checks passed. The checker independently builds the full
four-dimensional Christoffel symbols, their derivatives and Ricci tensor from
rational metric 2-jets, then checks the rotating-shape focusing and curvature
identities at three rational rotation points and two radial jets each. It also
checks the moving-frame connection, cancellation by the parallel rotation,
nonvacuum result from ignoring rotation, and endpoint coefficients.

The rational jets obey r''=-s^2 r. The all-u trigonometric solution, positivity
over the loop and general ODE uniqueness are written arguments, not inferred
from sampling. The checker does not numerically integrate transport or prove
a general characteristic Einstein theorem.

Receipt: `research/voevodsky/two-polarization-characteristic-selection.json`.
The new implementation uses only the standard library and exact Fractions.

## References and boundary

- `research/voevodsky/characteristic-shear-and-corner-data-select-a-plane-wave.md`
- `research/voevodsky/exact-vacuum-plane-wave-realizes-tidal-eigenframe-return.md`
- `research/voevodsky/tidal-eigenframes-form-stratified-descent-data.md`

The remaining unrestricted problem is causal constraint/evolution gluing for
local Einstein solutions beyond this symmetry reduction. Within the present
sector, reconstruction and transport are explicit. Further claims should be
measured against that boundary rather than counted as progress merely because
another finite fixture passes.
