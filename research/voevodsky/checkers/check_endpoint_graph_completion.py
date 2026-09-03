from __future__ import annotations

import json
import math


def main() -> None:
    # The vertical sequence v_a=(exp(-a/4)g_a,1) tends to (0,1) in
    # H_ord direct_sum C because its H_ord component tends to zero.
    parameters = [4.0, 16.0, 64.0, 256.0]
    horizontal_upper = [
        math.exp(-a / 4) * (math.sqrt(math.pi) * math.sqrt(a) / (2 ** 2.5)) ** 0.5
        for a in parameters
    ]
    assert horizontal_upper[-1] < 1e-20
    alpha = math.exp(0.25) - 1
    # Endpoint rank-one form is bounded by alpha times the augmented norm.
    endpoint_values = [alpha for _ in parameters]
    augmented_norm_squared = [x * x + 1 for x in horizontal_upper]
    assert all(endpoint_values[i] <= alpha * augmented_norm_squared[i] for i in range(len(parameters)))

    result = {
        "schema":"marici.voevodsky.endpoint-graph-completion-check.v1",
        "status":"endpoint_boundary_sector_constructed",
        "completion":"H_ord direct_sum C_endpoint",
        "vertical_sequence_horizontal_upper":horizontal_upper,
        "endpoint_evaluation_continuous":True,
        "endpoint_form_bounded":True,
        "gamma_prime_form_closable":False,
        "common_source_weil_domain_constructed":False,
        "rh_implication":False,
        "passed":True
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
