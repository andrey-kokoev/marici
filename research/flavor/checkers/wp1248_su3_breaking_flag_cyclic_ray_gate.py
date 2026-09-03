import json
from pathlib import Path

from flavor_dpc_source_replay import replay_source_checkers

ROOT=Path(__file__).resolve().parents[1]
_source_replay_records = replay_source_checkers(1084,1085,1086,1087,1088,1089)
wp1084=json.loads((ROOT/"results"/"wp1084_localized_quartet_flag_refinement_no_go.json").read_text())
wp1085=json.loads((ROOT/"results"/"wp1085_flux_wilson_doublet_flag_gate.json").read_text())
wp1086=json.loads((ROOT/"results"/"wp1086_wilson_flag_cyclic_ray_gate.json").read_text())
wp1087=json.loads((ROOT/"results"/"wp1087_wilson_history_dilation_gate.json").read_text())
wp1088=json.loads((ROOT/"results"/"wp1088_history_bundle_volume_reference_gate.json").read_text())
wp1089=json.loads((ROOT/"results"/"wp1089_oriented_adjoint_doublet_breaking_no_go.json").read_text())
assert wp1084["classification"].startswith("localized-quartet flag no-go")
assert wp1085["classification"].startswith("conditional constructor")
assert wp1086["classification"].startswith("conditional flag no-go for the ray")
assert wp1087["classification"].startswith("conditional history constructor")
assert wp1088["classification"].startswith("conditional reference no-go")
assert wp1089["classification"].startswith("current-source no-go")
# The conditional Wilson route is explicit, but the current source lacks an
# oriented adjoint ray, coherent seed, physical history, rho, and descent.
localized_refinement_no_go=True
wilson_split_conditional=True
simple_flag_conditional=True
isometric_history_conditional=True
volume_reference_missing=True
oriented_adjoint_ray=False
ordered_weight_lines=False
cyclic_seed=False
physical_history=False
rho=False
physical16_descent=False
assert localized_refinement_no_go and wilson_split_conditional and simple_flag_conditional
assert isometric_history_conditional and volume_reference_missing
assert not (oriented_adjoint_ray or ordered_weight_lines or cyclic_seed or physical_history or rho or physical16_descent)
result={
    "schema":"marici.flavor.wp1248.v1",
    "status":"PASS",
    "question":"Can a Wilson or adjoint route derive the SU(3)-breaking flag and cyclic ray?",
    "dpc":{
        "conjecture":"A source-fixed Wilson or adjoint breaking may refine the localized 2+1 flag into an ordered three-line Krylov source.",
        "rivals":["localized quartet refinement","generic Wilson doublet split","Wilson 1+1+1 flag","three-grade history bundle","history volume reference","oriented adjoint doublet breaking"],
        "risky_consequences":["the existing localization gives an unbroken A triplet and only a B-side 2+1 flag","a generic Wilson line would split to 1+1+1 but does not select phase, eigenbasis, or ordering","a simple flag still makes every selected eigenline non-cyclic","unitary Wilson evolution admits an exact isometric three-grade bundle only conditionally","the bundle gives determinant amplitude D and a comparison node but no weight-minus-three rho","natural doublet endomorphisms remain scalar, while an adjoint direction requires orientation"],
        "falsification_attempt":"the current source does not supply the oriented adjoint ray, ordered weight lines, coherent cyclic seed, physical grade register, rho, or Physical16 descent.",
        "residual":"derive an oriented adjoint ray in su(2)_B from a source packet; then derive cyclic preparation, history, rho, and Physical16 descent",
        "disposition":"accept the Wilson/history constructors conditionally; reject them as sourced dynamics"
    },
    "common_branching":wp1084["common_branching"],
    "spectra":wp1084["spectra"],
    "wilson_line":wp1085["wilson_line"],
    "conditional_branching":wp1085["conditional_branching"],
    "wilson_flag":wp1086["wilson_flag"],
    "krylov_witnesses":wp1086["krylov_witnesses"],
    "history_bundle":wp1087["history_bundle"],
    "history_supply":wp1087["conditional_supply"],
    "determinant":wp1088["determinant"],
    "history_bundle_supply":wp1088["history_bundle_supply"],
    "schur_gate":wp1089["schur_gate"],
    "adjoint_direction_gate":wp1089["adjoint_direction_gate"],
    "current_source_supply":wp1089["current_source_supply"],
    "localized_refinement_no_go":localized_refinement_no_go,
    "wilson_split_conditional":wilson_split_conditional,
    "simple_flag_conditional":simple_flag_conditional,
    "isometric_history_conditional":isometric_history_conditional,
    "volume_reference_missing":volume_reference_missing,
    "oriented_adjoint_ray":oriented_adjoint_ray,
    "ordered_weight_lines":ordered_weight_lines,
    "cyclic_seed":cyclic_seed,
    "physical_history":physical_history,
    "rho":rho,
    "physical16_descent":physical16_descent,
    "classification":"conditional flag-cyclic-ray gate: Wilson history constructors exist, oriented source ray absent",
    "remaining_gate":"derive an oriented adjoint ray in su(2)_B, then coherent cyclic preparation, physical history, rho, and Physical16 descent",
    "hostile_gate":"do not call localization refinement, Wilson split, simple flag, isometric history, determinant amplitude, or scalar adjoint data a source flag and cyclic ray",
    "claim_boundary":"WP1084 through WP1089 provide conditional constructor algebra and current-source no-go; no source dynamics or descent is derived",
    "disposition":"SU(3)-breaking flag/cyclic-ray leaf resolved conditionally; oriented-adjoint-ray rival selected"
}
(ROOT/"results"/"wp1248_su3_breaking_flag_cyclic_ray_gate.json").write_text(json.dumps(result,indent=2)+"\n")
print("WP1248 PASS: Wilson route conditional, oriented adjoint ray absent")
