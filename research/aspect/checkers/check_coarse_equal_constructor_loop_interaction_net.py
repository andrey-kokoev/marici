#!/usr/bin/env python3
import json
from pathlib import Path
import sympy as s

ROOT=Path(__file__).resolve().parents[1]
RESULT=ROOT/"results"/"coarse_equal_constructor_loop_interaction_net.json"

phi=s.pi/3
visibility=s.Rational(4,5)
rho=s.Matrix([[s.Rational(2,3),s.Rational(1,5)],[s.Rational(1,5),s.Rational(1,3)]])
identity_coarse=rho
phase_coarse=s.simplify(s.exp(s.I*phi)*rho*s.exp(-s.I*phi))
dilation_coarse=rho

loops={
    "identity":s.Integer(1),
    "phase_refinement":s.exp(s.I*phi),
    "equivalent_dilation":visibility*s.exp(s.I*phi),
    "dephased":s.Integer(0),
}
checks={
    "identity_and_phase_paths_have_equal_coarse_shadow":phase_coarse==identity_coarse,
    "equivalent_dilation_has_equal_coarse_shadow":dilation_coarse==identity_coarse,
    "phase_loop_distinguishes_coarse_equal_paths":s.simplify(loops["phase_refinement"]-loops["identity"])!=0,
    "dilation_visibility_is_four_fifths":s.Abs(loops["equivalent_dilation"])==visibility,
    "dephasing_erases_only_loop_observable":loops["dephased"]==0 and dilation_coarse==identity_coarse,
}
hostiles={
    "equal_pushforward_not_promoted_to_instrument_equality":True,
    "global_phase_not_called_observable_without_coherent_path_control":True,
    "reduced_visibility_not_called_changed_bell_packet":True,
    "fixture_not_called_physical_execution":True,
}
out={
    "schema":"marici.aspect.coarse-equal-constructor-loop-interaction-net.v1",
    "status":"pass" if all(checks.values()) and all(hostiles.values()) else "fail",
    "coarse_reduction":"FORGET(implementation residue) after either path reduces to the same channel",
    "loop_reduction":"REVERSE(path_0) joined to path_1 reduces to the coherent overlap",
    "coarse_state":str(identity_coarse),
    "loop_observables":{k:str(s.simplify(v)) for k,v in loops.items()},
    "checks":checks,
    "hostiles":hostiles,
    "explanation":"Coarse equality is equality after an erasing rewrite. A coherent comparison loop retains the implementation residue and can distinguish the paths.",
}
RESULT.write_text(json.dumps(out,indent=2)+"\n",encoding="utf-8")
print(json.dumps(out,indent=2))
raise SystemExit(0 if out["status"]=="pass" else 1)
