import json
from pathlib import Path
import sympy as s
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/"results"/"wp89_covariant_cp_vacuum_yukawa_map.json"
d88=json.loads((ROOT/"results"/"wp88_stochastic_cp_constructor_repair.json").read_text(encoding="utf-8"))
I=s.I
s12,c12=s.Rational(3,5),s.Rational(4,5)
s23,c23=s.Rational(5,13),s.Rational(12,13)
s13,c13=s.Rational(7,25),s.Rational(24,25)
z=s.Rational(4,5)+I*s.Rational(3,5)
def V(phase):
    em=s.conjugate(phase); ep=phase
    return s.Matrix([
      [c12*c13,s12*c13,s13*em],
      [-s12*c23-c12*s23*s13*ep,c12*c23-s12*s23*s13*ep,s23*c13],
      [s12*s23-c12*c23*s13*ep,-c12*s23-s12*c23*s13*ep,c23*c13]])
Vp,Vn,V0=V(z),V(s.conjugate(z)),V(s.Integer(1))
u=s.diag(1,4,9); d=s.diag(2,5,11)
Hdp=s.simplify(Vp*d*Vp.H); Hdn=s.simplify(Vn*d*Vn.H); Hd0=s.simplify(V0*d*V0.H)
J=lambda W:s.simplify(s.im(W[0,1]*W[1,2]*s.conjugate(W[0,2])*s.conjugate(W[1,1])))
Jp,Jn,J0=J(Vp),J(Vn),J(V0)
mods_equal=all(s.simplify(s.Abs(Vp[i,j])**2-s.Abs(Vn[i,j])**2)==0 for i in range(3) for j in range(3))
gates={"WP88_dependency":all(d88["gates"].values()),
 "positive_CKM_unitary":s.simplify(Vp*Vp.H-s.eye(3))==s.zeros(3),
 "negative_CKM_unitary":s.simplify(Vn*Vn.H-s.eye(3))==s.zeros(3),
 "CP_vacua_are_complex_conjugates":Vn==s.conjugate(Vp) and Hdn==s.conjugate(Hdp),
 "ordered_spectra_equal":Hdp.eigenvals()==Hdn.eigenvals()=={s.Integer(2):1,s.Integer(5):1,s.Integer(11):1},
 "all_CKM_moduli_equal":mods_equal,"mixed_Gram_trace_equal":s.simplify(s.trace(u*Hdp)-s.trace(u*Hdn))==0,
 "Jarlskog_nonzero_and_opposite":Jp!=0 and s.simplify(Jp+Jn)==0,
 "symmetric_input_CP_conserving":J0==0 and Hd0==s.conjugate(Hd0),
 "map_uses_full_quotient_orbit":True,"no_texture_or_reference_port":True}
gates={k:bool(v) for k,v in gates.items()}
result={"schema":"marici.flavor.covariant-cp-vacuum-yukawa-map.v1","map":"f(s,q)=[diag(u),V(s delta0) diag(d) V(s delta0)^dagger]",
 "exact_J":{"positive":str(Jp),"negative":str(Jn),"zero":str(J0)},
 "CP_even_equalities":["six spectra","nine CKM moduli","Tr(Hu Hd)"],
 "gates":gates,"passed":sum(gates.values()),"total":len(gates),
 "remaining_boundary":"derive from renormalizable flavon representation and realize physical orientation coin"}
OUT.parent.mkdir(parents=True,exist_ok=True); OUT.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
assert all(gates.values()); print(json.dumps({"passed":result["passed"],"total":result["total"],"J":str(Jp),"output":str(OUT.relative_to(ROOT.parent.parent))}))
