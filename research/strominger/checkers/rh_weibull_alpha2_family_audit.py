import json,math
from decimal import Decimal as D,localcontext
from pathlib import Path
N=20
def det(a):
 a=[r[:] for r in a];last=1;n=len(a)
 for k in range(n-1):
  q=a[k][k]
  for i in range(k+1,n):
   for j in range(k+1,n):a[i][j]=(a[i][j]*q-a[i][k]*a[k][j])//last
  last=q
 return a[-1][-1]
def solve(A,b):
 A=[r[:]+[v] for r,v in zip(A,b)];m=len(A)
 for i in range(m):
  k=max(range(i,m),key=lambda r:abs(A[r][i]));A[i],A[k]=A[k],A[i];q=A[i][i]
  for j in range(i,m+1):A[i][j]/=q
  for r in range(m):
   if r!=i:
    q=A[r][i]
    for j in range(i,m+1):A[r][j]-=q*A[i][j]
 return [A[i][-1] for i in range(m)]
def estimate(p):
 off=p-1;ds=[1]+[det([[math.factorial(p*(i+j)+off) for j in range(n)] for i in range(n)]) for n in range(1,N+2)];rows=[]
 with localcontext() as c:
  c.prec=90
  for n in range(8,N+1):
   av=(D(ds[n+1])*D(ds[n-1])/D(ds[n])**2).sqrt()/D(2**p);rows.append((n,float(av/D(n**p))))
 X=[[1,n**-2,n**-3,n**-4] for n,y in rows];v=[y for n,y in rows];G=[[sum(x[i]*x[j] for x in X) for j in range(4)] for i in range(4)];b=[sum(x[i]*y for x,y in zip(X,v)) for i in range(4)];coef=solve(G,b);a2=coef[1]/coef[0];target=-(1-1/p)/4
 return {"p":p,"beta":1/p,"A":coef[0],"alpha2":a2,"target":target,"residual":a2-target}
rows=[estimate(p) for p in (1,2,3,4)]
checks={"laguerre_alpha2_zero":abs(rows[0]["alpha2"])<1e-8,"cross_beta_formula_falsified":abs(rows[1]["residual"])>.01 and abs(rows[2]["residual"])>.01,"quarter_matches_minus_three_sixteenths":abs(rows[-1]["alpha2"]+3/16)<5e-4,"finite_outputs":all(math.isfinite(r["alpha2"]) for r in rows)}
result={"schema":"marici.strominger.rh_weibull_alpha2_family_audit.v1","status":"passed" if all(checks.values()) else "failed","verdict":"Exact determinant families falsify the guessed cross-beta law alpha2=-(1-beta)/4 at beta=1/2 and 1/3, while the quarter-Weibull fit remains within 1e-6 of -3/16. The quarter value is therefore special finite evidence, not a universal consequence.","checks":checks,"rows":rows,"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
base=Path(__file__).parents[1];(base/"results"/"rh_weibull_alpha2_family_audit.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps(result,indent=2))
