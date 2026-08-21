# The primitive Mobius half-line cannot discretize the zeta spectrum

Epistemic-graph event: 1395.

## Source-derived candidate

The admitted eight-point primitive half-line atlas has a candidate medial
Mobius carrier with fundamental core `pi_1 congruent Z`.  Conditional on the
missing primitive PC quotient, ordered normal signs select the orientation
local system.  Thus the strongest available boundary data are:

- one cyclic core; and
- holonomy `eta=+1` or `eta=-1`.

No metric length or identification of that core with logarithmic scale is
source-derived.

## Dilation compactification

Grant the candidate its strongest analytic realization.  Put `y=log x`,
choose a positive circumference `L`, and impose

`f(y+L)=eta f(y)`

on the dilation generator

`D_L=-i d/dy`.

This gives a self-adjoint operator with compact resolvent.  Its eigenvalues
are exactly

`lambda_n=2 pi n/L`, if `eta=+1`,

and

`lambda_n=(2n+1)pi/L`, if `eta=-1`.

The holonomy changes only the half-spacing offset.  The positive spectral
count is linear:

`N_D(T)=L T/(2 pi)+O(1)`.

## Hostile comparison with zeta zeros

The Riemann--von Mangoldt count of positive nontrivial-zero ordinates is

`N_zeta(T)=T/(2 pi) log(T/(2 pi))-T/(2 pi)+O(log T)`.

Its leading growth is `T log T`, not `T`.  Therefore no fixed `L` and neither
available holonomy can make the compactified dilation spectrum equal the
zeta-zero ordinates, even asymptotically.

This failure is stronger than the missing length datum.  Fitting `L` to one
or finitely many zeros cannot repair the Weyl-law mismatch.  The determinant
of the circle operator is correspondingly trigonometric, not `xi`.

## Typing verdict

The primitive Mobius carrier supplies topological cyclicity and a sign local
system, but not the scale-dependent phase-space volume needed for the
`T log T` zero count.  It is therefore falsified as the requested direct
boundary quotient of Mellin dilation.

This does not rule out an infinite graph, energy-dependent boundary,
noncompact scattering quotient, or a higher-dimensional phase space.  Any
such replacement is additional structure and must be source-derived without
using `xi` or its zeros as input.

## Scope

The Mobius carrier itself remains conditional on its missing PC matching
maps.  The no-go grants those maps and the most favorable analytic circle
realization, so the spectral mismatch is independent of that earlier gap.
