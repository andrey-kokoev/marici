# Ordered-pair radial Stokes generalizes, but does not authorize, the response target

Date: 2026-09-08

## Correction to the diagonal claim

The previous packet called the diagonal obstruction closed after defining the
combined response to be `R+2E`.  That wording was too strong.  The identity is
an exact source formula for the response *required* by cancellation, but
placing that response in the fixed conservative G4 column is precisely the
missing source-authority theorem.  Defining a port by the cancellation it must
produce would be circular.

## Ordered-pair identity

The radial Stokes relation is not restricted to diagonal theta labels.  For any
ordered pair of sufficiently rapid source atoms `f,g`, set

\[
\rho_{f,g}(t)=\int_a^b f(u)g(u+t)\,du,
\]

\[
e_{f,g}(t)=\frac12[f(b)g(b+t)-f(a)g(a+t)],
\]

and

\[
w_{f,g}(t)=\int_a^b
[f'(u)g(u+t)-f(u)g'(u+t)]\,du.
\]

Integration by parts gives

\[
\rho_{f,g}'=e_{f,g}-\frac12w_{f,g}.
\]

Therefore every ordered pair has the Laplace identity

\[
zR_{f,g}-\rho_{f,g}(0)
=E_{f,g}-\frac12W_{f,g}.
\]

The algebraically required combined response is uniformly

\[
I_{f,g}^{({\rm resp})}=R_{f,g}+2E_{f,g}.
\]

If a source comparison realizes this response in the conservative column,
then ordinary plus endpoint plus response vanishes parameterwise for every
ordered pair and every jet.  Diagonal and off-diagonal cases need no different
Stokes formula; product and ratio labels remain in `rho_{f,g}`.

## Exact remaining theorem

The live question is not deriving another cancellation formula.  It is proving
a crossing map

\[
\mathcal T_{\rm pair\to G4}:
\mathcal G_{\rm pair,rad}
\longrightarrow
\mathcal G_{\rm conservative}
\]

from an independently declared arithmetic/Green constructor such that its
response readout equals `R+2E`, while preserving:

- ordered pair, product, ratio, prime, and grade labels;
- shell concatenation;
- reciprocal and analytic-transpose orientation;
- the fixed five-port metric and adjoint;
- the Evans history and Xi seam mismatch;
- completion and all multiplicity jets.

Without this map, `R+2E` is a uniquely specified response target, not an
inhabitant of the physical G4 port.  With it, pairwise normal convergence would
allow theta-label and shell assembly.

## Disposition

Prior research has already fixed the complete pairwise density that a valid G4
response must realize.  It has not supplied the independent pair-to-G4
crossing.  The correction prevents a tautological cancellation from being
mistaken for the RH-bearing chain map.
