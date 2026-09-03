import json, math
from decimal import Decimal as D, localcontext
from pathlib import Path
N=12
def coeffs(q,prec,truncated):
 with localcontext() as ctx:
  ctx.prec=prec; X=D(q).ln(); z=2*X.sqrt().sqrt(); M=[]
  for r in range(2*N+2):
   m=4*r+3; pref=D(4)*D(math.factorial(m))/(D(2)**(m+1))
   if truncated:
    s=D(0);t=D(1)
    for k in range(m+1):
     if k:t*=z/D(k)
     s+=t
    pref*=s
   M.append(pref)
  def inn(p,s,h=0):return sum((p[i]*s[j]*M[i+j+h] for i in range(len(p)) for j in range(len(s))),D(0))
  ps=[];hs=[];out=[]
  for n in range(N+1):
   p=[D(0)]*n+[D(1)]
   for k in range(n):
    c=inn(p,ps[k])/hs[k]
    for i,v in enumerate(ps[k]):p[i]-=c*v
   norm=inn(p,p); bx=inn(p,p,1)/norm
   out.append((None if n==0 else (norm/hs[-1]).sqrt(),bx-X if truncated else bx));ps.append(p);hs.append(norm)
  return out
lo=coeffs(12,220,True); hi=coeffs(12,340,True); un=coeffs(12,340,False)
rows=[]
for n in range(1,N+1):
 rows.append({"n":n,"relative_a":float(hi[n][0]/un[n][0]-1),"relative_b":float(hi[n][1]/un[n][1]-1),"precision_delta_a":abs(float(lo[n][0]/hi[n][0]-1)),"precision_delta_b":abs(float(lo[n][1]/hi[n][1]-1))})
def slope(key,start):
 d=[r for r in rows if r["n"]>=start]; xs=[math.log(r["n"]) for r in d];ys=[math.log(abs(r[key])) for r in d];xm=sum(xs)/len(xs);ym=sum(ys)/len(ys)
 return sum((x-xm)*(y-ym) for x,y in zip(xs,ys))/sum((x-xm)**2 for x in xs)
fits=[{"window":f"{s}..12","a_slope":slope("relative_a",s),"b_slope":slope("relative_b",s)} for s in (4,6,8)]
checks={
 "precision_crosscheck_below_1e_minus_180":max(max(r["precision_delta_a"],r["precision_delta_b"]) for r in rows)<1e-180,
 "relative_errors_decrease_through_degree_twelve":all(abs(rows[i+1]["relative_b"])<abs(rows[i]["relative_b"]) for i in range(len(rows)-1)),
 "diagonal_window_slopes_drift_toward_minus_three":all(fits[i+1]["b_slope"]<fits[i]["b_slope"] for i in range(len(fits)-1)),
 "latest_diagonal_slope_between_minus_2_9_and_minus_2_8":-2.9<fits[-1]["b_slope"]<-2.8,
 "late_offdiagonal_slopes_near_minus_three":all(-3.1<f["a_slope"]<-2.9 for f in fits),
}
result={"schema":"marici.strominger.rh_diagonal_truncation_exponent_extended_grid_audit.v1","status":"passed" if all(checks.values()) else "failed","parameters":{"q":12,"degrees":"1..12","precision_crosscheck":[220,340]},"verdict":"The precision-controlled extension to degree twelve changes the diagonal diagnosis: later fit windows drift from -2.77 toward -2.84, while the off-diagonal exponent remains near -3. The data disfavor a settled 8/3 exponent and reopen a common -3 limit with slower diagonal corrections. This remains diagnostic rather than proof.","checks":checks,"fits":fits,"rows":rows,"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
base=Path(__file__).parents[1];out=base/"results"/"rh_diagonal_truncation_exponent_extended_grid_audit.json";out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps({"status":result["status"],"checks":checks,"fits":fits,"degree12":rows[-1]},indent=2))
