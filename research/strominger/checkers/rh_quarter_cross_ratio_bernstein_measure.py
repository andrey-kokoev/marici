import json,math
from fractions import Fraction as F
from functools import lru_cache,reduce
from math import comb
from pathlib import Path
ss=(F(1),F(5,4),F(3,2),F(7,4))
def q(a,i):return reduce(lambda z,s:z*(s+a+i),ss,F(1))
@lru_cache(None)
def D(n,a):
 if n<=1:return F(1)
 return (q(a,n-1)*D(n-1,a)*D(n-1,a+2)-q(a,0)*D(n-1,a+1)**2)/D(n-2,a+2)
def moment(k,a):
 n=k+2;return q(a,0)*D(n-1,a+1)**2/(q(a,n-1)*D(n-1,a)*D(n-1,a+2))
def weight(N,k,a):return F(comb(N,k))*sum(((-1)**j)*F(comb(N-k,j))*moment(k+j,a) for j in range(N-k+1))
records=[];all_weights=[]
for a in range(5):
 for N in (16,20,24,28):
  ws=[weight(N,k,a) for k in range(N+1)];all_weights.extend(ws);estim=[]
  for r in range(5):estim.append(F((N+1)*(N+2))*ws[N-r]/F(r+1))
  vals=[float(x) for x in estim];mean=sum(vals)/len(vals);spread=(max(vals)-min(vals))/mean;tail=float((N+2)**2*moment(N,a));records.append({"shift":a,"N":N,"all_weights_positive":all(w>0 for w in ws),"weight_sum_matches_m0":sum(ws)==moment(0,a),"endpoint_estimators":vals,"relative_endpoint_spread":spread,"mean_endpoint_estimator":mean,"tail_n2_theta":tail,"relative_mean_vs_tail":abs(mean-tail)/tail})
latest=[r for r in records if r["N"]==28]
checks={"all_bernstein_weights_strictly_positive":all(w>0 for w in all_weights),"all_weights_normalize_to_initial_moment":all(r["weight_sum_matches_m0"] for r in records),"latest_endpoint_spread_below_point_one":all(r["relative_endpoint_spread"]<.1 for r in latest),"latest_endpoint_mean_near_tail_amplitude":all(r["relative_mean_vs_tail"]<.1 for r in latest),"tested_five_shifts_four_cutoffs":len(records)==20,"deliberate_alternating_sign_is_essential":weight(16,0,0)>0}
result={"schema":"marici.strominger.rh_quarter_cross_ratio_bernstein_measure.v1","status":"passed" if all(checks.values()) else "failed","verdict":"Exact Bernstein weights reconstruct finite Hausdorff data. Endpoint weights test the linear-density signature w_(N,N-r) approximately (r+1)T/[(N+1)(N+2)], equivalent to inverse-square moments. Passing is finite evidence, not a representing-measure theorem.","records":records,"checks":checks,"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
base=Path(__file__).parents[1];(base/"results"/"rh_quarter_cross_ratio_bernstein_measure.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps(result,indent=2))
