#!/usr/bin/env python3
"""Complete the barcode packet from a source-owned G12 checkpoint using independent G31 presentations."""
from __future__ import annotations
import contextlib, importlib, io, json, os, pickle, sys
from collections import deque
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
BEN=ROOT/"research"/"benincasa"; NCHK=ROOT/"research"/"nima"/"checkers"
sys.path[:0]=[str(BEN),str(BEN/"checkers"),str(NCHK)]
P=int(sys.argv[1]) if len(sys.argv)>1 and sys.argv[1].isdigit() else 32009
os.environ.update({"MARICI_FIELD_PRIME":str(P),"MARICI_RESIDUE_CHART":"G31",
 "MARICI_K_DEPTH":"3","MARICI_MAX_JET_ORDER":"0","MARICI_TWIST":"physical"})
with contextlib.redirect_stdout(io.StringIO()):
    jet=importlib.import_module("check_rank26_physical_source_covariant_jet_census")
k,q=jet.source_polynomials()
kd=[{e:jet.pder(poly,a) for e,poly in k.items()} for a in range(3)]
qd=[{n:{e:jet.pder(poly,a) for e,poly in qp.items()} for n,qp in q.items()} for a in range(3)]
num={e:dict(poly) for e,poly in q[jet.NUMERATOR_NAMES[0]].items()}
for e,poly in q[jet.NUMERATOR_NAMES[1]].items(): jet.padd(num.setdefault(e,{}),poly)
ROOT_PREFIX=(0,1,1,1,1,1)

def clean(v): return {int(k):int(x)%P for k,x in v.items() if x%P}
def axpy(v,a,w):
    for k,x in w.items():
        y=(v.get(k,0)-a*x)%P
        if y:v[k]=y
        else:v.pop(k,None)
class SparseBasis:
    def __init__(self): self.rows=[]; self.piv={}
    def reduce(self,v,coords=None):
        v=clean(v); coords={} if coords is None else coords
        for p,i in sorted(self.piv.items()):
            a=v.get(p,0)
            if a:
                axpy(v,a,self.rows[i]); coords[i]=(coords.get(i,0)+a)%P
                if not coords[i]:coords.pop(i)
        return v,coords
    def add(self,v):
        r,_=self.reduce(v)
        if not r:return None
        p=min(r); inv=pow(r[p],-1,P); r={k:x*inv%P for k,x in r.items()}
        i=len(self.rows); self.rows.append(r); self.piv[p]=i; return i
    def coordinates(self,v):
        r,c=self.reduce(v,{})
        if r:raise ValueError(("outside span",min(r)))
        return c

def presentation(depth):
    jet.K_DEPTH=depth; jet.RESIDUE_CHART="G31"
    jet.charts.GAMMA=jet.GAMMA; jet.charts.AMBIENT=14
    jet.charts.CUTOFF=7; jet.charts.K_DEPTH=depth
    return jet.charts.presentation(jet.FIBER,jet.POINT,jet.NAMES)
def reachable(pres,depth):
    jet.K_DEPTH=depth
    roots=sorted({pres["columns"][(*ROOT_PREFIX,e)] for e,poly in num.items() if poly})
    found=set(roots); queue=deque(roots)
    while queue:
        c=queue.popleft(); label=pres["ordered_columns"][c]; targets=set()
        for axis in range(3):targets.update(jet.connection_poly(label,axis,pres,kd[axis],qd[axis]))
        for t in sorted(targets):
            if t not in found:found.add(t);queue.append(t)
    return sorted(found)
def quotient(depth):
    p=presentation(depth); reach=reachable(p,depth); b=SparseBasis()
    for c in reach:b.add(jet.prior.reduce_complete({c:1},p["pivots"]))
    return {"pres":p,"reach":reach,"basis":b}
def sparse(v):
    v=clean(v); ii=sorted(v); return {"indices":ii,"values":[v[i] for i in ii]}
def label_json(x):
    if isinstance(x,tuple):return [label_json(y) for y in x]
    return x
def chart_label(label):
    """Source-derived sigma_23 map: swap retained fiber exponents.

    Pole-level positions already follow the paired source/target mark orders;
    the Poincare-residue pullback contributes the common sign -1.
    """
    *head,exponent=label
    return (*head,(exponent[1],exponent[0]))
def mapped_label(tgt,label):
    c=tgt["pres"]["columns"][chart_label(label)]
    return clean(jet.prior.reduce_complete({c:(P-1)},tgt["pres"]["pivots"]))
def transport_rows(rows,source_labels,tgt):
    out=[]
    for row in rows:
        v={}
        for pos,a in row.items():
            mv=mapped_label(tgt,source_labels[pos])
            for k,x in mv.items():v[k]=(v.get(k,0)+a*x)%P
        out.append(clean(v))
    return out
def rank(rows):
    b=SparseBasis()
    for r in rows:b.add(r)
    return len(b.rows)

