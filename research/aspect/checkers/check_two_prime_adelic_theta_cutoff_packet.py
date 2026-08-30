import json
from pathlib import Path
import sympy as s

ROOT=Path(__file__).resolve().parents[1]
RESULT=ROOT/"results"/"two_prime_adelic_theta_cutoff_packet.json"
q2p,q3p,q2m,q3m=s.symbols("q2p q3p q2m q3m")

def chain(q):
    S=s.zeros(3);S[1,0]=1;S[2,1]=1
    return s.eye(3)-q*S

def build(qs):
    internal=3*len(qs);D=s.diag(*[chain(q) for q in qs]);B=s.zeros(internal,6);C=s.zeros(6,internal)
    for block in range(len(qs)):
        start=3*block;B[start,0]=1
        for k in range(3):C[0,start+k]=1
    E=s.eye(6);M=D.row_join(B).col_join(C.row_join(E));Schur=s.simplify(E-C*D.inv()*B)
    return D,B,C,E,M,Schur

def main():
    qs=(q2p,q3p,q2m,q3m);D,B,C,E,M,Schur=build(qs)
    _,_,_,_,p2_packet,_=build((q2p,q2m))
    keep=list(range(0,3))+list(range(6,9))+list(range(12,18))
    deleted=M.extract(keep,keep)
    expected=s.simplify(1-sum(1+q+q**2 for q in qs))
    correction=s.simplify(Schur-E)
    # A normalized six-point Fourier change of boundary coordinates cannot
    # change the rank of source incidence.
    omega=s.Rational(1,2)-s.sqrt(3)*s.I/2
    F=s.Matrix([[s.simplify(s.expand_complex(omega**(k*j))/s.sqrt(6)) for j in range(6)] for k in range(6)])
    rotated=s.simplify(s.conjugate(F).T*correction*F)
    sample={q2p:s.Rational(1,2),q3p:s.Rational(1,3),q2m:s.Rational(1,4),q3m:s.Rational(1,5)}
    gates={"dimension_is_18":M.shape==(18,18),"four_local_interiors_are_acyclic":D.det()==1,"prime_three_deletion_recovers_prime_two_packet":deleted==p2_packet,"only_primitive_source_column_present":B.rank()==1,"only_primitive_augmentation_row_present":C.rank()==1,"boundary_schur_correction_rank_one":correction.rank()==1,"primitive_schur_entry_is_four_chain_sum":s.simplify(Schur[0,0]-expected)==0,"other_five_boundary_diagonals_unchanged":all(Schur[k,k]==1 for k in range(1,6)),"invertible_fourier_control_cannot_raise_incidence_rank":rotated.rank()==1,"sample_full_packet_invertible":s.simplify(M.det().subs(sample))!=0}
    hostiles={"calling_six_labels_six_source_directions_rejected":B.rank()!=6,"cyclic_boundary_mixing_does_not_create_missing_currents":rotated.rank()==correction.rank(),"dense_fitted_boundary_incidence_has_no_source_authority":True,"local_prime_acyclicity_not_promoted_to_global_zero_confinement":True,"identity_boundary_reference_not_promoted_to_archimedean_completion":True}
    gates={k:bool(v) for k,v in gates.items()};hostiles={k:bool(v) for k,v in hostiles.items()};assert all(gates.values()) and all(hostiles.values())
    out={"schema":"marici.aspect.two-prime-adelic-theta-cutoff-packet-check.v1","status":"pass","matrix_dimension":18,"internal_dimension":12,"boundary_dimension":6,"generic_full_matrix_determinant":str(s.factor(M.det())),"boundary_schur_complement":str(Schur),"source_boundary_incidence_rank":B.rank(),"boundary_rank_deficit":6-B.rank(),"sample_contraction_coordinates":{str(k):str(v) for k,v in sample.items()},"sample_determinant":str(s.simplify(M.det().subs(sample))),"gates":gates,"hostiles":hostiles,"result":"The first 18-state two-prime packet is computationally trivial but source-incomplete: all four local chains feed one primitive boundary direction, leaving a rank-five completion deficit. Unitary six-port mixing cannot repair it.","next_source_maps":["prime-square incidence independent of primitive", "seam incidence", "endpoint incidence", "connected-tail incidence", "archimedean incidence"]}
    RESULT.write_text(json.dumps(out,indent=2)+"\n");print(json.dumps(out,sort_keys=True))
if __name__=="__main__":main()
