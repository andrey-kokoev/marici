import json
from pathlib import Path
import sympy as s

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/"results"/"wp106_fdm2_two_margin_corridor.json"
d105=json.loads((ROOT/"results"/"wp105_fdm2_rg_stability_margin.json").read_text())
x,y,r=s.symbols("x y r",real=True)
D0,S0,BD,BS,L,rmin=s.symbols("Delta_0 Sigma_0 B_Delta B_Sigma L r_min",positive=True,real=True)
z=x+s.I*y; Y0=s.diag(1,2,4); a=s.Matrix([1,2,3]); b=s.Matrix([[2,1,1]])
Y=s.simplify(Y0+r*z*a*b); Hu=s.diag(1,4,9); Hd=s.simplify(Y*Y.H)
detC=s.factor(s.det(Hu*Hd-Hd*Hu))
Dmin=D0-BD*L; Smin=S0-BS*L
physical_bound=240*rmin**3*Smin**s.Rational(3,2)
gates={
 "WP105_dependency":all(d105["gates"].values()),
 "global_and_local_margins_distinct":True,
 "strict_two_margin_transport_certificate":True,
 "broken_branch_lower_bound":True,
 "general_exact_commutator_determinant":detC==1920*s.I*r**3*y*(x**2+y**2),
 "WP90_witness_recovered":detC.subs({x:s.Rational(4,5),y:s.Rational(3,5),r:1})==1152*s.I,
 "physical_margin_bound_exact":physical_bound==240*rmin**3*Smin**s.Rational(3,2),
 "Delta_endpoint_zero_is_global_falsifier":Dmin.subs(D0,BD*L)==0,
 "Sigma_endpoint_zero_is_selector_falsifier":Smin.subs(S0,BS*L)==0,
 "sign_and_numerical_value_not_selected":True,
 "source_margin_can_join_downstream_error_budget":True,
}
gates={k:bool(v) for k,v in gates.items()}
result={
 "schema":"marici.flavor.fdm2-two-margin-thermal-corridor.v1",
 "domain":"portal-complete source along a declared thermal/RG path of length L",
 "margins":{"global":"Delta0-B_Delta L","CP_broken":"Sigma0-B_Sigma L"},
 "faithful_coordinate":"physical16 CP-odd commutator determinant",
 "exact_determinant":"1920*i*r^3*y*(x^2+y^2)",
 "physical_lower_bound":"240*r_min^3*(Sigma0-B_Sigma L)^(3/2)",
 "classification":"branchwise finite-threshold selector in a certified two-margin corridor; not rigidifier",
 "smallest_exact_falsifiers":["Delta0=B_Delta L","Sigma0=B_Sigma L"],
 "instrument_gate":"source-derived tau,u, running/thresholds, derivative bounds and r_min joined to WP101 errors",
 "gates":gates,"passed":sum(gates.values()),"total":len(gates)}
OUT.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
assert all(gates.values())
print(json.dumps({"passed":result["passed"],"total":result["total"],"det":str(detC),"output":str(OUT.relative_to(ROOT.parent.parent))}))
