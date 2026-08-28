#!/usr/bin/env python3
"""Exact-relation submodule and quotient Hilbert census on the source-reachable graph."""
from __future__ import annotations
import contextlib, importlib, io, json, os, sys
from collections import Counter, defaultdict, deque
from pathlib import Path

ROOT=Path(__file__).resolve().parents[3]
BEN=ROOT/"research"/"benincasa"; NCHK=ROOT/"research"/"nima"/"checkers"
sys.path[:0]=[str(BEN),str(BEN/"checkers"),str(NCHK)]
P=int(sys.argv[1]); CHART=sys.argv[2] if len(sys.argv)>2 else "G12"
KDEPTH=int(sys.argv[3]) if len(sys.argv)>3 else 3
os.environ.update({
 "MARICI_FIELD_PRIME":str(P),"MARICI_RESIDUE_CHART":CHART,
 "MARICI_K_DEPTH":str(KDEPTH),"MARICI_MAX_JET_ORDER":"0","MARICI_TWIST":"physical",
})
with contextlib.redirect_stdout(io.StringIO()):
    jet=importlib.import_module("check_rank26_physical_source_covariant_jet_census")
base=jet.base
jet.charts.GAMMA=jet.GAMMA; jet.charts.AMBIENT=14; jet.charts.CUTOFF=7; jet.charts.K_DEPTH=KDEPTH
pres=jet.charts.presentation(jet.FIBER,jet.POINT,jet.NAMES)
k,q=jet.source_polynomials()
kd=[{e:jet.pder(poly,a) for e,poly in k.items()} for a in range(3)]
qd=[{n:{e:jet.pder(poly,a) for e,poly in qp.items()} for n,qp in q.items()} for a in range(3)]

adj=defaultdict(set)
for col,label in enumerate(pres["ordered_columns"]):
    for axis in range(3):
        adj[col].update(jet.connection_poly(label,axis,pres,kd[axis],qd[axis]))

n={e:dict(poly) for e,poly in q[jet.NUMERATOR_NAMES[0]].items()}
for e,poly in q[jet.NUMERATOR_NAMES[1]].items(): jet.padd(n.setdefault(e,{}),poly)
root_prefix=(0,1,1,1,1,1)
roots=sorted({pres["columns"][(*root_prefix,e)] for e,poly in n.items() if poly})
distance={r:0 for r in roots}; reachable=set(roots); queue=deque(roots)
while queue:
    c=queue.popleft()
    for t in sorted(adj[c]):
        if t not in reachable:
            reachable.add(t); distance[t]=distance[c]+1; queue.append(t)

def grade(col):
    label=pres["ordered_columns"][col]
    return label[0],sum(x-1 for x in label[1:-1])

generated=Counter(grade(c) for c in reachable)
quotient_spans=defaultdict(dict)
global_span={}
cross_grade_reductions=[]
zero_images=0
reduced_images={}
for c in sorted(reachable):
    g=grade(c)
    red=jet.prior.reduce_complete({c:1},pres["pivots"])
    reduced_images[c]=red
    if not red: zero_images+=1
    target_grades=sorted({grade(t) for t in red})
    if any(h!=g for h in target_grades):
        cross_grade_reductions.append({"source_column":c,"source_grade":list(g),"target_grades":[list(h) for h in target_grades]})
    base.add_pivot(dict(red),quotient_spans[g])
    base.add_pivot(dict(red),global_span)

quotient={g:len(span) for g,span in quotient_spans.items()}
relation={g:generated[g]-quotient.get(g,0) for g in generated}
ks=sorted({g[0] for g in generated}); os_=sorted({g[1] for g in generated})
base_q=quotient.get((ks[0],os_[0]),0)
factorizes=bool(base_q) and all(
    quotient.get((i,j),0)*base_q==quotient.get((i,os_[0]),0)*quotient.get((ks[0],j),0)
    for i in ks for j in os_
)
filtered={}
for ik in ks:
    for jo in os_:
        span={}
        for c,red in reduced_images.items():
            g=grade(c)
            if g[0]<=ik and g[1]<=jo:
                base.add_pivot(dict(red),span)
        filtered[(ik,jo)]=len(span)
