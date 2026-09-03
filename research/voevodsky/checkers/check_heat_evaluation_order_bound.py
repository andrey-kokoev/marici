from __future__ import annotations

import json
import math


def main() -> None:
    labels = [0.0, 0.7, 1.9, 3.4, 5.8, 9.0]
    rows = []
    for t in (0.1, 0.5, 1.0, 2.0):
        dual_norm_sq = sum(
            (math.exp(-t * labels[i]) - math.exp(-t * labels[i + 1])) ** 2
            / (2 * (labels[i + 1] - labels[i]))
            for i in range(len(labels) - 1)
        )
        continuum_bound = t * math.exp(-2 * t * labels[0]) / 4
        assert dual_norm_sq <= continuum_bound + 1e-14
        rows.append({"t":t,"finite_dual_norm_squared":dual_norm_sq,"continuum_bound":continuum_bound})

    result = {
        "schema":"marici.voevodsky.heat-evaluation-order-bound-check.v1",
        "status":"heat_functional_bound_verified",
        "bound":"||L_t||^2 <= (t/4) exp(-2 t lambda_0)",
        "rows":rows,
        "gaussian_jet_density_proved":False,
        "completed_form_action_constructed":False,
        "rh_implication":False,
        "passed":True
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
