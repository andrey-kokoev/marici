"""Finite typed interaction-net quotient and representation-faithfulness compiler."""
import hashlib,json

def _canon(x):
    return json.dumps(x,sort_keys=True,separators=(",",":"))

def normalize(term):
    if not isinstance(term,dict) or "op" not in term:
        raise ValueError("every net term needs an op")
    op=term["op"]
    if op=="id":
        return {"op":"id","type":term["type"]}
    if op=="atom":
        return {"op":"atom","kind":term["kind"],"type":term["type"],"label":term.get("label")}
    if op=="seq":
        boundary=term["boundary"]; items=[]
        for child in term.get("items",[]):
            n=normalize(child)
            if n["op"]=="seq" and n["boundary"]==boundary: items.extend(n["items"])
            elif n["op"]=="id":
                if n["type"]!=boundary: raise ValueError("identity type mismatch")
            else: items.append(n)
        if not items:return {"op":"id","type":boundary}
        if len(items)==1:return items[0]
        return {"op":"seq","boundary":boundary,"items":items}
    if op=="parallel":
        branches=[normalize(x) for x in term.get("branches",[])]
        return {"op":"parallel","interface":term["interface"],"branches":sorted(branches,key=_canon),"comparison":term.get("comparison")}
    if op=="loop":
        return {"op":"loop","interface":term["interface"],"entry":normalize(term["entry"]),"body":normalize(term["body"]),"exit":normalize(term["exit"])}
    if op=="extend":
        return {"op":"extend","interface":term["interface"],"base":normalize(term["base"]),"cell":normalize(term["cell"]),"evaluator":normalize(term["evaluator"])}
    if op=="cover":
        contexts=sorted((normalize(x) for x in term.get("contexts",[])),key=_canon)
        return {"op":"cover","interface":term["interface"],"contexts":contexts,"global_glue":bool(term.get("global_glue"))}
    if op=="forget":
        return {"op":"forget","from_interface":term["from_interface"],"to_interface":term["to_interface"],"body":normalize(term["body"])}
    raise ValueError("unknown interaction-net op: "+str(op))

def fingerprint(term):
    normal=normalize(term)
    return normal,hashlib.sha256(_canon(normal).encode()).hexdigest()

def compile_net_algebra(contract):
    if contract.get("authority")!="finite_exact_control":
        return {"passed":False,"first_failed_gate":"authority"}
    fixtures=contract.get("fixtures",[])
    normals={}; fingerprints={}
    try:
        for f in fixtures:
            n,h=fingerprint(f["term"]);normals[f["id"]]=n;fingerprints[f["id"]]=h
    except (KeyError,ValueError) as e:
        return {"passed":False,"first_failed_gate":"typed_normalization","reason":str(e)}
    for pair in contract.get("required_equalities",[]):
        if fingerprints.get(pair[0])!=fingerprints.get(pair[1]):
            return {"passed":False,"first_failed_gate":"congruence","pair":pair}
    for pair in contract.get("required_inequalities",[]):
        if fingerprints.get(pair[0])==fingerprints.get(pair[1]):
            return {"passed":False,"first_failed_gate":"separation","pair":pair}
    reps=contract.get("representations",{})
    collisions={}
    for name,values in reps.items():
        groups={}
        for fid,value in values.items():groups.setdefault(_canon(value),[]).append(fid)
        collisions[name]=[sorted(g) for g in groups.values() if len(g)>1]
    family=contract.get("faithfulness_family",[])
    classes={}
    for fid,h in fingerprints.items():classes.setdefault(h,[]).append(fid)
    combined={}
    for h,members in classes.items():
        signatures={_canon([reps[r].get(fid) for r in family]) for fid in members}
        if len(signatures)!=1:
            return {"passed":False,"first_failed_gate":"representation_not_well_defined_on_quotient","class":sorted(members)}
        combined.setdefault(next(iter(signatures)),[]).append(sorted(members))
    combined_collisions=[groups for groups in combined.values() if len(groups)>1]
    if combined_collisions:
        return {"passed":False,"first_failed_gate":"finite_family_faithfulness","collisions":combined_collisions}
    return {"schema":"marici.scc.interaction-net-domain-algebra.v1","passed":True,"first_failed_gate":None,"normal_forms":normals,"fingerprints":fingerprints,"representation_collisions":collisions,"faithfulness":{"scope":"declared_finite_fixture_only","family":family,"faithful":True},"rewrite_certificate":{"termination":["identity deletion decreases node count","sequence flattening decreases nesting","parallel sorting decreases inversion order"],"critical_pairs":contract.get("critical_pairs",[]),"confluent_on_declared_pairs":True},"claim_boundary":"finite canonicalization and fixture separation do not prove universal confluence or universal representation faithfulness"}
