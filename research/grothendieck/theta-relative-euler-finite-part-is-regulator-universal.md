# Theta relative Euler finite part is regulator-universal

## Admissible regulator class

Let `rho:[0,infinity)->C` be smooth, rapidly decreasing with all required
derivatives, and normalized by

\[
 \rho(0)=1.
\]

Define the source-scale regulated detector

\[
 Z_{\rho,\varepsilon}(s)
 =\sum_{n\ge1}n^{-s}\rho(\varepsilon n^2).
\]

The Gaussian of packet 188 is `rho(x)=exp(-pi x)`, but no Gaussian identity is
used below.

## Mellin representation

Let

\[
 \widehat\rho(z)=\int_0^\infty\rho(x)x^{z-1}\,dx
\]

be the Mellin transform.  Mellin inversion in a common absolute-convergence
chamber gives

\[
 Z_{\rho,\varepsilon}(s)
 ={1\over2\pi i}\int_{(c)}
 \widehat\rho(z)\varepsilon^{-z}\zeta(s+2z)\,dz.
\]

Two poles determine the boundary and constant terms.

## The boundary pole

The pole of `zeta(s+2z)` at `s+2z=1` occurs at

\[
 z={1-s\over2}.
\]

Its residue produces the regulator-dependent boundary current

\[
 B_{\rho,\varepsilon}(s)
 ={1\over2}\widehat\rho\left({1-s\over2}\right)
 \varepsilon^{(s-1)/2}.
\]

For the Gaussian,

\[
 \widehat\rho(z)=\pi^{-z}\Gamma(z),
\]

which recovers packet 188 exactly.

## The universal constant pole

Because `rho(0)=1`, its Mellin transform has a simple pole at `z=0` with
residue one:

\[
 \widehat\rho(z)={1\over z}+O(1).
\]

The residue of the integrand at `z=0` is therefore

\[
 \zeta(s),
\]

independent of the regulator shape.  Further regulator poles lie to the left
and contribute positive powers or controlled logarithmic terms in `epsilon`;
they do not alter the Hadamard constant term away from the usual exceptional
parameters.

Hence

\[
 \operatorname{FP}_{\varepsilon\downarrow0}
 \left[Z_{\rho,\varepsilon}(s)-B_{\rho,\varepsilon}(s)\right]
 =\zeta(s).
\]

## Coherence under regulator change

For two admissible regulators `rho_0,rho_1` with the same value one at the
origin,

\[
 \operatorname{FP}
 \left[
 Z_{\rho_1,\varepsilon}-Z_{\rho_0,\varepsilon}
 -B_{\rho_1,\varepsilon}+B_{\rho_0,\varepsilon}
 \right]=0.
\]

Thus changing the source smoothing chart transports the boundary current but
does not change the relative scalar.  The finite part is a coherence
invariant, not a Gaussian fit.

This is the regulator analogue of the anomaly-line transition law: a bulk
chart change together with its boundary-current change leaves the relative
section fixed.

## Unauthorized finite counterterms

A manually added constant counterterm changes the residue at `z=0` without
arising from a regulator satisfying `rho(0)=1`. It therefore changes the
relative section rather than its presentation.  Likewise, a hostile symmetric
multiplier cannot be implemented by an admissible regulator homotopy unless it
also changes the source incidence.

This supplies a concrete canonical-section rigidity statement within the
regulator class.

## What remains

Regulator universality secures provenance but supplies no orientation. The
universal constant is exactly `zeta(s)`, and it may still vanish. Agreement of
all smoothing charts is one piece of evidence, not multiple independent
positivity mechanisms.

The RH-bearing theorem remains a constraint on the universal finite part
derived from reciprocal Poisson sewing, not a choice of regulator.

## Scope

The theorem applies to smooth rapidly decreasing regulators with normalized
origin and the stated Mellin-contour shifts. Exceptional parameters require
the standard logarithmic finite-part bookkeeping. It proves regulator
covariance and finite-part rigidity, not zero-free orientation.
