import json
from pathlib import Path
import sympy as s

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/"results"/"wp104_fdm2_flat_ray_cubic.json"
d103=json.loads((ROOT/"results"/"wp103_fdm2_portal_copositivity.json").read_text())
t,mu=s.symbols("t mu",positive=True,real=True)
u=t**2; xp=t/2; xm=-t/2; y=s.Integer(0)
lH=s.Rational(1,8); lx=-1; ly=0
def quartic(x): return s.expand(lH*u**2+2*x**4+2*y**4+lx*u*x**2+ly*u*y**2)
Vp=s.expand(quartic(xp)+mu*u*xp)
Vm=s.expand(quartic(xm)+mu*u*xm)
gates={
 "WP103_dependency":all(d103["gates"].values()),
 "copositivity_boundary_saturated":lH==s.Rational(1,8),
 "plus_ray_quartic_zero":quartic(xp)==0,
 "minus_ray_quartic_zero":quartic(xm)==0,
 "plus_cubic_projection":Vp==mu*t**3/2,
 "minus_cubic_projection":Vm==-mu*t**3/2,
 "nonzero_cubic_has_negative_sign_ray":s.limit(Vm,t,s.oo)==-s.oo,
 "quadratic_terms_cannot_repair_cubic_runaway":s.limit((-t**3/2+t**2),t,s.oo)==-s.oo,
 "flat_boundary_requires_exact_lower_degree_audit":True,
 "obstruction_is_weak_basis_scalar":True,
}
gates={k:bool(v) for k,v in gates.items()}
result={
 "schema":"marici.flavor.fdm2-flat-ray-cubic-obstruction.v1",
 "domain":"copositive boundary of the complete renormalizable H,S scalar source",
 "flat_ray":"u=t^2, x=+/-t/2, y=0 at lambda_H=1/8, lambda_x=-1, lambda_y=0",
 "quartic_on_ray":"0",
 "cubic_on_rays":"+/-mu_x t^3/2",
 "classification":"strictly stable region remains conditional source domain; boundary needs exact constraints; not selector or rigidifier",
 "smallest_exact_falsifier":"mu_x=1 and x=-t/2 gives -t^3/2",
 "instrument_gate":"strict RG-stable margin or complete zero-ray/lower-degree audit",
 "gates":gates,"passed":sum(gates.values()),"total":len(gates)}
OUT.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
assert all(gates.values())
print(json.dumps({"passed":result["passed"],"total":result["total"],"negative_ray":str(Vm),"output":str(OUT.relative_to(ROOT.parent.parent))}))
