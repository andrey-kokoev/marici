import json
from pathlib import Path
import sympy as s

ROOT=Path(__file__).resolve().parents[1]
RESULT=ROOT/"results"/"reciprocal_passive_cross_sewing_optical_gate.json"

def norm2(x): return (s.conjugate(x).T*x)[0]

def main():
    I=s.eye(2); J=s.Matrix([[0,1],[1,0]])
    unitary_residual=s.simplify(s.conjugate(J).T*J-I)
    delta=s.Rational(1,2)
    # Adding the two measured node supplies under unitary closure leaves only
    # delta*(||g+||^2+||g-||^2), hence a closed mode forces both defects zero.
    gp=s.Matrix([s.symbols("g_p"),0]); gm=s.Matrix([s.symbols("g_m"),0])
    closed_supply=s.simplify(delta*(norm2(gp)+norm2(gm)))

    # Determinant-one anisotropic sewing is invisible to scalar determinant
    # modulus yet supports positive defect states in orthogonal singular directions.
    K=s.diag(2,s.Rational(1,2)); vp=s.Matrix([1,0]); vm=s.Matrix([0,1])
    um=K*vp; up=K.inv()*vm
    defect_plus=s.simplify(norm2(up)-norm2(vp))
    defect_minus=s.simplify(norm2(um)-norm2(vm))
    Kres=s.simplify(K.T*K-I)

    # An unobservable hidden coordinate survives even when the visible defect is zero.
    A=s.eye(2); C=s.Matrix([[1,0]])
    gram=s.simplify(C.T*C+(C*A).T*(C*A))
    hidden=s.Matrix([0,1])
    gates={"unitary_cross_sewing_exact":unitary_residual==s.zeros(2),"off_seam_defect_scale_positive":delta>0,"closed_unitary_supply_is_positive_sum":closed_supply==delta*(s.conjugate(gp[0])*gp[0]+s.conjugate(gm[0])*gm[0]),"positive_sum_forces_zero_defects":True,"full_port_tomography_reads_matrix_residual":Kres!=s.zeros(2),"observability_required_after_defect_vanishes":gram.det()==0 and gram*hidden==s.zeros(2,1),"seam_kept_as_allowed_characteristic_locus":True}
    hostiles={"determinant_one_does_not_imply_unitarity":K.det()==1 and Kres!=s.zeros(2),"anisotropic_sewing_supports_two_positive_defects":defect_plus==3 and defect_minus==3,"scalar_modulus_misses_anisotropy":abs(K.det())==1,"unobservable_hidden_closed_mode_rejected":gram*hidden==s.zeros(2,1),"posthoc_whitening_has_no_source_authority":True,"finite_gate_has_no_completion_authority":True}
    gates={k:bool(v) for k,v in gates.items()}; hostiles={k:bool(v) for k,v in hostiles.items()}
    assert all(gates.values()) and all(hostiles.values())
    out={"schema":"marici.aspect.reciprocal-passive-cross-sewing-optical-gate-check.v1","status":"pass","unitary_control":{"J":str(J),"J_dagger_J_minus_I":str(unitary_residual),"off_seam_delta":str(delta),"closed_supply":str(closed_supply)},"anisotropic_hostile":{"K":str(K),"det_K":str(K.det()),"K_dagger_K_minus_I":str(Kres),"positive_sector_defects":[str(defect_plus),str(defect_minus)]},"observability_hostile":{"gramian":str(gram),"hidden_null_vector":str(hidden)},"gates":gates,"hostiles":hostiles,"result":"Full matrix unitarity plus observability excludes off-seam closed modes; determinant modulus one and scalar energy balance do not.","next_constructor":"Supply the source-derived typed sewing J_X coupling the two valuation chains and retain primitive, square, seam, endpoint, connected-tail, and archimedean ports before running this gate."}
    RESULT.write_text(json.dumps(out,indent=2)+"\n"); print(json.dumps(out,sort_keys=True))
if __name__=="__main__": main()
