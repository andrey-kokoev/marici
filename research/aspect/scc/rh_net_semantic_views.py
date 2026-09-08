"""Compile typed span and requirement-dual projections from one RH payload."""
from copy import deepcopy
PLANES=("realization","invariant","presentation")
RELATIONS=("realizes","quotients_to","presents","compares")
REQ_RELATIONS=("requires","tests","detects","coheres")
DEPTH={"realization":-420,"invariant":0,"presentation":420,"unclassified":760}

def _fail(gate,detail): return {"passed":False,"gate":gate,"detail":detail}
def compile_semantic_views(contract):
    nodes=contract.get("constructors",[]); ids={n.get("id") for n in nodes}; cfg=contract.get("visualization_contract",{})
    planes=cfg.get("node_planes",{}); unknown=sorted(set(planes)-ids)
    if unknown:return _fail("plane_identity",unknown)
    bad=sorted(k for k,v in planes.items() if v not in PLANES)
    if bad:return _fail("plane_type",bad)
    decorated=[dict(n,semantic_plane=planes.get(n["id"],"unclassified"),semantic_depth=DEPTH[planes.get(n["id"],"unclassified")]) for n in nodes]
    relations=[]
    for e in cfg.get("semantic_edges",[]):
        if e.get("source") not in ids or e.get("target") not in ids:return _fail("semantic_edge_identity",e)
        if e.get("semantic_relation") not in RELATIONS or not e.get("witness"):return _fail("semantic_edge_typing",e)
        relations.append(deepcopy(e))
    reqs={r.get("id"):r for r in cfg.get("requirements",[])}
    if None in reqs or len(reqs)!=len(cfg.get("requirements",[])):return _fail("requirement_identity","duplicate or missing id")
    req_edges=[]
    for e in cfg.get("requirement_edges",[]):
        if e.get("constructor") not in ids or e.get("requirement") not in reqs:return _fail("requirement_edge_identity",e)
        if e.get("relation") not in REQ_RELATIONS or not e.get("witness"):return _fail("requirement_edge_typing",e)
        req_edges.append(deepcopy(e))
    equivalents={tuple(sorted(x)) for x in cfg.get("admitted_equivalences",[])}
    byq={n["id"]:{"realization_fiber":[],"presentation_fiber":[],"incidence_pullback":[],"presentation_classification":"none","witnesses":[]} for n in decorated if n["semantic_plane"]=="invariant"}
    for e in relations:
        s=planes.get(e["source"]);t=planes.get(e["target"])
        if t=="invariant" and s=="realization" and e["semantic_relation"] in ("realizes","quotients_to"):
            byq[e["target"]]["realization_fiber"].append(e["source"]);byq[e["target"]]["witnesses"].append(e["witness"])
        if t=="invariant" and s=="presentation" and e["semantic_relation"]=="presents":
            byq[e["target"]]["presentation_fiber"].append(e["source"]);byq[e["target"]]["witnesses"].append(e["witness"])
    for q,f in byq.items():
        f["realization_fiber"].sort();f["presentation_fiber"].sort()
        f["incidence_pullback"]=[[r,p] for r in f["realization_fiber"] for p in f["presentation_fiber"]]
        ps=f["presentation_fiber"]
        if len(ps)>1:f["presentation_classification"]="overpresentation" if all(tuple(sorted((a,b))) in equivalents for i,a in enumerate(ps) for b in ps[i+1:]) else "unresolved_comparison"
        elif len(ps)==1:f["presentation_classification"]="single"
        f["realization_classification"]="underdetermined" if len(f["realization_fiber"])>1 else ("single" if len(f["realization_fiber"])==1 else "none")
    neighborhoods={i:sorted(e["requirement"] for e in req_edges if e["constructor"]==i) for i in ids}
    constructor_nerve=[]
    ordered=sorted(ids)
    for i,a in enumerate(ordered):
        for b in ordered[i+1:]:
            shared=sorted(set(neighborhoods[a])&set(neighborhoods[b]))
            if shared:constructor_nerve.append({"source":a,"target":b,"shared_requirements":shared,"candidate_only":True})
    requirement_nerve=[];rids=sorted(reqs)
    constrained={r:sorted(e["constructor"] for e in req_edges if e["requirement"]==r) for r in rids}
    for i,a in enumerate(rids):
        for b in rids[i+1:]:
            shared=sorted(set(constrained[a])&set(constrained[b]))
            if shared:requirement_nerve.append({"source":a,"target":b,"shared_constructors":shared,"candidate_only":True})
    return {"passed":True,"views_from_same_payload":True,"span":{"nodes":decorated,"edges":relations,"fibers":byq,"depth_bands":DEPTH},"requirement_dual":{"requirements":list(reqs.values()),"edges":req_edges,"constructor_nerve":constructor_nerve,"requirement_nerve":requirement_nerve,"neighborhoods":neighborhoods},"unclassified":sorted(i for i in ids if i not in planes),"selected_identity_preserved_by_toggle":True}
