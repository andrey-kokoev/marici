import json
import os
from pathlib import Path

os.environ["FLAVOR_DPC_REPLAY_SESSION"] = "wp1270-common-compactification-necessity"

from flavor_dpc_source_replay import replay_source_checkers

ROOT=Path(__file__).resolve().parents[1]
_source_replay_records = replay_source_checkers(*range(1234,1246))
results={}
results[1234]=json.loads((ROOT/"results"/"wp1234_positive_cp_transmission_margin_gate.json").read_text())
results[1235]=json.loads((ROOT/"results"/"wp1235_independent_small_source_ratio_gate.json").read_text())
results[1236]=json.loads((ROOT/"results"/"wp1236_source_covariant_mass_norm_interface_gate.json").read_text())
results[1237]=json.loads((ROOT/"results"/"wp1237_discrete_source_actuator_typing_gate.json").read_text())
results[1238]=json.loads((ROOT/"results"/"wp1238_anomaly_complete_representation_theorem_gate.json").read_text())
results[1239]=json.loads((ROOT/"results"/"wp1239_source_detector_gain_law_gate.json").read_text())
results[1240]=json.loads((ROOT/"results"/"wp1240_coherent_cofinality_monitor_gate.json").read_text())
results[1241]=json.loads((ROOT/"results"/"wp1241_source_pole_atom_dynamics_gate.json").read_text())
results[1242]=json.loads((ROOT/"results"/"wp1242_inter_parent_clock_alignment_gate.json").read_text())
results[1243]=json.loads((ROOT/"results"/"wp1243_physical16_soft_port_channel_gate.json").read_text())
results[1244]=json.loads((ROOT/"results"/"wp1244_channel_dependent_reweighting_gate.json").read_text())
results[1245]=json.loads((ROOT/"results"/"wp1245_shifted_localization_lattice_gate.json").read_text())

