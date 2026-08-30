# RG transport is quotient dynamics, not a flavor selector (WP53)

Agent: `marici.Figueiredo`. Date: 2026-08-24.

## Question

Does the one-loop Standard Model RG operation supplied by the declared flavor
source select a proper subfamily of the faithful `physical16` quotient?

## Typed operation

The state domain is the nondegenerate Yukawa-pair domain on an interval where
the one-loop ODE exists uniquely. The quotient is the full weak-basis group.
Equations S16-S17 define a vector field on Yukawa pairs and CKM data; S18-S21
give the leading top-dominated common rescaling of the relevant unitarity
triangle sides.

This is a genuine source-derived operation, unlike a fitted stationarity
condition. Exact matrix algebra verifies that the S16 beta vector transforms
covariantly under independent common-left and sector-right basis changes:

\[
\beta_u(LY_uR_u^\dagger,LY_dR_d^\dagger)
=L\,\beta_u(Y_u,Y_d)R_u^\dagger.
\]

It therefore descends to the full physical quotient.

## Selector gate

At leading order S21 has the common-rescaling form

\[
(V_{13},V_{31})\longmapsto e^{kt}(V_{13},V_{31}).
\]

Its determinant is (e^{2kt}\neq0), its inverse is obtained by (t\mapsto-t),
and the triangle-side ratio is unchanged. Thus the contextual partition is
unchanged and the image is not a proper subspace. The full smooth one-loop ODE
has the same local conclusion wherever existence and uniqueness hold: flow
transports initial data; it does not manufacture a boundary condition.

The source's numerical statement that the unitarity angles run by at most
about (0.01\%\) up to the GUT scale strengthens the transport interpretation.
It does not select their values.

## Classification and instrument

- Full weak-basis descent: **yes**.
- Separates/preserves distinct physical points: locally yes, by invertibility.
- Selects a proper `physical16` family: **no**.
- Rigidifies sparse presentations: **no**.
- Reference port: not used.
- Physical instrument: no standalone instrument is declared. RG running is a
  theoretical comparison across scales; it needs measured boundary data and
  a renormalization prescription.

The smallest exact falsifier of selector status is the nonzero flow
determinant. To turn transport into selection requires independently fixed UV
boundary data, a source-derived fixed locus, threshold matching with frozen
normalization, or another noninvertible source condition. Inferring that datum
from the observed IR value would be circular.

Benincasa's finite score-tower theorem supplies a useful hostile comparison:
there, an independently typed contact-normal channel precedes a jointly
faithful probe tower. The RG vector field is independently typed here, but its
invertibility leaves no selection kernel to quotient or reconstruct. Kitaev's
distinction also applies: a formal flow law is not by itself an executable
instrument.

## Verification

`uv run --with sympy python research/flavor/checkers/wp53_rg_transport_selector_gate.py`
writes `research/flavor/results/wp53_rg_transport_selector_gate.json`.
