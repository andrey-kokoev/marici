"""SCC maintenance tools over materialized repository evidence only."""
from fractions import Fraction
from pathlib import Path
import hashlib
from categorical_apparatus_compiler import LAYERS,PROFILE,compile_categorical_apparatus
from categorical_residual_compiler import KINDS,compile_categorical_residual
from explanation_debugger import CHAINS,debug_explanation,propagate_comparison_budget

VALID_PROFILE=(True,False,"not_constructed")
AXES=("coefficient_type","quotient_convention","dimension","source_order","target_order","completion_type","readout_type","bound_type")

def migrate(c):
 if not isinstance(c,dict):raise ValueError("legacy contract must be an object")
 layers={k:{"status":"not_constructed"} for k in LAYERS};residuals=[]
 prior=None
 for old,new in (("diagram","base_computad"),("cells","cells_and_laws"),("completion","partial_completion")):
  if c.get(old):
   locator=c.get(old+"_locator")
   if locator:
    spec={"status":"constructed","artifact_locator":locator}
    if prior:spec["depends_on"]=[prior]
    layers[new]=spec;prior=new
   else:residuals.append({"field":old,"reason":"legacy presence lacks artifact locator"})
 profile={k:"not_constructed" for k in PROFILE}
 cert=c.get("observational_rank_certificate")
 if isinstance(cert,dict) and cert.get("locator"):profile["certificate_backend"]=True
 out={"schema":"marici.scc.categorical-apparatus.v1","migration":"legacy_no_inference","layers":layers,"conformance":profile,"migration_residuals":residuals,"legacy_source":c}
 out["compiler_check"]=compile_categorical_apparatus(out);return out

def batch_audit(c):
 compilers={"categorical_apparatus":compile_categorical_apparatus,"categorical_residual":compile_categorical_residual,"explanation_debug":debug_explanation};items=[]
 for i,x in enumerate(c.get("contracts",[])):
  if not isinstance(x,dict) or "id" not in x or not isinstance(x.get("contract"),dict) or x.get("kind","categorical_apparatus") not in compilers:items.append({"id":x.get("id",i) if isinstance(x,dict) else i,"passed":False,"first_failed_gate":"batch_item"});continue
  kind=x.get("kind","categorical_apparatus");r=compilers[kind](x["contract"]);items.append({"id":x["id"],"kind":kind,"passed":r["passed"],"first_failed_gate":r.get("first_failed_gate"),"conformance":r.get("conformance",{})})
 return {"schema":"marici.scc.batch-conformance.v2","items":items,"passed":bool(items) and all(x["passed"] for x in items)}

def profile_diff(c):
 a,b=c["before"],c["after"];rank={"not_constructed":0,False:1,True:2};changes=[];invalid=[]
 for k in PROFILE:
  x,y=a.get(k,"not_constructed"),b.get(k,"not_constructed")
  if x not in VALID_PROFILE or y not in VALID_PROFILE:invalid.append(k);continue
  if x!=y:changes.append({"coordinate":k,"before":x,"after":y,"change":"gain" if rank[y]>rank[x] else "regression"})
 return {"schema":"marici.scc.profile-diff.v1","passed":not invalid,"changes":changes,"invalid_coordinates":invalid,"scalar_score":None}

def promotion_lint(c):
 findings=[];rules=(("literal_zero","literal_zero_witness","quotient zero cannot promote to literal zero"),("strict_selection","selection_invariance_witness","filler existence cannot promote to strict selection"),("identity","univalent_completion_witness","weak equivalence cannot promote to identity"),("observational_quotient","readout_witness","completion cannot promote to observation"),("global_complete","global_promotion_theorem","bounded completeness cannot promote globally"),("physical_backend","physical_interface_witness","mathematical realization cannot promote to physics"))
 def walk(x,path):
  if isinstance(x,dict):
   for claim,witness,reason in rules:
    if x.get(claim) is True and not x.get(witness):findings.append({"path":path,"claim":claim,"missing_witness":witness,"reason":reason})
   for k,v in x.items():walk(v,path+"/"+str(k))
  elif isinstance(x,list):
   for i,v in enumerate(x):walk(v,path+"/"+str(i))
 walk(c,"");return {"schema":"marici.scc.promotion-lint.v2","passed":not findings,"findings":findings}