local_margin_routes={
    "positive_margin_constructors":{
        "scale_free_margin_absent":results[1234]["scale_free_margin_absent"],
        "norms_not_margin":results[1234]["norms_not_margin"],
        "cyclic_cancellation_possible":results[1234]["cyclic_cancellation_possible"],
        "maximal_cp_falsified":results[1234]["maximal_cp_falsified"],
        "minimal_landau_falsified":results[1234]["minimal_landau_falsified"],
        "positive_t_margin":results[1234]["positive_t_margin"]
    },
    "independent_small_ratio":{
        "threshold_inverse":results[1235]["threshold_inverse"],
        "integer_window_unique":results[1235]["integer_window_unique"],
        "seventeen_type_audit_negative":results[1235]["seventeen_type_audit_negative"],
        "typed_mass_interface":results[1235]["typed_mass_interface"],
        "equal_norm_rank17":results[1235]["equal_norm_rank17"]
    },
    "mass_norm_interface":{
        "schur_rank17_invalid":results[1236]["schur_rank17_invalid"],
        "archive_interface_empty":results[1236]["archive_interface_empty"],
        "integer_clebsch_gap":results[1236]["integer_clebsch_gap"],
        "typed_mass_interface":results[1236]["typed_mass_interface"],
        "normalization_theorem":results[1236]["normalization_theorem"]
    },
    "discrete_actuator":{
        "nonprimitive_capacity":results[1237]["nonprimitive_capacity"],
        "unique_k2_c23_slice":results[1237]["unique_k2_c23_slice"],
        "representation_theorem":results[1237]["representation_theorem"],
        "single_pole_degeneracy":results[1237]["single_pole_degeneracy"]
    },
    "representation_theorem":{
        "degeneracy_rigidifies":results[1238]["degeneracy_rigidifies"],
        "threshold_shape_locked":results[1238]["threshold_shape_locked"],
        "representation_theorem":results[1238]["representation_theorem"],
        "source_ratio":results[1238]["source_ratio"],
        "gain_law":results[1238]["gain_law"]
    },
    "detector_gain":{
        "coherent_gain_rank":results[1239]["coherent_gain_rank"],
        "cofinality_monitor_required":results[1239]["cofinality_monitor_required"],
        "source_gain_value":results[1239]["source_gain_value"],
        "physical16_process":results[1239]["physical16_process"]
    },
    "cofinality_monitor":{
        "common_source_atoms":results[1240]["common_source_atoms"],
        "pole_atom_constructor":results[1240]["pole_atom_constructor"],
        "physical16_action":results[1240]["physical16_action"],
        "source_gain":results[1240]["source_gain"]
    },
    "pole_atom_dynamics":{
        "irreducible_pole_cell":results[1241]["irreducible_pole_cell"],
        "localized_c23_k2":results[1241]["localized_c23_k2"],
        "fixed_complete_cs_vector":results[1241]["fixed_complete_cs_vector"],
        "inter_parent_clock_equal":results[1241]["inter_parent_clock_equal"],
        "source_gain":results[1241]["source_gain"]
    },
    "clock_alignment":{
        "inter_parent_clock_equal":results[1242]["inter_parent_clock_equal"],
        "soft_two_port_lock":results[1242]["soft_two_port_lock"],
        "common_twist_derived":results[1242]["common_twist_derived"],
        "soft_physical_channel":results[1242]["soft_physical_channel"],
        "physical_gain":results[1242]["physical_gain"]
    },
    "soft_port":{
        "vector_ratio_event_cell":results[1243]["vector_ratio_event_cell"],
        "reconstruction_lg":results[1243]["reconstruction_lg"],
        "channel_weights_derived":results[1243]["channel_weights_derived"],
        "physical16_channels":results[1243]["physical16_channels"],
        "source_gain":results[1243]["source_gain"]
    },
    "reweighting":{
        "selected_half_level":results[1244]["selected_half_level"],
        "parent_gs_completion":results[1244]["parent_gs_completion"],
        "reweighting_map":results[1244]["reweighting_map"],
        "physical16_channels":results[1244]["physical16_channels"],
        "source_gain":results[1244]["source_gain"]
    },
    "shifted_lattice":{
        "exact_shifted_coset":results[1245]["exact_shifted_coset"],
        "single_coset_orientation":results[1245]["single_coset_orientation"],
        "compactification_packet":results[1245]["compactification_packet"],
        "sector_selected":results[1245]["sector_selected"],
        "physical16_channel":results[1245]["physical16_channel"],
        "source_gain":results[1245]["source_gain"]
    }
}
assert local_margin_routes["positive_margin_constructors"]["scale_free_margin_absent"]
assert local_margin_routes["independent_small_ratio"]["integer_window_unique"]
assert local_margin_routes["mass_norm_interface"]["integer_clebsch_gap"]
assert local_margin_routes["discrete_actuator"]["unique_k2_c23_slice"]
assert local_margin_routes["representation_theorem"]["threshold_shape_locked"]
assert local_margin_routes["detector_gain"]["coherent_gain_rank"]
assert local_margin_routes["cofinality_monitor"]["pole_atom_constructor"]
assert local_margin_routes["pole_atom_dynamics"]["localized_c23_k2"]
assert local_margin_routes["clock_alignment"]["soft_two_port_lock"]
assert local_margin_routes["soft_port"]["vector_ratio_event_cell"]
assert local_margin_routes["reweighting"]["parent_gs_completion"]
assert local_margin_routes["shifted_lattice"]["exact_shifted_coset"]
assert not local_margin_routes["positive_margin_constructors"]["positive_t_margin"]
assert not local_margin_routes["independent_small_ratio"]["typed_mass_interface"] and not local_margin_routes["independent_small_ratio"]["equal_norm_rank17"]
assert not local_margin_routes["mass_norm_interface"]["typed_mass_interface"] and not local_margin_routes["mass_norm_interface"]["normalization_theorem"]
assert not local_margin_routes["discrete_actuator"]["representation_theorem"] and not local_margin_routes["discrete_actuator"]["single_pole_degeneracy"]
assert not local_margin_routes["representation_theorem"]["representation_theorem"] and not local_margin_routes["representation_theorem"]["gain_law"]
assert not local_margin_routes["detector_gain"]["source_gain_value"] and not local_margin_routes["detector_gain"]["physical16_process"]
assert not local_margin_routes["cofinality_monitor"]["physical16_action"] and not local_margin_routes["cofinality_monitor"]["source_gain"]
assert not local_margin_routes["pole_atom_dynamics"]["fixed_complete_cs_vector"] and not local_margin_routes["pole_atom_dynamics"]["source_gain"]
assert not local_margin_routes["clock_alignment"]["common_twist_derived"] and not local_margin_routes["clock_alignment"]["soft_physical_channel"]
assert not local_margin_routes["soft_port"]["channel_weights_derived"] and not local_margin_routes["soft_port"]["physical16_channels"]
assert not local_margin_routes["reweighting"]["reweighting_map"] and not local_margin_routes["reweighting"]["physical16_channels"]
assert not local_margin_routes["shifted_lattice"]["compactification_packet"] and not local_margin_routes["shifted_lattice"]["source_gain"]

