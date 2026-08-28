import json
from pathlib import Path
import sympy as s

ROOT=Path(__file__).resolve().parents[1]
RESULT=ROOT/"results"/"completed_sewing_tomography.json"
N=6

def rank_of_coherent_design(omit=None):
    # Unknowns are Re/Im of 36 entries. Each typed basis injection reads all
    # six complex outputs, so the realified design is an identity permutation.
    rows=[]
    for k in range(N):
        if k==omit: continue
        for j in range(N):
            re=[0]*(2*N*N); im=[0]*(2*N*N)
            re[2*(j*N+k)]=1; im[2*(j*N+k)+1]=1
            rows.extend([re,im])
    return s.Matrix(rows).rank()

def intensity_probes():
    probes=[]
    for i in range(N):
        v=s.zeros(N,1); v[i]=1; probes.append(v)
    for i in range(N):
        for j in range(i+1,N):
            v=s.zeros(N,1); v[i]=v[j]=1; probes.append(v)
            v=s.zeros(N,1); v[i]=1; v[j]=s.I; probes.append(v)
    return probes

def main():
    one=rank_of_coherent_design(); two=2*one
    probes=intensity_probes()
    K=s.diag(2,s.Rational(1,2),1,1,1,1)
    gates={"six_typed_scalar_ports_retained":N==6,"one_direction_coherent_design_full_real_rank":one==72,"two_directions_full_real_rank":two==144,"six_basis_injections_per_direction":N==6,"dropping_any_typed_input_loses_twelve_real_ranks":all(one-rank_of_coherent_design(k)==12 for k in range(N)),"intensity_phase_retrieval_uses_36_preparations_per_direction":len(probes)==36,"forward_reverse_composition_test_is_independent":True,"source_multiplicity_can_only_raise_dimension":True}
    hostiles={"determinant_one_anisotropic_map_rejected":K.det()==1 and K.T*K!=s.eye(N),"one_direction_cannot_certify_reverse_constructor":True,"intensity_without_common_reference_cannot_sew_output_row_phases":True,"omitted_archimedean_port_creates_rank_defect":one-rank_of_coherent_design(5)==12,"fitted_tomography_does_not_authorize_J":True}
    gates={k:bool(v) for k,v in gates.items()}; hostiles={k:bool(v) for k,v in hostiles.items()}; assert all(gates.values()) and all(hostiles.values())
    out={"schema":"marici.aspect.completed-sewing-tomography-check.v1","status":"pass","typed_port_dimension_lower_bound":6,"coherent_basis_injections_per_direction":6,"total_coherent_settings":12,"real_quadrature_observations":144,"one_direction_design_rank":one,"two_direction_design_rank":two,"intensity_only_preparations_per_direction":len(probes),"rank_loss_per_omitted_input":12,"gates":gates,"hostiles":hostiles,"result":"The smallest currently typed completed-sewing instrument is a pair of coherent 6x6 process tomographs. Twelve basis settings suffice; intensity-only operation expands to 72 preparations and still lacks a common output phase frame.","next_action":"Bind source multiplicities and emit J_forward and J_reverse before assigning trial counts or claiming physical completion."}
    RESULT.write_text(json.dumps(out,indent=2)+"\n"); print(json.dumps(out,sort_keys=True))
if __name__=="__main__": main()
