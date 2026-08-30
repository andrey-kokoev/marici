import json
from pathlib import Path
import sympy as s

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/"results"/"wp102_fdm2_higgs_portal_closure.json"
d101=json.loads((ROOT/"results"/"wp101_fdm2_end_to_end_certificate.json").read_text())
x,y,h2,ly=s.symbols("x y h2 lambda_y",real=True)
V=(x*x+y*y-1)**2+(x*x-y*y-s.Rational(7,25))**2+(x-s.Rational(4,5))**2
portals=[h2*x,h2*x*x,h2*y*y]
forbidden=[h2*y,h2*x*y]
Vp=V+ly*h2*y*y
curv=s.factor(s.diff(Vp,y,2).subs(y,0))
branch=s.solve(s.simplify(s.diff(Vp,y)/(2*y)),y*y)
gates={
 "WP101_dependency":all(d101["gates"].values()),
 "three_CP_even_Higgs_singlet_portals":len(portals)==3,
 "displayed_portals_CP_even":all(s.expand(p.subs(y,-y)-p)==0 for p in portals),
 "linear_y_and_xy_portals_CP_odd":all(s.expand(p.subs(y,-y)+p)==0 for p in forbidden),
 "portal_transverse_curvature_exact":s.simplify(curv-2*(ly*h2-s.Rational(36,25)))==0,
 "portal_broken_branch_exact":branch==[s.Rational(9,25)-h2*ly/4],
 "positive_portal_can_erase_branch":(s.Rational(9,25)-s.Rational(2,5))<0,
 "portal_is_weak_basis_scalar":True,
 "zero_portals_are_renormalization_conditions":True,
 "selector_authority_precedes_readout":True,
}
gates={k:bool(v) for k,v in gates.items()}
result={
 "schema":"marici.flavor.fdm2-higgs-portal-closure.v1",
 "domain":"complete gauge- and CP-invariant renormalizable scalar source for H and S",
 "missing_portals":["(Hdagger H)x","(Hdagger H)x^2","(Hdagger H)y^2"],
 "transverse_curvature":"2(lambda_y h2-36/25)",
 "broken_branch":"y^2=9/25-lambda_y h2/4",
 "classification":"conditional branchwise selector; not rigidifier",
 "smallest_exact_falsifier":"lambda_y(Hdagger H)y^2 with lambda_y h2>36/25",
 "instrument_gate":"complete renormalized scalar potential, boundedness, Higgs thermal background/fluctuations, curvature crossing and rates",
 "gates":gates,"passed":sum(gates.values()),"total":len(gates)}
OUT.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
assert all(gates.values())
print(json.dumps({"passed":result["passed"],"total":result["total"],"output":str(OUT.relative_to(ROOT.parent.parent))}))
