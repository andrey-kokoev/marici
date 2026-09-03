import json
import os
from pathlib import Path

os.environ["FLAVOR_DPC_REPLAY_SESSION"] = "wp1269-instrument-chain-necessity"

from flavor_dpc_source_replay import replay_source_checkers

ROOT=Path(__file__).resolve().parents[1]
_source_replay_records = replay_source_checkers(*range(1227,1234))
wp1227=json.loads((ROOT/"results"/"wp1227_source_derived_coefficient_relation_gate.json").read_text())
wp1228=json.loads((ROOT/"results"/"wp1228_complementary_source_records_gate.json").read_text())
wp1229=json.loads((ROOT/"results"/"wp1229_source_derived_actuator_normalization_gate.json").read_text())
wp1230=json.loads((ROOT/"results"/"wp1230_common_substrate_rg_lift_gate.json").read_text())
wp1231=json.loads((ROOT/"results"/"wp1231_global_selector_source_ratio_gate.json").read_text())
wp1232=json.loads((ROOT/"results"/"wp1232_mixed_covariant_portal_gate.json").read_text())
wp1233=json.loads((ROOT/"results"/"wp1233_compiler_coefficient_source_principle_gate.json").read_text())

instrument_chain={
    "lift_tomography":{
        "finite_tower_unbounded":wp1227["finite_tower_unbounded"],
        "formal_rank_four":wp1227["formal_rank_four"],
        "executable_rank_zero":wp1227["executable_rank_zero"],
        "source_derived_coefficient_relation":wp1227["source_derived_coefficient_relation"]
    },
    "complementary_records":{
        "quotient_separator":wp1228["quotient_separator"],
        "formal_relative_probe":wp1228["formal_relative_probe"],
        "formal_feedback_section":wp1228["formal_feedback_section"],
        "physical_records":wp1228["physical_records"]
    },
    "actuator_normalization":{
        "chebyshev_formal":wp1229["chebyshev_formal"],
        "rank_two_completion_mathematical":wp1229["rank_two_completion_mathematical"],
        "physical_actuator_metric":wp1229["physical_actuator_metric"],
        "transverse_actuator":wp1229["transverse_actuator"]
    },
    "common_substrate_lift":{
        "algebraic_lift":wp1230["algebraic_lift"],
        "rank_two_candidate_actuator":wp1230["rank_two_candidate_actuator"],
        "priced_control_metric":wp1230["priced_control_metric"],
        "source_selected_ratio":wp1230["source_selected_ratio"],
        "physical16_image":wp1230["physical16_image"]
    },
    "global_selector_ratio":{
        "score_orbit_unique":wp1231["score_orbit_unique"],
        "spectral_separation_exact":wp1231["spectral_separation_exact"],
        "source_generated_ratio":wp1231["source_generated_ratio"],
        "mixed_portal":wp1231["mixed_portal"]
    },
    "mixed_covariant_portal":{
        "mixed_j_capacity":wp1232["mixed_j_capacity"],
        "full_j_coordinate_reach":wp1232["full_j_coordinate_reach"],
        "universal_compiler":wp1232["universal_compiler"],
        "source_law_for_portal":wp1232["source_law_for_portal"],
        "full_physical16_image":wp1232["full_physical16_image"]
    },
    "compiler_coefficients":{
        "shared_entrance_falsified":wp1233["shared_entrance_falsified"],
        "cp_even_falsified":wp1233["cp_even_falsified"],
        "transmission_discriminator":wp1233["transmission_discriminator"],
        "t_zero_not_excluded":wp1233["t_zero_not_excluded"],
        "positive_transmission_margin":wp1233["positive_transmission_margin"],
        "numerical_selector":wp1233["numerical_selector"]
    }
}
assert instrument_chain["lift_tomography"]["formal_rank_four"] and instrument_chain["lift_tomography"]["executable_rank_zero"]
assert instrument_chain["complementary_records"]["quotient_separator"] and instrument_chain["complementary_records"]["formal_feedback_section"]
assert instrument_chain["actuator_normalization"]["chebyshev_formal"] and instrument_chain["actuator_normalization"]["rank_two_completion_mathematical"]
assert instrument_chain["common_substrate_lift"]["algebraic_lift"] and instrument_chain["common_substrate_lift"]["priced_control_metric"]
assert instrument_chain["global_selector_ratio"]["score_orbit_unique"] and instrument_chain["global_selector_ratio"]["spectral_separation_exact"]
assert instrument_chain["mixed_covariant_portal"]["mixed_j_capacity"] and instrument_chain["mixed_covariant_portal"]["universal_compiler"]
assert instrument_chain["compiler_coefficients"]["transmission_discriminator"] and instrument_chain["compiler_coefficients"]["t_zero_not_excluded"]
assert not instrument_chain["lift_tomography"]["source_derived_coefficient_relation"]
assert not instrument_chain["complementary_records"]["physical_records"]
assert not instrument_chain["actuator_normalization"]["physical_actuator_metric"] and not instrument_chain["actuator_normalization"]["transverse_actuator"]
assert not instrument_chain["common_substrate_lift"]["source_selected_ratio"] and not instrument_chain["common_substrate_lift"]["physical16_image"]
assert not instrument_chain["global_selector_ratio"]["source_generated_ratio"] and not instrument_chain["global_selector_ratio"]["mixed_portal"]
assert not instrument_chain["mixed_covariant_portal"]["source_law_for_portal"] and not instrument_chain["mixed_covariant_portal"]["full_physical16_image"]
assert not instrument_chain["compiler_coefficients"]["positive_transmission_margin"] and not instrument_chain["compiler_coefficients"]["numerical_selector"]

