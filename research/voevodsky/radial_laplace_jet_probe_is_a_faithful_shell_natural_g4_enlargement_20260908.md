# The radial Laplace-jet probe is a faithful shell-natural G4 enlargement

Date: 2026-09-08

## Source graph

The minimal diagonal response graph retains

\[
(ho,e,w,ho(0)),
\qquad
D_tho=e-\frac12w,
\]

in the rapid translation-history module.  Define the entire Laplace sections

\[
R(z)=\int_0^\infty e^{-zt}\rho(t)\,dt,
\quad
E(z)=\int_0^\infty e^{-zt}e(t)\,dt,
\quad
W(z)=\int_0^\infty e^{-zt}w(t)\,dt.
\]

The canonical enlarged boundary probe is

\[
\Pi_{\rm rad}(ho,e,w,ho(0))
=(\rho(0),R,E,W).
\]

It uses no Xi zero and no shell-fitted coefficient.

## Exact Green relation and jets

Integration by parts gives the entire identity

\[
zR(z)-\rho(0)=E(z)-\frac12W(z).
\]

Every parameter derivative is a source moment:

\[
\partial_z^jR(z)
=(-1)^j\int_0^\infty t^je^{-zt}\rho(t)\,dt,
\]

and similarly for `E,W`.  Thus the probe retains the complete analytic-
transpose multiplicity-jet family before divisor restriction.

At `z=0`, the displayed quotient for `R` has a removable numerator because the
graph relation forces

\[
-\rho(0)=E(0)-\frac12W(0).
\]

No singular zero-frequency normalization is introduced.

## Faithfulness

The Laplace transform is injective on the rapid radial module.  Consequently
`R(z)` on any open parameter set determines `rho`; retaining `E` and `W`
separately also preserves the endpoint and Wronskian source channels.  This is
the minimal correction to the fixed two-scalar wall/incidence plane, which
cannot represent the infinite-rank shell family.

## Shell and label naturality

For adjacent shells,

\[
(\rho,e,w)_{[a,c]}
=(\rho,e,w)_{[a,b]}+(\rho,e,w)_{[b,c]}.
\]

Therefore `Pi_rad` is additive under shell concatenation.  Translation-orbit
synthesis preserves theta labels, and external prime/grade coefficients remain
outside the analytic Laplace probe.  Reciprocal slot reversal changes the sign
of `W` while retaining the ordered pair data.

## G4 consequence

This constructs the previously missing function-valued boundary enlargement

\[
\mathcal G_{\rm rad}
\longrightarrow
\mathcal G_{\rm wall,inc}^{\rm enlarged}
\]

at the analytic level.  The old scalar linking port may be a later matrix
coefficient of this section but cannot replace it.

Candidate one is now narrowed to the arithmetic attachment: derive the
prime/grade loading and joint-column adjoint acting on `(rho(0),R,E,W)`, and
prove that its shell sum agrees with the complete Evans residual.  Xi-adic
filtration must be tested only after that source codiagonal is frozen.

No residual cancellation or RH claim follows from the probe itself.