associated={}
for ik in ks:
    for jo in os_:
        associated[(ik,jo)]=(
            filtered[(ik,jo)]
            - filtered.get((ik-1,jo),0)
            - filtered.get((ik,jo-1),0)
            + filtered.get((ik-1,jo-1),0)
        )
distance_filtered={}
for cutoff in range(max(distance.values())+1):
    span={}
    for c,red in reduced_images.items():
        if distance[c]<=cutoff:
            base.add_pivot(dict(red),span)
    distance_filtered[cutoff]=len(span)
distance_associated={
    d:distance_filtered[d]-distance_filtered.get(d-1,0)
    for d in distance_filtered
}
packet={
 "schema":"marici.source-reachable-exact-relation-quotient-hilbert.v1",
 "prime":P,"chart":CHART,"k_depth":KDEPTH,
 "generated_rank":len(reachable),
 "global_quotient_rank":len(global_span),
 "global_relation_kernel_rank":len(reachable)-len(global_span),
 "zero_coordinate_images":zero_images,
 "cross_grade_reduction_count":len(cross_grade_reductions),
 "cross_grade_examples":cross_grade_reductions[:20],
 "filtered_quotient_table":[
   {"k_cutoff":g[0],"occurrence_cutoff":g[1],"rank":filtered[g]}
   for g in sorted(filtered)
 ],
 "associated_rees_table":[
   {"k_pole":g[0],"occurrence_degree":g[1],"multiplicity":associated[g]}
   for g in sorted(associated)
 ],
 "associated_rees_nonnegative":all(v>=0 for v in associated.values()),
 "generator_distance_filtered_ranks":{str(d):n for d,n in distance_filtered.items()},
 "generator_distance_associated_ranks":{str(d):n for d,n in distance_associated.items()},
 "grade_table":[
   {"k_pole":g[0],"occurrence_degree":g[1],"generated":generated[g],
    "relation_kernel":relation[g],"quotient_image":quotient.get(g,0)}
   for g in sorted(generated)
 ],
 "quotient_k_occurrence_rank_one_factorization":factorizes if not cross_grade_reductions else None,
 "normalized_quotient_occurrence_coefficients":(
   [quotient[(ks[0],j)]//base_q for j in os_] if factorizes else None
 ),
 "normalized_quotient_k_coefficients":(
   [quotient[(i,os_[0])]//base_q for i in ks] if factorizes else None
 ),
 "checks":{
   "generated_rank_matches_orbit_census":len(reachable)>0,
   "rank_nullity":len(global_span)+(len(reachable)-len(global_span))==len(reachable),
   "relation_reduction_preserves_k_occurrence_grade":not cross_grade_reductions,
 },
 "passed":len(reachable)>0,
}
out=BEN/"results"/f"source-reachable-relation-quotient-hilbert-{CHART.lower()}-k{KDEPTH}-p{P}.json"
out.write_text(json.dumps(packet,indent=2)+"\n",encoding="utf-8")
print(json.dumps({
 "schema":packet["schema"],"prime":P,"chart":CHART,"k_depth":KDEPTH,
 "generated_rank":packet["generated_rank"],"global_quotient_rank":packet["global_quotient_rank"],
 "global_relation_kernel_rank":packet["global_relation_kernel_rank"],
 "zero_coordinate_images":zero_images,"cross_grade_reduction_count":len(cross_grade_reductions),
 "quotient_factorizes":packet["quotient_k_occurrence_rank_one_factorization"],
 "normalized_occurrence":packet["normalized_quotient_occurrence_coefficients"],
 "normalized_k":packet["normalized_quotient_k_coefficients"],
 "associated_rees_nonnegative":packet["associated_rees_nonnegative"],
 "generator_distance_associated_ranks":packet["generator_distance_associated_ranks"],
 "checks":packet["checks"],"passed":packet["passed"]
},indent=2))
if not packet["passed"]: raise SystemExit(1)
