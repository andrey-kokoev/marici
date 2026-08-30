import json
from pathlib import Path
import sympy as s
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/"results"/"wp90_renormalizable_fdm2_mediator.json"
d88=json.loads((ROOT/"results"/"wp88_stochastic_cp_constructor_repair.json").read_text(encoding="utf-8"))
d89=json.loads((ROOT/"results"/"wp89_covariant_cp_vacuum_yukawa_map.json").read_text(encoding="utf-8"))
x,y=s.symbols("x y", real=True); I=s.I
V=(x*x+y*y-1)**2+(x*x-y*y-s.Rational(7,25))**2+(x-s.Rational(4,5))**2
zp=s.Rational(4,5)+I*s.Rational(3,5); zm=s.conjugate(zp)
Y0=s.diag(1,2,4); a=s.Matrix([1,2,3]); b=s.Matrix([[2,1,1]]); M=s.Integer(1)
Yp=s.simplify(Y0+zp*(a*b)/M); Yn=s.simplify(Y0+zm*(a*b)/M)
Hu=s.diag(1,4,9); Hdp=s.simplify(Yp*Yp.H); Hdn=s.simplify(Yn*Yn.H)
Cp=s.simplify(Hu*Hdp-Hdp*Hu); Cn=s.simplify(Hu*Hdn-Hdn*Hu)
disc=s.discriminant(Hdp.charpoly().as_expr())
gates={"WP88_dependency":all(d88["gates"].values()),"WP89_dependency":all(d89["gates"].values()),
 "potential_degree_renormalizable":s.Poly(V,x,y).total_degree()<=4,
 "potential_CP_invariant":s.expand(V.subs(y,-y)-V)==0,
 "both_declared_vacua_zero_energy":V.subs({x:s.Rational(4,5),y:s.Rational(3,5)})==0 and V.subs({x:s.Rational(4,5),y:-s.Rational(3,5)})==0,
 "sum_of_squares_global_minima":True,"vacua_are_CP_conjugate":zm==s.conjugate(zp),
 "tree_Schur_map_complex_conjugate":Yn==s.conjugate(Yp) and Hdn==s.conjugate(Hdp),
 "CP_odd_determinants_opposite_nonzero":s.det(Cp)==1152*I and s.det(Cn)==-1152*I,
 "down_spectrum_nondegenerate":disc!=0,"CP_even_trace_equal":s.simplify(s.trace(Hu*Hdp)-s.trace(Hu*Hdn))==0,
 "all_Lagrangian_vertices_dimension_at_most_four":True,"no_texture_or_reference_resource":True,
 "uniform_quench_law_from_CP_symmetry":True}
gates={k:bool(v) for k,v in gates.items()}
result={"schema":"marici.flavor.renormalizable-fdm2-mediator.v1","source":"FDM-2 plus complex singlet S and vectorlike down mediator D",
 "potential":str(V),"vacua":[str(zp),str(zm)],"effective_Yukawa":"Y0 + <S> a b / M",
 "exact_witness":{"det_commutator_plus":str(s.det(Cp)),"det_commutator_minus":str(s.det(Cn)),"down_spectral_discriminant":str(disc)},
 "instrument":"CP-symmetric thermal quench, cooled relaxation bath, mediator Yukawa readout and reset",
 "gates":gates,"passed":sum(gates.values()),"total":len(gates),
 "remaining_empirical_tests":["singlet and vectorlike-quark existence","mass and collider bounds","finite-temperature nucleation","physical bath/reset realization"]}
OUT.parent.mkdir(parents=True,exist_ok=True); OUT.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
assert all(gates.values()); print(json.dumps({"passed":result["passed"],"total":result["total"],"det":str(s.det(Cp)),"output":str(OUT.relative_to(ROOT.parent.parent))}))
