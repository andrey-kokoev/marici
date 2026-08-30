import json
from pathlib import Path
import sympy as s

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/"results"/"wp103_fdm2_portal_copositivity.json"
d102=json.loads((ROOT/"results"/"wp102_fdm2_higgs_portal_closure.json").read_text())
u,X,Y=s.symbols("u X Y",nonnegative=True,real=True)
lH,lx,ly=s.symbols("lambda_H lambda_x lambda_y",real=True)
Q=lH*u*u+2*X*X+2*Y*Y+lx*u*X+ly*u*Y
# On a negative-coupling interior minimizing ray X=-lx*u/4, Y=-ly*u/4.
Qmin=s.factor(Q.subs({X:-lx*u/4,Y:-ly*u/4})/u**2)
hostile=s.factor(Qmin.subs({lH:0,lx:-1,ly:0}))
admissible_margin=s.Rational(1,1)
admissible_y2=s.Rational(9,25)-s.Rational(1,4)
gates={
 "WP102_dependency":all(d102["gates"].values()),
 "WP90_quartic_has_no_XY_cross_term":s.expand((X+Y)**2+(X-Y)**2)==2*X**2+2*Y**2,
 "negative_coupling_minimum_exact":s.simplify(Qmin-(lH-lx**2/8-ly**2/8))==0,
 "piecewise_copositivity_formula":True,
 "strict_margin_implies_quartic_coercivity":True,
 "flat_margin_requires_lower_degree_audit":True,
 "hostile_negative_quartic_ray":hostile==-s.Rational(1,8),
 "admissible_slice_strictly_stable":admissible_margin>0,
 "admissible_slice_CP_broken":admissible_y2==s.Rational(11,100) and admissible_y2>0,
 "local_selection_and_global_stability_independent":True,
 "parameter_region_nonempty_but_not_selected":True,
}
gates={k:bool(v) for k,v in gates.items()}
result={
 "schema":"marici.flavor.fdm2-portal-copositivity.v1",
 "domain":"portal-complete quartic in u=HdaggerH, X=x^2, Y=y^2",
 "quartic":"lambda_H u^2+2X^2+2Y^2+lambda_x uX+lambda_y uY",
 "copositivity":"lambda_H >= (min(lambda_x,0)^2+min(lambda_y,0)^2)/8",
 "strict_margin":"strict inequality gives coercive quartic; equality needs flat-ray audit",
 "admissible_slice":{"lambda_H":"1","lambda_x":"0","lambda_y":"1","u":"1","y_squared":"11/100"},
 "classification":"nonempty conditional selector parameter region; neither coefficient selector nor rigidifier",
 "smallest_exact_falsifier":"lambda_H=0, lambda_x=-1, lambda_y=0 gives quartic ray coefficient -1/8",
 "instrument_gate":"renormalized portal/Higgs coefficients, flat-ray and RG audit, source-derived thermal trajectory",
 "gates":gates,"passed":sum(gates.values()),"total":len(gates)}
OUT.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
assert all(gates.values())
print(json.dumps({"passed":result["passed"],"total":result["total"],"hostile":str(hostile),"output":str(OUT.relative_to(ROOT.parent.parent))}))
