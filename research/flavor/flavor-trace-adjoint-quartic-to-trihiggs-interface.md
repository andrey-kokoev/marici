# Trace-adjoint quartic to triple-Higgs interface

Work package: WP560  
Owner: marici.Figueiredo

## Common-frame construction

WP559 derives a connected four-point source operation, but leaves it outside a
physical instrument. WP237 supplies the missing weak-basis-invariant entrance:
a trace-adjoint scalar mixes with the Higgs. Freeze one CP-even trace mode
\(s\), the Higgs radial mode \(h\), and a physical light eigenstate \(H\) with

\[
s=\sin\theta\,H+\cos\theta\,S.
\]

The source interaction

\[
V_s={\lambda_s\over4}s^4
\]

then contributes to the physical light-Higgs vertex by

\[
\left.{\partial^4 V_s\over\partial H^4}\right|_{H=S=0}
=6\lambda_s\sin^4\theta.
\]

If \(\lambda_H\) denotes the quartic coefficient used to normalize the
Standard Model light-Higgs vertex, the induced readout coordinate is

\[
\kappa_4=1+{\lambda_s\sin^4\theta\over\lambda_H},
\qquad
{\partial\kappa_4\over\partial\lambda_s}
={\sin^4\theta\over\lambda_H}.
\]

This derivative is nonzero on the preregistered domain
\(\lambda_s>0\), \(\lambda_H>0\), and \(\sin\theta\ne0\). Positivity of
\(\lambda_s\) is required by boundedness on the isolated large-\(s\) ray of
the declared quartic source. The derivative vanishes in the exact zero-mixing
limit. Because the entrance uses a trace-adjoint mode and the exit is a Higgs
mass-eigenstate coupling, the map descends under the full quark weak-basis
groupoid. It does not use a texture chart or a reference port.

## Physical instrument

WP417 admits the ATLAS search for nonresonant triple-Higgs production in the
six-bottom-quark final state. Its declared experimental domain is 126 inverse
femtobarns of 13 TeV proton-proton collisions. The analysis reconstructs six
bottom jets, validates a data-driven background model, and reports a
profile-likelihood constraint on the Higgs quartic modifier. The published
one-dimensional 95-percent interval at fixed trilinear modifier is
\(-230<\kappa_4<240\).

This supplies a candidate passive physical chain:

\[
pp\longrightarrow HHH\longrightarrow 6b
\longrightarrow \mathcal L_p(\kappa_4).
\]

The chain is a probe, not an actuator. Beam settings prepare collision
ensembles but do not command \(\lambda_s\). The nonzero derivative proves that
an appropriately completed likelihood can be source-sensitive. It does not
authorize reuse of the published one-parameter likelihood.

## Statistical boundary

The admitted public summary carries a confidence interval and its support
assumptions, including fixed \(\kappa_3\). Trace-adjoint/Higgs mixing generally
also rescales Standard Model Higgs production and decay vertices and changes
the physical trilinear interaction. Therefore the published one-dimensional
\(\kappa_4\) likelihood is not yet a response model for the portal domain.
Using it would freeze directions that the source map changes.

The public summary also does not carry a covariance or full nuisance-response
object parallelized with the trace-adjoint portal parameters. A confidence
interval is not silently converted into a Gaussian variance.

Consequently five interface fields are now named and supported:

1. proton-collision preparation;
2. quartic-sensitive triple-Higgs production;
3. calibrated six-bottom readout;
4. finite exposure and background calibration;
5. a profile-likelihood uncertainty interval.

Two further fields remain absent:

6. signal templates on the mixed-scalar source domain, including correlated
   production, decay, trilinear, and quartic changes;
7. a transportable covariance-bearing likelihood for
   \((\lambda_s,\theta,\lambda_H,\kappa_3,\nu)\), where \(\nu\) denotes
   detector and theory nuisances.

Without both, the physical response rank and uncertainty-stable separation of
the WP559 hostile pair are not admitted.

## Classification and falsifiers

WP560 names a physically executed candidate readout and derives the missing
source-to-Higgs quartic arrow, but their statistical model domains do not yet
match. It is an interface construction, not an admitted end-to-end flavor
instrument, source selector, or executable coefficient actuator.

The smallest exact source falsifier is \(\sin\theta=0\), where the detector
response to \(\lambda_s\) vanishes. The smallest statistical falsifier is a
profile likelihood whose nuisance-profiled curvature in the portal direction
is zero. The remaining gate is a mixed-scalar signal and detector model on the
same source domain, plus its common-frame calibrated covariance, followed by a
positive weighted Gram test that survives its declared uncertainties.

## Reproduction

Run:

    uv run --offline --with sympy python research/flavor/checkers/wp560_trace_adjoint_quartic_trihiggs_interface.py

The generated result is
research/flavor/results/wp560_trace_adjoint_quartic_trihiggs_interface.json.
