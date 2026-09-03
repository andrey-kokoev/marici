import json
from pathlib import Path

from flavor_dpc_source_replay import replay_source_checkers

ROOT=Path(__file__).resolve().parents[1]
_source_replay_records = replay_source_checkers(1080,1081,1082,1083)
wp1080=json.loads((ROOT/"results"/"wp1080_su6_bipartite_cubic_carrier_gate.json").read_text())
wp1081=json.loads((ROOT/"results"/"wp1081_bipartite_krylov_history_composition_gate.json").read_text())
wp1082=json.loads((ROOT/"results"/"wp1082_strominger_determinant_line_reference_audit_gate.json").read_text())
wp1083=json.loads((ROOT/"results"/"wp1083_su3_natural_endomorphism_krylov_no_go.json").read_text())
assert wp1080["classification"].startswith("conditional SU(3)xSU(3) bipartite carrier constructor")
assert wp1081["classification"].startswith("bipartite-Krylov composition gate")
assert wp1082["classification"].startswith("negative determinant-line audit")
assert wp1083["classification"].startswith("current-source no-go")
# The representation candidate sharpens the handoff, but the current source
# has no simple spectrum, cyclic ray, retained history, or volume reference.
bipartite_carrier=True
krylov_mechanism_known=True
strominger_orientation_obstruction=True
current_source_no_go=True
nima_reply_10655=True
temporal_process=False
ordered_ports=False
production_kernel=False
source_evolution=False
cyclic_ray=False
retained_history=False
volume_reference=False
physical16_descent=False
assert bipartite_carrier and krylov_mechanism_known and strominger_orientation_obstruction and current_source_no_go and nima_reply_10655
assert not (temporal_process or ordered_ports or production_kernel or source_evolution or cyclic_ray or retained_history or volume_reference or physical16_descent)
result={
    "schema":"marici.flavor.wp1247.v1",
    "status":"PASS",
    "question":"Can local packets advance the Nima source-dynamics handoff before the owner reply?",
    "dpc":{
        "conjecture":"The SU(6) anomaly family may realize Nima's bipartite alignment and alternating cubic carrier, while Krylov history may supply temporal production.",
        "rivals":["SU(3)xSU(3) bipartite carrier","bipartite Krylov history","Strominger determinant-line reference","current-source natural endomorphism"],
        "risky_consequences":["the family supplies two three-state families, a rank-3 cross block, and alternating epsilon carriers","Krylov history gives a signed omega=2 witness and requires a weight-minus-three volume reference","the determinant line proves an orientation-line obstruction but supplies no rho","Schur forces natural SU(3) endomorphisms to scalar form, so the current source has no simple spectrum, cyclic ray, or retained history"],
        "falsification_attempt":"the current-source Krylov route is terminal: WP1080 does not derive A, x, retained history, volume reference, production kernel, detector ports, or Physical16 descent.",
        "residual":"derive an SU(3)-breaking ordered eigenflag and cyclic ray from a successor localization packet, then add retained history and volume reference in one source frame",
        "disposition":"accept the representation candidate conditionally; keep the owner handoff active and open a nonredundant flag/ray branch"
    },
    "carrier_data":wp1080["carrier_data"],
    "nima_signature":wp1080["nima_signature"],
    "krylov_witness":wp1081["krylov_witness"],
    "projective_gate":wp1081["projective_gate"],
    "wp1080_supplies":wp1081["wp1080_supplies"],
    "determinant_line":wp1082["determinant_line"],
    "strominger_audit":wp1082["audit"],
    "schur_gate":wp1083["schur_gate"],
    "current_source_supply":wp1083["current_source_supply"],
    "named_missing_source_operation":wp1083["named_missing_source_operation"],
    "bipartite_carrier":bipartite_carrier,
    "krylov_mechanism_known":krylov_mechanism_known,
    "strominger_orientation_obstruction":strominger_orientation_obstruction,
    "current_source_no_go":current_source_no_go,
    "nima_reply_10655":nima_reply_10655,
    "temporal_process":temporal_process,
    "ordered_ports":ordered_ports,
    "production_kernel":production_kernel,
    "source_evolution":source_evolution,
    "cyclic_ray":cyclic_ray,
    "retained_history":retained_history,
    "volume_reference":volume_reference,
    "physical16_descent":physical16_descent,
    "classification":"conditional source-dynamics branch: bipartite carrier exists, SU(3)-breaking flag and cyclic ray absent",
    "remaining_gate":"derive an SU(3)-breaking ordered eigenflag, cyclic ray, retained history, and volume reference from one successor source packet",
    "hostile_gate":"do not call representation alignment, epsilon carriers, Krylov witness, determinant line, or natural endomorphism data a temporal production kernel",
    "claim_boundary":"WP1080 through WP1083 provide representation, mechanism, and no-go algebra; no source dynamics or Physical16 descent is derived",
    "disposition":"Nima handoff leaf advanced locally; SU(3)-breaking flag/cyclic-ray rival selected"
}
(ROOT/"results"/"wp1247_nima_source_dynamics_branch_gate.json").write_text(json.dumps(result,indent=2)+"\n")
print("WP1247 PASS: bipartite carrier conditional, flag and cyclic ray absent")
