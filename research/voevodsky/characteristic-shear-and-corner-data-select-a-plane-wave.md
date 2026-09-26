# Characteristic shear and corner data select a polarized plane wave

## Result

There is a physically typed selection interface in the exact plane-wave sector:

    complete null shear history + corner area/expansion + coordinate/frame gauge
       -> unique local vacuum solution in the declared ansatz.

Einstein's null focusing equation fixes the remaining area function. It does
not choose the shear history or the corner data. Thus this is a genuine
boundary-value section of the solution family, not an intrinsic selection of
one universe from fibration alone.

An explicit rational-power family also realizes a previously missing feature:
a geodesic observer encounters zero tidal curvature at one event and a simple
spectrum nearby. Its transported frame survives while the instantaneous tidal
frame loses all determining power at that event.

## Relation to prior results

- `research/voevodsky/exact-plane-wave-overlap-gluing-and-characteristic-freedom.md`
  showed compatible local patches with distinct extensions beyond their common
  characteristic data.
- `research/voevodsky/exact-vacuum-plane-wave-realizes-tidal-eigenframe-return.md`
  supplied the observer and tidal readout for Brinkmann waves.
- `research/nima/marici-machian-gravity-direction.md` requires the complete
  gravitational state, not matter alone, and retains symmetric frame strata.

A repository search for Rosen coordinates, Raychaudhuri and characteristic
shear found no prior matching gravitational implementation. This note adds a
bounded characteristic reconstruction, not a general double-null Einstein
existence theorem. The vacuum law is an admitted physical input throughout.

## A real null boundary, not an incorrectly labelled coordinate slice

Use polarized Rosen coordinates (u,V,X,Y):

    ds^2=-2 du dV+p(u)^2 dX^2+q(u)^2 dY^2,
    p=r exp(beta), q=r exp(-beta), r>0.

Both u=constant and V=constant are null hypersurfaces. Along a generator of
V=constant with X,Y fixed, u is affine. The transverse metric is

    gamma=r^2 diag(exp(2 beta),exp(-2 beta)).

This must not be confused with v=constant in the earlier Brinkmann metric:
there g^vv=-K, so such a surface is not generally null. The coordinate change
below supplies the appropriate characteristic surface.

The optical expansion and squared shear for this congruence are

    theta=2 r'/r,
    sigma_ab sigma^ab=2 beta'^2.

In this polarized setting beta (up to its initial value) encodes the conformal
shape/shear history. Its interpretation presumes the affine parameter and
transverse labels have been fixed; a rescaling of null normals changes the
numerical optical data.

## Einstein's focusing equation

