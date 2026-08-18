"""Exact three-step cyclic saturation of the complete Hom divisor family."""
from __future__ import annotations
import json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/"research/benincasa"));sys.path.insert(0,str(ROOT/"research/nima"))
from check_cyclic_hom_divisor_orbits import P,NAMES,add,mul,scale,power,normalize
from audit_gysin_hom_pole_lattice import source_factors
OUT=Path(__file__).with_name("finite-cyclic-hom-divisor-saturation.json")
ONE={(0,0):1};TWO={(0,0):2};U0=({(1,0):1},ONE);V0=({(0,1):1},ONE)

def radd(a,b):return (add(mul(a[0],b[1]),mul(b[0],a[1])),mul(a[1],b[1]))
def rneg(a):return (scale(a[0],-1),a[1])
def rsub(a,b):return radd(a,rneg(b))
def rmul(a,b):return (mul(a[0],b[0]),mul(a[1],b[1]))
def rinv(a):return (a[1],a[0])
def rdiv(a,b):return rmul(a,rinv(b))
def rpow(a,n):
 r=(ONE,ONE)
 for _ in range(n):r=rmul(r,a)
 return r
def rconst(n):return ({(0,0):n%P},ONE)
def rho(U,V):
 d=rsub(U,V)
 return rdiv(rmul(rconst(2),U),d),rdiv(rmul(rconst(2),rsub(rconst(2),V)),d)
def peval(poly,U,V):
 out=({},ONE)
 for (i,j),c in poly.items():out=radd(out,rmul(rconst(c),rmul(rpow(U,i),rpow(V,j))))
 return out
def key(poly):
 q,_=normalize(poly);return tuple((i,j,c) for (i,j),c in sorted(q.items()))
def req(a,b):return key(mul(a[0],b[1]))==key(mul(b[0],a[1]))

def main():
 factors=source_factors(P)[0]+source_factors(P)[1]
 U,V=U0,V0;steps=[];numerators={};boundaries={};orbits={name:[] for name in NAMES};classes=[];u3=v3=None
 originals={name:(poly,(poly,ONE)) for name,poly in factors}
 for step in range(4):
  rows=[]
  for name,poly in factors:
   r=peval(poly,U,V);nk=key(r[0]);dk=key(r[1]);numerators.setdefault(nk,[]).append((step,name));boundaries.setdefault(dk,[]).append((step,name))
   ci=next((i for i,q in enumerate(classes) if req(r,q)),None)
   if ci is None:ci=len(classes);classes.append(r)
   orbits[name].append({"step":step,"rational_divisor_class":ci})
   rows.append({"label":name,"numerator_terms":[list(x) for x in nk],"denominator_terms":[list(x) for x in dk]})
  steps.append({"step":step,"factors":rows})
  if step==3:u3,v3=U,V
  U,V=rho(U,V)
 closure=all(req(peval(poly,U0,V0),peval(poly,u3,v3)) for _,poly in factors)
 result={"schema":"marici.finite-cyclic-hom-divisor-saturation.v1","prime":P,"factor_count":len(factors),
  "distinct_rational_divisor_classes":len(classes),"raw_cleared_numerator_count_before_common_factor_cancellation":len(numerators),"distinct_normalization_denominator_forms":len(boundaries),"three_step_rational_closure":closure,
  "label_orbits":orbits,"interpretation":"finite labelled three-chart saturation; numerator and denominator supports retained separately"}
 OUT.write_text(json.dumps(result,indent=2)+"\n");print(json.dumps({"rational_classes":len(classes),"raw_numerators":len(numerators),"boundaries":len(boundaries),"closure":closure}))
if __name__=="__main__":main()
