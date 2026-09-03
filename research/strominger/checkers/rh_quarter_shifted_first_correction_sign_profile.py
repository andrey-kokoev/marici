import json,math
from fractions import Fraction as F
from functools import lru_cache,reduce
from pathlib import Path
ss=(F(1),F(5,4),F(3,2),F(7,4))
def q(a,i):return reduce(lambda z,s:z*(s+a+i),ss,F(1))
@lru_cache(None)
def R(n,a):
 if n<=1:return F(1)
 return (q(a,n-1)*R(n-1,a)*R(n-1,a+2)-q(a,0)*R(n-1,a+1)**2)/R(n-2,a+2)
def solve(A,b):
 A=[r[:]+[v] for r,v in zip(A,b)];m=len(A)
 for i in range(m):
  p=max(range(i,m),key=lambda k:abs(A[k][i]));A[i],A[p]=A[p],A[i];z=A[i][i]
  for j in range(i,m+1):A[i][j]/=z
  for k in range(m):
   if k!=i:
    z=A[k][i]
    for j in range(i,m+1):A[k][j]-=z*A[i][j]
 return [A[i][-1] for i in range(m)]
def fit(a,lo):
 data=[]
 for n in range(lo,49):
  theta=q(a,0)*R(n-1,a+1)**2/(q(a,n-1)*R(n-1,a)*R(n-1,a+2));data.append((n,float(n*n*theta)))
 X=[[1,1/n,1/n**2,1/n**3] for n,y in data];Y=[y for n,y in data];G=[[sum(x[i]*x[j] for x in X) for j in range(4)] for i in range(4)];b=[sum(x[i]*y for x,y in zip(X,Y)) for i in range(4)];c=solve(G,b);return {"lo":lo,"hi":48,"limit":c[0],"first_correction":c[1],"second_correction":c[2],"third_correction":c[3]}
profiles=[]
for a in range(13):
 fits=[fit(a,lo) for lo in (10,18,26,34)];profiles.append({"shift":a,"fits":fits,"first_correction_signs":[1 if x["first_correction"]>0 else -1 for x in fits]})
checks={"all_fits_finite":all(math.isfinite(v) for p in profiles for f in p["fits"] for v in f.values()),"positive_first_correction_at_shifts_zero_one":all(all(s==1 for s in profiles[a]["first_correction_signs"]) for a in (0,1)),"negative_first_correction_at_shifts_two_through_six":all(all(s==-1 for s in profiles[a]["first_correction_signs"]) for a in range(2,len(profiles))),"signs_stable_across_nested_windows":all(len(set(p["first_correction_signs"]))==1 for p in profiles),"limits_positive_and_shift_dependent":all(p["fits"][-1]["limit"]>0 for p in profiles) and len({round(p["fits"][-1]["limit"],8) for p in profiles})==len(profiles)}
result={"schema":"marici.strominger.rh_quarter_shifted_first_correction_sign_profile.v1","status":"passed" if all(checks.values()) else "failed","verdict":"Nested cubic-correction fits test whether the first inverse-degree coefficient changes sign between shifts one and two, explaining the observed convergence-direction split. This is finite recognition, not an asymptotic theorem.","profiles":profiles,"checks":checks,"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
base=Path(__file__).parents[1];(base/"results"/"rh_quarter_shifted_first_correction_sign_profile.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps(result,indent=2))
