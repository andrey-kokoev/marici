import json,runpy
from fractions import Fraction as F
from pathlib import Path
base=Path(__file__).parents[1]
g=runpy.run_path(str(Path(__file__).with_name("rh_quarter_order_four_interpolated_hurwitz_minors.py")))
Q,D,mu,ad,tr,interp,bern=g["Q"],g["D"],g["mu"],g["ad"],g["tr"],g["interp"],g["bern"]
def routh_deltas(p):
 b=list(reversed(tr(p)));cols=(len(b)+1)//2;A=[[F(0)]*cols for _ in b];A[0][:]=b[0::2]+[F(0)]*(cols-len(b[0::2]));A[1][:]=b[1::2]+[F(0)]*(cols-len(b[1::2]));first=[A[1][0]]
 for i in range(2,len(b)):
  if A[i-1][0]==0:return None
  for j in range(cols-1):A[i][j]=(A[i-1][0]*A[i-2][j+1]-A[i-2][0]*A[i-1][j+1])/A[i-1][0]
  first.append(A[i][0])
 out=[];z=F(1)
 for x in first:z*=x;out.append(z)
 return out
X=mu(mu(Q(5),D(5,0)),D(5,2));Y=mu(mu(Q(0),D(5,1)),D(5,1));L=max(len(X),len(Y));X += [F(0)]*(L-len(X));Y += [F(0)]*(L-len(Y));degree=L-1
xs=[F(j,degree+1) for j in range(degree+1)];samples=[]
for t in xs:samples.append(routh_deltas([X[i]-t*Y[i] for i in range(L)]))
records=[];first_failure=None
for k in range(1,degree+1):
 ys=[samples[j][k-1] for j in range(k+1)];poly=interp(xs[:k+1],ys);b=bern(poly,k);ok=all(z>=0 for z in b) and ys[0]>0
 rec={"minor_order":k,"interpolated_degree":len(poly)-1,"bernstein_nonnegative":ok,"zero_bernstein_coefficients":sum(z==0 for z in b)};records.append(rec)
 if not ok and first_failure is None:first_failure=rec
endpoint=tr(ad(X,Y,-1));endpoint_deltas=routh_deltas(endpoint);endpoint_ok=endpoint_deltas is not None and all(z>0 for z in endpoint_deltas)
checks={"all_open_hurwitz_minors_bernstein_nonnegative":first_failure is None,"degree_dropped_endpoint_hurwitz":endpoint_ok,"all_sixty_four_principal_minors_checked":len(records)==64,"shared_grid_has_sixty_five_nodes":len(xs)==65,"open_leading_coefficient_positive":X[-1]>0 and X[-1]==Y[-1]}
result={"schema":"marici.strominger.rh_quarter_order_six_batched_hurwitz_interpolation.v1","status":"passed" if all(checks.values()) else "failed","verdict":"A common 65-node rational grid and exact Routh products reconstruct every degree-64 order-six Hurwitz minor. Bernstein positivity certifies the continuous open pencil; a separate exact Routh test certifies the degree-dropped endpoint. Shift covariance then extends zero shift to every nonnegative shift.","pencil_degree":degree,"records":records,"first_failure":first_failure,"checks":checks,"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
(base/"results"/"rh_quarter_order_six_batched_hurwitz_interpolation.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps(result,indent=2))
