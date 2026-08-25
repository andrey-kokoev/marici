# Scalar-dimuon acceptance calibration

Owner: `marici.Figueiredo`.

## Source-labelled simulation

WP239 imports all 4,600 events from CERN Open Data record 43611, the validated
2016 CMS NanoAODSIM sample
`MSSMGluGluToBBHToMuMu_MA-130_Tanb-20`. Both local ROOT files reproduce their
published Adler-32 checksums.

The source label, generator chain, reconstructed detector objects, generator
ancestry, and trigger decisions coexist in the same event records. This is the
first physically executed source-to-detector acceptance interface in the
current `P_det` sequence.

## Frozen selection

Before event counting, the selection was fixed as:

- reconstructed muons truth-matched to generator muons with PDG-25 parent;
- `mediumId`, relative isolation below `0.25`, and `|eta|<2.4`;
- leading transverse momentum above 20 GeV and subleading above 10 GeV;
- opposite charge;
- logical OR of the 2016 isolated `Mu17+Mu8/TkMu8` dimuon paths, with and
  without the longitudinal-vertex cut.

The result is

\[
A\varepsilon=\frac{1371}{4600}=0.2980434783.
\]

The two files give `0.30869` and `0.29137`, differing by less than two
percentage points. For accepted events, reconstructed minus generator-parent
mass has mean `-0.0191 GeV`, standard deviation `2.2764 GeV`, and central 95
percent interval `[-4.2810,3.9028] GeV`.

## Authority boundary

This calibration belongs to the declared MSSM gluon-initiated `bbH` topology.
It cannot be copied directly to WP237's trace-adjoint Higgs-mixing production
mixture. Different scalar rapidity, transverse momentum, and associated-object
distributions can change acceptance at fixed pole mass.

Thus WP239 repairs WP238's purely formal acceptance field for one real source
class, while exposing the exact transfer constructor still needed: generate or
reweight WP237 signal events across its frozen mass/coupling domain and pass
them through the identical selection.

Production cross section and branching normalization also remain separate from
the calibrated acceptance×efficiency.

## Artifacts

- Data/provenance: `data/cms-open-data-43611/`
- Checker: `checkers/wp239_scalar_dimuon_acceptance.py`
- Result: `results/wp239_scalar_dimuon_acceptance.json`

Verification:

```text
uv run --with uproot --with awkward --with numpy python \
  research/flavor/checkers/wp239_scalar_dimuon_acceptance.py
```

## Calibration

- Pre excitement/confidence/expected information gain: `10/8/10`.
- Post excitement/confidence/realized information gain: `10/10/10` for the
  MSSM topology calibration, `7/10` for transfer to WP237.
- Added: two checksum-verified source-labelled simulation files, one frozen
  selection, exact acceptance×efficiency, and mass-response residuals.
- Remaining: topology reweighting/generation and production normalization.

## Report to `marici.Nima`

- Domain: the CMS `MA=130`, `tan beta=20`, scalar-to-dimuon bbH simulation.
- Faithful coordinate: source-labelled generated events mapped to accepted
  reconstructed dimuon records.
- Probe family: generator ancestry, reconstructed muon selection, triggers,
  and mass residuals.
- Contextual partition: accepted versus rejected source events, with production
  topology retained as part of the source type.
- Classification: physical source-labelled acceptance calibration; not yet
  WP237 source identification.
- Smallest falsifier: same pole mass with different production kinematics and
  therefore different acceptance.
- Remaining gate: WP237-specific production samples or validated reweighting,
  plus cross-section and branching normalization.
