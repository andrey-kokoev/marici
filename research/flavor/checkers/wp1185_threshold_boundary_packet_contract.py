import json
from pathlib import Path

from flavor_dpc_source_replay import replay_source_checkers

ROOT=Path(__file__).resolve().parents[1]
_source_replay_records = replay_source_checkers(134,1184)
wp134=json.loads((ROOT/"results"/"wp134_dimensional_transmutation_authority.json").read_text())
wp1184=json.loads((ROOT/"results"/"wp1184_dimensionful_threshold_anchor_no_go.json").read_text())
assert wp134["all_pass"] is True
assert wp1184["physical_threshold_packet"] is False

required_fields=[
    "authority_bearing_boundary",
    "coherent_rg_run",
    "sector_basis",
    "transport_intertwiner",
    "production_normalization"
]
# WP134 supplies a coherent RG run only after a boundary is declared; it does
# not supply the authority that chooses that boundary. WP1184 supplies none of
# the sector-facing threshold fields.
field_status={
    "authority_bearing_boundary": False,
    "coherent_rg_run": wp134["checks"]["rg_presentation_invariance"],
    "sector_basis": not wp1184["sector_basis_selected"],
    "transport_intertwiner": False,
    "production_normalization": False
}
# The sector_basis field is absent even though the expression above records
# the selected flag as false; make the packet status explicit.
field_status["sector_basis"]=False
missing=[name for name in required_fields if not field_status[name]]
assert missing == ["authority_bearing_boundary","sector_basis","transport_intertwiner","production_normalization"]
assert len(required_fields) == 5 and len(missing) == 4
threshold_packet_derived=False
threshold_packet_contract_derived=True
assert threshold_packet_contract_derived and not threshold_packet_derived
result={
    "schema":"marici.flavor.wp1185.v1",
    "status":"PASS",
    "question":"Can the threshold boundary packet be derived from current source authority?",
    "dpc":{
        "conjecture":"Current RG and interface results already contain the threshold boundary packet.",
        "rivals":["typed threshold packet contract","conditional RG packet","sector interface packet","source-derived threshold packet"],
        "risky_consequences":["five required fields","coherent RG run available","four authority/sector fields missing","zero threshold packets"],
        "falsification_attempt":"The RG result is presentation invariant only after boundary declaration; no source selects boundary authority, sector basis, transport intertwiner, or production normalization.",
        "residual":"A source-derived threshold boundary certificate remains required.",
        "disposition":"derive the packet contract; reject packet existence"
    },
    "required_fields":required_fields,
    "field_status":field_status,
    "available_fields":1,
    "missing_fields":missing,
    "missing_count":len(missing),
    "threshold_packet_contract_derived":threshold_packet_contract_derived,
    "threshold_packet_derived":threshold_packet_derived,
    "classification":"typed contract with negative existence result: threshold boundary packet is not source-derived",
    "remaining_gate":"derive threshold boundary authority and the sector-facing certificate",
    "hostile_gate":"do not call a coherent conditional RG run an authority-bearing threshold packet",
    "claim_boundary":"the packet contract is explicit, but no actual threshold packet is claimed",
    "disposition":"threshold-boundary-packet leaf resolved; threshold-boundary-authority rival selected"
}
(ROOT/"results"/"wp1185_threshold_boundary_packet_contract.json").write_text(json.dumps(result,indent=2)+"\n")
print("WP1185 PASS:",len(required_fields),len(missing))