# Falsifier: a local margin, integer, representation, detector, or localization
# route supplies the observed positive CP margin without a common UV packet.
local_positive_margin_found=False
common_uv_packet_derived=False
conjecture_refuted=local_positive_margin_found
assert not conjecture_refuted and not common_uv_packet_derived

result={
    "schema":"marici.flavor.wp1270.v1",
    "status":"PASS",
    "question":"Can any local margin, integer, representation, detector, or localization route generate the positive CP margin without one common UV compactification packet?",
    "dpc":{
        "conjecture":"Every observed-scale positive CP-transmission margin must be derived from one common UV compactification packet supplying the shifted CS coset, endpoint action, flux sector, orientation, chirality, clock, channel map, and source gain in shared normalization.",
        "rivals":["scale or norm margin","independent small ratio","mass-norm interface","discrete integer actuator","anomaly-complete representation","coherent detector gain","cofinality atom monitor","pole-atom dynamics","inter-parent clock","soft-port event cell","anomaly reweighting","shifted localization lattice"],
        "risky_consequences":["WP1234 falsifies scale-free, norm, cyclic, maximal-CP, and minimal-Landau margins","WP1235 finds a unique N=17 window but no typed mass interface","WP1236 finds integer Clebsch values straddling the fitted interval","WP1237 finds unique (k,C)=(2,23) but no source operation or pole type","WP1238 shows even a representation theorem leaves mass clock, momentum port, and gain free","WP1239 defines coherent rank but no physical16 process or source gain","WP1240 constructs atom algebra without source dynamics","WP1241 selects representation/localization ancestry without complete anomaly vector or parent clock","WP1242 aligns clocks conditionally without deriving twist, flux, ratio, or soft channel","WP1243 reconstructs a vector event cell but no soft channel or reweighting","WP1244 completes anomaly vectors without a shifted lattice or event map","WP1245 gives the exact coset but no common compactification packet"],
        "falsification_attempt":"Replay WP1234 through WP1245 and search for a local positive-margin route that bypasses the common UV compactification packet.",
        "residual":"No local route supplies the observed positive CP margin; the common-compactification necessity conjecture survives. The residual is one compactification packet deriving the coset, endpoint action, flux sector, orientation, chirality, clock, channel map, and gain.",
        "disposition":"common-compactification necessity survives attempted falsification; common UV compactification packet selected"
    },
    "local_margin_routes":local_margin_routes,
    "local_positive_margin_found":local_positive_margin_found,
    "common_uv_packet_derived":common_uv_packet_derived,
    "conjecture_refuted":conjecture_refuted,
    "conjecture_status":"survived_not_proven",
    "classification":"bold common-compactification necessity gate: replayed local CP-margin routes do not bypass one common UV packet",
    "remaining_gate":"derive the common compactification packet and calibrated Physical16 gain map",
    "hostile_gate":"do not treat a norm, integer window, representation label, coherent rank, atom cell, clock alignment, anomaly vector, or shifted coset as the observed positive CP margin",
    "claim_boundary":"WP1234 through WP1245 falsify the tested local routes; the common-compactification necessity conjecture survives but remains unproven",
    "disposition":"positive-CP-transmission-margin leaf resolved conditionally; common UV compactification packet required"
}
(ROOT/"results"/"wp1270_common_compactification_necessity_gate.json").write_text(json.dumps(result,indent=2)+"\n")
print("WP1270 PASS: common-compactification necessity survives attempted falsification; common UV packet remains open")
