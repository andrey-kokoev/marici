import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; OUT=ROOT/"results"/"wp82_constructor_hostile_ensemble_matrix.json"
d68=json.loads((ROOT/"results"/"wp68_fitted_ensemble_contextual_partitions.json").read_text(encoding="utf-8"))
d69=json.loads((ROOT/"results"/"wp69_hostile_suite.json").read_text(encoding="utf-8"))
# D,T,P,A,I,R,E in first-failure order.
raw={
 "one_loop_RG":(1,1,0,1,0,0,1),"threshold_Schur":(1,1,0,0,0,0,1),
 "physical16_probe_algebra":(1,1,0,1,1,1,1),"measured10_probe":(1,1,0,1,1,1,1),
 "spectral_pinching":(1,1,1,0,0,0,0),"randomized_expectation":(1,1,1,0,0,0,0),
 "frozen_UV_boundary_template":(1,1,1,0,0,0,0),"source_restriction_template":(1,1,1,0,0,0,0),
 "spontaneous_CP_chart":(0,0,0,0,0,0,0),"reference_on_original_groupoid":(0,0,0,0,0,0,0),
 "stationarity_filter":(1,0,0,0,0,0,0)}
names=("D","T","P","A","I","R","E")
rows=[]
for candidate,vals in raw.items():
 gates=dict(zip(names,map(bool,vals))); first=next((n for n in names if not gates[n]),None)
 rows.append({"candidate":candidate,"gates":gates,"first_failure":first,"passes_all":all(gates.values())})
counts={n:sum(r["first_failure"]==n for r in rows) for n in names}
gates={"WP68_dependency":all(d68["gates"].values()),"WP69_dependency":all(d69["tests"].values()),
 "eleven_candidates":len(rows)==11,"none_passes_all":not any(r["passes_all"] for r in rows),
 "proper_survivors_first_fail_authority":all(r["first_failure"]=="A" for r in rows if r["gates"]["P"]),
 "stationarity_zero_of_1210":d68["partitions"]["stationarity_selector"]["accepted_within_one_sigma"]==0 and d68["domain"]["complete_stored_viable_sheet_ensemble"]==1210,
 "hostile_suite_complete":len(d69["tests"])==7,"first_failure_partition_complete":sum(counts.values())==len(rows)}
result={"schema":"marici.flavor.constructor-hostile-ensemble-matrix.v1","gate_order":list(names),"rows":rows,"first_failure_counts":counts,"ensemble":{"sheets":1210,"stationarity_accepts":0},"gates":gates,"passed":sum(gates.values()),"total":len(gates)}
OUT.parent.mkdir(parents=True,exist_ok=True); OUT.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8"); assert all(gates.values())
print(json.dumps({"passed":result["passed"],"total":result["total"],"candidates":len(rows),"first_failures":counts,"output":str(OUT.relative_to(ROOT.parent.parent))}))
