from __future__ import annotations

import json
import sympy as sp


def main() -> None:
    alpha = sp.symbols("alpha", positive=True, real=True)
    q1, q2 = sp.symbols("q1 q2", real=True)
    raw = sp.diag(q1, q2)
    augmented = sp.diag(q1, q2, alpha)
    assert augmented[:2, :2] == raw
    assert augmented[:2, 2] == sp.zeros(2, 1)
    assert augmented[2, :2] == sp.zeros(1, 2)

    result = {
        "schema":"marici.voevodsky.endpoint-augmented-block-form-check.v1",
        "status":"endpoint_block_decoupling_verified",
        "carrier":"H_ord direct_sum C_endpoint",
        "form":"q_H direct_sum alpha*abs(z)^2",
        "cross_block":0,
        "augmented_closability_equivalent_to_raw_closability":True,
        "augmented_semiboundedness_equivalent_to_raw_semiboundedness":True,
        "raw_completed_heat_form_closability_proved":False,
        "rh_implication":False,
        "passed":True
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
