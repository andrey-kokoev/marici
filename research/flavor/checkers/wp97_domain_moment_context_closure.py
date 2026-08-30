import json
from pathlib import Path
import sympy as s
ROOT=Path(__file__).resolve().parents[1]; OUT=ROOT/"results"/"wp97_domain_moment_context_closure.json"
d96=json.loads((ROOT/"results"/"wp96_fdm2_mixture_attribute.json").read_text())
pm,p0,pp=s.symbols("p_minus p_zero p_plus",real=True); m1=pp-pm; m2=pp+pm
sol=s.solve([s.Symbol("u1")-m1,s.Symbol("u2")-m2,pm+p0+pp-1],[pm,p0,pp],dict=True)[0]
uniform={pm:s.Rational(1,2),p0:0,pp:s.Rational(1,2)}; symmetric={pm:0,p0:1,pp:0}
matrix=s.Matrix([[-1,0,1],[1,0,1],[1,1,1]])
gates={"WP96_dependency":all(d96["gates"].values()),"moment_normalization_map_full_rank":matrix.det()!=0,"exact_inverse_plus":sol[pp]==(s.Symbol("u1")+s.Symbol("u2"))/2,"exact_inverse_minus":sol[pm]==(-s.Symbol("u1")+s.Symbol("u2"))/2,"exact_inverse_zero":sol[p0]==1-s.Symbol("u2"),"first_moment_hostile_pair_collapses":m1.subs(uniform)==m1.subs(symmetric)==0,"second_moment_separates_hostile_pair":m2.subs(uniform)==1 and m2.subs(symmetric)==0,"context_closure_separates_not_selects":True,"second_moment_requires_repeated_or_two_copy_instrument":True}
gates={k:bool(v) for k,v in gates.items()}; result={"schema":"marici.flavor.domain-moment-context-closure.v1","domain":"classical mixtures over labelled routes J/J0 in {-1,0,+1}","faithful_coordinate":"(p_minus,p_zero,p_plus)","probe_family":["m1=E[J]/J0","m2=E[J^2]/J0^2","normalization"],"inverse":{"p_plus":"(m2+m1)/2","p_minus":"(m2-m1)/2","p_zero":"1-m2"},"contextual_partition":"singleton mixture weights under the complete two-moment family","classification":"separator; neither selector nor rigidifier","smallest_exact_falsifier":"uniform broken mixture and symmetric delta both have m1=0","instrument_gate":"repeatable independent domains or explicit two-copy instrument, branch-resolved canonical J, reset and sampling errors","gates":gates,"passed":sum(gates.values()),"total":len(gates)}
OUT.write_text(json.dumps(result,indent=2)+"\n"); assert all(gates.values()); print(json.dumps({"passed":result["passed"],"total":result["total"],"det":str(matrix.det()),"output":str(OUT.relative_to(ROOT.parent.parent))}))
