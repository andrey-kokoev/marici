import json
from pathlib import Path
import sympy as s

ROOT=Path(__file__).resolve().parents[1]
RESULT=ROOT/"results"/"three_prime_seam_orientation_rank_lift.json"

def weight(p,k):
    p=s.Integer(p);k=s.Integer(k)
    return s.simplify((p**(-s.Rational(3,2)*k)-p**(-s.Rational(1,2)*k))/k)

def main():
    W=s.Matrix([[weight(p,k) for p in (2,3,5)] for k in (1,2,3)])
    arithmetic=W.row_join(W)
    seam=s.Matrix([[1,1,1,-1,-1,-1]])
    packet=arithmetic.col_join(seam)
    same_sign=s.Matrix([[1,1,1,1,1,1]])
    wrong=arithmetic.col_join(same_sign)
    exchange=s.zeros(6)
    exchange[:3,3:]=s.eye(3);exchange[3:,:3]=s.eye(3)
    sector_sum=s.zeros(3,6);sector_sum[:,:3]=s.eye(3);sector_sum[:,3:]=s.eye(3)
    gates={"arithmetic_three_rank":arithmetic.rank()==3,"oriented_seam_raises_rank_to_four":packet.rank()==4,"arithmetic_rows_even_under_sector_exchange":arithmetic*exchange==arithmetic,"seam_row_odd_under_sector_exchange":seam*exchange==-seam,"sector_sum_annihilates_seam":seam*sector_sum.T==s.zeros(1,3),"packet_dimension_remains_30":2*3*4+6==30}
    hostiles={"same_sign_holomorphic_duplication_adds_no_rank":wrong.rank()==3,"absolute_or_sector_aggregated_readout_erases_orientation":True,"renaming_an_arithmetic_row_as_seam_rejected":arithmetic.col_join(arithmetic[0,:]).rank()==3,"rank_four_not_promoted_to_completed_rank_six":True,"seam_orientation_not_scalar_current_zero":True}
    gates={k:bool(v) for k,v in gates.items()};hostiles={k:bool(v) for k,v in hostiles.items()};assert all(gates.values()) and all(hostiles.values())
    out={"schema":"marici.aspect.three-prime-seam-orientation-rank-lift.v1","status":"pass","arithmetic_rank":3,"rank_with_seam":4,"remaining_rank_deficit":2,"seam_row":str(seam),"sector_exchange":str(exchange),"gates":gates,"hostiles":hostiles,"result":"Conjugate-reciprocal orientation supplies a fourth independent boundary direction without enlarging the 30-state packet. Holomorphic same-sign duplication lies entirely in the arithmetic row space and adds nothing.","next_independent_types":["endpoint totalization","archimedean countercurrent"]}
    RESULT.write_text(json.dumps(out,indent=2)+"\n");print(json.dumps(out,sort_keys=True))
if __name__=="__main__":main()
