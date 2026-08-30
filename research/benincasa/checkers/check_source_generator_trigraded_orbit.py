#!/usr/bin/env python3
"""Source-generator orbit and multigraded Hilbert census for the marked residue packet."""
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

jet.charts.GAMMA=jet.GAMMA
jet.charts.AMBIENT=14
jet.charts.CUTOFF=7
jet.charts.K_DEPTH=KDEPTH
pres=jet.charts.presentation(jet.FIBER,jet.POINT,jet.NAMES)
k,q=jet.source_polynomials()
kd=[{e:jet.pder(poly,a) for e,poly in k.items()} for a in range(3)]
qd=[{n:{e:jet.pder(poly,a) for e,poly in qp.items()} for n,qp in q.items()} for a in range(3)]

adj=defaultdict(set)
edge_types=Counter()
for col,label in enumerate(pres["ordered_columns"]):
    kp,*rest=label; exp=rest.pop(); levels=tuple(rest)
    for axis in range(3):
        row=jet.connection_poly(label,axis,pres,kd[axis],qd[axis])
        for target in row:
            adj[col].add(target)
            tl=pres["ordered_columns"][target]
            if tl[0]==kp+1:
                edge_types["K_raise"]+=1
            else:
                changed=[i for i,(a,b) in enumerate(zip(levels,tl[1:-1])) if b==a+1]
                edge_types[f"mark_raise_{changed[0] if len(changed)==1 else 'mixed'}"]+=1

n={e:dict(poly) for e,poly in q[jet.NUMERATOR_NAMES[0]].items()}
for e,poly in q[jet.NUMERATOR_NAMES[1]].items():
    jet.padd(n.setdefault(e,{}),poly)
base_label=(0,1,1,1,1,1)
roots=sorted({pres["columns"][(*base_label,e)] for e,poly in n.items() if poly})

distance={r:0 for r in roots}
queue=deque(roots)
while queue:
    c=queue.popleft()
    for t in sorted(adj[c]):
        if t not in distance:
            distance[t]=distance[c]+1
            queue.append(t)

by_distance=Counter(distance.values())
hilbert=Counter()
for c,d in distance.items():
    label=pres["ordered_columns"][c]
    kp=label[0]; levels=label[1:-1]; exp=label[-1]
    occurrence_degree=sum(x-1 for x in levels)
    hilbert[(kp,occurrence_degree,exp[0],exp[1])]+=1

outgoing_by_k=Counter()
outgoing_by_occ=Counter()
for c in distance:
    label=pres["ordered_columns"][c]
    for t in adj[c]:
        tl=pres["ordered_columns"][t]
        if tl[0]>label[0]: outgoing_by_k[(label[0],tl[0])]+=1
        od=sum(x-1 for x in label[1:-1]); td=sum(x-1 for x in tl[1:-1])
        if td>od: outgoing_by_occ[(od,td)]+=1

packet={
 "schema":"marici.source-generator-trigraded-orbit.v1",
 "prime":P,"chart":CHART,"k_depth":KDEPTH,
 "root_labels":[repr(pres["ordered_columns"][r]) for r in roots],
 "generator_edge_type_counts":dict(sorted(edge_types.items())),
 "reachable_rank":len(distance),
 "max_generator_distance":max(distance.values()) if distance else None,
 "distance_counts":{str(k):v for k,v in sorted(by_distance.items())},
 "hilbert_terms":[
   {"k_pole":k,"occurrence_degree":o,"fiber_degree":[a,b],"multiplicity":m}
   for (k,o,a,b),m in sorted(hilbert.items())
 ],
 "k_edge_counts":[{"from":a,"to":b,"count":n} for (a,b),n in sorted(outgoing_by_k.items())],
 "occurrence_edge_counts":[{"from":a,"to":b,"count":n} for (a,b),n in sorted(outgoing_by_occ.items())],
 "checks":{
   "roots_are_source_numerator_support":bool(roots),
   "all_reachable_labels_in_frozen_presentation":all(c<len(pres["ordered_columns"]) for c in distance),
   "generator_types_separated":edge_types["K_raise"]>0 and any(k.startswith("mark_raise_") for k in edge_types),
 },
 "passed":bool(roots) and edge_types["K_raise"]>0,
}
out=BEN/"results"/f"source-generator-trigraded-orbit-{CHART.lower()}-k{KDEPTH}-p{P}.json"
out.write_text(json.dumps(packet,indent=2)+"\n",encoding="utf-8")
print(json.dumps({
 "schema":packet["schema"],"prime":P,"chart":CHART,"k_depth":KDEPTH,
 "reachable_rank":packet["reachable_rank"],"max_generator_distance":packet["max_generator_distance"],
 "distance_counts":packet["distance_counts"],"k_edge_counts":packet["k_edge_counts"],
 "occurrence_edge_counts":packet["occurrence_edge_counts"],"hilbert_term_count":len(packet["hilbert_terms"]),
 "checks":packet["checks"],"passed":packet["passed"]
},indent=2))
if not packet["passed"]: raise SystemExit(1)
