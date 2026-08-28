#!/usr/bin/env python3
"""Contributor-facing Stratified Coherence Compiler command line."""
from __future__ import annotations
import hashlib, importlib.metadata, importlib.util, json, platform, re, subprocess, sys
from pathlib import Path

HERE=Path(__file__).resolve().parent; ROOT=HERE.parents[2]
STATE_DIR=ROOT/".ai"/"tmp"/"scc-state"
REGISTRY=json.loads((HERE/"registry.v1.json").read_text(encoding="utf-8"))
CENTRAL_CHECKS={x["id"]:x for x in REGISTRY["checks"]}

def usage():
    print("SCC — Stratified Coherence Compiler")
    print("usage: scc.py init <owner> <model-id> | import <checker> [--write] | models | dashboard [--markdown] | doctor | plan | capsule <model> | graph-packet <model|all> | validate <manifest|all> | status <model|all> | check <model|all> | explain <model|all> | impact <model> | transfers <model> | freeze <model> | challenge <model> <checker> <survives|falsifies> | watch | run <check|group> [--verbose]")

def validate_model(m):
    if "_load_error" in m: return ["invalid JSON: "+m["_load_error"]]
    errors=[]
    for k in ("id","owner","classification","stratum","inputs","checks"):
        if k not in m: errors.append("missing required field: "+k)
    if errors:return errors
    if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_.-]*",m["id"]): errors.append("id contains unsupported characters")
    if not isinstance(m["inputs"],list) or not all(isinstance(x,str) for x in m["inputs"]): errors.append("inputs must be an array of workspace-relative paths")
    if not isinstance(m["checks"],list) or not m["checks"]: errors.append("checks must be a non-empty array")
    else:
        sibling_ids={c.get("id") for c in m["checks"] if isinstance(c,dict) and c.get("id")}
        for i,c in enumerate(m["checks"]):
            if isinstance(c,str) and c not in CENTRAL_CHECKS: errors.append(f"checks[{i}] names unknown central check: {c}")
            elif isinstance(c,dict):
                if not c.get("id"): errors.append(f"checks[{i}] missing id")
                if not c.get("path"): errors.append(f"checks[{i}] missing path")
                for requirement in c.get("requires",[]):
                    if requirement in sibling_ids: errors.append(f"checks[{i}].requires names sibling check {requirement}; requires accepts Python modules only and checks already run in manifest order")
            elif not isinstance(c,str): errors.append(f"checks[{i}] must be a check id or object")
    for key in ("depends_on","consumes","provides","missing_constructors"):
        if key in m and (not isinstance(m[key],list) or not all(isinstance(x,str) for x in m[key])): errors.append(key+" must be an array of strings")
    if "next_falsifier" in m and not isinstance(m["next_falsifier"],str): errors.append("next_falsifier must be a string")
    return errors

def discover():
    records=[]
    legacy=json.loads((HERE/"models.v1.json").read_text(encoding="utf-8"))
    records += [(str(HERE/"models.v1.json"),m) for m in legacy["models"]]
    for p in sorted((ROOT/"research").glob("*/scc-models/*.json")):
        try:
            raw=json.loads(p.read_text(encoding="utf-8")); records.append((str(p),raw.get("model",raw)))
        except (OSError,json.JSONDecodeError) as e: records.append((str(p),{"_load_error":str(e)}))
    models={}; errors=[]
    for locator,raw in records:
        m=dict(raw); m["_manifest"]=locator; found=validate_model(m)
        manifest_path=Path(locator)
        if "scc-models" in manifest_path.parts:
            index=manifest_path.parts.index("scc-models")
            locus=manifest_path.parts[index-1]
            if m.get("owner","").lower()!=("marici."+locus).lower(): found.append(f"owner {m.get('owner')} does not match manifest locus {locus}")
        if found: errors.append({"manifest":locator,"errors":found}); continue
        if m["id"] in models: errors.append({"manifest":locator,"errors":["duplicate model id: "+m["id"]]}); continue
        models[m["id"]]=m
    for m in models.values():
        for dep in m.get("depends_on",[]):
            if dep not in models: errors.append({"manifest":m["_manifest"],"errors":["unknown dependency: "+dep]})
    visiting=set();visited=set()
    def visit(mid,trail):
        if mid in visiting:
            errors.append({"manifest":models[mid]["_manifest"],"errors":["dependency cycle: "+" -> ".join(trail+[mid])]});return
        if mid in visited:return
        visiting.add(mid)
        for dep in models[mid].get("depends_on",[]):
            if dep in models:visit(dep,trail+[mid])
        visiting.remove(mid);visited.add(mid)
    for mid in models:visit(mid,[])
    return models,errors

