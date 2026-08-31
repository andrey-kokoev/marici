import json
from decimal import Decimal as D, getcontext
from pathlib import Path
getcontext().prec=80
MAXK=6; CUTS=(5000,20000,100000); B=D(1)/D(4)

def solve(M,b):
 n=len(b); a=[M[i][:]+[b[i]] for i in range(n)]
 for c in range(n):
  p=max(range(c,n),key=lambda i:abs(a[i][c])); a[c],a[p]=a[p],a[c]
  q=a[c][c]; a[c]=[z/q for z in a[c]]
  for i in range(n):
   if i!=c:
    q=a[i][c]; a[i]=[x-q*y for x,y in zip(a[i],a[c])]
 return [a[i][-1] for i in range(n)]
# Accumulate all scalar moments once: G_jk depends only on j+k.
sums=[D(0)]*(2*MAXK+1); snapshots={}; ci=0
for n in range(3,CUTS[-1]+1):
 x=D(n).ln(); invw2=D(1)/(D(n)*(D(2)*(x**B)).exp()); p=D(1)
 for r in range(2*MAXK+1): sums[r]+=p*invw2; p*=x
 if n==CUTS[ci]:
  snapshots[n]=sums[:]; ci+=1
  if ci==len(CUTS): break
w2sq=D(2)*(D(2)*(D(2).ln()**B)).exp(); l2=D(2).ln(); trials=[]
for K in range(3,MAXK+1):
 row=[]; b=[-(l2**j) for j in range(K+1)]
 for N in CUTS:
  s=snapshots[N]; G=[[s[j+k] for k in range(K+1)] for j in range(K+1)]; lam=solve(G,b)
  norm=(w2sq+sum(b[i]*lam[i] for i in range(K+1))).sqrt()
  res=max(abs(sum(G[j][k]*lam[k] for k in range(K+1))-b[j]) for j in range(K+1))
  row.append({"N":N,"norm":str(norm),"residual":str(res)})
 trials.append({"K":K,"cutoffs":row})
checks={
 "all_solves_have_small_residual":all(D(x["residual"])<D("1e-48") for r in trials for x in r["cutoffs"]),
 "norms_decrease_with_adaptive_cutoff":all(all(D(r["cutoffs"][i+1]["norm"])<=D(r["cutoffs"][i]["norm"]) for i in range(2)) for r in trials),
 "largest_cutoff_norms_increase_through_tested_orders":all(D(trials[i+1]["cutoffs"][-1]["norm"])>=D(trials[i]["cutoffs"][-1]["norm"]) for i in range(len(trials)-1)),
}
ratios=[]
for r in trials:
 x=r["cutoffs"]; ratios.append(str((D(x[1]["norm"])-D(x[2]["norm"]))/D(x[2]["norm"])))
result={"schema":"marici.strominger.rh_subhardy_adaptive_cutoff_gram_audit.v1","status":"passed" if all(checks.values()) else "failed","parameters":{"a":"1","beta":"1/4","cutoffs":CUTS,"orders":"3..6"},"verdict":"Adaptive high-precision Gram sums test whether fixed-cutoff growth disappears when the label cutoff reaches 100000. Monotone cutoff decrease is verified. The remaining order growth and last-step cutoff changes are numerical diagnostics only; neither boundedness nor divergence in moment order is proved.","checks":checks,"relative_norm_drop_20000_to_100000":ratios,"trials":trials,"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
out=Path(__file__).parents[1]/"results"/"rh_subhardy_adaptive_cutoff_gram_audit.json"; out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8"); print(json.dumps({k:v for k,v in result.items() if k!="trials"},indent=2)); print(json.dumps({"largest_cutoff_norms":[r["cutoffs"][-1]["norm"] for r in trials]},indent=2))
