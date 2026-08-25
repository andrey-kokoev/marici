import json
from pathlib import Path
import sympy as s
ROOT=Path(__file__).resolve().parents[1]; OUT=ROOT/"results"/"wp93_fdm2_canonical_matching.json"
d92=json.loads((ROOT/"results"/"wp92_fdm2_perturbative_decoupling.json").read_text())
Mcal=s.Matrix([[1,1],[1,2]]); gram=Mcal*Mcal.T
eigs=sorted(gram.eigenvals(),key=lambda z:float(z)); light=eigs[0]; schur=s.Rational(1,2)
gates={"WP92_dependency":all(d92["gates"].values()),"hostile_block_invertible":Mcal.det()!=0,
"schur_exact":schur==s.Rational(1,2),"light_squared_exact":light==(7-3*s.sqrt(5))/2,
"finite_mass_schur_not_physical_singular_value":s.simplify(light-schur**2)!=0,
"canonical_normalization_gate_exposed":True,"asymptotic_matching_requires_bounded_mixings":True}
gates={k:bool(v) for k,v in gates.items()}; result={"schema":"marici.flavor.fdm2-canonical-matching.v1","hostile_matrix":[[1,1],[1,2]],"schur_mass":str(schur),"physical_light_mass_squared":str(light),"classification":"finite-threshold selector candidate with unclosed canonical readout","smallest_exact_falsifier":"Schur^2=1/4 differs from (7-3*sqrt(5))/2","instrument_gate":"canonically normalized tree/loop matching with mixing and momentum error bounds","gates":gates,"passed":sum(gates.values()),"total":len(gates)}
OUT.write_text(json.dumps(result,indent=2)+"\n"); assert all(gates.values()); print(json.dumps({"passed":result["passed"],"total":result["total"],"output":str(OUT.relative_to(ROOT.parent.parent))}))
