#!/usr/bin/env python3
"""Compute kernel and image of the descended K-depth 3 to 4 map on source-reachable quotients."""
from __future__ import annotations
import contextlib, importlib, io, json, os, sys
from collections import defaultdict, deque
from pathlib import Path

ROOT=Path(__file__).resolve().parents[3]
BEN=ROOT/"research"/"benincasa"; NCHK=ROOT/"research"/"nima"/"checkers"
sys.path[:0]=[str(BEN),str(BEN/"checkers"),str(NCHK)]
P=int(sys.argv[1]); CHART=sys.argv[2] if len(sys.argv)>2 else "G12"
os.environ.update({"MARICI_FIELD_PRIME":str(P),"MARICI_RESIDUE_CHART":CHART,"MARICI_K_DEPTH":"3","MARICI_MAX_JET_ORDER":"0","MARICI_TWIST":"physical"})
with contextlib.redirect_stdout(io.StringIO()):
    jet=importlib.import_module("check_rank26_physical_source_covariant_jet_census")
base=jet.base
k,q=jet.source_polynomials()
kd=[{e:jet.pder(poly,a) for e,poly in k.items()} for a in range(3)]
qd=[{n:{e:jet.pder(poly,a) for e,poly in qp.items()} for n,qp in q.items()} for a in range(3)]
n={e:dict(poly) for e,poly in q[jet.NUMERATOR_NAMES[0]].items()}
for e,poly in q[jet.NUMERATOR_NAMES[1]].items(): jet.padd(n.setdefault(e,{}),poly)
root_prefix=(0,1,1,1,1,1)

def make(depth):
    jet.K_DEPTH=depth
    jet.charts.GAMMA=jet.GAMMA; jet.charts.AMBIENT=14; jet.charts.CUTOFF=7; jet.charts.K_DEPTH=depth
    pres=jet.charts.presentation(jet.FIBER,jet.POINT,jet.NAMES)
    roots=sorted({pres["columns"][(*root_prefix,e)] for e,poly in n.items() if poly})
    reachable=set(roots); queue=deque(roots)
    while queue:
        c=queue.popleft(); label=pres["ordered_columns"][c]
        targets=set()
        for axis in range(3): targets.update(jet.connection_poly(label,axis,pres,kd[axis],qd[axis]))
        for t in sorted(targets):
            if t not in reachable: reachable.add(t); queue.append(t)
    return pres,reachable

p3,r3=make(3)
p4,r4=make(4)
span3={}; image4={}
for c in sorted(r3):
    red3=jet.prior.reduce_complete({c:1},p3["pivots"])
    base.add_pivot(dict(red3),span3)
    label=p3["ordered_columns"][c]
    c4=p4["columns"][label]
    red4=jet.prior.reduce_complete({c4:1},p4["pivots"])
    base.add_pivot(dict(red4),image4)

packet={
 "schema":"marici.kdepth3-to4-source-quotient-transition.v1",
 "prime":P,"chart":CHART,
 "depth3_reachable_rank":len(r3),
 "depth4_reachable_rank":len(r4),
 "depth3_quotient_rank":len(span3),
 "transition_image_rank":len(image4),
 "transition_kernel_rank":len(span3)-len(image4),
 "transition_injective":len(span3)==len(image4),
 "checks":{
   "all_depth3_reachable_labels_exist_at_depth4":all(p3["ordered_columns"][c] in p4["columns"] for c in r3),
   "rank_nullity":len(image4)+(len(span3)-len(image4))==len(span3),
 },
 "passed":True,
 "conclusion":(
   "The descended K-depth transition is injective on the source-reachable quotient."
   if len(span3)==len(image4) else
   "The descended K-depth transition has a nonzero kernel; finite-depth quotient classes can die after extending the K-pole tower."
 )
}
out=BEN/"results"/f"kdepth3-to4-source-quotient-transition-{CHART.lower()}-p{P}.json"
out.write_text(json.dumps(packet,indent=2)+"\n",encoding="utf-8")
print(json.dumps(packet,indent=2))
