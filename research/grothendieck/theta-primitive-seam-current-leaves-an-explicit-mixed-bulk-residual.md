# Theta primitive seam current leaves an explicit mixed bulk residual

## Centered doubled flow

Put \(z=\delta+i\tau=s-1/2\). After removing the common \(1/2\) decay,
write the two reciprocal tail variables as

\[
 \psi_+'=-z\psi_+-F,
 \qquad
 \psi_-'=\bar z\psi_--F,
\]

where \(F(q)\) is the real source forcing in the common theta frame.

Introduce symmetric and antisymmetric coordinates

\[
 m={\psi_++\psi_-\over\sqrt2},
 \qquad
 d={\psi_+-\psi_-\over\sqrt2}.
\]

Their exact equations are

\[
 m'=-i\tau m-\delta d-\sqrt2F,
\]

and

\[
 d'=-\delta m-i\tau d.
\]

The forcing is symmetric: it disappears from the equation for \(d\).

## Polarized flux

The native indefinite current and positive bulk are

\[
 J=|\psi_+|^2-|\psi_-|^2
 =2\operatorname{Re}(m\bar d),
\]

and

\[
 N=|\psi_+|^2+|\psi_-|^2
 =|m|^2+|d|^2.
\]

Direct differentiation gives

\[
 2\delta N
 =-J'-2\sqrt2\operatorname{Re}(F\bar d).
\]

This is the exact forced residual against Nima's hyperbolic splitting.

## Canonical primitive seam antiderivative

Retain the primitive seam variable

\[
 H(q)=\int_0^qF(v)\,dv,
 \qquad H'=F.
\]

The only immediate local current that differentiates to the forcing
polarization is

\[
 J_H=2\sqrt2\operatorname{Re}(H\bar d).
\]

Using

\[
 \bar d'=-\delta\bar m+i\tau\bar d
\]

gives

\[
 J_H'
 =2\sqrt2\operatorname{Re}(F\bar d)
 +2\sqrt2\operatorname{Re}
 \left(-\delta H\bar m+i\tau H\bar d\right).
\]

Therefore the completed identity after primitive seam retention is

\[
 2\delta N
 =-(J+J_H)'+R_{\mathrm{mix}},
\]

where

\[
 R_{\mathrm{mix}}
 =-2\sqrt2\delta\operatorname{Re}(H\bar m)
 +2\sqrt2\operatorname{Re}(i\tau H\bar d).
\]

## Consequence

The primitive seam current cancels the explicit forcing term, but it does not
close the conservation law. It transports the obstruction into a mixed
seam--bulk bilinear residual.

This residual is generically nonzero. On the real centered ray
\(\tau=0\), it reduces to

\[
 R_{\mathrm{mix}}
 =-2\sqrt2\delta\operatorname{Re}(H\bar m).
\]

On the critical seam \(\delta=0\), it reduces to

\[
 R_{\mathrm{mix}}
 =2\sqrt2\operatorname{Re}(i\tau H\bar d).
\]

Neither term vanishes from reciprocal symmetry alone.

## Next typed gate

Any closing current must come from a source channel whose derivative equals
\(-R_{\mathrm{mix}}\) before endpoint evaluation. The remaining candidates
are the prime-square channel, the Clark shear, and the archimedean modular
boundary. A scalar cancellation after integration is insufficient.

The smallest falsifier is one finite labelled source for which the declared
square and archimedean currents leave either coefficient of
\(H\bar m\) or \(H\bar d\) nonzero.

## Scope

This is an exact local calculation for the centered forced doubled tail
system. It proves that primitive seam retention alone is insufficient. It
does not yet include the square, Clark, or archimedean currents and therefore
does not close the full conservation route.
