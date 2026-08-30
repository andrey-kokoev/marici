# Flavor topology-transfer gate (WP241)

## Question

Can WP240's executable, collision-calibrated scalar-presence operation be
transported from its declared CMS MSSM source to the WP237 trace-adjoint Higgs
portal and thereby identify a flavor constructor?

## Typed objects

The calibrated source is CMS Open Data record 43611: POWHEG V2 plus Pythia8,
MSSM bottom-associated Higgs production, parent PDG 25, generator mass
`133.774002075 GeV`, width `0.641044974327 GeV`, and a forced muon-pair decay.
WP239 measured acceptance times efficiency as `1371/4600`. WP240 combined that
response with certified DoubleMuon collision data and remains an executable
physical source-presence test on this bounded MSSM domain.

The target is the weak-basis-invariant WP237 trace-adjoint Higgs portal. Its
mixing creates a dimuon route, but the current source action fixes neither an
accessible pole mass and width nor a production cross section and physical
muon branching fraction. Its production law has not been matched to the MSSM
`bbH` generator.

## Transfer criterion

Normalized shape transport requires independently validated equality or
reweighting of production law, spin/CP law, mass, width, decay law, and detector
selection. Yield transport additionally requires

\[
 N_s={\cal L}\,\sigma_s\,\operatorname{BR}_{s\to\mu\mu}A_s\epsilon_s r_s
\]

with every factor source-derived or experimentally calibrated in one frame. A
forced generator decay is not a physical branching-ratio prediction. Both
transfers presently fail; this is a source-support failure, not a fit failure.

## Exact hostile pair

At fixed luminosity, branching, efficiency, and residue, `(sigma,A)=(2,1/4)`
and `(1,1/2)` produce identical accepted yield. The observation has rank one
on these two microscopic factors. A nonzero fitted scalar yield identifies
presence only within the declared MSSM hypothesis, not the trace-adjoint source.

## Classification and falsifier

- admitted domain: WP240's CMS MSSM scalar/background family, with the
  trace-adjoint target kept as a distinct source domain;
- faithful coordinate: source-labelled detector response modulo the frozen
  smooth-background nuisance, not measured-ten and not `physical16`;
- authorized probe: certified dimuon invariant mass plus the labelled MSSM
  response;
- contextual partition: MSSM scalar present/absent is separated; trace-adjoint
  sources with equal effective yield remain equivalent;
- operation: physical identifier on the MSSM domain, but neither selector nor
  identifier for the trace-adjoint domain;
- smallest falsifier: the two `(sigma,A)` assignments above;
- remaining gate: a trace-adjoint sample or validated reweighting carrying
  physical production, branching, mass, width, uncertainties, and the same
  detector selection.

The WP237 trace couplings and dimuon readout separately descend under the full
weak-basis groupoid, but no source-authorized map joins them. A reference port
does not repair missing production and branching authority.

Run `python research/flavor/checkers/wp241_topology_transfer_gate.py` to generate
the exact JSON result.
