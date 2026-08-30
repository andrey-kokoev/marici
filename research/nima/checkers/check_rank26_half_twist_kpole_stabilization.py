#!/usr/bin/env python3
"""Extend the five-mark physical half-twist through higher K-pole depth."""
from __future__ import annotations
import contextlib, importlib, io, json, sys
from itertools import product
from pathlib import Path

ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/"research"/"benincasa"))
with contextlib.redirect_stdout(io.StringIO()):
    b=importlib.import_module("physical_four_mark_residue_twisted_derham")
P=b.PRIME
OUT=Path(__file__).resolve().parents[1]/"results"/f"rank26_half_twist_kpole_stabilization_p{P}.json"
NAMES=("g1","g2","g3","g23","g31")

def reduce_complete(row,pivots):
    row=dict(row)
    while True:
        active=[c for c in row if c in pivots]
        if not active:return row
        c=max(active);a=row[c]
        for j,v in pivots[c].items():b.add_value(row,j,-a*v)

def presentation(gamma,ambient,cutoff,k_depth):
    k,all_q=b.fiber_data(2,3,4);qs=[all_q[n] for n in NAMES];q_depth=2
    lowmons=b.monomials_at_most(cutoff)
    low=[(0,*levels,m) for levels in product(range(1,2),repeat=5) for m in lowmons]
    lowset=set(low); ambmons=b.monomials_at_most(ambient+4); ordered=list(low)
    for kp in range(k_depth+1):
      for levels in product(range(1,q_depth+1),repeat=5):
       ordered.extend(label for m in ambmons if (label:=(kp,*levels,m)) not in lowset)
    cols={label:i for i,label in enumerate(ordered)};piv={}
    kd=[b.derivative(k,a) for a in range(2)];qd=[[b.derivative(q,a) for a in range(2)] for q in qs]
    for kp in range(k_depth):
      for levels in product(range(1,q_depth+1),repeat=5):
       if any(x==q_depth for x in levels):continue
       for axis in range(2):
        for exp in b.monomials_at_most(ambient):
         row={}
         if exp[axis]:
          d=list(exp);d[axis]-=1;b.add_value(row,cols[(kp,*levels,tuple(d))],exp[axis])
         for term,c in kd[axis].items():b.add_value(row,cols[(kp+1,*levels,b.shifted(exp,term))],(gamma-kp)*c)
         for qi,lev in enumerate(levels):
          raised=list(levels);raised[qi]+=1
          for term,c in qd[qi][axis].items():b.add_value(row,cols[(kp,*raised,b.shifted(exp,term))],-lev*c)
         b.add_pivot(row,piv)
    for kp in range(k_depth):
      for levels in product(range(1,q_depth+1),repeat=5):
       for exp in b.monomials_at_most(ambient-4):
        row={cols[(kp,*levels,exp)]:1}
        for term,c in b.multiply_monomial(k,exp,-1):b.add_value(row,cols[(kp+1,*levels,term)],c)
        b.add_pivot(row,piv)
    for qi,q in enumerate(qs):
      for kp in range(k_depth+1):
       for levels in product(range(1,q_depth+1),repeat=5):
        if levels[qi]==q_depth:continue
        raised=list(levels);raised[qi]+=1
        for exp in b.monomials_at_most(ambient-1):
         row={cols[(kp,*levels,exp)]:1}
         for term,c in b.multiply_monomial(q,exp,-1):b.add_value(row,cols[(kp,*raised,term)],c)
         b.add_pivot(row,piv)
    free=[i for i in range(len(low)) if i not in piv]
    return {"low":low,"ordered":ordered,"columns":cols,"pivots":piv,"free":free,"k":k,"qs":qs,"k_depth":k_depth}

