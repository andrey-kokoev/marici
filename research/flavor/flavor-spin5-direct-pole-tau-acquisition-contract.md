# Direct-pole Spin(5) tau acquisition contract (WP895)

## Question

What is the smallest executable experiment that can replace WP894's failed
tau-template transport without fitting a detector kernel to the desired two
pole answer?

## Authoritative source chain

The [CMS 140 GeV tau record](https://opendata.cern.ch/record/19459) publishes
the validated production chain used by the existing pilot: a Pythia8
generator fragment, `CMSSW_7_1_19` GEN-SIM, `CMSSW_7_6_1` pile-up HLT/RECO
with global tag `76X_mcRun2_asymptotic_v12`, and `CMSSW_7_6_3` MiniAODSIM.
The same official family contains 130, 140, and 160 GeV records, but no record
at either Spin(5) pole.

The exact distances to the nearest existing grid points are

\[
133.774002075-130=3.774002075\ \mathrm{GeV},
\]

and

\[
160-151.287002563=8.712997437\ \mathrm{GeV}.
\]

Neither substitution is an exact source preparation.

## Frozen acquisition operation

For each preregistered mass
\(M\in\{133.774002075,151.287002563\}\) GeV:

1. derive a self-consistent Spin(5)-radial Higgs-portal source card at \(M\),
   including the mass-local Standard Model partial widths, mixing-scaled total
   width, tau branching fraction,
   bottom-associated production normalization, and mass-dependent phase-space
   cuts; declare a neutral CP-even PDG-25-like parent and retain its daughter
   ancestry in the output;
2. generate independent events with a recorded random seed and event count;
3. replay the published 2015 GEN-SIM, pile-up HLT/RECO, and MiniAODSIM chain
   with the same releases, tune, global tags, and pile-up source;
4. apply WP251's unchanged trigger and object-matching operation and WP253's
   frozen visible-mass bins;
5. process the full weighted sample and the frozen DY, top, W, and data-derived
   QCD controls;
6. emit selected counts, efficiencies, widths, luminosity normalization, raw
   null trials, covariance, nuisance variations, source-card hash, production
   configuration hashes, parent spin/parity and ancestry, and detector-frame
   provenance.

No unrelated MSSM spectrum is required. The two masses, selections, bins, and acceptance tests must be frozen before
event inspection. The source cards must be independently validated; replacing
only a mass token in the official MSSM fragment is forbidden because that
fragment also contains a different source spectrum and mass-dependent
phase-space support.

## Acceptance and claim boundary

Let \(J_{\rm tau}\) be the two selected template columns after background and
nuisance completion. Admission requires

\[
\operatorname{rank}J_{\rm tau}=2,
\qquad
\inf_{\eta\in\mathcal U}
\lambda_{\min}(J_{\rm tau}(\eta)^T W J_{\rm tau}(\eta))>0,
\]

where \(W\) and the uncertainty set \(\mathcal U\) are calibrated independently
of the rank result. A zero selected column, proportional columns, an
uncertainty-supported zero eigenvalue, a source-card validation failure, or
any change to WP251/WP253 after unblinding is a decisive falsifier.

WP895 is an executable acquisition specification, not an executed detector
result. It constructs no flavor selector and grants no present identification
authority. Completion requires the two generated and reconstructed event
records plus the declared calibration outputs.

Run:

~~~text
uv run --with sympy python research/flavor/checkers/wp895_spin5_direct_pole_tau_acquisition_contract.py
~~~
