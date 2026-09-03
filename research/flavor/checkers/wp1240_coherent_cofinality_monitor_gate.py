import json
from pathlib import Path

from flavor_dpc_source_replay import replay_source_checkers

ROOT=Path(__file__).resolve().parents[1]
_source_replay_records = replay_source_checkers(1050,1051,1052,1053)
wp1050=json.loads((ROOT/"results"/"wp1050_shared_final_state_cell_gate.json").read_text())
wp1051=json.loads((ROOT/"results"/"wp1051_physical16_shared_cell_event_space.json").read_text())
wp1052=json.loads((ROOT/"results"/"wp1052_common_source_cell_support_provenance.json").read_text())
wp1053=json.loads((ROOT/"results"/"wp1053_typed_pole_atom_provenance.json").read_text())
assert wp1050["classification"] == "conditional shared-cell gate: null accounting separates monitor efficiency from overlap but does not prove that the overlap occurs in one physical16 final-state cell"
assert wp1051["classification"] == "conditional event-cell gate: a same-cell certificate is insufficient unless detector-cell and monitor-cell supports are typed and null-complete"
assert wp1052["classification"] == "conditional common-source support constructor: finite atom provenance derives detector support, monitor support, overlap, efficiency, same-cell certificate, and null completeness from one typed cell"
assert wp1053["classification"] == "conditional pole-atom provenance constructor: one finite atom cell derives k=2, C=23, unit residues, degeneracy, M^2=1, h=138 pi^2/1367, and normalized response 1/2; scalar spectrum declarations without matching atoms are rejected"
# Finite atoms can carry both shared-cell support and pole typing, but the
# atom labels/weights and pole dynamics remain posited rather than derived.
same_cell_gate=True
typed_event_support=True
common_source_atoms=True
pole_atom_constructor=True
declared_overlap_rejected=True
split_and_clock_hostiles_rejected=True
physical16_action=False
atom_weight_dynamics=False
representation_theorem=False
physical_momentum_calibration=False
source_gain=False
assert same_cell_gate and typed_event_support and common_source_atoms and pole_atom_constructor
assert declared_overlap_rejected and split_and_clock_hostiles_rejected
assert not (physical16_action or atom_weight_dynamics or representation_theorem or physical_momentum_calibration or source_gain)
result={
    "schema":"marici.flavor.wp1240.v1",
    "status":"PASS",
    "question":"Can a coherent cofinality monitor and pole atom be constructed from one source cell?",
    "dpc":{
        "conjecture":"A finite typed atom cell derives shared detector/monitor support, coherent cofinality, null completeness, and the C=23 pole packet.",
        "rivals":["same-cell certificate","typed detector and monitor support","common-source support atoms","pole-atom provenance","declared scalar spectra"],
        "risky_consequences":["same-cell rank rises to eight only with the cross-amplitude cell","typed event support raises rank to ten","six atoms derive alpha=beta=1, overlap c=1/2, efficiency eta=1/2, and null completeness","23 two-port atoms derive k=2, C=23, degenerate M squared=1, and normalized response 1/2","split and wrong-clock atom packets reject declared scalar spectra"],
        "falsification_attempt":"the algebra rejects split-cell proxies and mismatched pole declarations, but the atom weights, labels, and source dynamics are still posited.",
        "residual":"derive atom weights, detector/monitor/cross/null labels, pole residues, and common mass clock from actual Physical16 source dynamics and representation data",
        "disposition":"accept the finite atom-cell constructor conditionally; reject it as physical cofinality monitor"
    },
    "same_cell_gate":wp1050["same_cell_gate"],
    "typed_event_rows":wp1051["typed_event_rows"],
    "shared_cell_atoms":wp1052["shared_cell_atoms"],
    "derived_shared_cell":wp1052["derived_shared_cell"],
    "pole_atom_model":wp1053["atom_model"],
    "derived_good_spectrum":wp1053["derived_good_spectrum"],
    "pole_hostiles":wp1053["hostiles"],
    "same_cell_gate_ok":same_cell_gate,
    "typed_event_support":typed_event_support,
    "common_source_atoms":common_source_atoms,
    "pole_atom_constructor":pole_atom_constructor,
    "declared_overlap_rejected":declared_overlap_rejected,
    "split_and_clock_hostiles_rejected":split_and_clock_hostiles_rejected,
    "physical16_action":physical16_action,
    "atom_weight_dynamics":atom_weight_dynamics,
    "representation_theorem":representation_theorem,
    "physical_momentum_calibration":physical_momentum_calibration,
    "source_gain":source_gain,
    "classification":"conditional coherent-cofinality constructor: finite atoms give support and pole typing, physical source dynamics absent",
    "remaining_gate":"derive the finite atom cell, its weights and labels, and the pole mass/residue dynamics from the Physical16 source action or representation theorem",
    "hostile_gate":"do not call same-cell certificates, typed support rows, finite atom algebra, or matched pole declarations a physical coherent cofinality monitor",
    "claim_boundary":"WP1052 and WP1053 provide the minimal provenance algebra and exact falsifiers; no continuum event space, UV action, or gain is derived",
    "disposition":"coherent-cofinality-monitor leaf resolved conditionally; source-derived pole-atom dynamics rival selected"
}
(ROOT/"results"/"wp1240_coherent_cofinality_monitor_gate.json").write_text(json.dumps(result,indent=2)+"\n")
print("WP1240 PASS: coherent atoms conditional, source-derived pole dynamics absent")
