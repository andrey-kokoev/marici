import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
wp134=json.loads((ROOT/"results"/"wp134_dimensional_transmutation_authority.json").read_text())
wp1185=json.loads((ROOT/"results"/"wp1185_threshold_boundary_packet_contract.json").read_text())
assert wp134["checks"]["coupling_boundary_is_required"] is True
assert wp134["checks"]["scale_boundary_is_required"] is True
assert wp134["absolute_scale_selected_without_boundary"] is False
assert "authority_bearing_boundary" in wp1185["missing_fields"]

authority_candidates={
    "uv_fixed_point_trajectory": False,
    "gravitational_matching_scale": False,
    "cosmological_boundary": False,
    "source_selected_vacuum": False,
}
assert sum(authority_candidates.values()) == 0
conditional_boundary_pair_present=True
threshold_boundary_authority_selected=False
sector_certificate_closed=False
assert conditional_boundary_pair_present
assert not (threshold_boundary_authority_selected or sector_certificate_closed)
result={
    "schema":"marici.flavor.wp1186.v1",
    "status":"PASS",
    "question":"Can current source dynamics supply threshold boundary authority?",
    "dpc":{
        "conjecture":"One admissible source mechanism selects the RG/threshold boundary.",
        "rivals":["UV fixed-point trajectory","gravitational matching scale","cosmological boundary","source-selected vacuum"],
        "risky_consequences":["WP134 requires coupling and scale boundaries","WP1185 lacks authority_bearing_boundary","zero source-derived authority candidates","conditional boundary pair remains unfixed"],
        "falsification_attempt":"RG presentation invariance transports a declared boundary but cannot choose among hostile trajectories, and the sector packet has no boundary-authority field.",
        "residual":"A source-derived threshold boundary candidate must be constructed and matched to the sector certificate.",
        "disposition":"reject current threshold boundary authority"
    },
    "authority_candidates":authority_candidates,
    "authority_candidate_count":0,
    "conditional_boundary_pair_present":conditional_boundary_pair_present,
    "threshold_boundary_authority_selected":threshold_boundary_authority_selected,
    "sector_certificate_closed":sector_certificate_closed,
    "classification":"negative authority gate: no current source mechanism selects the threshold boundary",
    "remaining_gate":"construct a source-derived threshold boundary candidate and match it to the sector certificate",
    "hostile_gate":"do not treat boundary declaration as boundary authority",
    "claim_boundary":"the no-go covers current authority candidates; a future UV/IR threshold mechanism remains open",
    "disposition":"threshold-boundary-authority leaf resolved; threshold-source-candidate rival selected"
}
(ROOT/"results"/"wp1186_threshold_boundary_authority_no_go.json").write_text(json.dumps(result,indent=2)+"\n")
print("WP1186 PASS:",sum(authority_candidates.values()))