def execution_layers(models,selected_ids=None):
    remaining=set(models if selected_ids is None else selected_ids);done=set();layers=[]
    while remaining:
        layer=sorted(mid for mid in remaining if set(models[mid].get("depends_on",[]))<=done)
        if not layer:return layers,sorted(remaining)
        layers.append(layer);done.update(layer);remaining-=set(layer)
    return layers,[]

def checks_for(m): return [dict(CENTRAL_CHECKS[c]) if isinstance(c,str) else dict(c) for c in m["checks"]]
def workspace_path(raw):
    p=(ROOT/raw).resolve(); p.relative_to(ROOT.resolve()); return p
def fingerprint(m):
    raw=list(m["inputs"])+[c["path"] for c in checks_for(m)]; paths=[]; missing=[]
    for item in raw:
        try:p=workspace_path(item)
        except ValueError: missing.append(item+" (outside workspace)"); continue
        paths.append(p)
        if not p.is_file():missing.append(item)
    h=hashlib.sha256(); h.update(json.dumps({k:v for k,v in m.items() if not k.startswith("_")},sort_keys=True).encode())
    for p in sorted(set(paths)):
        if p.is_file():h.update(str(p.relative_to(ROOT)).encode()); h.update(p.read_bytes())
    return h.hexdigest(),sorted(missing)
def state_path(mid): return STATE_DIR/(re.sub(r"[^A-Za-z0-9_.-]+","-",mid)+".json")
def load_state(mid):
    p=state_path(mid); return json.loads(p.read_text(encoding="utf-8")) if p.is_file() else None
def model_status(m):
    digest,missing=fingerprint(m); prior=load_state(m["id"])
    label="missing_input" if missing else "never_checked" if prior is None else "stale" if prior["fingerprint"]!=digest else "current_checks_passed" if prior["passed"] else "current_checks_failed"
    return {"id":m["id"],"status":label,"owner":m["owner"],"classification":m["classification"],"missing":missing}

def run_checks(checks,verbose=False):
    outcomes=[]
    for c in checks:
        deps=[x for x in c.get("requires",[]) if importlib.util.find_spec(x) is None]
        if deps: outcomes.append({"id":c["id"],"status":"unavailable","missing_dependencies":deps}); break
        try:path=workspace_path(c["path"])
        except ValueError: outcomes.append({"id":c["id"],"status":"invalid_path"}); break
        done=subprocess.run([sys.executable,str(path)],cwd=ROOT,capture_output=True,text=True)
        out={"id":c["id"],"status":"passed" if done.returncode==0 else "failed","returncode":done.returncode}
        try:
            packet=json.loads(done.stdout)
            out["result"]={"passed":packet.get("passed"),"classification":packet.get("classification",packet.get("status")),"admitted_scope":packet.get("admitted_scope"),"residuals":packet.get("residuals",[]),"missing_constructors":packet.get("missing_constructors",[]),"next_falsifier":packet.get("next_falsifier",packet.get("next_gate")),"conclusion":packet.get("conclusion",packet.get("verdict"))}
            out["result"]={k:v for k,v in out["result"].items() if v not in (None,[],"")}
        except json.JSONDecodeError: out["result"]={"adapter":"exit-code-only"}
        if verbose or done.returncode: out["stdout"]=done.stdout[-4000:]; out["stderr"]=done.stderr[-4000:]
        outcomes.append(out)
        if done.returncode:break
    passed=len(outcomes)==len(checks) and all(x.get("returncode")==0 for x in outcomes)
    return outcomes,passed
def check_model(m,verbose=False):
    digest,missing=fingerprint(m)
    if missing:return {"id":m["id"],"status":"missing_input","missing":missing,"passed":False}
    outcomes,passed=run_checks(checks_for(m),verbose)
    digest,post_missing=fingerprint(m)
    if post_missing:
        return {"id":m["id"],"status":"missing_input_after_check","missing":post_missing,"passed":False,"outcomes":outcomes}
    previous=load_state(m["id"])
    prior_results=[x.get("result",{}) for x in previous.get("outcomes",[])] if previous else []
    new_results=[x.get("result",{}) for x in outcomes]
    changed=[{"check":outcomes[i]["id"],"before":prior_results[i] if i<len(prior_results) else None,"after":new_results[i]} for i in range(len(new_results)) if i>=len(prior_results) or prior_results[i]!=new_results[i]]
    record={"schema":"marici.scc.model-state.v1","id":m["id"],"fingerprint":digest,"passed":passed,"outcomes":outcomes}
    STATE_DIR.mkdir(parents=True,exist_ok=True); state_path(m["id"]).write_text(json.dumps(record,indent=2)+"\n",encoding="utf-8")
    return {"id":m["id"],"status":"checks_passed" if passed else "checks_failed","passed":passed,"outcomes":outcomes,"scientific_delta":changed}

