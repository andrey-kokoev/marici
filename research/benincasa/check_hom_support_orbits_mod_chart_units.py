"""Quotient cyclic Hom marked sections by normalization chart units."""
from __future__ import annotations
import json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/"research/benincasa"));sys.path.insert(0,str(ROOT/"research/nima"))
from check_finite_cyclic_hom_divisor_saturation import P,U0,V0,rho,peval,rsub,rmul,rpow,rinv,req,rconst
from audit_gysin_hom_pole_lattice import source_factors
OUT=Path(__file__).with_name("hom-support-orbits-mod-chart-units.json")

def evpoly(q,u,v):return sum(c*pow(u,i,P)*pow(v,j,P) for (i,j),c in q.items())%P
def evrat(r,u,v):return evpoly(r[0],u,v)*pow(evpoly(r[1],u,v),P-2,P)%P
POINTS=((7,11),(13,19),(23,29),(31,43))
def sig(r):
 vals=[evrat(r,*x) for x in POINTS];iv=pow(vals[0],P-2,P);return tuple(x*iv%P for x in vals[1:])
def sdiv(a,b):return tuple(x*pow(y,P-2,P)%P for x,y in zip(a,b))

def main():
 factors=source_factors(P)[0]+source_factors(P)[1]
 U,V=U0,V0;sections=[];ds=[]
 for step in range(3):
  ds.append(rsub(U,V))
  for name,poly in factors:sections.append({"step":step,"label":name,"r":peval(poly,U,V)})
  U,V=rho(U,V)
 unit_product=rmul(rmul(ds[0],ds[1]),ds[2]);unit_relation=req(unit_product,rconst(8))
 units={}
 for a in range(-10,11):
  for b in range(-10,11):
   q=rmul(rpow(ds[0],a) if a>=0 else rpow(rinv(ds[0]),-a),rpow(ds[1],b) if b>=0 else rpow(rinv(ds[1]),-b))
   units.setdefault(sig(q),[]).append((a,b,q))
 classes=[]
 for item in sections:
  si=sig(item["r"]);placed=False
  for ci,cl in enumerate(classes):
   ratio=sdiv(si,sig(cl[0]["r"]))
   for a,b,q in units.get(ratio,[]):
    if req(item["r"],rmul(cl[0]["r"],q)):
     item["unit_exponents_from_representative"]=[a,b];cl.append(item);placed=True;break
   if placed:break
  if not placed:item["unit_exponents_from_representative"]=[0,0];classes.append([item])
 result={"schema":"marici.hom-support-orbits-mod-chart-units.v1","prime":P,"normalization_unit_relation":"d0*d1*d2=8","unit_relation_verified":unit_relation,
  "unit_search_box":{"d0":[-10,10],"d1":[-10,10]},"marked_section_count":len(sections),"support_class_count":len(classes),
  "classes":[{"class":i,"members":[{"step":x["step"],"label":x["label"],"unit_exponents_from_representative":x["unit_exponents_from_representative"]} for x in cl]} for i,cl in enumerate(classes)],
  "all_classes_three_chart":all(len(cl)==3 for cl in classes)}
 OUT.write_text(json.dumps(result,indent=2)+"\n");print(json.dumps({"classes":len(classes),"sizes":[len(x) for x in classes],"unit_relation":unit_relation}))
if __name__=="__main__":main()
