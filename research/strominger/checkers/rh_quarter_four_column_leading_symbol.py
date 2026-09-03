import json,math
from fractions import Fraction as F
from functools import reduce
from pathlib import Path
def rise(x,k):
 r=F(1)
 for j in range(k):r*=x+j
 return r
def det(a):
 a=[r[:] for r in a];n=len(a);out=F(1)
 for k in range(n):
  p=next(i for i in range(k,n) if a[i][k]);a[k],a[p]=a[p],a[k]
  if p!=k:out=-out
  z=a[k][k];out*=z
  for j in range(k,n):a[k][j]/=z
  for i in range(k+1,n):
   z=a[i][k]
   for j in range(k,n):a[i][j]-=z*a[k][j]
 return out
def S(n,t):
 ss=tuple(F(1)+F(k,4)+t for k in range(4))
 return F(1) if n==0 else det([[reduce(lambda z,s:z*rise(s+i,j),ss,F(1)) for j in range(n)] for i in range(n)])
def degree_lead(values):
 layers=[values]
 while len(layers[-1])>1 and any(layers[-1][1:]):layers.append([b-a for a,b in zip(layers[-1],layers[-1][1:])])
 # Highest nonzero constant finite-difference layer.
 d=max(i for i,v in enumerate(layers) if any(v));return d,layers[d][0]/math.factorial(d)
rows=[]
for n in range(1,9):
 upper=2*n*(n-1);vals=[S(n,F(t)) for t in range(upper+2)];d,lead=degree_lead(vals)
 rows.append({"n":n,"raw_degree_bound":upper,"actual_degree":d,"leading_coefficient":str(lead),"degree_over_n2":d/(n*n)})
checks={"all_degrees_below_raw_bound":all(r["actual_degree"]<=r["raw_degree_bound"] for r in rows),"leading_coefficients_positive":all(F(r["leading_coefficient"])>0 for r in rows),"exact_degree_three_halves_n_n_minus_one":all(r["actual_degree"]==3*r["n"]*(r["n"]-1)//2 for r in rows),"nontrivial_cancellation_occurs":any(r["actual_degree"]<r["raw_degree_bound"] for r in rows[1:]),"degree_density_not_one_quarter":abs(rows[-1]["degree_over_n2"]-.25)>1}
result={"schema":"marici.strominger.rh_quarter_four_column_leading_symbol.v1","status":"passed" if all(checks.values()) else "failed","verdict":"Exact finite differences give deg_t S_n=3n(n-1)/2 through n=8, so the fixed-n large-shift degree density tends 3/2, not 1/4. The quarter amplitude cannot come from this iterated leading-symbol limit; the large-degree and large-shift limits do not commute.","checks":checks,"rows":rows,"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
base=Path(__file__).parents[1];(base/"results"/"rh_quarter_four_column_leading_symbol.json").write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps(result,indent=2))
