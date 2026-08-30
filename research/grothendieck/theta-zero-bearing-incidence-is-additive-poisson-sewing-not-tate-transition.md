# Theta zero-bearing incidence is additive Poisson sewing, not Tate transition

## The exact global split

Let `f` be the standard self-dual Schwartz--Bruhat source on the adeles, with
the fixed self-dual Haar normalization.  The Tate zeta integral is

\[
 Z(f,s)=\int_{\mathbb A^\times}f(x)|x|^s\,d^\times x.
\]

Split the ideles at `|x|=1` and apply Poisson summation to the inner chamber.
With the conventional boundary orientation, the meromorphic continuation is

\[
\boxed{
 Z(f,s)=A_f(s)+A_{\widehat f}(1-s)
 +{\widehat f(0)\over s-1}-{f(0)\over s},}
\]

where

\[
 A_f(s)=\int_{|x|\ge1}f(x)|x|^s\,d^\times x.
\]

For the self-dual standard source, `f=hat(f)` and `f(0)=hat(f)(0)`.  The
completed entire readout is obtained only after retaining both reciprocal
bulk terms and both polar boundary currents.

## Division of labor

Packets 174--176 show that finite-place Tate transitions form invertible
anomaly lines with a perfect reciprocal pairing.  Those transitions cannot
create a divisor.

The displayed continuation formula identifies the distinct zero-bearing
operation:

\[
\boxed{
\text{multiplicative Tate transition transports the coefficient type;}
\quad
\text{additive Poisson sewing forms the scalar section}.}
\]

A zero is therefore cancellation in the four-channel incidence

\[
 A_f(s),
 \qquad
 A_{\widehat f}(1-s),
 \qquad
 {\widehat f(0)\over s-1},
 \qquad
 -{f(0)\over s},
\]

not failure of any local `gamma_p` transition.

## Two sectors secretly presenting one section

The reciprocal half-planes are not two scalar functions later declared
equal.  They are two convergent presentations entering one Poisson-sewn
relative section.  Their common value type is protected by the invariant
anomaly-line pairing, while their additive incidence can lose transversality.

This makes the geometry precise:

\[
\boxed{
\text{two complementary localizations}
\longrightarrow
\text{one completed relative section}
\longrightarrow
\text{possible scalar cancellation}.}
\]

The critical seam is fixed before the zero question by reciprocal duality.
RH would require the additional theorem that this particular four-channel
source incidence cannot cancel off that seam.

## Green-current consequence

The cutoff-invariant pairing from packet 176 is the carrier for the boundary
current, but its zero-bearing insertion must be the Poisson incidence above.
A candidate Green identity must therefore retain four typed terms before
aggregation.  In particular, cancellation of an Euler anomaly against an
archimedean pole after scalar summation is not a source-local proof.

At finite cutoff `X`, write `I_X(s)` for the source-derived approximation to
the four-channel incidence and `U_(X,Y)` for Tate transport.  The required
descent law is

\[
\boxed{
 I_Y\circ U_{X,Y}=I_X}
\]

as a boundary-bearing map, with the primitive and square anomaly coordinates
retained.  Its defect

\[
 \mathfrak D_{X,Y}=I_YU_{X,Y}-I_X
\]

is the exact typed residual to compute next.

## Scope

The global split is the standard Tate--Poisson continuation identity.  This
packet does not prove that the four-channel incidence is nonzero off the seam,
nor that a proposed finite Euler approximation satisfies the required descent
law.  It identifies where the divisor can and cannot live.

The hostile symmetric multiplier now has a precise burden: it may preserve
the transition lines and reciprocal pairing, but it must supply a new
four-channel Poisson incidence.  Without such a source lift it is not an
authorized modification of the distinguished section.
