# UV source and equivalence conventions (WP117)

## Admissible source class

An admissible member is a tuple

\[
 \mathfrak S=(\Phi,G,R_\Phi,S_{\rm UV},\Lambda,\mathcal R,
 \mathcal B,\mu_{\rm UV}),
\]

where `Phi` are dynamical UV fields, `G` and `R_Phi` are gauge data,
`S_UV` is a local action with a declared coefficient domain, `Lambda` is the
source scale, `R` is a renormalization scheme, `B` is boundary data, and
`mu_UV` is a normalized positive state on admitted UV configurations modulo
source equivalence. None may contain an observed quark mass, CKM entry,
Jarlskog invariant, or a function chosen by optimizing those outputs.

This is a class contract, not a claim that the current source supplies a
member. The declared flavor source does not yet specify `S_UV`, its coefficient
law, or `mu_UV`.

## Four parameter types

| Type | Members | Can affect the physical ensemble? |
|---|---|---|
| Source inputs | field content, representations, action coefficients, boundary law | Yes, only when independently authorized |
| Gauge/presentation | UV gauge representative, weak-basis frame, texture chart labels | No |
| Renormalization data | input/output scale, scheme, matching prescription | Yes, through covariant transport; must be frozen |
| Derived observables | `physical16`, measured ten, canonical moments, detector outcomes | Readout only; cannot define upstream data |

## Equivalence groupoid

The source groupoid contains UV gauge transformations and declared field
redefinitions. The target groupoid is the full weak-basis quotient, not the
nine-link texture groupoid. Chart changes may change presentation weights but
must not change the quotient measure. A relational reference, if introduced,
creates a new stabilizer groupoid and must be declared as a new experiment.

For quotient map `q`, UV-to-flavor map `F`, and source measure `mu`, descent
requires both

\[
 F(gx)=F(x),\qquad \mu(gA)=\mu(A)
\]

for every admitted source arrow `g`. The induced physical ensemble is
`F_* mu`. Equality of maps without equality of measures is insufficient.

## Decisive falsifier

Two source-equivalent presentations receiving unequal orbit weights induce
presentation-dependent probabilities on `physical16`. That falsifies the UV
selector even when both presentations map to the same measured-ten point.
