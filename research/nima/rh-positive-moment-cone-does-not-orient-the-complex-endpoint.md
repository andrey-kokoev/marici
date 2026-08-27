# RH positive moment cone does not orient the complex endpoint

## Result

The most natural source cone is the cone of moment sequences of positive measures. It is pointed, has full linear span, and is preserved by real translation and the associated Pascal moment transport.

Nevertheless, the complex endpoint transform can vanish off seam on this cone.

Take the positive measure

\[
\mu=\delta_0+2\delta_1.
\]

Its moment sequence is Hankel-positive by construction. Its exponential endpoint transform is

\[
F(z)=1+2e^z.
\]

At

\[
e^z=-\frac12,
\]

we obtain \(F(z)=0\). Equivalently,

\[
z=-\log 2+(2k+1)\pi i,
\]

which has nonzero horizontal displacement.

Thus a positive source measure, positive Hankel matrices, and translation-stable moment cone do not imply complex zero-reflection.

## Why the cone argument fails

For real spectral displacement, the exponential evaluation may lie in the dual positive cone. Vertical Mellin evolution introduces phases. The complex endpoint functional leaves the real dual cone and positive contributions can cancel.

Grothendieck's pure-label rotation obstruction is the same fact at the ray level: a full phase rotation carries a positive ray to its negative, so no fixed real pointed cone is invariant under all vertical transports.

## Remaining cone variants

A viable nonlinear orientation would need more structure than source positivity:

- a transported cone field rather than one fixed cone;
- a phase-quotiented direct-dual relational cone;
- an acute complex sector whose width remains below \(\pi\);
- a distinguished nonlinear orbit with correlated phases;
- a restricted semigroup rather than the full vertical group.

Each option must still make the endpoint functional strictly zero-reflecting and reject the two-atom hostile.

## DPC verdict

Candidate: positive-measure or Hankel-positive moment cone.

Verdict: rejected by the two-atom off-seam zero.

Candidate: fixed real pointed cone invariant under full Mellin transport.

Verdict: rejected by the phase-flip ray.

Surviving nonlinear target: a source-derived transported relational cone or distinguished orbit carrying phase coherence strong enough to prevent complex cancellation.

## Finite falsifier

Any proposed cone field must be tested on two positive labelled atoms with unequal weights. Transport them to a spectral point where their endpoint phases are opposite. If the transported state remains admissible while its scalar endpoint vanishes, the cone field is not an orientation mechanism.
