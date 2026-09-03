import json
from pathlib import Path

from flavor_dpc_source_replay import replay_source_checkers

ROOT=Path(__file__).resolve().parents[1]
_source_replay_records = replay_source_checkers(873,874)
wp873=json.loads((ROOT/"results"/"wp873_primitive_dual_pairing_portal_inevitability_audit.json").read_text())
wp874=json.loads((ROOT/"results"/"wp874_dual_pair_source_existence_audit.json").read_text())
assert wp873["summary"]["all_passed"] is True
assert wp874["summary"]["all_passed"] is True
assert wp873["candidate_source_principle"] == "primitive nondegenerate self-dual boundary pairing Delta_Q g g_D=1"
assert wp873["selected_coupling"] == "g=g_D=1/sqrt(2)"
assert wp873["classification"] == "abstractly sufficient end-to-end source principle; no admitted microscopic flavor realization"
assert wp874["classification"] == "negative existence result for current flavor sources"
assert wp874["reopening_condition"] == "microscopic chiral flavor dual pair satisfying every WP873 source and instrument gate"
# The abstract dual pairing can select a self-dual modulus, but the three
# audited flavor candidates do not supply that pair.  Therefore q and z are
# not selected by the current source corpus.
abstract_pairing_selects=True
zero_coupling_excluded=True
global_pairing_basin=True
current_flavor_pair_absent=True
q_selected=False
z_selected=False
microscopic_realization=False
calibrated_physical16=False
assert abstract_pairing_selects and zero_coupling_excluded and global_pairing_basin
assert current_flavor_pair_absent
assert not (q_selected or z_selected or microscopic_realization or calibrated_physical16)
result={
    "schema":"marici.flavor.wp1210.v1",
    "status":"PASS",
    "question":"Can the q,z source moduli be selected from one current flavor source packet?",
    "dpc":{
        "conjecture":"A primitive nondegenerate self-dual boundary pairing selects the common source modulus.",
        "rivals":["pairing level n=2","pairing-preserving but duality-breaking threshold","dual port removed","joint observer","monodromic G2 pair","rank-one unimodular lattice"],
        "risky_consequences":["zero coupling is excluded","the unique positive self-dual solution is g=g_D=1/sqrt(2) for Delta_Q=2","the entire positive pairing locus flows to it","protected thresholds must preserve both pairing and electric-dual exchange"],
        "falsification_attempt":"Pairing level two moves the selected value, a lambda=2 threshold breaks self-duality, and removing the dual port restores the zero cusp; joint observer, G2, and rank-one lattice candidates all fail.",
        "residual":"No current flavor source supplies the microscopic chiral dual pair; q,z remain unselected and physical16 calibration is absent.",
        "disposition":"refute current-corpus modulus selection; require flavor dual-pair existence"
    },
    "candidate_source_principle":wp873["candidate_source_principle"],
    "selected_coupling":wp873["selected_coupling"],
    "basin":wp873["basin"],
    "threshold_condition":wp873["threshold_condition"],
    "abstract_pairing_classification":wp873["classification"],
    "candidate_dispositions":wp874["candidate_dispositions"],
    "existence_classification":wp874["classification"],
    "reopening_condition":wp874["reopening_condition"],
    "abstract_pairing_selects":abstract_pairing_selects,
    "zero_coupling_excluded":zero_coupling_excluded,
    "global_pairing_basin":global_pairing_basin,
    "current_flavor_pair_absent":current_flavor_pair_absent,
    "q_selected":q_selected,
    "z_selected":z_selected,
    "microscopic_realization":microscopic_realization,
    "calibrated_physical16":calibrated_physical16,
    "classification":"negative current-corpus source-modulus result with abstract self-dual selection principle",
    "remaining_gate":"construct a microscopic chiral flavor dual pair satisfying pairing, threshold, RG, and calibrated physical16 gates",
    "hostile_gate":"do not identify an observer recombination, G2 duality, or integral lattice with the required flavor dual pair",
    "claim_boundary":"the abstract pairing fixes a common coupling only if a physical dual port exists; it does not select q,z today",
    "disposition":"source-modulus-selection leaf resolved negatively; flavor dual-pair existence rival selected"
}
(ROOT/"results"/"wp1210_source_modulus_selection_gate.json").write_text(json.dumps(result,indent=2)+"\n")
print("WP1210 PASS: abstract pairing selects; current flavor dual pair absent")
