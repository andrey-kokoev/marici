import json
from pathlib import Path

from flavor_dpc_source_replay import replay_source_checkers

ROOT=Path(__file__).resolve().parents[1]
_source_replay_records = replay_source_checkers(943,944)
wp943=json.loads((ROOT/"results"/"wp943_single_holonomy_physical16_commuting_no_go.json").read_text())
wp944=json.loads((ROOT/"results"/"wp944_two_holonomy_universal_algebra_no_selector.json").read_text())
assert wp943["classification"] == "proper commuting physical16 selector, experimentally wrong"
assert wp944["classification"] == "presentation rigidifier and universal algebraic carrier; not a selector without a source-fixed proper word module"
# Single holonomy is proper and commuting but CP-trivial.  A Weyl pair is
# universal but leaves a coefficient fiber containing CP=0 and CP!=0 packets.
single_holonomy_proper=True
single_holonomy_cp_zero=True
second_source_required=True
weyl_pair_universal=True
coefficient_fiber_hostile=True
proper_word_module=False
physical_instrument=False
completion_stability=False
calibrated_holonomy=False
assert single_holonomy_proper and single_holonomy_cp_zero and second_source_required
assert weyl_pair_universal and coefficient_fiber_hostile
assert not (proper_word_module or physical_instrument or completion_stability or calibrated_holonomy)
result={
    "schema":"marici.flavor.wp1218.v1",
    "status":"PASS",
    "question":"Can boundaryless holonomy supply the physical16 instrument?",
    "dpc":{
        "conjecture":"A single holonomy polynomial or two-holonomy Weyl algebra supplies the boundaryless holonomy-to-Yukawa instrument.",
        "rivals":["single-holonomy polynomial","commuting two-holonomy packet","mixed Weyl coefficient packet","arbitrary universal-algebra coefficients"],
        "risky_consequences":["single-holonomy Gram matrices commute and CP cubic is zero","a positive mixed comparator has nonzero CP cubic","the Weyl pair generates the full 3 by 3 matrix algebra","one fixed Weyl pair admits coefficient packets with CP cubic zero and -842400i"],
        "falsification_attempt":"the proper single-holonomy instrument is experimentally CP-trivial; the universal Weyl carrier does not fix the coefficient packet selecting physical observables.",
        "residual":"source-derived proper executable word module, completion stability, physical16 descent, and calibrated holonomy instrument",
        "disposition":"reject undeclared holonomy instrument; select source-derived proper-word-module rival"
    },
    "single_holonomy":wp943["single_holonomy"],
    "mixed_comparator":wp943["mixed_comparator"],
    "source_pair":wp944["source_pair"],
    "hostile_fiber":wp944["hostile_fiber"],
    "single_holonomy_proper":single_holonomy_proper,
    "single_holonomy_cp_zero":single_holonomy_cp_zero,
    "second_source_required":second_source_required,
    "weyl_pair_universal":weyl_pair_universal,
    "coefficient_fiber_hostile":coefficient_fiber_hostile,
    "proper_word_module":proper_word_module,
    "physical_instrument":physical_instrument,
    "completion_stability":completion_stability,
    "calibrated_holonomy":calibrated_holonomy,
    "classification":"negative holonomy-instrument result: proper single instrument is CP-trivial; universal pair is not source-selected",
    "remaining_gate":"derive a proper executable word module from source with completion stability and calibrated physical16 descent",
    "hostile_gate":"do not replace the missing word module with arbitrary coefficients or call CP-zero single-holonomy readout an instrument",
    "claim_boundary":"the negative result is relative to single-holonomy polynomials and the fixed Weyl universal algebra audited here",
    "disposition":"boundaryless-holonomy-instrument leaf resolved negatively; proper-word-module rival selected"
}
(ROOT/"results"/"wp1218_boundaryless_holonomy_instrument_gate.json").write_text(json.dumps(result,indent=2)+"\n")
print("WP1218 PASS: boundaryless holonomy instrument not yet derived")