def provenance_lock(c,root="."):
 base=Path(root).resolve();out=[];errors=[]
 for raw in c.get("artifacts",[]):
  p=(base/raw).resolve()
  try:p.relative_to(base)
  except ValueError:errors.append({"path":raw,"reason":"outside root"});continue
  if not p.is_file():errors.append({"path":raw,"reason":"not a materialized regular file"});continue
  data=p.read_bytes();entry={"path":raw,"sha256":hashlib.sha256(data).hexdigest(),"size":len(data),"schema_identity":None}
  if p.suffix.lower()==".json":
   try:
    import json as _json;obj=_json.loads(data);entry["schema_identity"]=obj.get("$id") or obj.get("schema") if isinstance(obj,dict) else None
   except (UnicodeDecodeError,_json.JSONDecodeError):errors.append({"path":raw,"reason":"invalid JSON"});continue
  out.append(entry)
 return {"schema":"marici.scc.provenance-lock.v1","passed":not errors and bool(out),"artifacts":out,"errors":errors}

def hostile_replay(c,compilers):
 out=[]
 for i,case in enumerate(c.get("cases",[])):
  compiler=compilers.get(case.get("compiler"))
  if compiler is None:out.append({"id":case.get("id",i),"preserved":False,"reason":"unknown compiler"});continue
  try:r=compiler(case.get("contract",{}));actual=bool(r["passed"])
  except (KeyError,TypeError,ValueError) as e:out.append({"id":case.get("id",i),"preserved":False,"reason":str(e)});continue
  expected=case.get("expected_pass");out.append({"id":case.get("id",i),"expected":expected,"actual":actual,"preserved":isinstance(expected,bool) and actual==expected})
 return {"schema":"marici.scc.hostile-replay.v1","passed":bool(out) and all(x["preserved"] for x in out),"cases":out}

def dependency_view(c):
 r=debug_explanation(c);chain=CHAINS.get(c.get("target_claim"),[]);sup=c.get("supplied",{})
 nodes=[{"id":x,"state":"supplied" if sup.get(x) else "missing"} for x in chain];edges=[{"source":chain[i],"target":chain[i+1]} for i in range(len(chain)-1)]
 dot="digraph explanation {\n"+"".join(f'  "{n["id"]}" [label="{n["id"]}\\n{n["state"]}"];\n' for n in nodes)+"".join(f'  "{e["source"]}" -> "{e["target"]}";\n' for e in edges)+"}"
 return {"schema":"marici.scc.dependency-view.v2","passed":bool(chain),"nodes":nodes,"edges":edges,"dot":dot,"first_missing":r.get("first_missing_arrow"),"retracted":r.get("retract_downstream",[])}

def dead_claims(c):
 supplied={k for k,v in c.get("supplied",{}).items() if v};claims=c.get("claims",{});live=set(supplied);changed=True
 while changed:
  changed=False
  for claim,reqs in claims.items():
   if claim not in live and all(x in live for x in reqs):live.add(claim);changed=True
 dead=[]
 for claim,reqs in claims.items():
  if claim not in live:dead.append({"claim":claim,"missing":[x for x in reqs if x not in live]})
 return {"schema":"marici.scc.dead-claims.v1","passed":not dead,"live_claims":sorted(set(claims)&live),"dead_claims":dead}

def monotonicity(c):
 violations=[];less=c.get("less_evidence",{});more=c.get("more_evidence",{})
 if all(k in more and more[k]==v for k,v in less.items()) and c.get("less_strength",0)>c.get("more_strength",0):violations.append("evidence_removal_strengthened")
 try:
  if Fraction(str(c.get("higher_cost",0)))>Fraction(str(c.get("lower_cost",0))) and Fraction(str(c.get("higher_residual",0)))>Fraction(str(c.get("lower_residual",0))):violations.append("cost_increase_improved_margin")
 except (ValueError,ZeroDivisionError):violations.append("malformed_numeric_axis")
 if c.get("less_constructed_completeness") is True and c.get("more_constructed_completeness") is not True:violations.append("removing_construction_created_completeness")
 return {"schema":"marici.scc.monotonicity.v1","passed":not violations,"violations":violations}

def fixtures(_c=None):
 f={"categorical_apparatus":{"passing":{"layers":{},"conformance":{}},"failing":{"layers":{"base_computad":{"status":"constructed"}}}},"categorical_residual":{"passing":{"residual":{"kind":"presentation_residual","codomain":"P"}},"failing":{"residual":{"kind":"unknown","codomain":"P"}}},"explanation_debug":{"passing":{"target_claim":"identity_from_equivalence","supplied":{"weak_equivalence_class":True,"localization":True,"univalent_completion":True}},"failing":{"target_claim":"identity_from_equivalence","supplied":{}}}}
 checks={"categorical_apparatus":(compile_categorical_apparatus(f["categorical_apparatus"]["passing"])["passed"] and not compile_categorical_apparatus(f["categorical_apparatus"]["failing"])["passed"]),"categorical_residual":(compile_categorical_residual(f["categorical_residual"]["passing"])["passed"] and not compile_categorical_residual(f["categorical_residual"]["failing"])["passed"]),"explanation_debug":(debug_explanation(f["explanation_debug"]["passing"])["passed"] and not debug_explanation(f["explanation_debug"]["failing"])["passed"])}
 return {"schema":"marici.scc.fixtures.v1","passed":all(checks.values()),"fixtures":f,"self_checks":checks}

