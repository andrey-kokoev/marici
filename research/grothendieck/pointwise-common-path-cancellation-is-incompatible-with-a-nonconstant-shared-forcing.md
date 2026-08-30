# Pointwise common-path cancellation is incompatible with a nonconstant shared forcing

## The proposed shortcut

The primitive-lifted Green identity closes if the reciprocal tail solutions
satisfy

\[
u+v=0
\]

throughout the scale interval. It is therefore essential to test whether the
native doubled flow can actually preserve that condition.

Use

\[
u'=-zu-cf,
\qquad
v'=+zv-cf,
\]

with one shared source forcing `f` and nonzero preparation amplitude `c`.

## Exact incompatibility

Assume `v=-u` on an interval. The second flow equation gives

\[
-u'=-zu-cf,
\]

or

\[
u'=zu+cf.
\]

The first equation simultaneously gives

\[
u'=-zu-cf.
\]

Therefore

\[
zu+cf=0,
\qquad
u'=0.
\]

If `z` is nonzero, then `u=-cf/z`; since `u` is constant, `f` must be constant
on the interval. If `z=0`, the relation becomes `cf=0`, impossible for nonzero
`c` and nontrivial `f`.

Hence a nonconstant nontrivial shared forcing admits no nonzero doubled
solution with pointwise common-mode cancellation on an interval.

## Consequence for modular sewing

The common-path residual in the primitive-lifted Green identity cannot be
removed by upgrading terminal Evans cancellation to `u+v=0` everywhere. That
upgrade is incompatible with the source flow itself for the theta forcing.

One of the following must instead occur:

- Fourier--Tate sewing changes the forcing incidence on the reciprocal sheet;
- an additional current differentiates to the common residual;
- the correct doubled variables are not the same-source pair `(u,v)` used
  here;
- the conservation route fails.

This is a strong typing test for any proposed reciprocal construction. If it
uses the same forcing on both signs of `z`, it may not impose pointwise
anti-diagonality except for a constant source.

## Minimal hostile

Take `z=1`, `c=1`, and `f(q)=1+q`. Pointwise `v=-u` would require
`u=-(1+q)`, while the flow comparison requires `u'=0`. The contradiction is
already visible at first derivative order.

## Revised singular gate

The only remaining current route is to derive the reciprocal forcing law
itself from Fourier--Tate transport and recompute the residual. The sign and
boundary incidence of the dual forcing are now load-bearing data. Guessing the
same forcing on both sheets is no longer adequate.
