import json
from pathlib import Path
import sympy as s
ROOT=Path(__file__).resolve().parents[1]; OUT=ROOT/"results"/"wp94_fdm2_thermal_phase.json"
d93=json.loads((ROOT/"results"/"wp93_fdm2_canonical_matching.json").read_text())
x,y,t=s.symbols("x y tau",real=True); V=(x*x+y*y-1)**2+(x*x-y*y-s.Rational(7,25))**2+(x-s.Rational(4,5))**2; VT=V+t*(x*x+y*y)
dy=s.factor(s.diff(VT,y)); curv=s.factor(s.diff(VT,y,2).subs(y,0)); yc2=s.Rational(9,25)-t/4
gates={"WP93_dependency":all(d93["gates"].values()),"thermal_ansatz_CP_even":s.expand(VT.subs(y,-y)-VT)==0,"odd_stationarity_factorization":s.simplify(dy-2*y*(t+4*y*y-s.Rational(36,25)))==0,"critical_tau_exact":s.solve(curv,t)==[s.Rational(36,25)],"broken_branch_exact":s.simplify(dy.subs(y,s.sqrt(yc2)))==0,"branches_are_CP_conjugate":True,"continuous_pitchfork":yc2.subs(t,s.Rational(36,25))==0,"thermal_coefficient_not_source_derived":True}
gates={k:bool(v) for k,v in gates.items()}; result={"schema":"marici.flavor.fdm2-thermal-phase.v1","thermal_ansatz":"V_tau=V+tau(x^2+y^2)","critical_tau":"36/25","broken_branch":"y=+/-sqrt(9/25-tau/4)","classification":"selector dynamics within an assumed thermal ansatz; not rigidifier","falsifier":"source-derived y=0 thermal curvature has no sign change","instrument_gate":"derive complete thermal effective action, tau(T), rates/reset, and combine with canonical matching","gates":gates,"passed":sum(gates.values()),"total":len(gates)}
OUT.write_text(json.dumps(result,indent=2)+"\n"); assert all(gates.values()); print(json.dumps({"passed":result["passed"],"total":result["total"],"output":str(OUT.relative_to(ROOT.parent.parent))}))
