import itertools,json,runpy
from fractions import Fraction as F
from pathlib import Path
base=Path(__file__).parents[1];g=runpy.run_path(str(Path(__file__).with_name("rh_quarter_hurwitz_transfer_p_matrix_vs_total_positivity.py")))
C,det,k=g["C"],g["det"],g["k"]
def dm(R,S):return F(1) if not R else det([[C[i][j] for j in S] for i in R])
def inv(A):
 n=len(A);M=[A[i][:]+[F(i==j) for j in range(n)] for i in range(n)]
 for j in range(n):
  p=next(i for i in range(j,n) if M[i][j]);M[j],M[p]=M[p],M[j];z=M[j][j];M[j]=[x/z for x in M[j]]
  for i in range(n):
   if i!=j:
    z=M[i][j];M[i]=[M[i][c]-z*M[j][c] for c in range(2*n)]
 return [r[n:] for r in M]
def sg(z):return 1 if z>0 else -1 if z<0 else 0
count=0;first_identity_failure=None;first_sign_failure=None;diag_failure=None;schur_sets=0
for r in range(k-1):
 for St in itertools.combinations(range(k),r):
  S=list(St);R=[x for x in range(k) if x not in S];pS=dm(S,S);AI=inv([[C[i][j] for j in S] for i in S]) if S else []
  def sc(i,j):
   return C[i][j] if not S else C[i][j]-sum(C[i][S[a]]*AI[a][b]*C[S[b]][j] for a in range(r) for b in range(r))
  schur_sets+=1
  for i in R:
   if sc(i,i)<=0 and diag_failure is None:diag_failure={"base":S,"index":i,"value":str(sc(i,i))}
  for i,j in itertools.combinations(R,2):
   u=sc(i,j);v=sc(j,i);ut=dm(S+[i],S+[j]);vt=dm(S+[j],S+[i]);count+=1
   if (ut!=pS*u or vt!=pS*v) and first_identity_failure is None:first_identity_failure={"base":S,"i":i,"j":j}
   if (sg(u)!=(-1)**(j-i+1) or sg(v)!=(-1)**(j-i)) and first_sign_failure is None:first_sign_failure={"base":S,"i":i,"j":j,"upper_sign":sg(u),"lower_sign":sg(v)}
checks={"all_1792_bordered_schur_identities_exact":count==1792 and first_identity_failure is None,"all_principal_schur_diagonals_positive":diag_failure is None,"all_schur_offdiagonals_follow_distance_orientation":first_sign_failure is None,"all_247_relevant_schur_complements_checked":schur_sets==247}
result={"schema":"marici.strominger.rh_quarter_terminal_bordered_schur_signs.v1","status":"passed" if all(checks.values()) else "failed","verdict":"Every principal Schur complement has positive diagonal. For i<j its upper entry has sign (-1)^(j-i+1), while the lower entry has sign (-1)^(j-i); all bordered-determinant identities are exact. Thus the bounded transfer belongs to a pivot-stable sign-skew class whose opposite off-diagonal products generate principal positivity.","schur_complement_count":schur_sets,"offdiagonal_pair_count":count,"first_identity_failure":first_identity_failure,"first_sign_failure":first_sign_failure,"diagonal_failure":diag_failure,"checks":checks,"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
(base/"results"/"rh_quarter_terminal_bordered_schur_signs.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps(result,indent=2))
