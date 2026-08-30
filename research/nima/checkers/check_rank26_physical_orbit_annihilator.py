#!/usr/bin/env python3
"""Extract the intrinsic dual line annihilating the physical source orbit."""
from __future__ import annotations
import contextlib,importlib,io,json,sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/"research"/"nima"/"checkers"))
with contextlib.redirect_stdout(io.StringIO()):
    model=importlib.import_module("check_rank26_half_twist_kpole_stabilization")
P=model.P
OUT=Path(__file__).resolve().parents[1]/"results"/f"rank26_physical_orbit_annihilator_p{P}.json"

def nullspace(rows,width):
    a=[[x%P for x in row] for row in rows];piv=[];r=0
    for c in range(width):
      k=next((i for i in range(r,len(a)) if a[i][c]),None)
      if k is None:continue
      a[r],a[k]=a[k],a[r];iv=pow(a[r][c],P-2,P);a[r]=[x*iv%P for x in a[r]]
      for i in range(len(a)):
       if i!=r and a[i][c]:
        q=a[i][c];a[i]=[(x-q*y)%P for x,y in zip(a[i],a[r])]
      piv.append(c);r+=1
      if r==len(a):break
    free=[c for c in range(width) if c not in piv];out=[]
    for f in free:
      v=[0]*width;v[f]=1
      for row,c in reversed(list(zip(a[:r],piv))):v[c]=(-sum(row[j]*v[j] for j in free))%P
      out.append(v)
    return out

def one_depth(depth):
    gamma=(-pow(2,P-2,P))%P;pres=model.presentation(gamma,14,7,depth)
    rank,span=model.source_saturation(pres,gamma,3,True);free=pres["free"];pos={c:i for i,c in enumerate(free)}
    dense=[[row.get(c,0) for c in free] for row in span.values()];ns=nullspace(dense,len(free));assert rank==25 and len(ns)==1
    cov=ns[0];support=[]
    for i,x in enumerate(cov):
      if x:
       label=pres["ordered"][free[i]];support.append({"free_coordinate":i,"label":[*label[:-1],list(label[-1])],"monomial":list(label[-1]),"degree":sum(label[-1]),"coefficient":x if x<=P//2 else x-P})
    assert all(sum(row.get(c,0)*cov[pos[c]] for c in free)%P==0 for row in span.values())
    return {"k_pole_depth":depth,"orbit_rank":rank,"annihilator_dimension":1,"annihilator_support":support,"support_degrees":sorted({x["degree"] for x in support})}

def main():
    rows=[one_depth(d) for d in (2,3)]
    sig=lambda r:[(x["label"],x["coefficient"]) for x in r["annihilator_support"]]
    payload={"schema":"marici.rank26-physical-frozen-krylov-annihilator.v2","prime":P,"gamma":"-1/2","operator_count":3,"depths":rows,"annihilator_identical_across_depths":sig(rows[0])==sig(rows[1]),"interpretation":"dual line of the frozen-point Krylov span; not yet a Gauss-Manin, horizontal, physical, or Leray object; no primal splitting selected"}
    payload["passed"]=all(r["annihilator_dimension"]==1 for r in rows)
    OUT.parent.mkdir(parents=True,exist_ok=True);OUT.write_text(json.dumps(payload,indent=2)+"\n",encoding="utf-8");print(json.dumps(payload,indent=2))
    if not payload["passed"]:raise SystemExit(1)
if __name__=="__main__":main()