def connection_image(label,gamma,axis,pres):
    kp,*rest=label;exp=rest.pop();levels=rest;kd,qd=b.parameter_derivative_data(axis);row={}
    if kp<pres["k_depth"]:
      for term,c in b.multiply_monomial(kd,exp,gamma-kp):
       target=(kp+1,*levels,term)
       if target in pres["columns"]:b.add_value(row,pres["columns"][target],c)
    for qi,lev in enumerate(levels):
      if lev>=2:continue
      raised=list(levels);raised[qi]+=1
      for term,c in b.multiply_monomial(qd[NAMES[qi]],exp,-lev):
       target=(kp,*raised,term)
       if target in pres["columns"]:b.add_value(row,pres["columns"][target],c)
    return row

def source_saturation(pres,gamma,operator_count,return_span=False):
    _,q=b.fiber_data(2,3,4);num=dict(q["g23"])
    for e,c in q["g31"].items():num[e]=(num.get(e,0)+c)%P
    base=(0,1,1,1,1,1);source={}
    for e,c in num.items():
      red=reduce_complete({pres["columns"][(*base,e)]:1},pres["pivots"])
      for j,v in red.items():
       if j in pres["free"]:b.add_value(source,j,c*v)
    num_derivatives=[]
    for axis in range(operator_count):
      _,qd=b.parameter_derivative_data(axis);dn=dict(qd["g23"])
      for e,c in qd["g31"].items():dn[e]=(dn.get(e,0)+c)%P
      num_derivatives.append(dn)
    labels={pres["columns"][l]:l for l in pres["low"]};span={};front=[(source,True)]
    while front:
      v,is_source=front.pop();before=len(span);b.add_pivot(dict(v),span)
      if len(span)==before:continue
      for axis in range(operator_count):
       image={}
       for j,c in v.items():
        for t,w in connection_image(labels[j],gamma,axis,pres).items():b.add_value(image,t,c*w)
       if is_source:
        for e,c in num_derivatives[axis].items():b.add_value(image,pres["columns"][(*base,e)],c)
       red=reduce_complete(image,pres["pivots"]);qv={j:w for j,w in red.items() if j in pres["free"]}
       if qv:front.append((qv,False))
    return (len(span),span) if return_span else len(span)

def main():
    fibers=[]
    for name,gamma in (("generic",5),("physical",(-pow(2,P-2,P))%P)):
     rows=[]
     for depth in (2,3):
      pres=presentation(gamma,14,7,depth)
      rows.append({"k_pole_depth":depth,"quotient_dimension":len(pres["free"]),"frozen_krylov_rank_two_operators":source_saturation(pres,gamma,2),"frozen_krylov_rank_three_operators":source_saturation(pres,gamma,3),"column_count":len(pres["columns"]),"relation_rank":len(pres["low"])-len(pres["free"])})
     fibers.append({"twist":name,"gamma":5 if name=="generic" else "-1/2","depths":rows})
    allrows=[r for f in fibers for r in f["depths"]]
    payload={"schema":"marici.rank26-half-twist-kpole-stabilization.v3","prime":P,"ambient":14,"cutoff":7,"fibers":fibers,"rank26_stable":all(r["quotient_dimension"]==26 for r in allrows),"two_operator_physical_frozen_residual_present":all(r["frozen_krylov_rank_two_operators"]==25 for f in fibers if f["twist"]=="physical" for r in f["depths"]),"three_operator_physical_frozen_cyclicity_restored":all(r["frozen_krylov_rank_three_operators"]==26 for f in fibers if f["twist"]=="physical" for r in f["depths"]),"typing":"finite frozen-point Krylov closure only; not an iterated Gauss-Manin orbit","scope":"K-pole depths 2 and 3; five q-poles remain at depth 2; every pivot eliminated before free-coordinate projection"}
    payload["passed"]=payload["rank26_stable"]
    OUT.parent.mkdir(parents=True,exist_ok=True);OUT.write_text(json.dumps(payload,indent=2)+"\n",encoding="utf-8");print(json.dumps(payload,indent=2))
    if not payload["passed"]:raise SystemExit(1)
if __name__=="__main__":main()
