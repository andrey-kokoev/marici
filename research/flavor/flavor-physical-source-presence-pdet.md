# Physical source-presence `P_det`

Owner: `marici.Figueiredo`.

## Admitted experiment

WP240 combines two independently frozen physical objects from the same CMS
2016 detector era:

- the checksum-verified, generator-labelled MSSM scalar-to-dimuon response from
  WP239;
- a checksum-verified 33,177-event DoubleMuon Run2016G collision shard from
  CERN Open Data record 31305, filtered by the official muon-physics
  certification mask.

The collision selection is exactly the WP239 reconstructed selection, without
truth matching. Sixty-six certified collision events lie in the frozen
110--150 GeV window.

## Quotient experiment

The physical question is binary source presence, not complete background
microscopy. A smooth exponential nuisance is calibrated from collision
sidebands outside 122--138 GeV and frozen before the signal fit. The source
coefficient is the nonnegative yield multiplying the independently generated
scalar response template.

After quotienting the frozen smooth-background nuisance, the response matrix
has two columns:

\[
J_{\mathrm{det}}=(T_{\mathrm{scalar}},T_{\mathrm{{background}}}).
\]

In the calibration-fold inverse-Poisson metric,

\[
\operatorname{rank}J_{\mathrm{det}}=2,
\qquad
\det(J_{\mathrm{det}}^TWJ_{\mathrm{det}})
=1.4120676\times10^{-3}>0.
\]

Thus scalar source presence is identifiable on the declared quotient. If the
signal template is replaced by the nuisance template, rank falls to one. This
is the exact hostile falsifier.

## Empirical disposition

The collision fit returns the signal yield at the numerical zero boundary
(`1e-6` events) and a likelihood improvement of only `1.35e-7` over the
background-only fit. The shard therefore contains no evidence for this MSSM
scalar source. That negative record does not remove the instrument's source-
presence identification capability.

## Scope

This is a genuine physical source-identifying `P_det` on the frozen domain:

`MSSM MA=130 bbH->mumu scalar present/absent modulo smooth collision background`.

It is not yet the requested WP128 trace-adjoint source identifier. That
transfer requires a source-authorized map from WP237 production and branching
parameters to the WP239 detector response. Equal spin/final state is
insufficient because production kinematics and normalization affect
acceptance and yield.

## Artifacts

- Collision provenance: `data/cms-open-data-31305/provenance.json`
- Collision shard: `data/cms-open-data-31305/nano_data2016_2-8.root`
- Certification mask:
  `data/cms-open-data-31305/Cert_271036-284044_13TeV_Legacy2016_Collisions16_JSON_MuonPhys.txt`
- Checker: `checkers/wp240_physical_source_presence_pdet.py`
- Result: `results/wp240_physical_source_presence_pdet.json`

## Calibration

- Pre excitement/confidence/expected information gain: `10/8/10`.
- Post excitement/confidence/realized information gain: `10/10/10` within the
  declared MSSM source-presence domain.
- Added: certified collision record, physical source template, nuisance
  quotient, positive-Gram rank certificate, and a negative source observation.
- Remaining: trace-adjoint production/branching transfer.

## Report to `marici.Nima`

- Domain: nonnegative MSSM `MA=130` scalar yield modulo a sideband-frozen
  smooth-background nuisance.
- Faithful coordinate: the certified 40-bin CMS dimuon response.
- Source-authorized probe family: reconstructed mass bins with the WP239
  generator-labelled scalar response.
- Contextual partition: singleton scalar-yield fibers; the observed shard lies
  at the absent-source boundary.
- Classification: source identifier and physical readout on the declared MSSM
  domain; not a `physical16` selector.
- Smallest falsifier: coincident signal/background templates, giving rank one.
- Remaining flavor gate: source-authorized WP237-to-WP239 production,
  branching, and kinematic transfer.
