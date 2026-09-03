import json
from pathlib import Path

from flavor_dpc_source_replay import replay_source_checkers

ROOT=Path(__file__).resolve().parents[1]
_source_replay_records = replay_source_checkers(1025,1026,1027,1028,1029)
wp1025=json.loads((ROOT/"results"/"wp1025_threshold_cube_inverse_readout.json").read_text())
wp1026=json.loads((ROOT/"results"/"wp1026_threshold_reciprocal_duality_no_go.json").read_text())
wp1027=json.loads((ROOT/"results"/"wp1027_source_ratio_interface_inventory.json").read_text())
wp1028=json.loads((ROOT/"results"/"wp1028_integer_mass_norm_window.json").read_text())
wp1029=json.loads((ROOT/"results"/"wp1029_source_seventeen_type_audit.json").read_text())
assert wp1025["classification"] == "cubic hierarchy amplifier and faithful inverse readout on a declared branch; neither selector nor source normalization"
assert wp1026["classification"] == "canonical duality is incompatible; quarter duality is a normalization rigidifier with a false numerical prediction, not a source selector"
assert wp1027["classification"] == "source selectors exist, but the source-to-threshold interface family is empty; numerical rescaling would be a rigidifier, not selection"
assert wp1028["classification"] == "discrete common-source interface family with a unique data-compatible member; conditional selector if and only if source theory independently derives N=17"
assert wp1029["classification"] == "all seventeens are differently typed; gauge rank is a support rigidifier and fails the equal-norm condition, so none derives M^2=17 f^2"
# The threshold readout is faithful on its branch and N=17 is the unique
# integer normal form in the fitted window, but no typed source arrow derives
# the threshold ratio or equal-norm mass projector.
threshold_inverse=True
quarter_duality_falsified=True
prior_ratio_interfaces_empty=True
integer_window_unique=True
seventeen_type_audit_negative=True
source_equation_for_r=False
typed_mass_interface=False
equal_norm_rank17=False
radiative_closure=False
calibrated_count_observable=False
assert threshold_inverse and quarter_duality_falsified and prior_ratio_interfaces_empty
assert integer_window_unique and seventeen_type_audit_negative
assert not (source_equation_for_r or typed_mass_interface or equal_norm_rank17 or radiative_closure or calibrated_count_observable)
result={
    "schema":"marici.flavor.wp1235.v1",
    "status":"PASS",
    "question":"Can an independent source ratio fix the threshold coordinate r=f/M?",
    "dpc":{
        "conjecture":"Threshold inverse readout, reciprocal duality, prior source ratios, or the integer N=17 mass window independently fixes r.",
        "rivals":["threshold cube inverse readout","reciprocal duality","existing source-ratio inventory","integer mass-norm window","independent source-seventeen audit"],
        "risky_consequences":["each fitted J magnitude has one r on 0<r<=1/4","the reconstructed outer bracket is strictly below 1/4","six prior selector values have zero typed arrows into f/M","N=17 is the unique integer compatible with the fitted window","six independent seventeens exist but none is an equal-norm messenger mass projector"],
        "falsification_attempt":"quarter duality is falsified, old source ratios have no interface, and the only surviving N=17 normal form is not independently derived or radiatively closed.",
        "residual":"source-covariant dimensionless interface into f/M, rank-17 equal-norm mass projector, radiative stability, and a calibrated count/spectroscopy observable",
        "disposition":"accept N=17 as a conditional normal form only; reject it as source-derived ratio"
    },
    "threshold_response":wp1025["exact_response"],
    "reconstructed_r_bracket":wp1025["reconstructed_r_outer_bracket"],
    "quarter_rejected_sheets":wp1026["ensemble_sheets_rejected_by_quarter_prediction"],
    "prior_source_ratios":wp1027["admitted_source_ratio_family"],
    "compatible_integer_multiplicities":wp1028["compatible_integer_multiplicities"],
    "predicted_abs_J_float":wp1028["predicted_abs_J_float"],
    "neighbour_falsifiers":wp1028["neighbour_falsifiers"],
    "seventeen_inventory":wp1029["source_seventeen_inventory"],
    "threshold_inverse":threshold_inverse,
    "quarter_duality_falsified":quarter_duality_falsified,
    "prior_ratio_interfaces_empty":prior_ratio_interfaces_empty,
    "integer_window_unique":integer_window_unique,
    "seventeen_type_audit_negative":seventeen_type_audit_negative,
    "source_equation_for_r":source_equation_for_r,
    "typed_mass_interface":typed_mass_interface,
    "equal_norm_rank17":equal_norm_rank17,
    "radiative_closure":radiative_closure,
    "calibrated_count_observable":calibrated_count_observable,
    "classification":"conditional small-ratio normal form: N=17 is data-compatible but lacks typed source realization",
    "remaining_gate":"derive a source-covariant mass-norm interface realizing N=17 as an equal-norm rank-17 projector, then close radiative corrections and calibrate a count observable",
    "hostile_gate":"do not call inverse readout, quarter duality, prior selector values, data compatibility, or unrelated seventeens an independent source ratio",
    "claim_boundary":"WP1028 isolates a sharp conditional candidate but no typed arrow derives it from source dynamics",
    "disposition":"independent small-source-ratio leaf resolved conditionally; mass-norm-interface rival selected"
}
(ROOT/"results"/"wp1235_independent_small_source_ratio_gate.json").write_text(json.dumps(result,indent=2)+"\n")
print("WP1235 PASS: N=17 conditional, typed mass-norm interface absent")
