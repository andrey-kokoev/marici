# The bilateral gluing feature is endpoint minus Wronskian with oriented wall traces cancelling only after summation

## Question

How does the folded free gluing coordinate factor through the completed-theta radial source features?

## Claim boundary

For the whole-line radial derivative source, the gluing coordinate factors exactly as the bilateral endpoint response minus one half of the bilateral Wronskian response. The two oriented half-line formulas each retain the wall trace with opposite incidence signs; that wall pair cancels only in their declared bilateral codiagonal. This constructs the complete source-level feature factorization and all of its parameter jets. It does not identify the feature carrier or codiagonal with G4's authoritative conservative complex.

## Whole-line radial graph

Let the completed-theta shell correlation be defined for every real separation and satisfy

\[
D_t\rho(t)=e(t)-\frac12w(t)=:q(t).
\]

All four functions decay faster than every exponential at both separation ends. Define

\[
R_+(z)=\int_0^\infty e^{-zt}\rho(t)\,dt,
\qquad
R_-(z)=\int_{-\infty}^0e^{-zt}\rho(t)\,dt,
\]

and define \(E_\pm,W_\pm\) by the same oriented domains.

## Two oriented wall identities

Integration by parts on the positive half-line gives

\[
\int_0^\infty e^{-zt}q(t)\,dt
=zR_+(z)-\rho(0)
=E_+(z)-\frac12W_+(z).
\]

On the negative half-line it gives

\[
\int_{-\infty}^0 e^{-zt}q(t)\,dt
=zR_-(z)+\rho(0)
=E_-(z)-\frac12W_-(z).
\]

The wall value is therefore a directed two-port coordinate:

\[
(-\rho(0),+\rho(0)).
\]

It must be retained through the two oriented factors. Deleting it in either factor breaks that factor's Stokes identity.

## Bilateral codiagonal

The canonical fold identifies the free gluing coordinate with

\[
A_z(\mathcal F_uq)
=\int_{\mathbb R}e^{-zt}q(t)\,dt.
\]

Adding the two oriented identities yields

\[
A_z(\mathcal F_uq)
=z\bigl(R_+(z)+R_-(z)\bigr)
\]

and

\[
A_z(\mathcal F_uq)
=E_{\rm bi}(z)-\frac12W_{\rm bi}(z),
\]

where

\[
E_{\rm bi}=E_++E_-,
\qquad
W_{\rm bi}=W_++W_-.
\]

The sewing phase has already cancelled under folding, while the wall traces cancel under the separate oriented codiagonal. These are distinct operations.

## Jet and shell compatibility

Every expression is entire on the whole-line rapid source, so differentiating in \(z\) transports the factorization to every multiplicity jet. Adjacent-shell composition is additive in \(q,e,w\); intermediate shell endpoints cancel before bilateral probing. Ordered-pair reflection transports the negative component through label swap and moving-shell endpoint pushforward, as established in the predecessor packet.

## Minimal feature carrier

Before codiagonalization, the source feature object must retain

\[
\bigl(
-\rho(0),E_+,W_+;
+\rho(0),E_-,W_-
\bigr).
\]

The bilateral readout is the fixed linear map

\[
(-\rho(0),E_+,W_+;
+\rho(0),E_-,W_-)
\longmapsto
E_++E_--\frac12(W_++W_-).
\]

This fixes the Wronskian coefficient \(-1/2\) and the wall orientation at source level. It does not authorize replacing the function-valued \(W_\pm\) by one scalar incidence before the entire probe family is formed.

## G4 conformance gate

A G4 realization must expose a six-coordinate oriented feature carrier or an explicitly faithful equivalent, together with a comparison map that preserves:

1. the two wall signs;
2. endpoint and Wronskian variance;
3. the coefficient \(-1/2\);
4. reciprocal label and moving-shell transport;
5. every entire jet;
6. the bilateral codiagonal only after those checks.

The current SCC witness does not expose this interface. Consequently the source factorization is complete, while canonical G4 identification remains authority- and interface-blocked.

## Direction rescore

- Source-level gluing-feature factorization: completed.
- Identification with G4's boundary carrier: 10/10, but requires Aspect-owned interface exposure.
- Arithmetic loading on the six-coordinate carrier: 9/10, executable once the interface is exposed.
- Universal free cancellation: 0/10.

## Disposition

The bilateral gluing defect is no longer an unspecified boundary feature. It is exactly the codiagonal of two directed wall, endpoint, and Wronskian packets. The next depth-first work is the finite polarized comparison with G4; without authoritative G4 traces and return types, further source manipulation would be redundant. No RH conclusion is authorized.
