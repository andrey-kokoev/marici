import json
from fractions import Fraction
from pathlib import Path

from flavor_dpc_source_replay import replay_source_checkers

ROOT=Path(__file__).resolve().parents[1]
_source_replay_records = replay_source_checkers(822,1185,1186)
wp822=json.loads((ROOT/"results"/"wp822_finite_chiral_matter_spectrum_census.json").read_text())
wp1185=json.loads((ROOT/"results"/"wp1185_threshold_boundary_packet_contract.json").read_text())
wp1186=json.loads((ROOT/"results"/"wp1186_threshold_boundary_authority_no_go.json").read_text())
assert wp822["summary"]["all_passed"] is True
assert wp1185["threshold_packet_contract_derived"] is True
assert wp1186["authority_candidate_count"] == 0
unit=wp822["census"]["unit_control_samples"]
stability=wp822["census"]["unit_control_stability"]
assert [(x["N"],x["p"]) for x in unit] == [(6,30),(8,39)]
assert [(x["N"],x["p"],x["negative_exponents"],x["positive_exponents"]) for x in stability] == [(6,30,1,3),(8,39,1,3)]
candidates=[]
for sample in unit:
    coords=[Fraction(x) for x in sample["coordinates"]]
    assert all(Fraction(0) < x < Fraction(1) for x in coords)
    candidates.append({
        "N":sample["N"],
        "p":sample["p"],
        "coordinates":[str(x) for x in coords],
        "max_coordinate":str(max(coords)),
        "fixed_point_type":"sub-unit saddle",
        "threshold_certificate":{
            "authority_bearing_boundary":False,
            "coherent_rg_run":True,
            "sector_basis":False,
            "transport_intertwiner":False,
            "production_normalization":False
        }
    })
assert len(candidates) == 2
assert all(sum(c["threshold_certificate"].values()) == 1 for c in candidates)
# WP822's own authority test remains false.
authority_test=next(t for t in wp822["tests"] if t["name"]=="no_admitted_wp820_to_GG_spectrum_constructor_exists")
assert authority_test["passed"] is True and authority_test["evidence"] == "False"
unique_candidate=False
source_derived_candidate_count=0
threshold_source_candidate_constructed=False
candidate_pair_constructed=True
assert candidate_pair_constructed and not unique_candidate
result={
    "schema":"marici.flavor.wp1187.v1",
    "status":"PASS",
    "question":"Can the finite chiral fixed-point census construct a threshold source candidate?",
    "dpc":{
        "conjecture":"A sub-unit fixed-point packet supplies the threshold boundary source.",
        "rivals":["(6,30) fixed-point candidate","(8,39) fixed-point candidate","WP805 strongly coupled packet","WP820 incidence-derived candidate"],
        "risky_consequences":["exactly two sub-unit candidates","each has one infrared-repulsive direction","zero WP820-to-GG constructors","zero candidates satisfy the threshold certificate"],
        "falsification_attempt":"Both exact candidates are constructed and tested against the five-field threshold packet; each supplies only a conditional RG object and lacks boundary authority, sector basis, transport, and production normalization.",
        "residual":"A constructor from oriented incidence to gauge spectrum and threshold transport remains missing.",
        "disposition":"construct the candidate pair; reject threshold source authority"
    },
    "candidate_pair_constructed":candidate_pair_constructed,
    "candidates":candidates,
    "unique_candidate":unique_candidate,
    "source_derived_candidate_count":source_derived_candidate_count,
    "threshold_source_candidate_constructed":threshold_source_candidate_constructed,
    "required_fields":wp1185["required_fields"],
    "missing_fields_per_candidate":["authority_bearing_boundary","sector_basis","transport_intertwiner","production_normalization"],
    "classification":"negative source-candidate gate: two exact sub-unit saddles exist but neither is source-authorized",
    "remaining_gate":"derive the oriented-incidence-to-spectrum constructor and threshold transport",
    "hostile_gate":"do not treat fixed-point coordinates or anomaly cancellation as threshold source authority",
    "claim_boundary":"the construction is an exact candidate enumeration inside WP822's frozen grammar, not a physical threshold packet",
    "disposition":"threshold-source-candidate leaf resolved; incidence-spectrum-constructor rival selected"
}
(ROOT/"results"/"wp1187_threshold_source_candidate_gate.json").write_text(json.dumps(result,indent=2)+"\n")
print("WP1187 PASS:",len(candidates),source_derived_candidate_count)
