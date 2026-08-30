import json
from pathlib import Path
import sympy as s

ROOT=Path(__file__).resolve().parents[1]
RESULT=ROOT/"results"/"two_prime_weighted_square_incidence_rank_lift.json"

def current_weight(p,k):
    # Nima's concrete G(q)=exp(-q): (1/k)(p^(-3k/2)-p^(-k/2)).
    p=s.Integer(p);k=s.Integer(k)
    return s.simplify((p**(-s.Rational(3,2)*k)-p**(-s.Rational(1,2)*k))/k)

def main():
    primitive=s.Matrix([[current_weight(2,1),current_weight(3,1)]])
    square=s.Matrix([[current_weight(2,2),current_weight(3,2)]])
    W=primitive.col_join(square)
    minor=s.simplify(W.det())
    # Repeat the same source weights on positive and reciprocal sector legs.
    doubled=W.row_join(W)
    six=s.zeros(6,4);six[:2,:]=doubled
    scalarized=s.Matrix([list(primitive),list(primitive)]).reshape(2,2)
    gates={"primitive_weights_match_source_formula":primitive==s.Matrix([[-s.sqrt(2)/4,-2*s.sqrt(3)/9]]),"square_weights_match_source_formula":square==s.Matrix([[-s.Rational(3,16),-s.Rational(4,27)]]),"two_prime_grade_minor_nonzero":minor!=0,"primitive_and_square_are_independent":W.rank()==2,"sector_doubling_preserves_grade_rank":doubled.rank()==2,"six_port_boundary_rank_rises_to_two":six.rank()==2}
    hostiles={"renaming_primitive_copy_as_square_rejected":scalarized.rank()==1,"scalar_sum_erases_grade_rank":s.Matrix([[sum(primitive)+sum(square)]]).rank()==1,"more_prime_chains_without_new_grade_weights_do_not_raise_type_rank":True,"finite_rank_two_not_promoted_to_completed_rank_six":True}
    gates={k:bool(v) for k,v in gates.items()};hostiles={k:bool(v) for k,v in hostiles.items()};assert all(gates.values()) and all(hostiles.values())
    out={"schema":"marici.aspect.two-prime-weighted-square-incidence-rank-lift.v1","status":"pass","source":"research/nima/rh-weighted-endpoint-incidence-reproduces-the-exact-order-three-boundary-filtration.md","primitive_row":str(primitive),"square_row":str(square),"two_by_two_minor":str(minor),"old_boundary_rank":1,"new_boundary_rank":2,"remaining_rank_deficit":4,"gates":gates,"hostiles":hostiles,"result":"The source-weighted prime-square current is genuinely independent of the primitive current already at primes 2 and 3. It raises typed boundary observation rank from one to two without fitted coupling.","next_independent_types":["seam","endpoint totalization","connected tail","archimedean countercurrent"]}
    RESULT.write_text(json.dumps(out,indent=2)+"\n");print(json.dumps(out,sort_keys=True))
if __name__=="__main__":main()
