"""Finite categorical coherence compilation for SCC.

The compiler manipulates declared maps and obligations. It assigns no causal or
temporal meaning to objects or arrows and does not certify undeclared physics.
"""
from __future__ import annotations
from collections import defaultdict, deque
import copy

SUPPORTED_HIGHER_STATES={"verified","falsified","unsupported"}
FIBER_SLOTS={"named_constructor_actions","observers","viewing_forms","authority","completion_topology","instrument_backaction"}

def _index(items): return {x["id"]:x for x in items}

def validate_diagram(d):
    errors=[]
    for key in ("id","objects","arrows","cells","obstructions","claims"):
        if key not in d: errors.append("missing "+key)
    if errors:return errors
    objects=_index(d["objects"]); arrows=_index(d["arrows"])
    if len(objects)!=len(d["objects"]):errors.append("duplicate object id")
    if len(arrows)!=len(d["arrows"]):errors.append("duplicate arrow id")
    for a in d["arrows"]:
        if a.get("source") not in objects or a.get("target") not in objects:errors.append("arrow endpoint missing: "+a["id"])
    for cell in d["cells"]:
        for route in cell.get("routes",[]):
            current=None
            for aid in route:
                if aid not in arrows:errors.append("cell arrow missing: "+cell["id"]+"/"+aid);break
                a=arrows[aid]
                if current is not None and a["source"]!=current:errors.append("noncomposable route: "+cell["id"]);break
                current=a["target"]
    for f in d.get("fibers",[]):
        slots=set(f.get("comparison_slots",[]))
        if slots!=FIBER_SLOTS:errors.append("fiber slots incomplete: "+f["id"])
    for h in d.get("higher_coherence",[]):
        if h.get("state") not in SUPPORTED_HIGHER_STATES:errors.append("invalid higher coherence state: "+h.get("id","?"))
        if h.get("state")=="verified" and not h.get("witness"):errors.append("verified higher coherence lacks witness: "+h["id"])
    return errors

def compile_cells(d):
    arrows=_index(d["arrows"]);out=[]
    for cell in d["cells"]:
        routes=[]
        for route in cell["routes"]:
            routes.append({"arrows":route,"composite":tuple(arrows[a].get("map_token",a) for a in route)})
        residuals=[{"left":routes[0]["composite"],"right":r["composite"],"zero":routes[0]["composite"]==r["composite"]} for r in routes[1:]]
        passed=all(x["zero"] for x in residuals) if residuals else False
        out.append({"id":cell["id"],"kind":cell.get("kind","commutation"),"routes":routes,"residuals":residuals,"passed":passed,"threshold":cell.get("threshold","exact_zero")})
    return out

def compile_fibers(d):
    out=[]
    for f in d.get("fibers",[]):
        comparisons=[]
        for pair in f.get("pairs",[]):
            slot_results=pair.get("slot_results",{})
            complete=set(slot_results)==FIBER_SLOTS
            all_pass=complete and all(slot_results.values())
            invertible=pair.get("invertible",False)
            comparisons.append({"left":pair["left"],"right":pair["right"],"same_profile":pair.get("same_profile",False),"slot_complete":complete,"verified_equivalent":all_pass and invertible,"first_failed_slot":next((s for s in f["comparison_slots"] if not slot_results.get(s,False)),None)})
        out.append({"id":f["id"],"profile":f["profile"],"comparisons":comparisons,"groupoid_arrows":[[p["left"],p["right"]] for p in comparisons if p["verified_equivalent"]]})
    return out

def obstruction_cones(d,failed_cells):
    edges=defaultdict(list)
    for edge in d.get("impact_edges",[]):edges[edge["from"]].append(edge["to"])
    cones={}
    for root in failed_cells:
        seen=set();q=deque([root])
        while q:
            x=q.popleft()
            for y in edges[x]:
                if y not in seen:seen.add(y);q.append(y)
        cones[root]=sorted(seen)
    return cones

