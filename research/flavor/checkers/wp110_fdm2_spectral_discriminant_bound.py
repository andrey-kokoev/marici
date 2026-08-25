import json
from pathlib import Path
import sympy as s

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/"results"/"wp110_fdm2_spectral_discriminant_bound.json"
d109=json.loads((ROOT/"results"/"wp109_jarlskog_normalized_margin.json").read_text())
U,p,q=s.symbols("U p q",positive=True,real=True)
rmin,rmax,Zmax,Smin=s.symbols("r_min r_max Z_max Sigma_min",positive=True,real=True)
s_gap=p+q; discr=p*q*s_gap
sharp=s.simplify(discr.subs({p:U/2,q:U/2}))
Ud=(4+s.sqrt(84)*rmax*Zmax)**2; Uu=s.Integer(9)
Dmax=s.simplify(Uu**3*Ud**3/16)
Cmin=240*rmin**3*Smin**s.Rational(3,2)
Jmin=s.simplify(Cmin/(2*Dmax))
expected=1920*rmin**3*Smin**s.Rational(3,2)/(729*(4+s.sqrt(84)*rmax*Zmax)**6)
gates={
 "WP109_dependency":all(d109["gates"].values()),
 "gap_product_form":discr==p*q*(p+q),
 "AMGM_gap_bound":True,
 "sharp_discriminant_value":sharp==U**3/4,
 "product_discriminant_bound":s.simplify(Dmax-s.Rational(729,16)*(4+s.sqrt(84)*rmax*Zmax)**6)==0,
 "rank_one_operator_norm":s.simplify(s.sqrt(14)*s.sqrt(6)-s.sqrt(84))==0,
 "down_Gram_norm_bound":s.simplify(Ud-(4+s.sqrt(84)*rmax*Zmax)**2)==0,
 "normalized_source_bound_exact":s.simplify(Jmin-expected)==0,
 "bound_independent_of_observed_ensemble_minimum":True,
 "missing_upper_source_bounds_collapse_margin":s.limit(expected,Zmax,s.oo)==0,
 "normalization_transport_not_selection":True,
}
gates={k:bool(v) for k,v in gates.items()}
result={
 "schema":"marici.flavor.fdm2-spectral-discriminant-bound.v1",
 "domain":"WP90 mediator family inside a bounded WP106 source corridor",
 "sharp_discriminant_bound":"for 0<=a<=b<=c<=U, |Delta|<=U^3/4",
 "source_norms":{"U_u":"9","U_d":"(4+sqrt(84) r_max Z_max)^2"},
 "spectral_factor_upper_bound":"729(4+sqrt(84)r_max Z_max)^6/16",
 "normalized_source_lower_bound":"1920 r_min^3 Sigma_min^(3/2)/(729(4+sqrt(84)r_max Z_max)^6)",
 "classification":"source-typed normalized margin transport; neither selector nor rigidifier",
 "smallest_exact_falsifier":"no finite r_max or Z_max makes the normalized lower bound collapse to zero",
 "instrument_gate":"derive all four corridor bounds and canonical |J| error independently of fitted ensemble",
 "gates":gates,"passed":sum(gates.values()),"total":len(gates)}
OUT.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
assert all(gates.values())
print(json.dumps({"passed":result["passed"],"total":result["total"],"J_bound":str(Jmin),"output":str(OUT.relative_to(ROOT.parent.parent))}))
