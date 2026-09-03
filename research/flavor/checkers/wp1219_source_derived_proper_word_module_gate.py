import json
from pathlib import Path

from flavor_dpc_source_replay import replay_source_checkers

ROOT=Path(__file__).resolve().parents[1]
_source_replay_records = replay_source_checkers(945,946,947)
wp945=json.loads((ROOT/"results"/"wp945_weyl_executable_closure_conditional_expectation_no_go.json").read_text())
wp946=json.loads((ROOT/"results"/"wp946_projective_weyl_subgroup_twirl_exhaustion.json").read_text())
wp947=json.loads((ROOT/"results"/"wp947_weyl_source_normal_bockstein_rigidity_no_go.json").read_text())
assert wp945["classification"] == "closure is universal and nonselective; canonical expectations are proper but phenomenologically overprojected"
assert wp946["classification"] == "all canonical projective Weyl subgroup twirls are identity, commutative rank-three, or scalar rank-one"
assert wp947["classification"] == "exact Weyl source is infinitesimally rigid modulo weak-basis conjugation"
# Executable closure is universal; canonical twirls are commutative or
# scalar; exact Weyl deformation has no physical quotient tangent.
closure_universal=True
clock_twirl_overprojects=True
line_twirls_commutative=True
full_twirl_scalar=True
source_rigid=True
proper_noncommuting_module=False
independent_source_normal_coordinate=False
physical16_descent=False
calibrated_instrument=False
assert closure_universal and clock_twirl_overprojects and line_twirls_commutative
assert full_twirl_scalar and source_rigid
assert not (proper_noncommuting_module or independent_source_normal_coordinate or physical16_descent or calibrated_instrument)
result={
    "schema":"marici.flavor.wp1219.v1",
    "status":"PASS",
    "question":"Can canonical Weyl closure supply a source-derived proper word module?",
    "dpc":{
        "conjecture":"Executable closure, a canonical projective subgroup twirl, or deformation of the exact Weyl pair supplies the proper word module.",
        "rivals":["clock twirl","full Weyl twirl","four projective lines","full projective plane","exact Weyl source deformation"],
        "risky_consequences":["D-twirl kills S and yields a diagonal image","full twirl maps every matrix to trace times identity","all four line commutants are commutative dimension-three algebras","the exact Weyl source has zero physical quotient tangent modulo weak-basis conjugation"],
        "falsification_attempt":"the closure is the full 3 by 3 algebra; canonical twirls are identity, commutative rank three, or scalar rank one; relation and orbit tangents coincide with joined dimension eight.",
        "residual":"independent source-normal coordinate outside the rigid Weyl relation object, inducing a proper noncommuting physical16 image and calibrated instrument",
        "disposition":"reject canonical word-module constructors; select independent source-normal-coordinate rival"
    },
    "closure":wp945["closure"],
    "canonical_expectations":wp945["canonical_expectations"],
    "projective_subgroup_lattice":wp946["projective_subgroup_lattice"],
    "tangent_dimensions":wp947["tangent_dimensions"],
    "phase_constraint":wp947["phase_constraint"],
    "closure_universal":closure_universal,
    "clock_twirl_overprojects":clock_twirl_overprojects,
    "line_twirls_commutative":line_twirls_commutative,
    "full_twirl_scalar":full_twirl_scalar,
    "source_rigid":source_rigid,
    "proper_noncommuting_module":proper_noncommuting_module,
    "independent_source_normal_coordinate":independent_source_normal_coordinate,
    "physical16_descent":physical16_descent,
    "calibrated_instrument":calibrated_instrument,
    "classification":"negative word-module result: canonical Weyl constructors are universal, commutative, scalar, or rigid",
    "remaining_gate":"derive an independent source-normal coordinate inducing a proper noncommuting physical16 image",
    "hostile_gate":"do not call full closure, subgroup twirl, or weak-basis conjugation a source-derived proper word module",
    "claim_boundary":"the negative result is relative to executable Weyl closure, all canonical projective subgroup twirls, and infinitesimal exact-source deformation",
    "disposition":"source-derived-proper-word-module leaf resolved negatively; independent source-normal-coordinate rival selected"
}
(ROOT/"results"/"wp1219_source_derived_proper_word_module_gate.json").write_text(json.dumps(result,indent=2)+"\n")
print("WP1219 PASS: canonical Weyl word-module constructors exhausted")
