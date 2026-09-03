#!/usr/bin/env python3
"""Translate and verify Voevodsky's categorical RH lifting plan v2."""
import hashlib,json
from pathlib import Path
from lifting_ir import compile_lifting_ir
ROOT=Path(__file__).resolve().parents[3];src=ROOT/"research/voevodsky/categorical-rh-lifting-layer-plan-v2.json";plan=json.loads(src.read_text(encoding="utf-8"))
layers=[];base=plan["base_object"];order_ok=True;previous_name=base
for p in plan["layers"]:
 order_ok &= p.get("forgets_to")==previous_name
 x={"id":p["name"],"base_ref":base,"total_ref":p["name"]+":total","kind":p["kind"],"state":p["state"]}
 if p["state"]!="not_constructed":x["projection"]="forget_"+p["name"]
 if p["state"] in ("inhabited","multiple_fillers","selected","coherent_section"):x["inhabitance_witness"]=p.get("evidence",[])
 if p["state"] in ("selected","coherent_section"):x["selector"]="source_declared_"+p["name"]
 if p["state"]=="coherent_section":x.update(selector_invariance_witness="plan_declared_invariance",section_coherence_witness="plan_declared_coherence")
 layers.append(x);base=x["total_ref"];previous_name=p["name"]
report=compile_lifting_ir({"root_object":plan["base_object"],"layers":layers})
first=report.get("first_obstruction",{}).get("layer");after=report.get("layers",[])[2:]
checks={"layer_order_matches_forgets_to":order_ok,"coherent_prefix_exact":report.get("surviving_prefix")==["packet_restriction_bracket"],"first_obstruction_matches":first==plan["first_obstruction"],"all_successors_globally_blocked":all(x["global_status"]=="blocked_by_prior_layer" for x in after),"observer_local_inhabitation_preserved":next(x for x in report["layers"] if x["id"]=="observer_coherence")["state"]=="inhabited","rh_not_promoted":next(x for x in report["layers"] if x["id"]=="rh_implication")["global_status"]=="blocked_by_prior_layer","rejected_substitutes_preserved":all("rejected_substitute" in p for p in plan["layers"] if p["name"] in ("common_closed_form_domain","gaussian_jet_form_core","source_weil_comparison","semibounded_completed_form"))}
result={"schema":"marici.scc.rh-lifting-plan-v2-result.v1","source":str(src.relative_to(ROOT)),"source_sha256":hashlib.sha256(src.read_bytes()).hexdigest(),"report":report,"acceptance_checks":checks,"passed":report["passed"] and all(checks.values()),"claim_boundary":"structural translation and blockage propagation only; no RH implication"}
out=Path(__file__).parent/"rh_lifting_plan_v2_results.json";out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps({"passed":result["passed"],"first_obstruction":report["first_obstruction"],"surviving_prefix":report["surviving_prefix"],"checks":checks},indent=2));raise SystemExit(0 if result["passed"] else 1)
