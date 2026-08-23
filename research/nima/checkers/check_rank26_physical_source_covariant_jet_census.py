#!/usr/bin/env python3
"""Exact polynomial-coefficient covariant-jet census before quotient reduction."""
from __future__ import annotations
import contextlib,importlib,io,json,os,sys
from pathlib import Path
from sympy import Poly,symbols,sympify

ROOT=Path(__file__).resolve().parents[3]
BEN=ROOT/"research"/"benincasa";NCHK=ROOT/"research"/"nima"/"checkers"
sys.path[:0]=[str(BEN),str(NCHK)]
with contextlib.redirect_stdout(io.StringIO()):
    base=importlib.import_module("physical_four_mark_residue_twisted_derham")
    charts=importlib.import_module("g12_g31_residue_chart_transition")
    prior=importlib.import_module("check_rank26_physical_annihilator_chart_transport")
K_DEPTH=int(os.environ.get("MARICI_K_DEPTH","2"))
MAX_ORDER=int(os.environ.get("MARICI_MAX_JET_ORDER","4"))
P=base.PRIME
def g23_fiber_data(x,y,z):
    source_k,source_q=base.fiber_data(z,y,x)
    k=charts.swap_exponents(source_k)
    mapping={"g1":"g3","g2":"g2","g3":"g1","g23":"g12","g31":"g31"}
    return k,{target:charts.swap_exponents(source_q[source]) for source,target in mapping.items()}

CHART=os.environ.get("MARICI_RESIDUE_CHART","G12")
if CHART=="G31":
    POINT=charts.TARGET_POINT;NAMES=charts.TARGET_NAMES;FIBER=charts.g31_fiber_data;NUMERATOR_NAMES=("g23","g12")
elif CHART=="G23":
    POINT=(4,3,2);NAMES=("g3","g2","g1","g12","g31");FIBER=g23_fiber_data;NUMERATOR_NAMES=("g12","g31")
else:
    POINT=charts.SOURCE_POINT;NAMES=charts.SOURCE_NAMES;FIBER=base.fiber_data;NUMERATOR_NAMES=("g23","g31")
POINT_OVERRIDE=os.environ.get("MARICI_POINT")
if POINT_OVERRIDE:
    POINT=tuple(int(x) for x in POINT_OVERRIDE.split(","))
TWIST=os.environ.get("MARICI_TWIST","physical")
GAMMA=5 if TWIST=="generic" else (-pow(2,P-2,P))%P
POINT_TAG="_at_"+"_".join(str(x) for x in POINT) if POINT_OVERRIDE else ""
OUT=ROOT/"research"/"nima"/"results"/f"rank26_{TWIST}_{CHART.lower()}_source_covariant_jet_census_k{K_DEPTH}{POINT_TAG}_p{P}.json"
base.reduce_row=prior.reduce_complete
Mon=tuple[int,int,int];Pol=dict[Mon,int]

def clean(p):return {e:c%P for e,c in p.items() if c%P}
def padd(dst,src,scale=1):
    for e,c in src.items():
      v=(dst.get(e,0)+scale*c)%P
      if v:dst[e]=v
      else:dst.pop(e,None)
def pscale(p,s):return clean({e:c*s for e,c in p.items()})
def pmul(a,b):
    out={}
    for e,c in a.items():
      for f,d in b.items():padd(out,{tuple(e[i]+f[i] for i in range(3)):c*d})
    return out
def pder(p,axis):
    out={}
    for e,c in p.items():
      if e[axis]:
       f=list(e);power=f[axis];f[axis]-=1;padd(out,{tuple(f):c*power})
    return out
def peval(p,point):return sum(c*pow(point[0],e[0],P)*pow(point[1],e[1],P)*pow(point[2],e[2],P) for e,c in p.items())%P
def from_expr(expr,xyz):
    return clean({tuple(int(i) for i in mon):int(c)%P for mon,c in Poly(expr,*xyz,modulus=P).terms()})

def source_polynomials():
    x,y,z=symbols("x y z");E=x+y+z;x2=x*x;y2=y*y;z2=z*z;c2=E*E
    kexpr={(4,0):x2,(2,2):-(x2+y2-z2),(0,4):y2,
      (2,0):x2*(x2-y2-z2)+c2*(y2-x2-z2),
      (0,2):y2*(y2-x2-z2)+c2*(x2-y2-z2),
      (0,0):z2*c2*c2+c2*z2*(z2-x2-y2)+z2*x2*y2}
    qexpr={
      "g1":{(0,1):1,(0,0):-y-z},"g2":{(1,0):1,(0,0):-x-z},
      "g3":{(1,0):1,(0,1):1,(0,0):z},"g23":{(0,1):1,(0,0):-x},
      "g31":{(1,0):1,(0,0):-y}}
    if CHART=="G31":
      swap=lambda expr:expr.xreplace({y:z,z:y})
      kexpr={(j,i):swap(expr) for (i,j),expr in kexpr.items()}
      qexpr={
        "g1":{(1,0):1,(0,0):-y-z},"g3":{(0,1):1,(0,0):-x-y},
        "g2":{(1,0):1,(0,1):1,(0,0):y},"g23":{(1,0):1,(0,0):-x},
        "g12":{(0,1):1,(0,0):-z}}
    elif CHART=="G23":
      swap=lambda expr:sympify(expr).xreplace({x:z,z:x})
      kexpr={(j,i):swap(expr) for (i,j),expr in kexpr.items()}
      source_q=qexpr
      mapping={"g1":"g3","g2":"g2","g3":"g1","g23":"g12","g31":"g31"}
      qexpr={target:{(j,i):swap(expr) for (i,j),expr in source_q[source].items()} for source,target in mapping.items()}
    return ({e:from_expr(v,(x,y,z)) for e,v in kexpr.items()},
      {n:{e:from_expr(v,(x,y,z)) for e,v in qp.items()} for n,qp in qexpr.items()})

