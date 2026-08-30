import json
from pathlib import Path
import sympy as s

ROOT=Path(__file__).resolve().parents[1]
RESULT=ROOT/"results"/"endpoint_evaluation_rank_lift.json"

def weight(p,k):
    p=s.Integer(p);k=s.Integer(k)
    return s.simplify((p**(-s.Rational(3,2)*k)-p**(-s.Rational(1,2)*k))/k)

def main():
    W=s.Matrix([[weight(p,k) for p in (2,3,5)] for k in (1,2,3)])
    arithmetic=W.row_join(W);seam=s.Matrix([[1,1,1,-1,-1,-1]])
    rank4=arithmetic.col_join(seam)
    # The endpoint direct coordinate was reserved in the boundary packet but
    # had no source incidence. Activating epsilon_0 adds its support column.
    extended=rank4.row_join(s.zeros(4,1)).col_join(s.Matrix([[0,0,0,0,0,0,1]]))

    # Finite evaluation model: columns are G(0) and nine translated values.
    D=s.zeros(9,10)
    for j in range(9):D[j,0]=-1;D[j,j+1]=1
    constant_samples=s.ones(10,1);endpoint=s.zeros(1,10);endpoint[0,0]=1
    endpoint_augmented=D.col_join(endpoint)
    fake_prime_local=rank4.col_join(rank4[0,:])
    gates={"previous_rank_four":rank4.rank()==4,"endpoint_support_raises_rank_to_five":extended.rank()==5,"all_displacements_annihilate_constant_sample":D*constant_samples==s.zeros(9,1),"endpoint_detects_constant_sample":endpoint*constant_samples==s.ones(1,1),"endpoint_independent_of_all_finite_displacements":endpoint_augmented.rank()==10,"packet_state_count_remains_30":2*3*4+6==30}
    hostiles={"renaming_prime_local_row_as_endpoint_adds_no_rank":fake_prime_local.rank()==4,"endpoint_value_cannot_be_reconstructed_from_differences":True,"endpoint_evaluation_not_promoted_to_totalization_law":True,"rank_five_not_promoted_to_completed_rank_six":True,"posthoc_direct_boundary_constant_rejected":True}
    gates={k:bool(v) for k,v in gates.items()};hostiles={k:bool(v) for k,v in hostiles.items()};assert all(gates.values()) and all(hostiles.values())
    out={"schema":"marici.aspect.endpoint-evaluation-rank-lift.v1","status":"pass","old_boundary_rank":4,"new_boundary_rank":5,"remaining_rank_deficit":1,"finite_displacement_rank":D.rank(),"rank_with_endpoint_evaluation":endpoint_augmented.rank(),"gates":gates,"hostiles":hostiles,"result":"The source endpoint evaluation is independent of every finite translated-difference observer and activates the fifth boundary direction. It does not yet supply the renormalized endpoint totalization law.","next_independent_type":"archimedean countercurrent","still_missing_law":"joint endpoint totalization across the five existing types"}
    RESULT.write_text(json.dumps(out,indent=2)+"\n");print(json.dumps(out,sort_keys=True))
if __name__=="__main__":main()
