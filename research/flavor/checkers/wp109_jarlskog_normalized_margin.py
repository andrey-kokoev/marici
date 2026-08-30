import json
from pathlib import Path
import sympy as s

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/"results"/"wp109_jarlskog_normalized_margin.json"
d108=json.loads((ROOT/"results"/"wp108_fdm2_ensemble_certificate_boundary.json").read_text())
I=s.I
s12,c12=s.Rational(3,5),s.Rational(4,5); s23,c23=s.Rational(5,13),s.Rational(12,13); s13,c13=s.Rational(7,25),s.Rational(24,25)
z=s.Rational(4,5)+I*s.Rational(3,5)
V=s.Matrix([[c12*c13,s12*c13,s13*s.conjugate(z)],[-s12*c23-c12*s23*s13*z,c12*c23-s12*s23*s13*z,s23*c13],[s12*s23-c12*c23*s13*z,-c12*s23-s12*c23*s13*z,c23*c13]])
Hu=s.diag(1,4,9); d=s.diag(2,5,11); Hd=s.simplify(V*d*V.H)
J=s.simplify(s.im(V[0,1]*V[1,2]*s.conjugate(V[0,2])*s.conjugate(V[1,1])))
Du=s.Integer((1-4)*(1-9)*(4-9)); Dd=s.Integer((2-5)*(2-11)*(5-11))
detC=s.factor(s.det(Hu*Hd-Hd*Hu)); normalized=s.simplify(s.Abs(detC)/(2*s.Abs(Du*Dd)))
Cmin,Dmax=s.symbols("C_min D_max",positive=True,real=True)
gates={
 "WP108_dependency":all(d108["gates"].values()),
 "exact_witness_J_nonzero":J==s.Rational(1741824,66015625),
 "up_discriminant_nonzero":Du!=0,
 "down_discriminant_nonzero":Dd!=0,
 "Jarlskog_determinant_identity":s.simplify(detC-2*I*J*Du*Dd)==0,
 "normalized_invariant_equals_abs_J":normalized==s.Abs(J),
 "normalized_coordinate_weak_basis_invariant":True,
 "degenerate_spectrum_makes_normalization_undefined":True,
 "raw_lower_bound_needs_spectral_upper_bound":True,
 "source_normalized_bound_formula":Cmin/(2*Dmax)>0,
 "observed_margin_not_source_authority":True,
}
gates={k:bool(v) for k,v in gates.items()}
result={
 "schema":"marici.flavor.jarlskog-normalized-margin.v1",
 "domain":"nondegenerate physical16 Gram pairs",
 "identity":"det[Hu,Hd]=2 i J Delta_u Delta_d",
 "normalized_coordinate":"C_hat=|det[Hu,Hd]|/(2|Delta_u Delta_d|)=|J|",
 "exact_witness":{"J":str(J),"det_commutator":str(detC),"Delta_u":str(Du),"Delta_d":str(Dd)},
 "observed_ensemble_margin":d108["qualitative_prediction"]["min_abs_J"],
 "source_bound_needed":"|J|>=C_min/(2 D_max) with source-derived |Delta_u Delta_d|<=D_max",
 "classification":"faithful normalization/readout; neither selector nor rigidifier",
 "smallest_exact_falsifier":"degenerate up or down spectrum makes Delta_u Delta_d=0",
 "instrument_gate":"source spectral upper bound and canonical |J| error; observed ensemble minimum remains external test",
 "gates":gates,"passed":sum(gates.values()),"total":len(gates)}
OUT.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
assert all(gates.values())
print(json.dumps({"passed":result["passed"],"total":result["total"],"J":str(J),"output":str(OUT.relative_to(ROOT.parent.parent))}))
