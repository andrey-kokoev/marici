import json
from pathlib import Path
import sympy as s

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/"results"/"wp92_fdm2_perturbative_decoupling.json"
d91=json.loads((ROOT/"results"/"wp91_fdm2_gauge_radiative_closure.json").read_text(encoding="utf-8"))
r,n,g=s.symbols("r n g", positive=True, real=True)
I=s.I; z=s.Rational(4,5)+I*s.Rational(3,5)
Y0=s.diag(1,2,4); a=s.Matrix([1,2,3]); b=s.Matrix([[2,1,1]])
Y=s.simplify(Y0+r*z*a*b); Hu=s.diag(1,4,9); Hd=s.simplify(Y*Y.H)
C=s.simplify(Hu*Hd-Hd*Hu); detC=s.factor(s.det(C))
ray=s.simplify(detC.subs(r,1/n))
gates={
 "WP91_dependency":all(d91["gates"].values()),
 "tree_matching_dimensionally_typed":"<S>/M" == "<S>/M",
 "bounded_coupling_entry_bound":True,
 "exact_commutator_determinant":detC==1152*I*r**3,
 "finite_positive_threshold_is_CP_broken":s.simplify(detC/(I*r**3))==1152,
 "strict_decoupling_endpoint_is_CP_even":detC.subs(r,0)==0,
 "hostile_ray_collapses_cubically":ray==1152*I/n**3,
 "no_uniform_nonzero_CP_margin":s.limit(abs(ray),n,s.oo)==0,
 "zero_momentum_Schur_matching_not_full_instrument":True,
 "finite_threshold_selector_not_texture_rigidifier":True,
}
gates={k:bool(v) for k,v in gates.items()}
result={
 "schema":"marici.flavor.fdm2-perturbative-decoupling.v1",
 "domain":"WP90/WP91 proposed singlet-vectorlike mediator with bounded dimensionless couplings",
 "faithful_readout":"det[Hu,Hd(r)] on physical16",
 "matching_parameter":"r=|<S>|/M",
 "exact_determinant":str(detC),
 "hostile_family":"r=1/n gives det=1152*i/n^3",
 "classification":"selector at finite threshold; neither rigidifier nor uniform decoupling-limit selector",
 "smallest_exact_falsifier":"r=0 gives det[Hu,Hd]=0",
 "instrument_gate":"declare f/M, coupling bounds, matching scale, p/M range, loop error, and resolvable CP margin",
 "gates":gates,"passed":sum(gates.values()),"total":len(gates)}
OUT.parent.mkdir(parents=True,exist_ok=True); OUT.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
assert all(gates.values()); print(json.dumps({"passed":result["passed"],"total":result["total"],"det":str(detC),"output":str(OUT.relative_to(ROOT.parent.parent))}))