def schema_compat(c):
 old,new=c["old"],c["new"];op=set(old.get("properties",{}));np=set(new.get("properties",{}));orr=set(old.get("required",[]));nrr=set(new.get("required",[]));type_changes=[]
 if isinstance(old.get("properties"),dict) and isinstance(new.get("properties"),dict):
  for k in op&np:
   if old["properties"][k].get("type")!=new["properties"][k].get("type"):type_changes.append(k)
 removed=sorted(op-np);new_required=sorted(nrr-orr)
 return {"schema":"marici.scc.schema-compat.v1","added":sorted(np-op),"removed":removed,"new_required":new_required,"type_changes":sorted(type_changes),"compatible":not removed and not new_required and not type_changes}

def normalize(c):
 r=c["result"]
 return {"schema":"marici.scc.result-envelope.v1","operation_succeeded":True,"subject_passed":bool(r.get("passed")),"compiler":c.get("compiler"),"first_failed_gate":r.get("first_failed_gate"),"minimal_obstruction":r.get("minimal_obstruction",[]),"evidence_locators":c.get("evidence_locators",[]),"downstream_retractions":r.get("retract_downstream",[]),"claim_boundary":r.get("claim_boundary"),"verification":c.get("verification",{})}

def residual_census(c):
 counts={k:0 for k in KINDS};unclassified=[];invalid=[]
 for i,x in enumerate(c.get("residuals",[])):
  ident=x.get("id",i);r=compile_categorical_residual({"residual":x})
  if r["passed"]:counts[x["kind"]]+=1
  elif x.get("kind") in counts:invalid.append({"id":ident,"gate":r["first_failed_gate"]})
  else:unclassified.append(ident)
 return {"schema":"marici.scc.residual-census.v1","passed":not unclassified and not invalid,"counts":counts,"unclassified":unclassified,"invalid":invalid}

def coverage(c):
 out={}
 for gate in c.get("gates",[]):
  states={x.get("outcome") for x in c.get("fixtures",[]) if x.get("gate")==gate and x.get("outcome") in ("pass","fail")};out[gate]="both" if states=={"pass","fail"} else (next(iter(states)) if states else "neither")
 return {"schema":"marici.scc.coverage-gap.v1","passed":all(v=="both" for v in out.values()) and bool(out),"coverage":out,"gaps":[k for k,v in out.items() if v!="both"]}

def budget_sensitivity(c):
 propagation=propagate_comparison_budget(c)
 if not propagation["passed"]:return {"schema":"marici.scc.budget-sensitivity.v1","passed":False,"propagation":propagation}
 costs=[Fraction(str(x["cost"])) for x in c.get("squares",[])];headroom=Fraction(propagation["residual_margin"])
 stages=[{"index":x["index"],"type":x["type"],"cost":x["cost"],"residual_headroom":x["after"],"fraction_of_total_cost":str(Fraction(x["cost"])/sum(costs,Fraction())) if sum(costs,Fraction()) else "0"} for x in propagation["trace"]]
 return {"schema":"marici.scc.budget-sensitivity.v2","passed":True,"dominant_index":None if not costs else max(range(len(costs)),key=costs.__getitem__),"headroom":str(headroom),"uniform_additional_cost_per_square":str(headroom/len(costs)) if costs else None,"stages":stages,"propagation":propagation}

def interface_match(c):
 left,right=c.get("left",{}),c.get("right",{});m=[]
 for k in AXES:
  if k not in left or k not in right:m.append({"axis":k,"reason":"missing declaration","left":left.get(k),"right":right.get(k)})
  elif left[k]!=right[k]:m.append({"axis":k,"reason":"mismatch","left":left[k],"right":right[k]})
 return {"schema":"marici.scc.interface-match.v2","passed":not m,"descriptor_pullback":"compatible_descriptors_only" if not m else "undefined","mismatches":m,"overlap_map_synthesized":False,"categorical_pullback_certified":False}

TOOLS={"migrate":migrate,"batch-audit":batch_audit,"profile-diff":profile_diff,"promotion-lint":promotion_lint,"dependency-view":dependency_view,"dead-claims":dead_claims,"monotonicity":monotonicity,"fixtures":fixtures,"schema-compat":schema_compat,"normalize":normalize,"residual-census":residual_census,"coverage":coverage,"budget-sensitivity":budget_sensitivity,"interface-match":interface_match}
