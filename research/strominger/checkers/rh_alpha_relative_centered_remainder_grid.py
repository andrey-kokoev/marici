import json,math
from decimal import Decimal as D,localcontext
from pathlib import Path
N=22
def det(a):
 a=[r[:] for r in a];p=1;n=len(a)
 for k in range(n-1):
  q=a[k][k]
  for i in range(k+1,n):
   for j in range(k+1,n):a[i][j]=(a[i][j]*q-a[i][k]*a[k][j])//p
  p=q
 return a[-1][-1]
def seq(alpha):
 q=int(4*alpha+3);ds=[1]+[det([[math.factorial(4*(i+j)+q) for j in range(n)] for i in range(n)]) for n in range(1,N+2)];vals={}
 with localcontext() as c:
  c.prec=100
  for n in range(1,N+1):vals[n]=(D(ds[n+1])*D(ds[n-1])/D(ds[n])**2).ln()
 return vals
zero=seq(0);rows=[]
for alpha in (.25,.5,1.):
 v=seq(alpha)
 for n in range(8,N+1):
  d2=(D((n+1)*math.log(n+1))+D((n-1)*math.log(n-1))-D(2*n*math.log(n)))
  rem=float(v[n]-zero[n]-D(4*alpha)*d2);rows.append({"alpha":alpha,"n":n,"centered_remainder":rem,"n2_remainder":n*n*rem})
late=[r for r in rows if r["n"]>=18]
checks={"all_outputs_finite":all(math.isfinite(r["n2_remainder"]) for r in rows),"late_n2_remainders_bounded":max(abs(r["n2_remainder"]) for r in late)<10,"raw_remainder_small_at_degree22":all(abs(next(r["centered_remainder"] for r in rows if r["alpha"]==a and r["n"]==22))<.01 for a in (.25,.5,1.)),"nonzero_controls_present":len({r["alpha"] for r in rows})==3}
result={"schema":"marici.strominger.rh_alpha_relative_centered_remainder_grid.v1","status":"passed" if all(checks.values()) else "failed","verdict":"Exact degree-22 determinant ratios show that after subtracting (alpha/beta) Delta^2(n log n), the relative centered remainder is compatible with O(n^-2) for three nonzero-alpha controls. This is finite boundedness evidence, not uniform remainder control.","checks":checks,"late_rows":late,"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
base=Path(__file__).parents[1];(base/"results"/"rh_alpha_relative_centered_remainder_grid.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps(result,indent=2))
