import json,math
from decimal import Decimal as D,localcontext
from pathlib import Path
def det(a):
 a=[r[:] for r in a];p=1;n=len(a)
 for k in range(n-1):
  q=a[k][k]
  for i in range(k+1,n):
   for j in range(k+1,n):a[i][j]=(a[i][j]*q-a[i][k]*a[k][j])//p
  p=q
 return a[-1][-1]
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
def estimate(alpha,N=18):
 q=int(4*alpha+3);ds=[1]+[det([[math.factorial(4*(i+j)+q) for j in range(n)] for i in range(n)]) for n in range(1,N+2)];ys=[]
 with localcontext() as c:
  c.prec=80
  for n in range(8,N+1):ys.append((n,float((D(ds[n+1])*D(ds[n-1])/D(ds[n])**2/D(256)).sqrt()/D(n**4))))
 X=[[n**(-p) for p in range(4)] for n,y in ys];v=[y for n,y in ys];G=[[sum(x[i]*x[j] for x in X) for j in range(4)] for i in range(4)];b=[sum(x[i]*y for x,y in zip(X,v)) for i in range(4)];coef=solve(G,b);return {"alpha":alpha,"moment_offset":q,"A":coef[0],"a1":coef[1]/coef[0],"predicted_alpha_over_2beta":2*alpha,"residual":coef[1]/coef[0]-2*alpha}
rows=[estimate(a) for a in (0,.25,.5,1.)]
checks={"alpha_zero_shift_near_zero":abs(rows[0]["a1"])<1e-4,"family_matches_alpha_over_2beta":max(abs(r["residual"]) for r in rows)<2e-3,"nonzero_alpha_controls_are_nonzero":all(r["a1"]>.1 for r in rows[1:]),"leading_A_independent_of_alpha":max(r["A"] for r in rows)-min(r["A"] for r in rows)<1e-3}
result={"schema":"marici.strominger.rh_hard_edge_first_fluctuation_family_audit.v1","status":"passed" if all(checks.values()) else "failed","verdict":"Exact determinant families for x^alpha exp(-2 x^1/4) support a1=alpha/(2 beta)=2 alpha. The source case alpha=0 therefore has no first fluctuation, while nonzero-alpha controls exhibit the predicted shift. This is a finite family diagnostic, not a universality theorem.","checks":checks,"rows":rows,"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
base=Path(__file__).parents[1];(base/"results"/"rh_hard_edge_first_fluctuation_family_audit.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps(result,indent=2))
