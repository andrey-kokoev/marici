#!/usr/bin/env python3
"""Audit G12 -> G31 transport of the physical frozen-Krylov annihilator."""
from __future__ import annotations
import contextlib,importlib,io,json,sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[3]
BEN=ROOT/"research"/"benincasa"; NCHK=ROOT/"research"/"nima"/"checkers"
sys.path[:0]=[str(BEN),str(NCHK)]
with contextlib.redirect_stdout(io.StringIO()):
    base=importlib.import_module("physical_four_mark_residue_twisted_derham")
    charts=importlib.import_module("g12_g31_residue_chart_transition")
    ann=importlib.import_module("check_rank26_physical_orbit_annihilator")
P=base.PRIME
OUT=ROOT/"research"/"nima"/"results"/f"rank26_physical_annihilator_chart_transport_p{P}.json"

def reduce_complete(row,pivots):
    row=dict(row)
    while True:
      active=[c for c in row if c in pivots]
      if not active:return row
      c=max(active);a=row[c]
      for j,v in pivots[c].items():base.add_value(row,j,-a*v)
base.reduce_row=reduce_complete

def rank(rows):
    piv={}
    for r in rows:base.add_pivot(dict(r),piv)
    return len(piv)

def inverse(a):
    n=len(a);w=[[x%P for x in row]+[1 if i==j else 0 for j in range(n)] for i,row in enumerate(a)]
    for c in range(n):
      k=next(i for i in range(c,n) if w[i][c]);w[c],w[k]=w[k],w[c]
      iv=pow(w[c][c],P-2,P);w[c]=[x*iv%P for x in w[c]]
      for i in range(n):
       if i!=c and w[i][c]:q=w[i][c];w[i]=[(x-q*y)%P for x,y in zip(w[i],w[c])]
    return [row[n:] for row in w]

def matmul(a,b):return [[sum(x*y for x,y in zip(row,col))%P for col in zip(*b)] for row in a]

def parameter_derivative_data(fiber,point,axis):
    nodes=tuple(range(-3,4));weights=[]
    for node in nodes:
      poly=[1];den=1
      for other in nodes:
       if other==node:continue
       nxt=[0]*(len(poly)+1)
       for d,c in enumerate(poly):nxt[d]=(nxt[d]-other*c)%P;nxt[d+1]=(nxt[d+1]+c)%P
       poly=nxt;den=den*(node-other)%P
      weights.append(poly[1]*pow(den,P-2,P)%P)
    kr={};qr={}
    for off,w in zip(nodes,weights):
      pt=list(point);pt[axis]+=off;k,q=fiber(*pt)
      for e,c in k.items():kr[e]=(kr.get(e,0)+w*c)%P
      for name,poly in q.items():
       dst=qr.setdefault(name,{})
       for e,c in poly.items():dst[e]=(dst.get(e,0)+w*c)%P
    return {e:c for e,c in kr.items() if c},{n:{e:c for e,c in q.items() if c} for n,q in qr.items()}

def connection_image(label,names,gamma,axis,pres,fiber,point):
    kp,*rest=label;exp=rest.pop();levels=rest;kd,qd=parameter_derivative_data(fiber,point,axis);row={}
    if kp<2:
      for term,c in base.multiply_monomial(kd,exp,gamma-kp):
       target=(kp+1,*levels,term)
       if target in pres["columns"]:base.add_value(row,pres["columns"][target],c)
    for qi,lev in enumerate(levels):
      if lev>=2:continue
      raised=list(levels);raised[qi]+=1
      for term,c in base.multiply_monomial(qd[names[qi]],exp,-lev):
       target=(kp,*raised,term)
       if target in pres["columns"]:base.add_value(row,pres["columns"][target],c)
    return row

def orbit_annihilator(pres,fiber,point,names,numerator_names,gamma):
    _,q=fiber(*point);num=dict(q[numerator_names[0]])
    for name in numerator_names[1:]:
      for e,c in q[name].items():num[e]=(num.get(e,0)+c)%P
    qpos={c:i for i,c in enumerate(pres["free_low"])};base_label=(0,*([1]*len(names)));source={}
    for e,c in num.items():
      red=reduce_complete({pres["columns"][(*base_label,e)]:1},pres["pivots"])
      for j,v in red.items():
       if j in qpos:base.add_value(source,j,c*v)
    nd=[]
    for axis in range(3):
      _,qd=parameter_derivative_data(fiber,point,axis);d={}
      for name in numerator_names:
       for e,c in qd[name].items():d[e]=(d.get(e,0)+c)%P
      nd.append(d)
    label_by={pres["columns"][l]:l for l in pres["low_labels"]};span={};front=[(source,True)]
    while front:
      v,is_source=front.pop();before=len(span);base.add_pivot(dict(v),span)
      if len(span)==before:continue
      for axis in range(3):
       image={}
       for j,c in v.items():
        for t,w in connection_image(label_by[j],names,gamma,axis,pres,fiber,point).items():base.add_value(image,t,c*w)
       if is_source:
        for e,c in nd[axis].items():base.add_value(image,pres["columns"][(*base_label,e)],c)
       red=reduce_complete(image,pres["pivots"]);qv={j:w for j,w in red.items() if j in qpos}
       if qv:front.append((qv,False))
    dense=[[row.get(c,0) for c in pres["free_low"]] for row in span.values()]
    ns=ann.nullspace(dense,len(pres["free_low"]));assert len(span)==25 and len(ns)==1
    return ns[0]

