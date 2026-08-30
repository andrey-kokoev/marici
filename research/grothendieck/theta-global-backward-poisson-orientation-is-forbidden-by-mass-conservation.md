# Theta global backward-Poisson orientation is forbidden by mass conservation

## Bounded question

Can the completed theta autocorrelation satisfy a pointwise one-sign comparison
between forward and backward Poisson continuation at every spectral height?

## Poisson evolution

Let

\[
\rho(t)=|\widehat f(t)|^2\ge0
\]

be the autocorrelation spectrum. Up to Fourier normalization, the forward
Poisson evolution is

\[
C(a,\cdot)=e^{-a|D|}\rho,
\qquad a>0.
\]

For the rapidly decaying theta source, the analytic continuation considered in
packet 232 is

\[
C(-a,\cdot)=e^{a|D|}\rho
\]

on its domain of existence.

## Conserved total mass

Both multipliers equal (1) at zero frequency. Whenever the continued
functions are integrable,

\[
\int_{\mathbb R}C(a,t)\,dt
=\int_{\mathbb R}\rho(t)\,dt
=\int_{\mathbb R}C(-a,t)\,dt.
\]

Therefore

\[
\int_{\mathbb R}
\left(C(a,t)-C(-a,t)\right)dt=0.
\]

## Global sign no-go

If the difference were nonnegative everywhere and strictly positive on a set
of positive measure, its integral would be positive. The same contradiction
holds for a nonpositive difference. Hence a nontrivial integrable source cannot
satisfy either global strict orientation

\[
C(a,t)>C(-a,t)
\]

or its reverse for all (t).

The difference must vanish identically or change sign. Thus the global theorem
proposed at the end of packet 232 is too strong.

## Consequence for the RH programme

RH does not require orientation at every spectral height. It requires a
conservation law on states satisfying the source-derived zero boundary
condition. The backward-Poisson comparison must therefore be restricted by the
Evans kernel relation or another reciprocal state equation before a sign can be
possible.

This explains why universal vertical-modulus monotonicity repeatedly met
hostile examples: mass conservation forbids it at the level of the unrestricted
boundary spectrum.

## Connection to reciprocal backreaction

The one-way boundary-control system has forward source incidence but no adjoint
return channel. Without that lower block, its admissible states are not a
self-adjoint or Lagrangian subspace on which the conserved-mass obstruction can
be refined.

The next constructor must first add source-derived reciprocal backreaction and
then ask for orientation only on its kernel states. Pointwise orientation of
the unrestricted Poisson field is now a closed branch.

## Scope

This packet disproves global one-sign forward-versus-backward Poisson
orientation under the stated integrability assumptions. It does not rule out
orientation on a source-derived Evans kernel or prove RH.
