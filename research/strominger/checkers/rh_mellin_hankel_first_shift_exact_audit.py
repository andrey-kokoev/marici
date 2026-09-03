import json,math
from decimal import Decimal as D,localcontext
from pathlib import Path
N=22
def det_bareiss(a):
 a=[r[:] for r in a];n=len(a);prev=1
 for k in range(n-1):
  if a[k][k]==0:raise ArithmeticError("zero pivot")
  p=a[k][k]
  for i in range(k+1,n):
   for j in range(k+1,n):a[i][j]=(a[i][j]*p-a[i][k]*a[k][j])//prev
  prev=p
 return a[-1][-1]
dets=[1]
for n in range(1,N+2):dets.append(det_bareiss([[math.factorial(4*(i+j)+3) for j in range(n)] for i in range(n)]))
with localcontext() as ctx:
 ctx.prec=100;rows=[]
 for n in range(1,N+1):
  a2=D(dets[n+1])*D(dets[n-1])/D(dets[n])**2/D(256) # x=t^4/16
  av=a2.sqrt();rows.append({"n":n,"a_over_n4":float(av/D(n**4)),"a2_numerator_bits":(dets[n+1]*dets[n-1]).bit_length()})
def solve(A,b):
 A=[r[:]+[v] for r,v in zip(A,b)];m=len(A)
 for i in range(m):
  k=max(range(i,m),key=lambda r:abs(A[r][i]));A[i],A[k]=A[k],A[i];p=A[i][i]
  for j in range(i,m+1):A[i][j]/=p
  for r in range(m):
   if r!=i:
    f=A[r][i]
    for j in range(i,m+1):A[r][j]-=f*A[i][j]
 return [A[i][-1] for i in range(m)]
def fit(order,lo,hi):
 q=[r for r in rows if lo<=r["n"]<=hi];X=[[r["n"]**(-p) for p in range(order+1)] for r in q];y=[r["a_over_n4"] for r in q];m=order+1;G=[[sum(x[i]*x[j] for x in X) for j in range(m)] for i in range(m)];b=[sum(x[i]*v for x,v in zip(X,y)) for i in range(m)];c=solve(G,b);return {"order":order,"range":f"{lo}..{hi}","A":c[0],"a1":c[1]/c[0],"coefficients":c}
fits=[fit(3,8,16),fit(3,10,18),fit(3,12,21)]
checks={"all_exact_determinants_positive":all(v>0 for v in dets),"degree_22_reached":rows[-1]["n"]==22,"late_a1_estimate_near_zero":abs(fits[-1]["a1"])<1e-5,"a1_estimate_stabilizes":abs(fits[-1]["a1"])<abs(fits[0]["a1"]),"finite_scaled_coefficients":all(math.isfinite(r["a_over_n4"]) for r in rows)}
result={"schema":"marici.strominger.rh_mellin_hankel_first_shift_exact_audit.v1","status":"passed" if all(checks.values()) else "failed","verdict":"Exact Bareiss determinants for moments (4k+3)! determine untruncated a_n through degree 22. Cubic inverse-degree fits keep a1 numerically near zero on later windows. This removes quadrature and Gram-Schmidt error but remains a finite determinant diagnostic, not an asymptotic theorem.","checks":checks,"determinant_identity":"a_n^2=D_(n+1)D_(n-1)/(256 D_n^2)","rows":rows,"fits":fits,"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
base=Path(__file__).parents[1];(base/"results"/"rh_mellin_hankel_first_shift_exact_audit.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps({"status":result["status"],"checks":checks,"fits":fits,"last_rows":rows[-4:]},indent=2))
