from __future__ import annotations

import json
from pathlib import Path


def main() -> None:
    path = Path("research/voevodsky/categorical-rh-realization-identity-residual-plan-v1.json")
    plan = json.loads(path.read_text(encoding="utf-8"))
    objects = {item["name"]: item for item in plan["objects"]}
    generators = {item["name"]: item for item in plan["generators"]}

    assert objects["order_realization"]["state"] == "inhabited"
    assert generators["identity_order"]["type"] == "order_realization -> order_realization"
    assert generators["identity_order"]["state"] == "defined"
    assert plan["loop"]["type"] == generators["identity_order"]["type"]
    assert plan["loop"]["state"] == "undefined"
    assert all(generators[name]["state"] == "missing" for name in plan["loop"]["blocked_by"])
    assert plan["residual"]["state"] == "not_formable_until_loop_defined"
    assert plan["faithfulness_gate"]["hilbert_level"] == "passed"
    assert plan["faithfulness_gate"]["graph_form_level"] == "open"
    assert plan["rh_implication"] is False

    result = {
        "schema":"marici.voevodsky.realization-identity-residual-plan-check.v1",
        "status":"typed_loop_and_residual_gates_verified",
        "identity_endomorphism_defined":True,
        "loop_same_endomorphism_type":True,
        "loop_defined":False,
        "residual_formable":False,
        "hilbert_faithfulness":True,
        "graph_form_faithfulness":False,
        "first_missing_typed_object":plan["first_missing_typed_object"],
        "rh_implication":False,
        "passed":True
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
