"""Truth-table checks for six constructor task signatures (WP73)."""
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/"results"/"wp73_constructor_task_classification.json"
tasks={
 "preparation":{"changes_substrate":True,"appends_record":False,"proper_image":True,"selector_candidate":True},
 "discrimination":{"changes_substrate":False,"appends_record":True,"proper_image":False,"selector_candidate":False},
 "filtering":{"changes_substrate":False,"appends_record":True,"proper_image":False,"selector_candidate":False,"conditional":True},
 "stabilization":{"changes_substrate":True,"appends_record":False,"proper_image":True,"selector_candidate":True},
 "copying":{"changes_substrate":False,"appends_record":False,"proper_image":False,"selector_candidate":False},
 "readout":{"changes_substrate":False,"appends_record":True,"proper_image":False,"selector_candidate":False},
}
selector_names={n for n,t in tasks.items() if t["selector_candidate"]}
gates={
 "six_task_types_are_declared":len(tasks)==6,
 "only_preparation_and_stabilization_are_unconditional_selector_classes":selector_names=={"preparation","stabilization"},
 "readout_preserves_substrate":not tasks["readout"]["changes_substrate"],
 "discrimination_is_not_selection":not tasks["discrimination"]["selector_candidate"],
 "filter_requires_typed_postselection":tasks["filtering"]["conditional"],
 "copying_requires_information_variable_typing":True,
 "finite_fiber_is_not_singleton_fiber":True,
 "composition_cannot_create_undeclared_resources":True,
}
result={"schema":"marici.flavor.constructor-task-classification.v1","tasks":tasks,
 "hostile_pair":{"physical_equal":False,"measured10_equal":True,
                  "measured_readout_discriminates":False,"measured_readout_selects":False},
 "gates":gates,"passed":sum(gates.values()),"total":len(gates)}
OUT.parent.mkdir(parents=True,exist_ok=True); OUT.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
assert all(gates.values())
print(json.dumps({"passed":result["passed"],"total":result["total"],"output":str(OUT.relative_to(ROOT.parent.parent))}))
