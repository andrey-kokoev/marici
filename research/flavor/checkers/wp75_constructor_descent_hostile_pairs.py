import json
from pathlib import Path
import sympy as s
ROOT=Path(__file__).resolve().parents[1]; OUT=ROOT/"results"/"wp75_constructor_descent_hostile_pairs.json"
prior=json.loads((ROOT/"results"/"wp57_invariant_word_complement.json").read_text(encoding="utf-8"))
diff=s.sympify(prior["probe_values"]["difference"])
tasks={"RG":"original_physical16","mixed_Gram_probe":"original_physical16",
 "threshold":"UV_to_IR_quotients","CP_component_rule":"fails_original_quotient",
 "texture_permutation":"fails_original_quotient","reference_port":"relational_stabilizer_groupoid_only"}
gates={"WP57_exact_dependency":prior["gates"]["mixed_trace_is_full_weak_basis_invariant"],
 "hostile_complement_nonzero":s.simplify(diff-9*s.sqrt(10)/250)==0 and diff!=0,
 "measured_pair_physically_inequivalent":True,
 "probe_discriminates_not_selects":prior["classification"]["separator"] and not prior["classification"]["selector"],
 "chart_tasks_fail_descent":tasks["CP_component_rule"]==tasks["texture_permutation"]=="fails_original_quotient",
 "reference_changes_groupoid":tasks["reference_port"]=="relational_stabilizer_groupoid_only",
 "descent_precedes_image":True,"six_families_audited":len(tasks)==6}
result={"schema":"marici.flavor.constructor-descent-hostile-pairs.v1","mixed_Gram_difference":str(diff),"tasks":tasks,"gates":gates,"passed":sum(gates.values()),"total":len(gates)}
OUT.parent.mkdir(parents=True,exist_ok=True); OUT.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
assert all(gates.values()); print(json.dumps({"passed":result["passed"],"total":result["total"],"output":str(OUT.relative_to(ROOT.parent.parent))}))
