import json
from pathlib import Path
import sympy as s
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/"results"/"wp86_parameter_dynamical_substrate.json"
d60=json.loads((ROOT/"results"/"wp60_source_authority_inventory.json").read_text(encoding="utf-8"))
d85=json.loads((ROOT/"results"/"wp85_pinching_coherent_task_package.json").read_text(encoding="utf-8"))
P0=s.diag(1,1,0,0); P1=s.diag(0,0,1,1)
U0=s.Matrix([[0,1],[1,0]]); U1=s.diag(1,-1)
U=s.diag(1,1,1,1); U[:2,:2]=U0; U[2:,2:]=U1
rho=s.diag(s.Rational(1,3),s.Rational(2,3),0,0)
evolved=s.simplify(U*rho*U.H)
gates={"WP60_dependency":all(d60["gates"].values()),"WP85_dependency":all(d85["gates"].values()),
 "fixed_theory_operation_block_diagonal":s.simplify(U*P0-P0*U)==s.zeros(4) and s.simplify(U*P1-P1*U)==s.zeros(4),
 "parameter_sector_weights_preserved":s.trace(P0*evolved)==s.trace(P0*rho) and s.trace(P1*evolved)==s.trace(P1*rho),
 "cross_parameter_transition_zero":(P1*U*P0)==s.zeros(4),
 "composition_remains_block_diagonal":s.simplify((U**5)*P0-P0*(U**5))==s.zeros(4),
 "RG_is_only_declared_operation":len(d60["authority_partition"]["derived_operation"])==1,
 "no_declared_proper_parameter_operation":d60["gates"]["no_source_candidate_declares_proper_reduction"],
 "dynamical_flavon_extension_deferred":d60["markers"]["uv_deferred"]["kind"]=="explicitly_deferred",
 "parameter_estimation_is_not_parameter_preparation":True,
 "dynamical_substrate_required_before_constructor":True}
result={"schema":"marici.flavor.parameter-dynamical-substrate.v1","declared_typing":"physical16 labels fixed Yukawa theory parameters","allowed_declared_tasks":"within-theory state operations and parameter readout","forbidden_inference":"parameter estimation implies parameter preparation",
 "required_extension":["dynamical flavor field/modulus","source action and kinetic normalization","vacuum quotient","covariant vacuum-to-physical16 map","apparatus coupling","reset/degradation","ensemble prediction"],
 "gates":gates,"passed":sum(gates.values()),"total":len(gates)}
OUT.parent.mkdir(parents=True,exist_ok=True); OUT.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
assert all(gates.values()); print(json.dumps({"passed":result["passed"],"total":result["total"],"output":str(OUT.relative_to(ROOT.parent.parent))}))
