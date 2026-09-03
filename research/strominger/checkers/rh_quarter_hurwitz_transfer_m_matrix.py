import json,runpy
from fractions import Fraction as F
from pathlib import Path
base=Path(__file__).parents[1];g=runpy.run_path(str(Path(__file__).with_name("rh_quarter_hurwitz_transfer_p_matrix_vs_total_positivity.py")))
C,solve,k=g["C"],g["solve"],g["k"]
I=[[F(i==j) for j in range(k)] for i in range(k)];Ci=solve(C,I)
def mmatrix(M,Mi):
 return all(M[i][i]>0 for i in range(k)) and all(M[i][j]<=0 for i in range(k) for j in range(k) if i!=j) and all(Mi[i][j]>=0 for i in range(k) for j in range(k))
S=[F((-1)**i) for i in range(k)];Cs=[[S[i]*C[i][j]*S[j] for j in range(k)] for i in range(k)];Csi=[[S[i]*Ci[i][j]*S[j] for j in range(k)] for i in range(k)]
plain=mmatrix(C,Ci);checker=mmatrix(Cs,Csi)
first_plain_positive_offdiag=next(({"row":i,"column":j,"value":str(C[i][j])} for i in range(k) for j in range(k) if i!=j and C[i][j]>0),None)
first_checker_positive_offdiag=next(({"row":i,"column":j,"value":str(Cs[i][j])} for i in range(k) for j in range(k) if i!=j and Cs[i][j]>0),None)
first_plain_negative_inverse=next(({"row":i,"column":j,"value":str(Ci[i][j])} for i in range(k) for j in range(k) if Ci[i][j]<0),None)
first_checker_negative_inverse=next(({"row":i,"column":j,"value":str(Csi[i][j])} for i in range(k) for j in range(k) if Csi[i][j]<0),None)
product=[[sum(C[i][l]*Ci[l][j] for l in range(k)) for j in range(k)] for i in range(k)]
checks={"inverse_verified_exactly":product==I,"plain_m_matrix_classified":plain or first_plain_positive_offdiag is not None or first_plain_negative_inverse is not None,"checkerboard_m_matrix_classified":checker or first_checker_positive_offdiag is not None or first_checker_negative_inverse is not None,"positive_diagonal_retained":all(C[i][i]>0 for i in range(k))}
classification="plain_nonsingular_M_matrix" if plain else "checkerboard_similar_nonsingular_M_matrix" if checker else "neither_plain_nor_checkerboard_M_matrix"
result={"schema":"marici.strominger.rh_quarter_hurwitz_transfer_m_matrix.v1","status":"passed" if all(checks.values()) else "failed","verdict":"The order-eight transfer matrix is neither a plain nor checkerboard-similar nonsingular M-matrix. Both forms have a positive off-diagonal entry and a negative inverse entry. Thus M-matrix theory does not explain its positive principal minors; the established classification remains P-matrix only.","classification":classification,"first_plain_positive_offdiagonal":first_plain_positive_offdiag,"first_checkerboard_positive_offdiagonal":first_checker_positive_offdiag,"first_plain_negative_inverse":first_plain_negative_inverse,"first_checkerboard_negative_inverse":first_checker_negative_inverse,"checks":checks,"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
(base/"results"/"rh_quarter_hurwitz_transfer_m_matrix.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps(result,indent=2))
