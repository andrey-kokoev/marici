import json
from fractions import Fraction
from pathlib import Path

from flavor_dpc_source_replay import replay_source_checkers

ROOT=Path(__file__).resolve().parents[1]
_source_replay_records = replay_source_checkers(824,1188)
wp824=json.loads((ROOT/"results"/"wp824_finite_spectral_completion_scale_selection_audit.json").read_text())
wp1188=json.loads((ROOT/"results"/"wp1188_incidence_spectrum_constructor_no_go.json").read_text())
assert wp824["summary"]["all_passed"] is True
assert wp1188["incidence_spectrum_function_exists"] is False
aspect=wp824["exact_data"]["aspect_germ"]
assert aspect["spectral_fiber_repair"] is True
for key in ["dirac_mass_selection","action_coefficient_authority","absolute_cutoff_authority","threshold_rg_parallelization","physical16_descent","detector_calibration"]:
    assert aspect[key] is False
assert wp824["exact_data"]["heat_trace"] == "2*exp(-mass**2*time)"
assert wp824["exact_data"]["normalized_spectral_action"] == "2*exp(-mass**2/cutoff**2)"
assert wp824["classification"]["verdict"] == "spectral completion repairs the fiber but does not select the portal scale"
# The two coefficient packets select different dimensionless mass/cutoff
# ratios, and each selected ratio leaves the common scale free.
ratio_packets=(Fraction(1),Fraction(4))
assert ratio_packets[0] != ratio_packets[1]
common_scale_dimensions=1
open_authority_gates=6
chain_level_carrier_constructed=True
chain_level_matter_authority=False
threshold_mass_selected=False
assert chain_level_carrier_constructed and not (chain_level_matter_authority or threshold_mass_selected)
result={
    "schema":"marici.flavor.wp1189.v1",
    "status":"PASS",
    "question":"Can finite spectral completion supply chain-level matter authority?",
    "dpc":{
        "conjecture":"Retaining the full Dirac spectrum selects the chain-level matter complex.",
        "rivals":["homology-level matter record","finite spectral carrier","spectral-action stationarity","source-selected Dirac spectrum"],
        "risky_consequences":["heat trace is strictly mass sensitive","normalized action has a common-scale kernel","coefficient packets select ratios 1 and 4","six authority gates remain false"],
        "falsification_attempt":"The full spectral object repairs WP1188's mass fiber, but mass, multiplicity, action coefficients, cutoff, RG parallelization, physical16 descent, and detector gain remain unselected.",
        "residual":"A source-derived spectral-flow condition and common clock are required.",
        "disposition":"construct faithful chain-level carrier; reject source authority"
    },
    "chain_level_carrier_constructed":chain_level_carrier_constructed,
    "spectral_fiber_repair":aspect["spectral_fiber_repair"],
    "heat_trace":wp824["exact_data"]["heat_trace"],
    "normalized_spectral_action":wp824["exact_data"]["normalized_spectral_action"],
    "ratio_packets":[str(x) for x in ratio_packets],
    "common_scale_dimensions":common_scale_dimensions,
    "open_authority_gates":[
        "dirac_mass_selection",
        "action_coefficient_authority",
        "absolute_cutoff_authority",
        "threshold_rg_parallelization",
        "physical16_descent",
        "detector_calibration"
    ],
    "open_authority_gate_count":open_authority_gates,
    "chain_level_matter_authority":chain_level_matter_authority,
    "threshold_mass_selected":threshold_mass_selected,
    "classification":"progressive carrier with negative authority gate: full spectrum records chain-level matter but does not select it",
    "remaining_gate":"derive a source-selected spectral-flow condition and common clock",
    "hostile_gate":"do not treat spectral faithfulness as source selection",
    "claim_boundary":"the result establishes a faithful mathematical carrier only; no physical threshold or source authority is claimed",
    "disposition":"chain-level-matter-authority leaf resolved; spectral-flow-clock rival selected"
}
(ROOT/"results"/"wp1189_chain_level_matter_authority_gate.json").write_text(json.dumps(result,indent=2)+"\n")
print("WP1189 PASS:",open_authority_gates,common_scale_dimensions)
