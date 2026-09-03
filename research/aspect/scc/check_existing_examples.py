#!/usr/bin/env python3
"""Apply repository-local SCC maintenance tools to the materialized model registry."""
from pathlib import Path
import json
from scc_toolkit import migrate,batch_audit,promotion_lint,provenance_lock,interface_match,AXES
ROOT=Path(__file__).resolve().parents[3]
models=json.loads((Path(__file__).parent/"models.v1.json").read_text())["models"]
inputs=sorted({p for m in models for p in m.get("inputs",[])})
lock=provenance_lock({"artifacts":inputs},ROOT)
migrations=[]
for m in models:
 r=migrate(m);constructed=[k for k,v in r["layers"].items() if v["status"]=="constructed"]
 migrations.append({"id":m["id"],"constructed_layers":constructed,"migration_residuals":r["migration_residuals"],"compiler_passed":r["compiler_check"]["passed"]})
batch=batch_audit({"contracts":[{"id":m["id"],"contract":migrate(m)} for m in models]})
lint=promotion_lint({"models":models})
promotion_keys={"literal_zero","strict_selection","identity","observational_quotient","global_complete","physical_backend"}
def count_keys(x):
 if isinstance(x,dict):return sum(k in promotion_keys for k in x)+sum(count_keys(v) for v in x.values())
 if isinstance(x,list):return sum(count_keys(v) for v in x)
 return 0
promotion_field_count=count_keys(models)
# Registry models do not declare the categorical interface axes. Test refusal rather than fabricate them.
interface_probe=interface_match({"left":models[0],"right":models[1]}) if len(models)>1 else None
result={"schema":"marici.scc.existing-examples-audit.v1","model_count":len(models),"unique_input_count":len(inputs),
 "provenance":{"passed":lock["passed"],"locked_count":len(lock["artifacts"]),"errors":lock["errors"]},
 "promotion_lint":{"applicable":promotion_field_count>0,"structured_fields_seen":promotion_field_count,"passed":lint["passed"],"findings":lint["findings"],"interpretation":"no structured promotion claims were present; this is not a prose audit"},
 "migration":{"all_compile":batch["passed"],"compile_interpretation":"vacuous when no categorical layers are constructed","profiles":migrations,
   "models_with_constructed_categorical_layers":sum(bool(x["constructed_layers"]) for x in migrations)},
 "interface_probe":{"passed":interface_probe["passed"],"missing_axes":[x["axis"] for x in interface_probe["mismatches"]],
   "categorical_pullback_certified":interface_probe["categorical_pullback_certified"]},
 "disposition":"registry examples are provenance-auditable but are not categorical-apparatus contracts; migration correctly refuses to infer categorical layers or interface pullbacks"}
out=Path(__file__).parent/"existing_examples_toolkit_results.json";out.write_text(json.dumps(result,indent=2)+"\n")
print(json.dumps(result,indent=2));raise SystemExit(0 if lint["passed"] and batch["passed"] else 1)