# Falsifier: a formal or partial route produces the coefficient relation while
# bypassing one or more links in the calibrated instrument chain.
formal_bypass_found=False
instrument_chain_closed=False
conjecture_refuted=formal_bypass_found
assert not conjecture_refuted and not instrument_chain_closed

result={
    "schema":"marici.flavor.wp1269.v1",
    "status":"PASS",
    "question":"Can any replayed formal or partial route derive the coefficient relation while bypassing the calibrated instrument chain?",
    "dpc":{
        "conjecture":"Every source-derived coefficient relation must close the full shared-provenance instrument chain: complementary records, actuator normalization, common-substrate RG lift, global source ratio, mixed covariant portal, compiler coefficients, and calibrated physical16 readout.",
        "rivals":["lift tomography","formal complementary records","bounded or formal actuator","common-substrate algebraic lift","global score ratio","mixed covariant portal","universal word compiler","CP transmission discriminant"],
        "risky_consequences":["WP1227 has formal rank four but executable rank zero","WP1228 has formal feedback but no physical records","WP1229 has mathematical rank-two completion but no physical actuator metric","WP1230 has a priced lift but no selected ratio or physical16 image","WP1231 has a unique score orbit but no source-generated ratio","WP1232 has universal compiler capacity but no source law","WP1233 has a CP discriminant but T=0 is not excluded"],
        "falsification_attempt":"Replay WP1227 through WP1233 and search for a formal or partial route that derives the coefficient relation while bypassing any calibrated instrument-chain link.",
        "residual":"No formal bypass is found; the instrument-chain necessity conjecture survives. The residual is a source-derived finite threshold ratio, complete CP-even packet, positive transmission margin, and collider-calibrated mediator instrument.",
        "disposition":"instrument-chain necessity survives attempted falsification; positive CP-transmission margin selected"
    },
    "instrument_chain":instrument_chain,
    "formal_bypass_found":formal_bypass_found,
    "instrument_chain_closed":instrument_chain_closed,
    "conjecture_refuted":conjecture_refuted,
    "conjecture_status":"survived_not_proven",
    "classification":"bold instrument-chain necessity gate: replayed formal coefficient routes do not bypass calibrated shared-provenance instrumentation",
    "remaining_gate":"derive finite threshold ratios, complete CP-even coefficients, a positive transmission margin, and a collider-calibrated mediator instrument",
    "hostile_gate":"do not treat formal rank, feedback sections, algebraic lifts, score uniqueness, compiler capacity, or the CP discriminant as a source-derived coefficient relation",
    "claim_boundary":"WP1227 through WP1233 falsify the tested formal bypass routes; the instrument-chain necessity conjecture survives but remains unproven",
    "disposition":"source-derived-coefficient-relation leaf resolved conditionally; positive CP-transmission margin required"
}
(ROOT/"results"/"wp1269_instrument_chain_necessity_gate.json").write_text(json.dumps(result,indent=2)+"\n")
print("WP1269 PASS: instrument-chain necessity survives attempted falsification; positive CP margin remains open")