cp_path=BEN/"results"/f"interaction-net-barcode-basis-stage1-p{P}.pkl"
with cp_path.open("rb") as fh: cp=pickle.load(fh)
g12=cp["g12"]; q3=g12[3]; q4=g12[4]
labels3=[q3["pres"]["ordered_columns"][c] for c in q3["reach"]]
labels4=[q4["pres"]["ordered_columns"][c] for c in q4["reach"]]
print("building independent G31 depth3",flush=True)
g31_3=quotient(3)
v3=transport_rows(cp["adapted_source"],labels3,g31_3)
b3=SparseBasis()
for v in v3:
    if b3.add(v) is None:raise ValueError("depth3 transport rank loss")
t3=[b3.coordinates(v) for v in v3]
print("building independent G31 depth4",flush=True)
g31_4=quotient(4)
v4=transport_rows(cp["adapted4_source"],labels4,g31_4)
b4=SparseBasis()
for v in v4:
    if b4.add(v) is None:raise ValueError("depth4 transport rank loss")
t4=[b4.coordinates(v) for v in v4]

def qcoords(tgt,src,rows):
    out=[]
    for row in rows:
        v={}
        for pos,a in row.items():
            c=src["reach"][pos]; label=src["pres"]["ordered_columns"][c]
            mv=mapped_label(tgt,label)
            for k,x in mv.items():v[k]=(v.get(k,0)+a*x)%P
        out.append(tgt["basis"].coordinates(clean(v)))
    return out

# Recreate G12 checks from checkpointed exact rows.
transition=cp["transition"]
checks={
 "source_label_counts":len(labels3)==4800 and len(labels4)==9120,
 "quotient_ranks":{"3":len(g12[3]["qb"].rows),"4":len(g12[4]["qb"].rows),
                   "5":len(g12[5]["qb"].rows),"6":len(g12[6]["qb"].rows)},
 "kernel_ranks":[20,26,26],
 "transition_ranks":{key.split("to")[-1]:rank([{i:v for i,v in zip(r["indices"],r["values"])} for r in block["rows"]])
                     for key,block in transition.items()},
 "emergence_count":len(cp["emergence_rows"]),
 "depth4_total_rank":len(g12[4]["qb"].rows),
 "dual3_count":len(cp["dual3"]),"dual4_count":len(cp["dual4"]),
 "chart_transport_ranks":{"depth3":rank(t3),"depth4":rank(t4)},
 "chart_flags_preserved":rank(t3[:20])==20 and rank(t3[:26])==26 and rank(t3[26:])==27
   and rank(t4[:33])==33 and rank(t4[33:])==1353,
}
passed=(checks["source_label_counts"] and checks["quotient_ranks"]=={"3":53,"4":1386,"5":3039,"6":4692}
 and checks["transition_ranks"]=={"4":33,"5":27,"6":27}
 and checks["emergence_count"]==1353 and checks["dual3_count"]==53 and checks["dual4_count"]==1353
 and checks["chart_transport_ranks"]=={"depth3":53,"depth4":1386} and checks["chart_flags_preserved"])
packet={
 "schema":"marici.aspect.interaction-net-barcode-basis-export.v1","prime":P,
 "conventions":{
  "row_action":"rows encode source vectors; transition rows are their quotient images",
  "label_order":"sorted exact reachable ordered-column labels",
  "adapted_depth3_order":["first_death"]*20+["second_death"]*6+["through_depth6"]*27,
  "depth4_adapted_order":"33 transported depth4 survivors followed by 1353 emergence-complement rows",
  "dual_pairing":"depth3 duals are raw-label functionals; emergence duals use the declared complement-coordinate pairing",
  "chart_transport":"identity on exact occurrence labels followed by independent G31 quotient reduction",
 },
 "source_label_order_depth3":[label_json(x) for x in labels3],
 "source_label_order_depth4":[label_json(x) for x in labels4],
 "adapted_depth3_quotient_basis":{
  "first_death_rows":[sparse(x) for x in cp["adapted_source"][:20]],
  "second_death_rows":[sparse(x) for x in cp["adapted_source"][20:26]],
  "through_depth6_rows":[sparse(x) for x in cp["adapted_source"][26:]],
 },
 "depth4_emergence_complement_rows":[sparse(x) for x in cp["emergence_rows"]],
 "transition_matrices":transition,
 "dual_pairing_matrices":{
  "depth3_adapted_duals":[sparse(x) for x in cp["dual3"]],
  "depth4_emergence_duals":[sparse(x) for x in cp["dual4"]],
 },
 "chart_transports":{
  "G12_to_G31_depth3":{"basis":"transported adapted depth3 basis","rows":[sparse(x) for x in t3]},
  "G12_to_G31_depth4":{"basis":"transported adapted depth4 basis","rows":[sparse(x) for x in t4]},
 },
 "checks":checks,"passed":passed,
}
out=BEN/"results"/f"interaction-net-barcode-basis-export-p{P}.json"
out.write_text(json.dumps(packet,separators=(",",":"))+"\n",encoding="utf-8")
print(json.dumps({"passed":passed,"output":str(out.relative_to(ROOT)),"bytes":out.stat().st_size,"checks":checks},indent=2))
if not passed:raise SystemExit(1)
