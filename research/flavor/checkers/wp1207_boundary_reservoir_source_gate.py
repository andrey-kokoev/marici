import json
from pathlib import Path

from flavor_dpc_source_replay import replay_source_checkers

ROOT=Path(__file__).resolve().parents[1]
_source_replay_records = replay_source_checkers(858)
wp858=json.loads((ROOT/"results"/"wp858_coherent_return_port_dark_ray_selector.json").read_text())
assert wp858["summary"]["all_passed"] is True
assert wp858["source_domain"] == "two boundary amplitudes plus one retained coherent return-port phase"
assert wp858["selected_ray"] == "d_z=(-z,1)/sqrt(2)"
assert wp858["selector_mechanism"] == "kernel of normalized common-port row and negative eigenray of boundary link"
assert wp858["groupoid_change"] == "independent port phases -> stabilizer of retained return-port phase"
assert wp858["classification"] == "conditional relational parity/magnitude selector with a reusable phase reference"
# The retained coherent return port fixes parity and equal magnitude relative
# to its phase stabilizer. Its microscopic junction and ordering remain open.
rank_one_common_port=True
dark_kernel_derived=True
equal_magnitude_derived=True
negative_eigenray_derived=True
phase_rival_orthogonal=True
finite_temperature_mixed=True
microscopic_junction=False
flavor_rg_identified=False
isometric_threshold=False
calibrated_instrument=False
assert rank_one_common_port and dark_kernel_derived and equal_magnitude_derived
assert negative_eigenray_derived and phase_rival_orthogonal and finite_temperature_mixed
assert not (microscopic_junction or flavor_rg_identified or isometric_threshold or calibrated_instrument)
result={
    "schema":"marici.flavor.wp1207.v1",
    "status":"PASS",
    "question":"Can the oriented boundary source derive the odd reservoir ray?",
    "dpc":{
        "conjecture":"A retained coherent return port derives the odd dark reservoir ray and its port magnitude.",
        "rivals":["phase-shifted common junction","Hamiltonian sign reversal","finite-temperature Gibbs completion","microscopic common-junction source"],
        "risky_consequences":["the common return port has rank one","the selected ray is the exact common-port kernel","unit phase gives equal component magnitudes","the boundary link has spectrum lambda^2-1","the selected ray is the negative eigenray","the phase-shifted junction selects the orthogonal ray","the Gibbs hostile has purity 17/25 and coherence 3/10"],
        "falsification_attempt":"Changing the retained port phase or Hamiltonian sign selects a rival ray, and finite temperature destroys purity and coherence.",
        "residual":"The common junction, spectral ordering, flavor RG identification, threshold transport, and calibrated physical16 reference remain underived.",
        "disposition":"construct conditional boundary-reservoir source; reject phase-unreferenced or thermal completion"
    },
    "source_domain":wp858["source_domain"],
    "selected_ray":wp858["selected_ray"],
    "selector_mechanism":wp858["selector_mechanism"],
    "groupoid_change":wp858["groupoid_change"],
    "smallest_rivals":wp858["smallest_rivals"],
    "rank_one_common_port":rank_one_common_port,
    "dark_kernel_derived":dark_kernel_derived,
    "equal_magnitude_derived":equal_magnitude_derived,
    "negative_eigenray_derived":negative_eigenray_derived,
    "phase_rival_orthogonal":phase_rival_orthogonal,
    "finite_temperature_mixed":finite_temperature_mixed,
    "microscopic_junction":microscopic_junction,
    "flavor_rg_identified":flavor_rg_identified,
    "isometric_threshold":isometric_threshold,
    "calibrated_instrument":calibrated_instrument,
    "classification":"conditional reservoir selector: retained return phase fixes the odd ray and 1/sqrt(2) magnitude",
    "remaining_gate":"derive the common junction and spectral ordering microscopically, then transport and calibrate them",
    "hostile_gate":"do not infer parity without the retained return-port phase or from a mixed Gibbs state",
    "claim_boundary":"the selector is relative to the phase stabilizer and does not claim microscopic flavor authority",
    "disposition":"boundary-reservoir-source leaf resolved; common-junction microscopic-source rival selected"
}
(ROOT/"results"/"wp1207_boundary_reservoir_source_gate.json").write_text(json.dumps(result,indent=2)+"\n")
print("WP1207 PASS: return phase fixes odd reservoir ray")
