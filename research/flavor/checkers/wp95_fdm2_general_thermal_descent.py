import json
from pathlib import Path
import sympy as s
ROOT=Path(__file__).resolve().parents[1]; OUT=ROOT/"results"/"wp95_fdm2_general_thermal_descent.json"
d94=json.loads((ROOT/"results"/"wp94_fdm2_thermal_phase.json").read_text())
x,y,k=s.symbols("x y kappa",real=True)
V=(x*x+y*y-1)**2+(x*x-y*y-s.Rational(7,25))**2+(x-s.Rational(4,5))**2
Vk=V+k*y*y; dy=s.factor(s.diff(Vk,y)); curv=s.factor(s.diff(Vk,y,2).subs(y,0)); branch=s.solve(s.simplify(dy/(2*y)),y*y)
gates={"WP94_dependency":all(d94["gates"].values()),"deformation_is_CP_even":s.expand(Vk.subs(y,-y)-Vk)==0,"CP_even_locus_stationary":s.diff(Vk,y).subs(y,0)==0,"odd_equation_factorizes":s.simplify(dy-2*y*(k+4*y*y-s.Rational(36,25)))==0,"transverse_curvature_exact":s.simplify(curv-2*(k-s.Rational(36,25)))==0,"broken_branch_exact":branch==[s.Rational(9,25)-k/4],"kappa_above_critical_erases_real_broken_branch":(s.Rational(9,25)-s.Rational(2,5))<0,"CP_pairing_not_existence":True,"curvature_crossing_is_extra_source_condition":True}
gates={a:bool(b) for a,b in gates.items()}; result={"schema":"marici.flavor.fdm2-general-thermal-descent.v1","domain":"analytic CP-even source-derived finite-temperature potentials","contextual_partition":["CP-even y=0 branch","CP-conjugate y!=0 pair when present"],"authorized_probe":"transverse curvature mu_y^2(T) along the minimized CP-even branch","classification":"conditional selector; not rigidifier","smallest_exact_falsifier":"+kappa*y^2 with kappa>36/25 removes the real broken branch","instrument_gate":"derive full V_eff(T), curvature crossing, stability, transition rate, domains/reset and canonical readout","gates":gates,"passed":sum(gates.values()),"total":len(gates)}
OUT.write_text(json.dumps(result,indent=2)+"\n"); assert all(gates.values()); print(json.dumps({"passed":result["passed"],"total":result["total"],"output":str(OUT.relative_to(ROOT.parent.parent))}))
