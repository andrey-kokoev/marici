# Local Tate defect channels exist off seam and change variance with height

Author: `marici.Grothendieck`

Date: 2026-08-26

Status: exact local falsifier and global scope reduction

## Question

The coisometry audit leaves a tempting source-support theorem: perhaps the
theta/Tate incidence authorizes defect ports only on the critical seam.  The
smallest honest test is one finite Tate place, before global completion.

Put

\[
 a=p^{-1/2},\qquad L=\log p,\qquad z=\sigma+it,
\]

and use the reciprocal local transition

\[
 \gamma_p(z)=\frac{1-ae^{-zL}}{1-ae^{zL}}.
\]

## Exact defect

Direct expansion gives

\[
 1-|\gamma_p(z)|^2
 =
 \frac{
 4a\sinh(\sigma L)
 \bigl(a\cosh(\sigma L)-\cos(tL)\bigr)
 }{|1-ae^{zL}|^2}.
\]

Hence the local defect vanishes identically on the seam
\(\sigma=0\), as required by local Tate unitarity.  Away from the seam it is
generically nonzero.  More strongly, its sign is not determined by the open
half-sector.

For any nonzero \(\sigma\) sufficiently close to the seam so that

\[
 a\cosh(\sigma L)<1,
\]

the bracket is negative at \(t=0\) and positive at
\(t=\pi/L\).  Thus a fixed local factor changes between contractive and
expansive behavior under vertical Mellin translation while remaining in the
same open half-sector.

The reciprocal sheet has the opposite normalized defect:

\[
 1-|\gamma_p(z)^{-1}|^2
 =-\frac{1-|\gamma_p(z)|^2}{|\gamma_p(z)|^2}.
\]

## Consequences

Local source incidence does not confine defect spaces to the critical seam.
Julia defect channels exist off seam, and their variance changes with the
vertical phase.  Therefore none of the following can be the missing RH law:

1. factorwise absence of defect channels in each open half-sector;
2. a factorwise contractive orientation chosen only from the sign of
   \(\Re z\);
3. a positive direct sum of local Julia defects whose cancellation is
   expected globally;
4. universal two-sector unitary dilation, which exists for every contraction
   and therefore has no zero-confining force.

A positive direct sum cannot cancel opposite local variances.  If a global
support law survives, it must glue the signed local incidences before positive
defect-space formation, or pass to a source-derived global quotient that is
not the factorwise Julia dilation.

## Relation to the phase obstruction

The sign-changing factor

\[
 a\cosh(\sigma L)-\cos(tL)
\]

is the local form of the phase information already lost by the positive
theta Hankel square.  Positive metricization retains defect magnitude but
forgets the ordered variance needed for cancellation.  The skew ordered port
retains that variance but has no intrinsic positive orientation.  These are
not competing incomplete proofs; they are two projections of one structural
tradeoff.

The earlier prime-two failure of a local acute cone is therefore not an
isolated numerical pathology.  It is forced by the exact local Tate defect
formula.

## Falsifier and surviving theorem

The seam-only local-support proposal is falsified by any prime \(p\), any
small nonzero \(\sigma\) satisfying
\(p^{-1/2}\cosh(\sigma\log p)<1\), and the two heights

\[
 t_0=0,
 \qquad
 t_1=\frac{\pi}{\log p}.
\]

The defect has opposite signs at these two points.

The surviving theorem-shaped target is irreducibly global:

> Derive a labelled reciprocal incidence form whose signed local defects,
> primitive and square boundary currents, and archimedean channel assemble
> before positive completion into a phase-sensitive global conservation law.

This calculation does not approach RH by another positivity reformulation.
It removes an impossible locality assumption from the remaining global
conservation programme.
