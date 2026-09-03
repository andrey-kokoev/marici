import json
from fractions import Fraction as F
from functools import lru_cache,reduce
from pathlib import Path
ss=(F(1),F(5,4),F(3,2),F(7,4))
def q(a,i):return reduce(lambda z,s:z*(s+a+i),ss,F(1))
@lru_cache(None)
def D(n,a):
 if n<=1:return F(1)
 return (q(a,n-1)*D(n-1,a)*D(n-1,a+2)-q(a,0)*D(n-1,a+1)**2)/D(n-2,a+2)
def moment(k,a):
 n=k+2;return q(a,0)*D(n-1,a+1)**2/(q(a,n-1)*D(n-1,a)*D(n-1,a+2))
def add(p,q,c=F(1)):
 r=p+[F(0)]*(max(0,len(q)-len(p)))
 for i,x in enumerate(q):r[i]+=c*x
 while len(r)>1 and r[-1]==0:r.pop()
 return r
def inner(p,qv,m):return sum(x*y*m[i+j] for i,x in enumerate(p) for j,y in enumerate(qv))
def xp(p):return [F(0)]+p
records=[];all_alpha=[];all_beta=[];all_residual=[];all_orth=[]
for a in range(5):
 m=[moment(k,a) for k in range(12)];polys=[];norms=[]
 for n in range(6):
  p=[F(0)]*n+[F(1)]
  for j,P in enumerate(polys):p=add(p,P,-inner(p,P,m)/norms[j])
  polys.append(p);norms.append(inner(p,p,m))
 for n in range(5):
  alpha=inner(xp(polys[n]),polys[n],m)/norms[n];beta=None if n==0 else norms[n]/norms[n-1];res=add(add(xp(polys[n]),polys[n+1],F(-1)),polys[n],-alpha)
  if n:res=add(res,polys[n-1],-beta)
  records.append({"shift":a,"order":n,"alpha":float(alpha),"beta":None if beta is None else float(beta),"recurrence_exact":all(x==0 for x in res),"norm_positive":norms[n]>0});all_alpha.append(alpha);all_residual.append(all(x==0 for x in res))
  if beta is not None:all_beta.append(beta)
 for i in range(6):
  for j in range(i):all_orth.append(inner(polys[i],polys[j],m)==0)
checks={"all_gram_norms_positive":all(r["norm_positive"] for r in records),"all_jacobi_alphas_between_zero_one":all(0<x<1 for x in all_alpha),"all_jacobi_betas_positive":all(x>0 for x in all_beta),"all_three_term_recurrences_exact":all(all_residual),"all_orthogonality_relations_exact":all(all_orth),"tested_five_shifts_five_orders":len(records)==25}
result={"schema":"marici.strominger.rh_quarter_cross_ratio_stieltjes_j_fraction.v1","status":"passed" if all(checks.values()) else "failed","verdict":"Exact Gram-Schmidt constructs finite Jacobi recurrences from quarter cross-ratio moments. Positive norms and beta coefficients, alpha in (0,1), exact orthogonality, and exact three-term recurrence support a finite [0,1]-moment model but do not prove an infinite representing measure.","records":records,"checks":checks,"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
base=Path(__file__).parents[1];(base/"results"/"rh_quarter_cross_ratio_stieltjes_j_fraction.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps(result,indent=2))
