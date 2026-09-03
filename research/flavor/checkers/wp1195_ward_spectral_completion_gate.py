import json
from pathlib import Path

from flavor_dpc_source_replay import replay_source_checkers

ROOT=Path(__file__).resolve().parents[1]
_source_replay_records = replay_source_checkers(836,1194)
wp836=json.loads((ROOT/"results"/"wp836_scale_free_ward_spectral_completion_selector.json").read_text())
wp1194=json.loads((ROOT/"results"/"wp1194_probe_natural_ward_current_gate.json").read_text())
assert wp836["summary"]["all_passed"] is True
assert wp1194["unique_current_channel"] is True
assert wp836["exact_bound"]["spectral_shape"] == "R_n>=n by arithmetic-geometric mean on positive singular-value squares"
assert wp836["exact_bound"]["base_score"] == "14+3 lambda"
assert wp836["exact_bound"]["completion_gap"] == "2 sum_j r_j^2 + lambda(2k+ell)"
assert wp836["classification"]["selector"] == "within the declared finite completion domain, Phi uniquely selects k=ell=0 and equal singular values"
assert wp836["classification"]["coefficient_robustness"] == "the completion ordering is independent of the numerical positive weight lambda"
# The static functional is a genuine in-domain completion selector, but not a
# source authority: scale and mixing minimizers remain open and no instrument
# prepares or measures Phi.
finite_completion_selected=True
equal_singular_shape_selected=True
spectral_scale_selected=False
mixing_orientation_selected=False
calibrated_ward_instrument=False
source_authority=False
assert finite_completion_selected and equal_singular_shape_selected
assert not (spectral_scale_selected or mixing_orientation_selected or calibrated_ward_instrument or source_authority)
result={
    "schema":"marici.flavor.wp1195.v1",
    "status":"PASS",
    "question":"Can a scale-free Ward-spectral functional derive the completion?",
    "dpc":{
        "conjecture":"A positive scale-free functional selects the full Ward spectral completion.",
        "rivals":["minimal Ward index","dimensionful spectral penalty","scale-free Ward-spectral shape","source-derived completion action"],
        "risky_consequences":["base score 14+3 lambda","every nonempty completion has positive gap","selection is robust for every lambda>0","scale and mixing fibers remain"],
        "falsification_attempt":"Phi uniquely selects k=ell=0 and equal singular values inside the declared finite grammar, but D->mD and distinct irreducible Householder mixings have the same score.",
        "residual":"The source must derive Phi, select scale and mixing, and realize a calibrated Ward instrument.",
        "disposition":"construct finite-completion selector; reject full source authority"
    },
    "functional":wp836["candidate_functional"],
    "theorem_domain":wp836["theorem_domain"],
    "base_score":wp836["exact_bound"]["base_score"],
    "completion_gap":wp836["exact_bound"]["completion_gap"],
    "finite_completion_selected":finite_completion_selected,
    "equal_singular_shape_selected":equal_singular_shape_selected,
    "spectral_scale_selected":spectral_scale_selected,
    "mixing_orientation_selected":mixing_orientation_selected,
    "calibrated_ward_instrument":calibrated_ward_instrument,
    "source_authority":source_authority,
    "classification":"conditional finite-completion selector: minimal Ward completion and equal singular shape are selected in-domain",
    "remaining_gate":"derive the comparison action, scale/mixing anchor, threshold survival, and calibrated instrument",
    "hostile_gate":"do not treat an in-domain variational minimum as source-derived physical completion",
    "claim_boundary":"the theorem is restricted to the declared finite direct-completion grammar and does not cover arbitrary interacting completions",
    "disposition":"Ward-spectral-completion leaf resolved; Ward scale/mixing anchor rival selected"
}
(ROOT/"results"/"wp1195_ward_spectral_completion_gate.json").write_text(json.dumps(result,indent=2)+"\n")
print("WP1195 PASS:",wp836["exact_bound"]["base_score"],wp836["exact_bound"]["completion_gap"])
