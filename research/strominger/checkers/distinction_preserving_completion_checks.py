import hashlib
import json
from copy import deepcopy
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "research" / "strominger"))
from distinction_preserving_completion import compile_contract

contract_path = ROOT / "research/strominger/contracts/distinction-preserving-completion.v1.json"
result_path = ROOT / "research/strominger/results/distinction_preserving_completion.json"
contract = json.loads(contract_path.read_text(encoding="utf-8"))
result = compile_contract(contract)

gates = {
    "exact_factorization_gate": result["finite_fixtures"]["preserved_coordinate"]["descends"],
    "erased_coordinate_has_kernel_witness": result["finite_fixtures"]["erased_coordinate"]["witness"] == ["0", "1"],
    "mixed_distinction_rejected": not result["finite_fixtures"]["mixed_repair"]["descends"],
    "L_split_into_three_typed_stages": result["theta"]["L_factorization"] == ["L_finite_incidence", "L_typed_completion", "L_scalar_readout"],
    "P_and_Q_have_distinct_completion_types": result["theta"]["completion_classes"]["P"] != result["theta"]["completion_classes"]["Q"],
    "finite_incidence_not_scalar_completion": result["theta"]["finite_incidence_authorized"] and not result["theta"]["completed_scalar_readout_authorized"],
    "global_tate_completion_is_joint_not_gradewise": result["theta"]["joint_global_completion_authorized"],
    "scalar_section_does_not_authorize_seam_operator": not result["theta"]["operator_lift_authorized"],
    "both_theta_hostiles_reject_descent": all(x["rejects_continuous_descent"] for x in result["theta"]["sequential_hostiles"].values()),
}

hostiles = {}
for name, mutate, expected in (
    ("conflate_completion_types", lambda c: c["theta_application"]["completion_classes"].update({"P":c["theta_application"]["completion_classes"]["Q"]}), "primitive_square_completion_types_conflated"),
    ("launder_finite_incidence", lambda c: c["theta_application"].update({"completed_scalar_readout_authorized":True}), "finite_incidence_laundered_to_scalar_completion"),
    ("launder_scalar_to_operator", lambda c: c["theta_application"]["operator_lift"].update({"source_authorized":True}), "scalar_tate_section_laundered_to_seam_operator"),
    ("split_global_completion_by_grade", lambda c: c["theta_application"]["joint_global_completion"].update({"gradewise_scalar_pushforward":True}), "global_tate_completion_mistyped"),
    ("delete_seam_witness", lambda c: c["theta_application"]["sequential_hostiles"][0].update({"required_distinction_limit":"0"}), "invalid_sequential_hostile:seam_translation"),
):
    candidate = deepcopy(contract)
    mutate(candidate)
    hostile = compile_contract(candidate)
    hostiles[name] = not hostile["passed"] and expected in hostile["errors"]

result["semantic_gates"] = gates
result["hostiles"] = hostiles
result["contract_sha256"] = hashlib.sha256(contract_path.read_bytes()).hexdigest()
result_path.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")

for name, passed in gates.items():
    print(("PASS" if passed else "FAIL") + " gate." + name)
for name, passed in hostiles.items():
    print(("PASS" if passed else "FAIL") + " hostile." + name)
if not result["passed"] or not all(gates.values()) or not all(hostiles.values()):
    raise SystemExit(1)
print(f"SUMMARY {sum(gates.values())}/{len(gates)}; HOSTILE {sum(hostiles.values())}/{len(hostiles)}")
