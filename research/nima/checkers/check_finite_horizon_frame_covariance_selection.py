"""Exact finite-horizon covariance branch-selection gate."""
import json
from pathlib import Path
import sympy as sp

v,L,k=sp.symbols("v L k", real=True, nonzero=True)
compose=lambda x,y:sp.cancel((x+y)/(1+k*x*y))
boundary_shift=sp.factor(compose(L,v)-L)
condition=sp.solve(sp.together(boundary_shift).as_numer_denom()[0],k)

# Galilean specialization.
galilean_shift=sp.simplify(((L+v)-L))
# Positive branch substitution.
positive_shift=sp.simplify(boundary_shift.subs(k,1/L**2))

assert condition==[L**(-2)]
assert galilean_shift==v
assert positive_shift==0

result={
 "schema":"marici.finite-horizon-frame-covariance-selection.v1",
 "premises":[
  "local constructor composition yields a finite nonzero probe horizon L in one frame",
  "frame transport acts by the homogeneous associative composition law",
  "the probe horizon is natural and therefore preserved by every frame transport",
 ],
 "checks":{
  "boundary_covariance_equation":"L (+)_k v - L = v*(1-k*L^2)/(1+k*L*v)",
  "unique_parameter":"k=1/L^2",
  "galilean_boundary_shift":"v",
  "positive_branch_boundary_shift":"0",
 },
 "repository_provenance_audit":{
  "machian_discrete_wave":"finite cone is built into the nearest-neighbor hyperbolic evolution rule",
  "null_ray_helicity":"Lorentz metric, time orientation, and future null ray are admitted source data",
  "carrier_bridge":"no established map currently derives spacetime frame transport or its finite horizon from the common Carrier",
 },
 "verdict":(
  "Finite local probe reach plus natural frame covariance selects the positive "
  "Lorentz-like branch exactly. The selection is presently conditional in "
  "Marici because the common Carrier has not yet been shown to derive the "
  "spacetime probe horizon and boost transport."
 )
}
out=Path(__file__).parents[1]/"results"/"finite_horizon_frame_covariance_selection.json"
out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
print(json.dumps(result,indent=2))
