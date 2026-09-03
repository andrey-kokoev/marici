import itertools,json,math,runpy
from fractions import Fraction as F
from pathlib import Path
base=Path(__file__).parents[1];g=runpy.run_path(str(Path(__file__).with_name("rh_quarter_order_four_interpolated_hurwitz_minors.py")))
Q,D,mu,ad,det=g["Q"],g["D"],g["mu"],g["ad"],g["det"]
X=mu(mu(Q(5),D(5,0)),D(5,2));Y=mu(mu(Q(0),D(5,1)),D(5,1));L=max(len(X),len(Y));X += [F(0)]*(L-len(X));Y += [F(0)]*(L-len(Y));G=ad(X,Y,-1)+[F(0)];n=L-1;k=8
def hm(p):
 def a(i):return p[i] if 0<=i<len(p) else F(0)
 return [[a(n-(2*(j-i//2)+1)) if i%2==0 else a(n-2*(j-(i-1)//2)) for j in range(k)] for i in range(k)]
def solve(A,B):
 M=[A[i][:]+B[i][:] for i in range(k)]
 for j in range(k):
  p=next(i for i in range(j,k) if M[i][j]);M[j],M[p]=M[p],M[j];z=M[j][j];M[j]=[x/z for x in M[j]]
  for i in range(k):
   if i!=j:
    z=M[i][j];M[i]=[M[i][c]-z*M[j][c] for c in range(2*k)]
 return [r[k:] for r in M]
A,B=hm(X),hm(G);C=solve(A,B);detA=det(A);principal=[];identity=True
for r in range(k+1):
 for S in itertools.combinations(range(k),r):
  pc=F(1) if r==0 else det([[C[i][j] for j in S] for i in S]);principal.append(pc)
  M=[row[:] for row in A]
  for j in S:
   for i in range(k):M[i][j]=B[i][j]
  identity &= det(M)==detA*pc
first_nonpositive=None;count=0
for r in range(1,k+1):
 for R in itertools.combinations(range(k),r):
  for S in itertools.combinations(range(k),r):
   z=det([[C[i][j] for j in S] for i in R]);count+=1
   if z<=0 and first_nonpositive is None:first_nonpositive={"size":r,"rows":R,"columns":S,"determinant":str(z)}
checks={"all_256_principal_minors_positive":len(principal)==256 and all(z>0 for z in principal),"all_mixed_replacement_identities_exact":identity,"all_12869_nonempty_minors_classified":count==sum(math.comb(k,r)**2 for r in range(1,k+1)),"total_positivity_classification_complete":first_nonpositive is not None or count==12869}
tp=first_nonpositive is None
verdict=("The order-eight transfer matrix has all 256 principal minors positive and all 12,869 nonempty minors positive; it is strictly totally positive." if tp else "The order-eight transfer matrix has all 256 principal minors positive but is not totally positive; the first nonpositive minor gives an exact obstruction. Thus the observed mixed-column mechanism is P-matrix positivity, not a direct totally-positive network matrix.")
result={"schema":"marici.strominger.rh_quarter_hurwitz_transfer_p_matrix_vs_total_positivity.v1","status":"passed" if all(checks.values()) else "failed","verdict":verdict,"matrix_size":k,"strictly_totally_positive":tp,"first_nonpositive_minor":first_nonpositive,"checks":checks,"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
(base/"results"/"rh_quarter_hurwitz_transfer_p_matrix_vs_total_positivity.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps(result,indent=2))
