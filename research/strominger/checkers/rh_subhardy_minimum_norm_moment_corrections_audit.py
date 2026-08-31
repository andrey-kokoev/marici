import json
from decimal import Decimal as D, getcontext
from pathlib import Path
getcontext().prec=90
A=D(1); B=D(1)/D(4)

def weight(n):
 x=D(n).ln(); return D(n).sqrt()*(A*(x**B)).exp()
def solve(M,b):
 n=len(b); a=[M[i][:]+[b[i]] for i in range(n)]
 for c in range(n):
  p=max(range(c,n),key=lambda i:abs(a[i][c])); a[c],a[p]=a[p],a[c]
  q=a[c][c]
  if q==0: raise ArithmeticError("singular Gram matrix")
  a[c]=[z/q for z in a[c]]
  for i in range(n):
   if i!=c:
    q=a[i][c]; a[i]=[x-q*y for x,y in zip(a[i],a[c])]
 return [a[i][-1] for i in range(n)]
def trial(K,N):
 logs=[D(n).ln() for n in range(3,N+1)]; invw=[D(1)/weight(n) for n in range(3,N+1)]
 G=[[sum((x**(j+k))*q*q for x,q in zip(logs,invw)) for k in range(K+1)] for j in range(K+1)]
 b=[-(D(2).ln()**j) for j in range(K+1)]
 lam=solve(G,b); correction=sum(b[i]*lam[i] for i in range(K+1)); norm2=weight(2)**2+correction
 residual=max(abs(sum(G[j][k]*lam[k] for k in range(K+1))-b[j]) for j in range(K+1))
 return norm2.sqrt(),residual
cutoffs=(200,1000,5000); orders=range(0,7)
data=[]
for K in orders:
 row=[]
 for N in cutoffs:
  norm,res=trial(K,N); row.append({"N":N,"norm":str(norm),"residual":str(res)})
 data.append({"K":K,"cutoffs":row})
last=[D(row["cutoffs"][-1]["norm"]) for row in data]
checks={
 "all_gram_solves_have_small_residual":all(D(x["residual"])<D("1e-60") for row in data for x in row["cutoffs"]),
 "minimum_norm_decreases_with_cutoff_at_each_order":all(all(D(r[i+1]["norm"])<=D(r[i]["norm"]) for i in range(len(r)-1)) for r in [row["cutoffs"] for row in data]),
 "required_norm_increases_with_cancelled_order_at_largest_cutoff":all(last[i+1]>=last[i] for i in range(len(last)-1)),
 "tested_norms_are_finite":all(x.is_finite() for x in last),
}
result={"schema":"marici.strominger.rh_subhardy_minimum_norm_moment_corrections_audit.v1","status":"passed" if all(checks.values()) else "failed","parameters":{"a":"1","beta":"1/4","anchor_label":2,"anchor_coefficient":"1"},"verdict":"High-precision finite Gram solves construct the minimum weighted-norm packet with c_2=1 and moments 0 through K cancelled. Cutoff monotonicity and solve residuals are checked. Growth or stabilization across K is numerical evidence only; a bounded weak-limit witness requires a uniform-in-K bound and cannot be inferred from this finite grid.","checks":checks,"largest_cutoff_norms_by_order":[str(x) for x in last],"trials":data,"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
out=Path(__file__).parents[1]/"results"/"rh_subhardy_minimum_norm_moment_corrections_audit.json"; out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8"); print(json.dumps({k:v for k,v in result.items() if k!="trials"},indent=2))