Direct calculation gives the only potentially nonzero Ricci component:

    Ric_uu=-(p''/p+q''/q)=-2(r''/r+beta'^2).

Hence vacuum is precisely

    r'' + beta'^2 r = 0.

This is the affine null Raychaudhuri equation in this symmetry-reduced ansatz.
For supplied sufficiently smooth beta on an interval and corner values

    r(u0)=r0>0, r'(u0)=r1,

ordinary linear ODE existence and uniqueness fixes r. Restrict to the interval
where r>0 so the Rosen chart is nonsingular. The boundary data can equivalently
specify initial area and expansion theta0=2r1/r0. Beta(u0), the coordinate scale,
transverse orientation and null normalization must also be retained.

A zero of r is a failure of this chart/optical description; this construction
does not automatically identify it with a curvature singularity or supply a
continuation through a caustic.

Thus the null conformal geometry and corner expansion are not arbitrary output
fittings: they are independently specifiable characteristic geometric data.
Their physical values still require a state/preparation/boundary prescription.
The field equation enforces their compatibility and propagates the area.

## Explicit comparison with the Brinkmann tidal readout

Set

    x=p X, y=q Y,
    v=V+(1/2)[p p' X^2+q q' Y^2].

Then the Brinkmann metric has profile

    A=diag(p''/p,q''/q).

The cross du dX and du dY terms cancel. The du^2 coefficient cancellation
in each direction is

    -(p p')' + p'^2 + (p''/p) p^2 = 0.

Under focusing, the profile is trace-free and

    A_11=beta''+2(r'/r) beta', A_22=-A_11.

The earlier central timelike geodesic and parallel spatial frame therefore
apply, with E_transverse=-A/2 and E_33=0. The entire field-to-observer map is
explicit; it is not a spectral matrix attached after solving an unrelated
ODE. Notice that reconstructing A requires the boundary shear AND expansion,
not just beta at a single point.

## Exact family and necessity of corner data

On u>0 choose

    beta=(3/10) log u.

The focusing equation becomes

    r''+(9/100)u^-2 r=0,

with basis solutions

    r_a=u^(9/10), r_b=u^(1/10).

Their Wronskian is -4/5, so every pair of corner values at u=1 selects unique
coefficients in r=c_a r_a+c_b r_b. Positive coefficients give r>0 on u>0.

For r=r_a,

    p=u^(6/5), q=u^(3/5),
    A=diag(6/25,-6/25)/u^2.

For r=(r_a+r_b)/2, the shear history and corner area r(1)=1 are identical,
but the initial expansion differs:

    r_a'(1)=9/10, r_mixed'(1)=1/2.

At the corner,

    A_11,a(1)=6/25,
    A_11,mixed(1)=0.

Thus shear history plus area alone does not select the solution. The corner
expansion is indispensable data. This provides a discriminating control for
the selection interface rather than simply announcing ODE uniqueness.

## A realized stabilizer change

For the mixed solution,

    A_11(1)=0, A_11'(1)=12/125 != 0.

Therefore E=0 at the observer event u=1 and has three distinct eigenvalues
(-A_11/2,0,A_11/2) in a sufficiently small punctured neighborhood. The local
spatial stabilizer changes from the generic four-element V4 to SO(3) at that
event. The parallel observer frame remains regular through it.

This is a zero-curvature EVENT of a nonflat solution, not a flat neighborhood.
Curvature derivatives are nonzero; a richer retained local jet can carry
orientation information that the instantaneous E readout loses. We do not
claim that the full local geometry has SO(3) symmetry there, only that the
zeroth-order electric tidal tensor has that stabilizer.

Since A_11 changes sign, a nondecreasing eigenvalue convention interchanges
the two transverse eigenlines through the collision. Fixed transported axes
continue, but the instantaneous tensor cannot select their ordering or signs
at the zero. Retaining observer/history data is useful precisely at this
forgetful boundary.

## What a no-shear condition selects

If beta'=0 on the entire relevant interval, focusing gives r''=0. Then
p and q are constant multiples of an affine r, so A=0: the metric is flat
where the chart is regular. Nonzero expansion of this shear-free congruence
can be coordinate/optical data rather than gravitational curvature.

Within THIS polarized plane-wave sector, a no-shear boundary history therefore
selects a no-wave solution. It does not select a Newtonian field or a nonzero
gravity law. Nor is this a theorem that every shear-free vacuum geometry is
flat. Adding nontrivial radiation requires nontrivial supplied boundary data.

## Fibration/section interpretation

Let the base consist of admissible tuples

    (beta(u),r0,r1,u0,affine/null normalization,transverse frame conventions).

Over each tuple, retain solutions of the focusing equation together with their
corner compatibility and observer realization. Before caustics, within the
fixed ansatz, the metric-function solution is unique. ODE evolution supplies
a section. If the base forgets r1, the preceding pair lies in one fiber but
has distinct tides. If it forgets the full beta history and retains only its
restriction to an overlap, the earlier radiative extension freedom returns.

This explains how a physical boundary condition selects a solution without
pretending that the general fibration primitive selects the boundary condition.
No probability distribution over the boundary histories is supplied here.
That would require additional statistical or quantum state input.

## Verification

Run:

    python research/voevodsky/check_characteristic_shear_selection.py

All 21 exact rational-power checks passed. They verify focusing, vacuum trace,
common conformal shear, coordinate cancellation, corner values and Wronskian,
selection of the mixed solution, distinct tidal readouts, the nonzero derivative
through the flat event, the shear-free flat control and rejection of an area
function that violates focusing.

Receipt: `research/voevodsky/characteristic-shear-selection.json`.
The checker manipulates finite sums of rational powers of u on u>0; no numerical
ODE integrator or floating-point approximation is used. General ODE uniqueness,
the all-profile Ricci formula and geometric interpretation are written
mathematics, not new proof-assistant theorems. This is an exact finite family
and a general reduced-ODE argument, not an unrestricted characteristic PDE solver.

## Current gain

The selection question has an explicit answer in one nontrivial sector:
complete characteristic shear and corner geometry determine the vacuum field
and its observer tidal record. We have also realized a genuine change of tidal
stabilizer along an exact solution. Neither step derives the boundary state,
Einstein dynamics or a preferred frame solely from fibration.
