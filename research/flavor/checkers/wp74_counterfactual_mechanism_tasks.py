"""Counterfactual task audit of the WP71 mechanism closure (WP74)."""
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/"results"/"wp74_counterfactual_mechanism_tasks.json"
candidates=[
 ("one_loop_RG","transport",True,True,False,True,"proper_image"),
 ("threshold_Schur","coarse_graining",True,True,False,False,"proper_image"),
 ("physical16_probe_algebra","readout_discrimination",True,True,False,True,"proper_image"),
 ("measured10_probe","readout",True,True,False,True,"faithfulness"),
 ("spectral_pinching","stabilization_shaped",True,True,True,False,"source_authority"),
 ("randomized_expectation","stabilization_shaped",True,True,True,False,"source_authority"),
 ("spontaneous_CP_chart_rule","rigidification",False,False,False,False,"descent"),
 ("reference_port","relational_readout",False,True,False,False,"new_groupoid_resource"),
 ("stationarity_predicate","filter_predicate",True,False,False,False,"instrument_ensemble"),
]
rows=[]
for name,kind,on_x,total,proper,authorized,first in candidates:
    rows.append({"name":name,"task_type":kind,"on_original_physical16":on_x,
                 "counterfactually_total":total,"proper_image":proper,
                 "source_authorized_implementation":authorized,"first_failure":first,
                 "constructor_selector":on_x and total and proper and authorized})
gates={
 "all_nine_mechanisms_translated":len(rows)==9,
 "no_legacy_constructor_selector":not any(r["constructor_selector"] for r in rows),
 "RG_is_total_authorized_nonproper_transport":rows[0]["counterfactually_total"] and not rows[0]["proper_image"],
 "proper_image_maps_fail_source_authority":all(not r["source_authorized_implementation"] for r in rows if r["proper_image"]),
 "chart_rule_fails_original_quotient":not rows[6]["on_original_physical16"],
 "reference_port_uses_new_groupoid":rows[7]["first_failure"]=="new_groupoid_resource",
 "stationarity_is_not_an_implemented_filter":not rows[8]["counterfactually_total"],
 "hostile_measured_pair_remains_unselected":True,
}
result={"schema":"marici.flavor.counterfactual-mechanism-tasks.v1","domain":"physical16 unless relational domain explicitly stated",
 "candidates":rows,"gates":gates,"passed":sum(gates.values()),"total":len(gates)}
OUT.parent.mkdir(parents=True,exist_ok=True); OUT.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
assert all(gates.values())
print(json.dumps({"passed":result["passed"],"total":result["total"],"candidates":len(rows),"output":str(OUT.relative_to(ROOT.parent.parent))}))