def synthesize_hostiles(d):
    hostiles=[]
    for cell in d["cells"]:
        hostiles.append({"id":"delete_"+cell["id"],"mutation":"delete_cell","target":cell["id"],"expected_first_failure":cell["id"]})
    for f in d.get("fibers",[]):
        for p in f.get("pairs",[]):
            if p.get("same_profile") and not (p.get("invertible") and all(p.get("slot_results",{}).values())):
                hostiles.append({"id":"collapse_"+p["left"]+"_"+p["right"],"mutation":"promote_same_profile_to_equivalence","target":f["id"],"expected_first_failure":"realization_fiber_equivalence"})
    return hostiles

def promotions(d,cell_results,fiber_results):
    passed_cells={x["id"] for x in cell_results if x["passed"]}
    equivalent={(p["left"],p["right"]) for f in fiber_results for p in f["comparisons"] if p["verified_equivalent"]}
    out=[]
    for p in d.get("promotions",[]):
        missing_cells=sorted(set(p.get("requires_cells",[]))-passed_cells)
        missing_fibers=[x for x in p.get("requires_equivalences",[]) if tuple(x) not in equivalent]
        missing_evidence=[x for x in p.get("evidence",[]) if not x.get("locator") or x.get("status")!="verified"]
        out.append({"id":p["id"],"admitted":not missing_cells and not missing_fibers and not missing_evidence,"missing_cells":missing_cells,"missing_equivalences":missing_fibers,"missing_evidence":missing_evidence})
    return out

def inverse_design(d,claim_id):
    claims=_index(d["claims"])
    if claim_id not in claims:return {"claim":claim_id,"status":"unknown_claim"}
    claim=claims[claim_id]; required=set(claim.get("requires",[])); available=set(d.get("available_witnesses",[])); missing=sorted(required-available)
    experiments=[]
    for e in d.get("experiments",[]):
        separates=sorted(set(e.get("separates",[]))&set(missing));
        if separates:experiments.append({"id":e["id"],"separates":separates,"gain":len(separates),"preregistered_threshold":e.get("preregistered_threshold")})
    experiments.sort(key=lambda x:(-x["gain"],x["id"]))
    return {"claim":claim_id,"status":"admitted" if not missing else "missing_witnesses","missing":missing,"ranked_experiments":experiments}

def compile_functors(d):
    out=[]
    for f in d.get("functors",[]):
        mapped_objects=set(f.get("object_map",{}));mapped_arrows=set(f.get("arrow_map",{}));source_objects=set(f.get("source_objects",[]));source_arrows=set(f.get("source_arrows",[]))
        preserves=all(f.get("preserves",{}).get(k,False) for k in ("identity","composition","declared_cells","authority"))
        out.append({"id":f["id"],"total_on_declared_source":mapped_objects==source_objects and mapped_arrows==source_arrows,"structure_preserving":preserves,"transfer_admitted":mapped_objects==source_objects and mapped_arrows==source_arrows and preserves})
    return out

def compile_diagram(d):
    errors=validate_diagram(d)
    if errors:return {"schema":"marici.scc.categorical-compilation.v1","diagram":d.get("id"),"errors":errors,"passed":False}
    cells=compile_cells(d);fibers=compile_fibers(d);failed=[x["id"] for x in cells if not x["passed"]]
    higher=[{"id":x["id"],"degree":x["degree"],"state":x["state"],"admitted":x["state"]=="verified" and bool(x.get("witness"))} for x in d.get("higher_coherence",[])]
    return {"schema":"marici.scc.categorical-compilation.v1","diagram":d["id"],"errors":[],"cells":cells,"fibers":fibers,"obstruction_cones":obstruction_cones(d,failed),"hostiles":synthesize_hostiles(d),"higher_coherence":higher,"promotions":promotions(d,cells,fibers),"functors":compile_functors(d),"inverse_design":{c["id"]:inverse_design(d,c["id"]) for c in d["claims"]},"passed":not failed and all(x["state"]!="falsified" for x in higher)}
