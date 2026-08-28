#!/usr/bin/env python3
"""Compute one K-depth transition on the source-reachable quotient without building the target orbit."""
from __future__ import annotations
import contextlib, importlib, io, json, os, sys
from collections import deque
from pathlib import Path

ROOT=Path(__file__).resolve().parents[3]
BEN=ROOT/"research"/"benincasa"; NCHK=ROOT/"research"/"nima"/"checkers"
sys.path[:0]=[str(BEN),str(BEN/"checkers"),str(NCHK)]
P=int(sys.argv[1]); CHART=sys.argv[2] if len(sys.argv)>2 else "G12"; DEPTH=int(sys.argv[3]) if len(sys.argv)>3 else 4
NEXT=int(sys.argv[4]) if len(sys.argv)>4 else DEPTH+1
os.environ.update({"MARICI_FIELD_PRIME":str(P),"MARICI_RESIDUE_CHART":CHART,"MARICI_K_DEPTH":str(DEPTH),"MARICI_MAX_JET_ORDER":"0","MARICI_TWIST":"physical"})
with contextlib.redirect_stdout(io.StringIO()):
    jet=importlib.import_module("check_rank26_physical_source_covariant_jet_census")
base=jet.base
k,q=jet.source_polynomials()
kd=[{e:jet.pder(poly,a) for e,poly in k.items()} for a in range(3)]
qd=[{n:{e:jet.pder(poly,a) for e,poly in qp.items()} for n,qp in q.items()} for a in range(3)]
n={e:dict(poly) for e,poly in q[jet.NUMERATOR_NAMES[0]].items()}
for e,poly in q[jet.NUMERATOR_NAMES[1]].items(): jet.padd(n.setdefault(e,{}),poly)
root_prefix=(0,1,1,1,1,1)

def presentation(depth):
    jet.K_DEPTH=depth
    jet.charts.GAMMA=jet.GAMMA; jet.charts.AMBIENT=14; jet.charts.CUTOFF=7; jet.charts.K_DEPTH=depth
    return jet.charts.presentation(jet.FIBER,jet.POINT,jet.NAMES)

def reachable(pres,depth):
    jet.K_DEPTH=depth
    roots=sorted({pres["columns"][(*root_prefix,e)] for e,poly in n.items() if poly})
    found=set(roots); queue=deque(roots)
    while queue:
        c=queue.popleft(); label=pres["ordered_columns"][c]; targets=set()
        for axis in range(3): targets.update(jet.connection_poly(label,axis,pres,kd[axis],qd[axis]))
        for t in sorted(targets):
            if t not in found: found.add(t); queue.append(t)
    return found

source=presentation(DEPTH); target=presentation(NEXT)
source_reachable=reachable(source,DEPTH)

failed_relations=[]
for pivot,row in sorted(source["pivots"].items()):
    mapped={}
    for col,value in row.items():
        tc=target["columns"][source["ordered_columns"][col]]
        mapped[tc]=(mapped.get(tc,0)+value)%P
        if not mapped[tc]: mapped.pop(tc)
    residual=jet.prior.reduce_complete(mapped,target["pivots"])
    if residual:
        failed_relations.append({
          "source_pivot":pivot,
          "source_label":repr(source["ordered_columns"][pivot]),
          "residual_labels":[repr(target["ordered_columns"][c]) for c in sorted(residual)[:20]],
        })

source_span={}; image_span={}
for c in sorted(source_reachable):
    red=jet.prior.reduce_complete({c:1},source["pivots"]); base.add_pivot(dict(red),source_span)
    tc=target["columns"][source["ordered_columns"][c]]
    red_next=jet.prior.reduce_complete({tc:1},target["pivots"]); base.add_pivot(dict(red_next),image_span)

packet={
 "schema":"marici.consecutive-kdepth-source-quotient-transition.v1",
 "prime":P,"chart":CHART,"source_depth":DEPTH,"target_depth":NEXT,
 "source_reachable_rank":len(source_reachable),
 "source_quotient_rank":len(source_span),
 "transition_image_rank":len(image_span),
 "transition_kernel_rank":len(source_span)-len(image_span),
 "failed_relation_count":len(failed_relations),
 "failure_examples":failed_relations[:20],
 "transition_descends":not failed_relations,
 "transition_injective":not failed_relations and len(source_span)==len(image_span),
 "checks":{
   "all_source_labels_exist_at_target":all(source["ordered_columns"][c] in target["columns"] for c in source_reachable),
   "relation_kernel_descent":not failed_relations,
   "rank_nullity":len(image_span)+(len(source_span)-len(image_span))==len(source_span),
 },
 "passed":not failed_relations,
}
out=BEN/"results"/f"kdepth{DEPTH}-to{NEXT}-source-quotient-transition-{CHART.lower()}-p{P}.json"
out.write_text(json.dumps(packet,indent=2)+"\n",encoding="utf-8")
print(json.dumps(packet,indent=2))
if not packet["passed"]: raise SystemExit(1)
