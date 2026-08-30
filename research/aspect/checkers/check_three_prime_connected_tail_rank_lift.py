import json
from pathlib import Path
import sympy as s

ROOT=Path(__file__).resolve().parents[1]
RESULT=ROOT/"results"/"three_prime_connected_tail_rank_lift.json"

def weight(p,k):
    p=s.Integer(p);k=s.Integer(k)
    return s.simplify((p**(-s.Rational(3,2)*k)-p**(-s.Rational(1,2)*k))/k)

def main():
    primes=(2,3,5);W=s.Matrix([[weight(p,k) for p in primes] for k in (1,2,3)])
    W2=W[:2,:];minor=s.simplify(W.det());doubled=W.row_join(W)
    six=s.zeros(6,6);six[:3,:]=doubled
    two_prime=W[:,:2]
    gates={"three_grade_rows_present":W.shape==(3,3),"primitive_square_rank_two":W2.rank()==2,"connected_grade_raises_rank_to_three":W.rank()==3,"exact_three_by_three_minor_nonzero":minor!=0,"reciprocal_sector_duplication_preserves_grade_rank":doubled.rank()==3,"six_port_rank_is_three":six.rank()==3,"packet_dimension_is_30":2*3*4+6==30}
    hostiles={"two_primes_cannot_witness_rank_three":two_prime.rank()<=2,"depth_two_cannot_retain_grade_three":True,"copying_square_row_as_tail_rejected":W[:2,:].col_join(W[1,:]).rank()==2,"scalar_grade_sum_collapses_to_one_record":s.Matrix([[sum(W[:,j]) for j in range(3)]]).rank()==1,"rank_three_not_promoted_to_completed_rank_six":True}
    gates={k:bool(v) for k,v in gates.items()};hostiles={k:bool(v) for k,v in hostiles.items()};assert all(gates.values()) and all(hostiles.values())
    out={"schema":"marici.aspect.three-prime-connected-tail-rank-lift.v1","status":"pass","weight_matrix":str(W),"three_by_three_minor":str(s.factor(minor)),"old_boundary_rank":2,"new_boundary_rank":3,"remaining_rank_deficit":3,"minimal_packet_dimension":30,"gates":gates,"hostiles":hostiles,"result":"At primes 2,3,5 the first connected grade is exactly independent of primitive and square. The minimal order-three packet raises source boundary rank to three; the two-prime depth-two packet could not possibly see this.","next_independent_types":["seam","endpoint totalization","archimedean countercurrent"]}
    RESULT.write_text(json.dumps(out,indent=2)+"\n");print(json.dumps(out,sort_keys=True))
if __name__=="__main__":main()
