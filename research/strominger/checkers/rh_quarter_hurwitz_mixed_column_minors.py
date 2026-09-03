import itertools,json,math,runpy
from fractions import Fraction as F
from pathlib import Path
base=Path(__file__).parents[1];g=runpy.run_path(str(Path(__file__).with_name("rh_quarter_order_four_interpolated_hurwitz_minors.py")))
Q,D,mu,ad,det,hurwitz_minor,interp,bern=g["Q"],g["D"],g["mu"],g["ad"],g["det"],g["hurwitz_minor"],g["interp"],g["bern"]
X=mu(mu(Q(5),D(5,0)),D(5,2));Y=mu(mu(Q(0),D(5,1)),D(5,1));L=max(len(X),len(Y));X += [F(0)]*(L-len(X));Y += [F(0)]*(L-len(Y));G=ad(X,Y,-1)+[F(0)];n=L-1
def hm(p,k):
 def a(i):return p[i] if 0<=i<len(p) else F(0)
 return [[a(n-(2*(j-i//2)+1)) if i%2==0 else a(n-2*(j-(i-1)//2)) for j in range(k)] for i in range(k)]
records=[];first_nonpositive=None;identity_failure=None;count=0
for k in range(1,9):
 A,B=hm(X,k),hm(G,k);sums=[F(0)]*(k+1);local=True
 for bits in itertools.product((0,1),repeat=k):
  M=[[B[i][j] if bits[j] else A[i][j] for j in range(k)] for i in range(k)];z=det(M);count+=1;sums[sum(bits)]+=z
  if z<=0:
   local=False
   if first_nonpositive is None:first_nonpositive={"minor_order":k,"column_pattern":"".join(map(str,bits)),"determinant":str(z)}
 xs=[F(j,k) for j in range(k+1)];ys=[hurwitz_minor([X[i]-t*Y[i] for i in range(L)],k) for t in xs];b=bern(interp(xs,ys),k);identity=all(b[j]==sums[j]/F(math.comb(k,j)) for j in range(k+1))
 if not identity and identity_failure is None:identity_failure={"minor_order":k}
 records.append({"minor_order":k,"mixed_determinant_count":2**k,"all_mixed_column_determinants_positive":local,"bernstein_mixed_sum_identity_exact":identity})
checks={"all_mixed_column_determinants_strictly_positive":first_nonpositive is None,"all_bernstein_mixed_sum_identities_exact":identity_failure is None,"tested_minor_orders_one_through_eight":len(records)==8,"tested_510_mixed_determinants":count==510}
result={"schema":"marici.strominger.rh_quarter_hurwitz_mixed_column_minors.v1","status":"passed" if all(checks.values()) else "failed","verdict":"For Hurwitz minor orders one through eight, each Bernstein coefficient equals the normalized sum of endpoint mixed-column determinants, and all 510 individual determinants are strictly positive. Thus bounded Bernstein positivity is termwise and cancellation-free.","records":records,"first_nonpositive":first_nonpositive,"identity_failure":identity_failure,"checks":checks,"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
(base/"results"/"rh_quarter_hurwitz_mixed_column_minors.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps(result,indent=2))