def import_draft(raw_path):
    path=workspace_path(raw_path)
    parts=path.relative_to(ROOT).parts
    if len(parts)<4 or parts[0]!="research": raise ValueError("checker must live under research/<owner>/...")
    locus=parts[1]; stem=path.stem; mid=re.sub(r"^(check_|audit_|certify_)","",stem).replace("_","-")
    results=[]
    for candidate in (ROOT/"research"/locus/"results").glob("*.json") if (ROOT/"research"/locus/"results").is_dir() else []:
        token=mid.replace("-","")
        if token in candidate.stem.replace("-","").replace("_",""): results.append(candidate.relative_to(ROOT).as_posix())
    checker_path=path.relative_to(ROOT).as_posix()
    return {"$schema":"../../aspect/scc/model-manifest.schema.json","schema":"marici.scc.model-manifest.v1","model":{"id":mid,"owner":"marici."+locus.capitalize(),"classification":"candidate_import_requires_review","stratum":"UNRESOLVED: declare the constant-type domain before admission","inputs":[checker_path]+sorted(results),"checks":[{"id":stem,"path":checker_path,"requires":[]}],"depends_on":[],"consumes":[],"provides":[],"missing_constructors":[],"next_falsifier":"UNRESOLVED"}}

def freeze_directory(m): return ROOT/"research"/m["owner"].split(".",1)[1].lower()/"scc-freezes"
def freezes_for(m): return sorted(freeze_directory(m).glob(m["id"]+".*.json")) if freeze_directory(m).is_dir() else []
def freeze_status(m):
    digest,_=fingerprint(m); files=freezes_for(m)
    if any(p.name.endswith(digest[:16]+".json") for p in files): return "current"
    return "stale" if files else "none"
def freeze_model(m):
    digest,missing=fingerprint(m)
    if missing:return {"id":m["id"],"status":"missing_input","missing":missing,"created":False}
    payload={"schema":"marici.scc.freeze.v1","model_id":m["id"],"fingerprint":digest,"owner":m["owner"],"classification":m["classification"],"stratum":m["stratum"],"depends_on":m.get("depends_on",[]),"consumes":m.get("consumes",[]),"provides":m.get("provides",[]),"missing_constructors":m.get("missing_constructors",[]),"next_falsifier":m.get("next_falsifier"),"manifest":{k:v for k,v in m.items() if not k.startswith("_")}}
    directory=freeze_directory(m);path=directory/(m["id"]+"."+digest[:16]+".json")
    if path.exists():return {"id":m["id"],"status":"already_frozen","freeze":str(path),"created":False}
    directory.mkdir(parents=True,exist_ok=True);path.write_text(json.dumps(payload,indent=2)+"\n",encoding="utf-8")
    return {"id":m["id"],"status":"frozen","freeze":str(path),"fingerprint":digest,"created":True}

def dependency_record(name):
    available=importlib.util.find_spec(name) is not None
    try: version=importlib.metadata.version(name)
    except importlib.metadata.PackageNotFoundError: version=None
    return {"name":name,"available":available,"version":version}

def environment_capsule(m):
    digest,missing=fingerprint(m); checks=checks_for(m); deps=sorted({d for c in checks for d in c.get("requires",[])})
    checker_hashes={}
    for c in checks:
        try:p=workspace_path(c["path"]); checker_hashes[c["id"]]=hashlib.sha256(p.read_bytes()).hexdigest() if p.is_file() else None
        except ValueError:checker_hashes[c["id"]]=None
    return {"schema":"marici.scc.environment-capsule.v1","model":m["id"],"model_fingerprint":digest,"missing_inputs":missing,"python":{"executable":sys.executable,"version":platform.python_version(),"implementation":platform.python_implementation()},"platform":platform.platform(),"dependencies":[dependency_record(d) for d in deps],"checker_sha256":checker_hashes}

