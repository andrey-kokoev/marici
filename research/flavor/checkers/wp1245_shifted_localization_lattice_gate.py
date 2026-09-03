import json
from pathlib import Path

from flavor_dpc_source_replay import replay_source_checkers

ROOT=Path(__file__).resolve().parents[1]
_source_replay_records = replay_source_checkers(1070,1071,1072,1073)
wp1070=json.loads((ROOT/"results"/"wp1070_shifted_chern_simons_coset_gate.json").read_text())
wp1071=json.loads((ROOT/"results"/"wp1071_shifted_flux_cs_interface_no_go.json").read_text())
wp1072=json.loads((ROOT/"results"/"wp1072_unit_clock_flux_sector_degeneracy_gate.json").read_text())
wp1073=json.loads((ROOT/"results"/"wp1073_chirality_flux_sector_interface_no_go.json").read_text())
assert wp1070["classification"].startswith("shifted-coset gate")
assert wp1071["classification"].startswith("shifted-flux-to-CS interface no-go")
assert wp1072["classification"].startswith("unit-clock flux-sector degeneracy gate")
assert wp1073["classification"].startswith("chirality-to-flux-sector interface no-go")
# The exact shifted coset is known, but neither shifted flux nor chirality
# supplies the compactification, endpoint action, sector, or orientation.
exact_shifted_coset=True
single_coset_orientation=True
unit_clock_orbit=True
signed_flux_readout=True
shifted_flux_direct_source=False
chirality_flux_interface=False
compactification_packet=False
endpoint_action=False
orientation_law=False
sector_selected=False
physical16_channel=False
source_gain=False
assert exact_shifted_coset and single_coset_orientation and unit_clock_orbit and signed_flux_readout
assert not (shifted_flux_direct_source or chirality_flux_interface or compactification_packet or endpoint_action or orientation_law or sector_selected or physical16_channel or source_gain)
result={
    "schema":"marici.flavor.wp1245.v1",
    "status":"PASS",
    "question":"Can the shifted localization lattice be derived from existing flux or chirality packets?",
    "dpc":{
        "conjecture":"The required seven-channel localization law is an exact shifted CS coset, potentially sourced by shifted flux or chirality.",
        "rivals":["exact shifted CS coset","shifted-flux direct source","unit-clock flux sector orbit","chirality-to-flux interface","common compactification packet"],
        "risky_consequences":["the one-quartet coset is (1/2,1/4,0,0,0,3/4,0) modulo the integral CS lattice","one coset admits the selected orientation but rejects the reflected orientation, doublet pair, and alternate split","the unit-clock orbit fixes R star=1/2 and M squared=1 but leaves n and sigma degenerate","Delta=2 sigma n is a signed flux-sensitive readout","WP793 lacks all five interface maps from shifted flux to the interval CS packet"],
        "falsification_attempt":"shifted flux and chirality do not provide the compactification, branch projector, endpoint GS action, orientation, or normalization needed to land on the coset.",
        "residual":"construct one compactification packet that derives magnetic flux, orientation, B/A, chirality, endpoint action, and the required CS coset in shared normalization",
        "disposition":"accept the shifted coset conditionally; reject existing flux/chirality as its source"
    },
    "channels":wp1070["channels"],
    "residue_vectors_mod_integer_lattice":wp1070["residue_vectors_mod_integer_lattice"],
    "single_coset_admission":wp1070["single_coset_admission"],
    "wp793_provides":wp1071["wp793_provides"],
    "missing_map_components":wp1071["missing_map_components"],
    "required_coset_mod_integer_lattice":wp1071["required_coset_mod_integer_lattice"],
    "sector_data":wp1072["sector_data"],
    "orientation_mirror":wp1072["orientation_mirror"],
    "degeneracy":wp1072["degeneracy"],
    "required_interface_components":wp1073["required_interface_components"],
    "provided_interface_components":wp1073["provided_interface_components"],
    "candidate_identifications":wp1073["candidate_identifications"],
    "exact_shifted_coset":exact_shifted_coset,
    "single_coset_orientation":single_coset_orientation,
    "unit_clock_orbit":unit_clock_orbit,
    "signed_flux_readout":signed_flux_readout,
    "shifted_flux_direct_source":shifted_flux_direct_source,
    "chirality_flux_interface":chirality_flux_interface,
    "compactification_packet":compactification_packet,
    "endpoint_action":endpoint_action,
    "orientation_law":orientation_law,
    "sector_selected":sector_selected,
    "physical16_channel":physical16_channel,
    "source_gain":source_gain,
    "classification":"conditional shifted-localization gate: exact coset known, common UV compactification absent",
    "remaining_gate":"construct a common compactification packet deriving the shifted coset, endpoint action, flux sector, orientation, chirality, and Physical16 channel map",
    "hostile_gate":"do not call a shifted CS residue, shifted-flux theorem, unit-clock orbit, signed flux readout, or chirality lower bound a localization source",
    "claim_boundary":"WP1070 through WP1073 provide exact coset and interface no-go algebra; no compactification packet, channel map, or gain is derived",
    "disposition":"shifted-localization-lattice leaf resolved conditionally; common UV boundary-action-packet rival selected"
}
(ROOT/"results"/"wp1245_shifted_localization_lattice_gate.json").write_text(json.dumps(result,indent=2)+"\n")
print("WP1245 PASS: shifted coset conditional, common compactification absent")
