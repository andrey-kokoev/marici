from __future__ import annotations
import itertools,json
from pathlib import Path
import sympy as sp
import check_six_point_nmhv_ordering_relations as rel
import check_six_point_chy_yang_mills_pfaffian as ym

ROOT=Path(__file__).resolve().parents[3];RESULT=ROOT/"research/nima/results/six-point-chy-all-ddm-gluon-components.json"

def pt_matrix(order,Z,I):
 out=I
 for r in range(6):out=out*(Z[order[r]]-Z[order[(r+1)%6]]).inv()
 return out

def kernel(negative,I,Z,inv,detprime):
 h={i:(-1 if i in negative else 1) for i in rel.LABELS};ek,ee=ym.dots(h);M={}
 for i in rel.LABELS:
  for j in rel.LABELS:
   if i!=j:
    M[i-1,j-1]=sp.Rational(1,2)*rel.sij(i,j)*inv(i,j)
    M[i+5,j+5]=ee[i,j]*inv(i,j);M[i+5,j-1]=ek[i,j]*inv(i,j);M[j-1,i+5]=-M[i+5,j-1]
  M[i-1,i-1]=sp.zeros(6);M[i+5,i+5]=sp.zeros(6)
  M[i+5,i-1]=-sum((ek[i,j]*inv(i,j) for j in rel.LABELS if j!=i),sp.zeros(6));M[i-1,i+5]=-M[i+5,i-1]
 M={key:2*value for key,value in M.items()};indices=[i for i in range(12) if i not in (0,1)]
 return (-1)**3*ym.pfaffian(M,indices,I,{})*detprime.inv()
def main():
 I,Z,inv,base_pt,detprime=ym.setup();orders=[(1,)+p+(6,) for p in itertools.permutations((2,3,4,5))];pts={o:pt_matrix(o,Z,I) for o in orders};rows=[];old=rel.TARGET
 try:
  for negative in itertools.combinations(range(1,7),3):
   rel.TARGET=negative;K=kernel(negative,I,Z,inv,detprime)
   residuals=[]
   for order in orders:residuals.append(sp.cancel(sp.trace(pts[order]*K)-rel.amplitude(order)))
   rows.append({"negative_helicity_legs":list(negative),"all_24_ddm_orderings_match":all(x==0 for x in residuals),"nonzero_residual_count":sum(x!=0 for x in residuals)})
 finally:rel.TARGET=old
 checks={"all_480_worldsheet_twistor_pairs_match":all(r["all_24_ddm_orderings_match"] for r in rows),"exactly_20_components":len(rows)==20,"exactly_24_ddm_orderings":len(orders)==24}
 out={"schema":"marici.nima.six_point_chy_all_ddm_gluon_components.result.v1","status":"passed" if all(checks.values()) else "failed","checks":checks,"components":rows,"claim_boundary":"Exact CHY reduced-Pfaffian residues match all 24 DDM-ordered momentum-twistor partial amplitudes for all 20 pure-gluon six-point NMHV helicity assignments at one rational fixture. This still precedes the explicit nonabelian color contraction."}
 RESULT.parent.mkdir(parents=True,exist_ok=True);RESULT.write_text(json.dumps(out,indent=2)+"\n",encoding="utf-8")
 if out["status"]!="passed":raise SystemExit(1)
if __name__=="__main__":main()