def row_add(row,column,poly):
    if not poly:return
    dst=row.setdefault(column,{});padd(dst,poly)
    if not dst:row.pop(column,None)

def connection_poly(label,axis,pres,kd,qd):
    kp,*rest=label;exp=rest.pop();levels=rest;row={}
    if kp<K_DEPTH:
      for term,poly in kd.items():
       target=(kp+1,*levels,base.shifted(exp,term))
       if target in pres["columns"]:row_add(row,pres["columns"][target],pscale(poly,GAMMA-kp))
    for qi,lev in enumerate(levels):
      if lev>=2:continue
      raised=list(levels);raised[qi]+=1
      for term,poly in qd[NAMES[qi]].items():
       target=(kp,*raised,base.shifted(exp,term))
       if target in pres["columns"]:row_add(row,pres["columns"][target],pscale(poly,-lev))
    return row

def differentiate_raw(raw,axis,pres,connections):
    out={}
    for column,coefficient in raw.items():
      row_add(out,column,pder(coefficient,axis))
      for target,factor in connections[(column,axis)].items():row_add(out,target,pmul(coefficient,factor))
    return out

def evaluate_reduce(raw,pres,free_set):
    numeric={c:peval(poly,POINT) for c,poly in raw.items() if peval(poly,POINT)}
    red=prior.reduce_complete(numeric,pres["pivots"])
    return {c:v for c,v in red.items() if c in free_set}

def main():
    charts.GAMMA=GAMMA;charts.AMBIENT=14;charts.CUTOFF=7;charts.K_DEPTH=K_DEPTH
    pres=charts.presentation(FIBER,POINT,NAMES);free_set=set(pres["free_low"])
    k,q=source_polynomials();kd=[{e:pder(poly,a) for e,poly in k.items()} for a in range(3)]
    qd=[{n:{e:pder(poly,a) for e,poly in qp.items()} for n,qp in q.items()} for a in range(3)]
    connections={}
    for column,label in enumerate(pres["ordered_columns"]):
      for axis in range(3):connections[(column,axis)]=connection_poly(label,axis,pres,kd[axis],qd[axis])
    n={e:dict(poly) for e,poly in q[NUMERATOR_NAMES[0]].items()}
    for e,poly in q[NUMERATOR_NAMES[1]].items():padd(n.setdefault(e,{}),poly)
    base_label=(0,1,1,1,1,1);root={pres["columns"][(*base_label,e)]:poly for e,poly in n.items()}
    span={};front={():root};orders=[]
    for order in range(MAX_ORDER+1):
      next_front={};new_count=0;independent_words=[]
      for word,raw in sorted(front.items()):
       v=evaluate_reduce(raw,pres,free_set);before=len(span);base.add_pivot(dict(v),span)
       if len(span)>before:new_count+=1;independent_words.append(list(word))
       if order<MAX_ORDER and len(span)<len(pres["free_low"]):
        for axis in range(3):next_front[word+(axis,)]=differentiate_raw(raw,axis,pres,connections)
      orders.append({"order":order,"jet_count":len(front),"new_independent_directions":new_count,"independent_words":independent_words,"cumulative_rank":len(span)})
      print(json.dumps(orders[-1]),flush=True)
      if len(span)==len(pres["free_low"]):break
      front=next_front
    dense=[[row.get(c,0) for c in pres["free_low"]] for row in span.values()]
    annihilator=prior.ann.nullspace(dense,len(pres["free_low"]))
    dual_rows=[]
    for vector in annihilator:
      support=[]
      for i,value in enumerate(vector):
       if value:
        label=pres["ordered_columns"][pres["free_low"][i]]
        support.append({"free_coordinate":i,"label":[*label[:-1],list(label[-1])],"coefficient":value if value<=P//2 else value-P})
      dual_rows.append(support)
    payload={"schema":"marici.rank26-source-covariant-jet-census.v5","prime":P,"twist":TWIST,"chart":CHART,"external_point":POINT,"gamma":5 if TWIST=="generic" else "-1/2","k_pole_depth":K_DEPTH,"max_jet_order":MAX_ORDER,"quotient_dimension":len(pres["free_low"]),"raw_before_reduction":True,"orders":orders,"full_cyclicity_reached":len(span)==len(pres["free_low"]),"first_full_order":next((r["order"] for r in orders if r["cumulative_rank"]==len(pres["free_low"])),None),"annihilator_dimension":len(annihilator),"annihilator_reduced_dual_basis":dual_rows,"passed":len(span)+len(annihilator)==len(pres["free_low"])}
    OUT.parent.mkdir(parents=True,exist_ok=True);OUT.write_text(json.dumps(payload,indent=2)+"\n",encoding="utf-8");print(json.dumps(payload,indent=2))
    if not payload["passed"]:raise SystemExit(1)
if __name__=="__main__":main()
