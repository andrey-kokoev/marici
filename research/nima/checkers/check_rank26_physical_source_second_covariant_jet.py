#!/usr/bin/env python3
"""Compute the genuine raw-before-reduction second source jet at gamma=-1/2."""
from __future__ import annotations
import contextlib,importlib,io,json,sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[3]
BEN=ROOT/"research"/"benincasa";NCHK=ROOT/"research"/"nima"/"checkers"
sys.path[:0]=[str(BEN),str(NCHK)]
with contextlib.redirect_stdout(io.StringIO()):
    base=importlib.import_module("physical_four_mark_residue_twisted_derham")
    charts=importlib.import_module("g12_g31_residue_chart_transition")
    prior=importlib.import_module("check_rank26_physical_annihilator_chart_transport")
P=base.PRIME
OUT=ROOT/"research"/"nima"/"results"/f"rank26_physical_source_second_covariant_jet_p{P}.json"
POINT=charts.SOURCE_POINT;NAMES=charts.SOURCE_NAMES
HALF=(-pow(2,P-2,P))%P
base.reduce_row=prior.reduce_complete

def poly_add(dst,src,scale=1):
    for e,c in src.items():
      value=(dst.get(e,0)+scale*c)%P
      if value:dst[e]=value
      else:dst.pop(e,None)

def derivative_data(point,axis):
    return prior.parameter_derivative_data(base.fiber_data,point,axis)

def second_derivative_data(point,mu,nu):
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
      shifted=list(point);shifted[nu]+=off
      kd,qd=derivative_data(tuple(shifted),mu)
      poly_add(kr,kd,w)
      for name,poly in qd.items():poly_add(qr.setdefault(name,{}),poly,w)
    return kr,qr

def connection_raw(label,axis,pres,kd,qd):
    kp,*rest=label;exp=rest.pop();levels=rest;row={}
    if kp<2:
      for term,c in base.multiply_monomial(kd,exp,HALF-kp):
       target=(kp+1,*levels,term)
       if target in pres["columns"]:base.add_value(row,pres["columns"][target],c)
    for qi,lev in enumerate(levels):
      if lev>=2:continue
      raised=list(levels);raised[qi]+=1
      for term,c in base.multiply_monomial(qd[NAMES[qi]],exp,-lev):
       target=(kp,*raised,term)
       if target in pres["columns"]:base.add_value(row,pres["columns"][target],c)
    return row

def numerator(qd):
    out=dict(qd["g23"]);poly_add(out,qd["g31"]);return out

def first_raw_dual(mu,nu,pres,k,q,first,second):
    """Return raw first derivative coefficients as (value,d_nu value)."""
    n=numerator(q);nmu=numerator(first[mu][1]);nnu=numerator(first[nu][1]);nmnu=numerator(second[mu][nu][1])
    base_label=(0,1,1,1,1,1);out={}
    def add(column,value,derivative):
      a,b=out.get(column,(0,0));a=(a+value)%P;b=(b+derivative)%P
      if a or b:out[column]=(a,b)
      else:out.pop(column,None)
    for e,c in nmu.items():add(pres["columns"][(*base_label,e)],c,nmnu.get(e,0))
    for e,c in n.items():
      label=(*base_label,e)
      raw=connection_raw(label,mu,pres,first[mu][0],first[mu][1])
      draw=connection_raw(label,mu,pres,second[mu][nu][0],second[mu][nu][1])
      for column,v in raw.items():add(column,c*v,nnu.get(e,0)*v+c*draw.get(column,0))
      for column,v in draw.items():
       if column not in raw:add(column,0,c*v)
    return out

def reduce_free(raw,pres):
    red=prior.reduce_complete(raw,pres["pivots"])
    return {c:v for c,v in red.items() if c in set(pres["free_low"])}

def main():
    charts.GAMMA=HALF;charts.AMBIENT=14;charts.CUTOFF=7
    pres=charts.presentation(base.fiber_data,POINT,NAMES);k,q=base.fiber_data(*POINT)
    first=[derivative_data(POINT,a) for a in range(3)]
    second=[[second_derivative_data(POINT,a,b) for b in range(3)] for a in range(3)]
    n=numerator(q);base_label=(0,1,1,1,1,1)
    source=reduce_free({pres["columns"][(*base_label,e)]:c for e,c in n.items()},pres)
    first_raw={};first_vectors={}
    for mu in range(3):
      dual=first_raw_dual(mu,0,pres,k,q,first,second)
      raw={c:v for c,(v,_) in dual.items() if v};first_raw[mu]=raw
      first_vectors[mu]=reduce_free(raw,pres)
    second_vectors={}
    for mu in range(3):
      for nu in range(3):
       dual=first_raw_dual(mu,nu,pres,k,q,first,second);raw={}
       # Differentiate coefficients of the raw first derivative.
       for c,(_,dv) in dual.items():base.add_value(raw,c,dv)
       # Differentiate every labelled rational-form basis factor.
       for c,(v,_) in dual.items():
        if not v:continue
        label=pres["ordered_columns"][c]
        for t,w in connection_raw(label,nu,pres,first[nu][0],first[nu][1]).items():base.add_value(raw,t,v*w)
       second_vectors[(mu,nu)]=reduce_free(raw,pres)
    stages=[];span={}
    def admit(name,v):
      before=len(span);base.add_pivot(dict(v),span);stages.append({"jet":name,"independent":len(span)>before,"cumulative_rank":len(span)})
    admit("s",source)
    for mu in range(3):admit(f"D{mu}s",first_vectors[mu])
    for mu in range(3):
      for nu in range(3):admit(f"D{nu}D{mu}s",second_vectors[(mu,nu)])
    payload={"schema":"marici.rank26-physical-source-second-covariant-jet.v1","prime":P,"gamma":"-1/2","quotient_dimension":len(pres["free_low"]),"method":"differentiate raw labelled representatives before quotient reduction","ordered_jet_stages":stages,"rank_through_order_zero":stages[0]["cumulative_rank"],"rank_through_order_one":stages[3]["cumulative_rank"],"rank_through_order_two":stages[-1]["cumulative_rank"],"missing_direction_restored_by_second_jet":len(span)==len(pres["free_low"]),"passed":len(span)<=len(pres["free_low"])}
    OUT.parent.mkdir(parents=True,exist_ok=True);OUT.write_text(json.dumps(payload,indent=2)+"\n",encoding="utf-8");print(json.dumps(payload,indent=2))
    if not payload["passed"]:raise SystemExit(1)
if __name__=="__main__":main()