def proportional(left,right):
    pivot=next((i for i,x in enumerate(right) if x),None)
    if pivot is None:return False,None
    scale=left[pivot]*pow(right[pivot],P-2,P)%P
    return all(a==scale*b%P for a,b in zip(left,right)),scale

def relation_descent_failures(source,target):
    failures=[]
    for pivot,row in source["pivots"].items():
      mapped=charts.map_row(row,source,target)
      residual=reduce_complete(mapped,target["pivots"])
      if residual:
       failures.append({"source_pivot":pivot,"residual_terms":len(residual)})
    return failures

def main():
    half=(-pow(2,P-2,P))%P
    charts.GAMMA=half;charts.AMBIENT=14;charts.CUTOFF=7
    source=charts.presentation(base.fiber_data,charts.SOURCE_POINT,charts.SOURCE_NAMES)
    target=charts.presentation(charts.g31_fiber_data,charts.TARGET_POINT,charts.TARGET_NAMES)
    forward_relation_failures=relation_descent_failures(source,target)
    reverse_relation_failures=relation_descent_failures(target,source)
    spos={c:i for i,c in enumerate(source["free_low"])};tpos={c:i for i,c in enumerate(target["free_low"])}
    T=[[0]*len(source["free_low"]) for _ in target["free_low"]]
    for j,c in enumerate(source["free_low"]):
      label=source["ordered_columns"][c]
      row=charts.quotient_vector(charts.map_label(label),target,-1)
      for tc,v in row.items():T[tpos[tc]][j]=v
    assert rank([{i:v for i,v in enumerate(row) if v} for row in T])==26
    Ti=inverse(T)
    # Source annihilator in the actual physical quotient basis.
    ell=[0]*26
    for label,coef in [((0,1,1,1,1,1,(4,1)),-1),((0,1,1,1,1,1,(5,0)),1)]:
      c=source["columns"][label];assert c in spos;ell[spos[c]]=coef%P
    independent_source=orbit_annihilator(source,base.fiber_data,charts.SOURCE_POINT,charts.SOURCE_NAMES,("g23","g31"),half)
    source_agrees,source_scale=proportional(ell,independent_source)
    transported=matmul([ell],Ti)[0]
    independent=orbit_annihilator(target,charts.g31_fiber_data,charts.TARGET_POINT,charts.TARGET_NAMES,("g23","g12"),half)
    agrees,scale=proportional(transported,independent)
    support=[]
    for i,v in enumerate(transported):
      if v:
       label=target["ordered_columns"][target["free_low"][i]]
       support.append({"free_coordinate":i,"label":[*label[:-1],list(label[-1])],"coefficient":v if v<=P//2 else v-P})
    check=matmul([transported],T)[0]
    payload={"schema":"marici.rank26-physical-frozen-krylov-chart-transport.v4","prime":P,"gamma":"-1/2","transition":"G12_to_G31","orientation_sign":-1,"transport_rank":26,"typing":"pointwise quotient transport of frozen-Krylov covectors; mismatch is diagnostic, not a curvature or physical claim","forward_relation_failure_count":len(forward_relation_failures),"reverse_relation_failure_count":len(reverse_relation_failures),"forward_relation_failure_sample":forward_relation_failures[:10],"reverse_relation_failure_sample":reverse_relation_failures[:10],"source_annihilator_support":[{"monomial":[4,1],"coefficient":-1},{"monomial":[5,0],"coefficient":1}],"source_line_equals_independent_source_line":source_agrees,"source_proportionality_scalar":source_scale,"transported_target_support":support,"contragredient_identity_holds":check==[x%P for x in ell],"independent_target_annihilator_computed":True,"transported_line_equals_independent_target_line":agrees,"expected_frozen_line_mismatch_observed":not agrees,"proportionality_scalar":scale,"passed":len(forward_relation_failures)==0 and len(reverse_relation_failures)==0 and source_agrees and check==[x%P for x in ell] and not agrees}
    OUT.parent.mkdir(parents=True,exist_ok=True);OUT.write_text(json.dumps(payload,indent=2)+"\n",encoding="utf-8");print(json.dumps(payload,indent=2))
    if not payload["passed"]:raise SystemExit(1)
if __name__=="__main__":main()