def main(argv):
    verbose="--verbose" in argv; write="--write" in argv; markdown="--markdown" in argv; argv=[x for x in argv if x not in ("--verbose","--write","--markdown")]; models,errors=discover()
    if not argv or argv==["help"]:usage();return 0
    if len(argv)==3 and argv[0]=="init":
        owner,mid=argv[1],argv[2]
        if not re.fullmatch(r"marici\.[A-Za-z][A-Za-z0-9_.-]*",owner): print("owner must look like marici.Name",file=sys.stderr);return 2
        if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_.-]*",mid): print("model id contains unsupported characters",file=sys.stderr);return 2
        locus=owner.split(".",1)[1].lower(); directory=ROOT/"research"/locus/"scc-models"; path=directory/(mid+".json")
        if path.exists(): print("refusing to overwrite existing manifest: "+str(path),file=sys.stderr);return 2
        draft={"$schema":"../../aspect/scc/model-manifest.schema.json","schema":"marici.scc.model-manifest.v1","model":{"id":mid,"owner":owner,"classification":"candidate","stratum":"TODO: exact constant-type domain or unresolved-stratum statement","inputs":[f"research/{locus}/TODO-input-packet.json"],"checks":[{"id":"TODO-check-id","path":f"research/{locus}/checkers/TODO_checker.py","requires":[]}]}}
        directory.mkdir(parents=True,exist_ok=True);path.write_text(json.dumps(draft,indent=2)+"\n",encoding="utf-8")
        print(json.dumps({"schema":"marici.scc.init.v1","manifest":str(path),"next":[f"edit {path}",f"python research/aspect/scc/scc.py validate {path}",f"python research/aspect/scc/scc.py check {mid}"]},indent=2));return 0
    if len(argv)==2 and argv[0]=="import":
        try:draft=import_draft(argv[1])
        except (OSError,ValueError) as e:print("cannot import checker: "+str(e),file=sys.stderr);return 2
        model=draft["model"]; locus=model["owner"].split(".",1)[1].lower(); path=ROOT/"research"/locus/"scc-models"/(model["id"]+".json")
        if write:
            if path.exists():print("refusing to overwrite existing manifest: "+str(path),file=sys.stderr);return 2
            path.parent.mkdir(parents=True,exist_ok=True);path.write_text(json.dumps(draft,indent=2)+"\n",encoding="utf-8")
        print(json.dumps({"schema":"marici.scc.import.v1","written":str(path) if write else None,"draft":draft,"unresolved":["classification","stratum","dependencies/capabilities","next_falsifier"],"next":f"rerun with --write, then validate {path}" if not write else f"edit unresolved fields, then validate {path}"},indent=2));return 0
    if argv==["models"]:
        print(json.dumps({"schema":"marici.scc.models-list.v1","models":[model_status(m) for m in models.values()],"discovery_errors":errors},indent=2));return 1 if errors else 0
    if argv==["dashboard"]:
        reverse={mid:0 for mid in models}
        for m in models.values():
            for dep in m.get("depends_on",[]): reverse[dep]=reverse.get(dep,0)+1
        rows=[]
        for m in models.values():
            s=model_status(m); rows.append({"model":m["id"],"owner":m["owner"],"scientific_state":m["classification"],"check_state":s["status"],"blockers":m.get("missing_constructors",[]),"downstream_models":reverse.get(m["id"],0),"freeze_state":freeze_status(m)})
        if markdown:
            print("| Model | Owner | Scientific state | Check state | Blockers | Downstream | Freeze |")
            print("|---|---|---|---|---|---:|---|")
            for r in rows: print(f'| {r["model"]} | {r["owner"]} | {r["scientific_state"]} | {r["check_state"]} | {"; ".join(r["blockers"]) or "-"} | {r["downstream_models"]} | {r["freeze_state"]} |')
        else: print(json.dumps({"schema":"marici.scc.dashboard.v1","models":rows,"discovery_errors":errors},indent=2))
        return 1 if errors else 0
    if argv==["doctor"]:
        dependencies=sorted({d for m in models.values() for c in checks_for(m) for d in c.get("requires",[])})
        path_issues=[]
        for m in models.values():
            _,missing=fingerprint(m)
            if missing:path_issues.append({"model":m["id"],"missing":missing})
        dep_records=[dependency_record(d) for d in dependencies]
        report={"schema":"marici.scc.doctor.v1","python":{"executable":sys.executable,"version":platform.python_version(),"implementation":platform.python_implementation()},"platform":platform.platform(),"model_count":len(models),"manifest_errors":errors,"path_issues":path_issues,"dependencies":dep_records,"healthy":not errors and not path_issues and all(d["available"] for d in dep_records)}
        print(json.dumps(report,indent=2));return 0 if report["healthy"] else 1
    if argv==["plan"]:
        stale=[mid for mid,m in models.items() if model_status(m)["status"] in ("stale","never_checked")]
        needed=set(stale)
        queue=list(stale)
        while queue:
            mid=queue.pop()
            for dep in models[mid].get("depends_on",[]):
                if dep not in needed:needed.add(dep);queue.append(dep)
        layers,blocked=execution_layers(models,needed)
        report={"schema":"marici.scc.plan.v1","stale_models":sorted(stale),"execution_layers":layers,"parallel_within_layer":True,"blocked":blocked,"passed":not blocked and not errors}
        print(json.dumps(report,indent=2));return 0 if report["passed"] else 1
    if len(argv)==2 and argv[0]=="capsule":
        target=models.get(argv[1])
        if not target:print("unknown SCC model: "+argv[1],file=sys.stderr);return 2
        print(json.dumps(environment_capsule(target),indent=2));return 0
    if len(argv)==2 and argv[0]=="graph-packet":
        selected=list(models.values()) if argv[1]=="all" else [models.get(argv[1])]
        if selected==[None]:print("unknown SCC model: "+argv[1],file=sys.stderr);return 2
        queue=list(selected);known={m["id"] for m in selected}
        while queue:
            current=queue.pop()
            for dep in current.get("depends_on",[]):
                if dep in models and dep not in known:known.add(dep);selected.append(models[dep]);queue.append(models[dep])
        selected_ids={m["id"] for m in selected};ops=[]
        for m in selected:ops.append({"op":"entity.declare","local_ref":"model-"+m["id"],"kind":"marici.scc:model","title":m["id"],"owner":m["owner"],"classification":m["classification"],"stratum":m["stratum"],"status":model_status(m)["status"]})
        for m in selected:
            for dep in m.get("depends_on",[]):
                relation={"op":"relation.declare","relation_type":"marici.scc:depends_on","source_ref":"model-"+m["id"]}
                relation["target_ref"]="model-"+dep
                ops.append(relation)
        print(json.dumps({"schema":"marici.scc.graph-packet.v1","authority":"none_dry_run_only","actor":"OWNER_REVIEW_REQUIRED","authority_basis":{"kind":"owner_review_required"},"operations":ops},indent=2));return 0
    if len(argv)==2 and argv[0]=="validate":
        if argv[1]=="all":report={"schema":"marici.scc.validation.v1","valid_models":sorted(models),"errors":errors,"passed":not errors}
        else:
            p=Path(argv[1]).resolve()
            try:raw=json.loads(p.read_text(encoding="utf-8")); found=validate_model(raw.get("model",raw))
            except (OSError,json.JSONDecodeError) as e:found=[str(e)]
            report={"schema":"marici.scc.validation.v1","manifest":str(p),"errors":found,"passed":not found}
        print(json.dumps(report,indent=2));return 0 if report["passed"] else 1
    if len(argv)==2 and argv[0] in ("status","check","explain"):
        selected=list(models.values()) if argv[1]=="all" else [models.get(argv[1])]
        if selected==[None]:print(f"unknown SCC model: {argv[1]}; run `scc.py models`",file=sys.stderr);return 2
        if argv[0]=="status": print(json.dumps({"schema":"marici.scc.status.v1","models":[model_status(m) for m in selected]},indent=2));return 0
        if argv[0]=="explain":
            reports=[{**model_status(m),"stratum":m["stratum"],"checks":[c["id"] for c in checks_for(m)],"manifest":m["_manifest"]} for m in selected]
            print(json.dumps({"schema":"marici.scc.explain.v1","models":reports},indent=2));return 0
        reports=[check_model(m,verbose) for m in selected]; passed=all(r["passed"] for r in reports)
        print(json.dumps({"schema":"marici.scc.check.v1","models":reports,"passed":passed},indent=2));return 0 if passed else 1
    if len(argv)==2 and argv[0]=="impact":
        if argv[1] not in models:print("unknown SCC model: "+argv[1],file=sys.stderr);return 2
        reverse={mid:[] for mid in models}
        for mid,m in models.items():
            for dep in m.get("depends_on",[]): reverse.setdefault(dep,[]).append(mid)
        seen=set(); frontier=[argv[1]]; layers=[]
        while frontier:
            nxt=sorted({child for parent in frontier for child in reverse.get(parent,[]) if child not in seen})
            if not nxt:break
            seen.update(nxt);layers.append(nxt);frontier=nxt
        print(json.dumps({"schema":"marici.scc.impact.v1","changed_model":argv[1],"downstream_layers":layers,"recheck_order":[argv[1]]+[x for layer in layers for x in layer]},indent=2));return 0
    if len(argv)==2 and argv[0]=="transfers":
        target=models.get(argv[1])
        if not target:print("unknown SCC model: "+argv[1],file=sys.stderr);return 2
        needs=list(dict.fromkeys(target.get("missing_constructors",[])+target.get("consumes",[]))); candidates=[]
        for mid,m in models.items():
            if mid==target["id"]:continue
            for need in needs:
                nt=set(re.findall(r"[a-z0-9]+",need.lower()))
                for capability in m.get("provides",[]):
                    ct=set(re.findall(r"[a-z0-9]+",capability.lower())); score=len(nt&ct)
                    if need==capability or score>=2: candidates.append({"need":need,"provider":mid,"capability":capability,"score":"exact" if need==capability else score})
        candidates.sort(key=lambda x:(x["score"]=="exact",x["score"] if isinstance(x["score"],int) else 999),reverse=True)
        print(json.dumps({"schema":"marici.scc.transfers.v1","model":target["id"],"needs":needs,"candidates":candidates},indent=2));return 0
    if len(argv)==2 and argv[0]=="freeze":
        target=models.get(argv[1])
        if not target:print("unknown SCC model: "+argv[1],file=sys.stderr);return 2
        report=freeze_model(target);print(json.dumps({"schema":"marici.scc.freeze-result.v1",**report},indent=2));return 0 if report["status"] in ("frozen","already_frozen") else 1
    if len(argv)==4 and argv[0]=="challenge":
        target=models.get(argv[1]); meaning=argv[3]
        if not target:print("unknown SCC model: "+argv[1],file=sys.stderr);return 2
        if meaning not in ("survives","falsifies"):print("zero-meaning must be survives or falsifies",file=sys.stderr);return 2
        digest,missing=fingerprint(target); frozen=[p for p in freezes_for(target) if p.name.endswith(digest[:16]+".json")]
        if missing:print(json.dumps({"schema":"marici.scc.challenge.v1","status":"missing_input","missing":missing},indent=2));return 1
        if not frozen:print(json.dumps({"schema":"marici.scc.challenge.v1","status":"baseline_not_frozen_or_stale","current_fingerprint":digest},indent=2));return 1
        checker={"id":Path(argv[2]).stem,"path":argv[2],"requires":[]}; outcomes,passed=run_checks([checker],verbose)
        effect=meaning if passed else ("falsifies" if meaning=="survives" else "survives")
        report={"schema":"marici.scc.challenge.v1","model":target["id"],"freeze":str(frozen[-1]),"baseline_fingerprint":digest,"zero_means":meaning,"outcomes":outcomes,"claim_effect":effect}
        directory=STATE_DIR/"challenges";directory.mkdir(parents=True,exist_ok=True);key=hashlib.sha256(json.dumps(report,sort_keys=True).encode()).hexdigest()[:16];(directory/(target["id"]+"."+key+".json")).write_text(json.dumps(report,indent=2)+"\n",encoding="utf-8")
        print(json.dumps(report,indent=2));return 0
    if argv==["watch"]:
        selected=[m for m in models.values() if model_status(m)["status"] in ("stale","never_checked")]
        reports=[check_model(m,verbose) for m in selected];passed=all(r["passed"] for r in reports)
        print(json.dumps({"schema":"marici.scc.watch.v1","rechecked":reports,"passed":passed},indent=2));return 0 if passed else 1
    if len(argv)==2 and argv[0]=="run":
        ids=REGISTRY.get("groups",{}).get(argv[1],[argv[1]]);unknown=[x for x in ids if x not in CENTRAL_CHECKS]
        if unknown:print("unknown SCC check: "+", ".join(unknown),file=sys.stderr);return 2
        outcomes,passed=run_checks([CENTRAL_CHECKS[x] for x in ids],verbose)
        print(json.dumps({"schema":"marici.scc.run.v1","target":argv[1],"outcomes":outcomes,"passed":passed},indent=2));return 0 if passed else 1
    usage();return 2
if __name__=="__main__":raise SystemExit(main(sys.argv[1:]))
