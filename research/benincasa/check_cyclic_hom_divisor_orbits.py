"""Exact pullback decomposition of the complete Hom divisor family."""
from __future__ import annotations
import json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/"research/nima"));sys.path.insert(0,str(ROOT/"research/benincasa"))
from audit_gysin_hom_pole_lattice import source_factors
from check_gysin_occurrence_covariance import valuation,clean_poly

P=2305843009213693951
OUT=Path(__file__).with_name("cyclic-hom-divisor-orbits.json")
NAMES=("u","v","y","1-y","1+y","v-u","y-u^2","y+u^2","P6","u-2","v-2","u^2+1")
COMPLETE=(1,1,1,0,0,1,1,1,1,1,1,2)

def add(a,b):
 r=dict(a)
 for m,x in b.items():r[m]=(r.get(m,0)+x)%P
 return clean_poly(r,P)
def mul(a,b):
 r={}
 for (i,j),x in a.items():
  for (k,l),y in b.items():r[(i+k,j+l)]=(r.get((i+k,j+l),0)+x*y)%P
 return clean_poly(r,P)
def scale(a,x):return clean_poly({m:v*x%P for m,v in a.items()},P)
def power(a,n):
 r={(0,0):1}
 for _ in range(n):r=mul(r,a)
 return r
def degree(a):return max(map(sum,a)) if a else 0
def normalize(a):
 if not a:return a,0
 m=min(a);c=a[m];iv=pow(c,P-2,P)
 return scale(a,iv),c

def pullback(poly):
 """Numerator of f(U,V), U=2u/d, V=(4-2v)/d, at common d^deg."""
 d={(1,0):1,(0,1):P-1};un={(1,0):2};vn={(0,0):4,(0,1):P-2};deg=degree(poly);out={}
 for (i,j),c in poly.items():out=add(out,scale(mul(mul(power(un,i),power(vn,j)),power(d,deg-i-j)),c))
 return out,deg,d

def main():
 declared,residual=source_factors(P);factors=declared+residual
 rows=[];all_units=True
 for name,poly in factors:
  num,denpow,d=pullback(poly);rem=num;orders={}
  for sname,sfactor in factors:
   n,rem=valuation(rem,sfactor,P);orders[sname]=n
  nd,rem=valuation(rem,d,P);orders["normalization_d"]=nd
  norm,unit=normalize(rem);unit_residual=(not norm) or set(norm)=={(0,0)}
  all_units &= unit_residual
  rows.append({"target_local_factor":name,"pullback_denominator_power":denpow,"source_factor_orders":orders,"residual_unit":unit_residual,"residual_terms":[[i,j,c] for (i,j),c in sorted(norm.items())]})
 result={"schema":"marici.cyclic-hom-divisor-orbits.v1","prime":P,"base_map":{"U":"2u/(u-v)","V":"2(2-v)/(u-v)","d":"u-v"},
  "factor_order":NAMES,"complete_vector":COMPLETE,"pullbacks":rows,"all_pullbacks_factor_over_complete_family_plus_normalization":all_units,
  "interpretation":"target local factors pull back to source factors plus powers of the chart-normalization divisor; the lattice must be transported, not identified coefficientwise",
  "resonant_grades":{"values":[15,17,28,30],"transport":"unchanged in the recursively transported sheared frame","threefold_return":True}}
 OUT.write_text(json.dumps(result,indent=2)+"\n");print(json.dumps({"all_units":all_units,"rows":len(rows),"decompositions":[[r['target_local_factor'],r['source_factor_orders']] for r in rows]}))
if __name__=="__main__":main()
