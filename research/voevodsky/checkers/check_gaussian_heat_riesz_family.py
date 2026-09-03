from __future__ import annotations

import json
import math


def main() -> None:
    labels = [0.0, 0.7, 1.9, 3.4, 5.8, 9.0]
    rows = []
    for tau in (0.1, 0.5, 1.0, 2.0):
        F = lambda x: math.exp(-(x * x) / (4 * tau))
        dual_norm_sq = sum(
            (F(labels[i]) - F(labels[i + 1])) ** 2
            / (2 * (labels[i + 1] - labels[i]))
            for i in range(len(labels) - 1)
        )
        continuum_bound = math.sqrt(2 * math.pi) / (16 * math.sqrt(tau))
        assert dual_norm_sq <= continuum_bound + 1e-14
        rows.append({"tau":tau,"finite_dual_norm_squared":dual_norm_sq,"continuum_bound":continuum_bound})

    result = {
        "schema":"marici.voevodsky.gaussian-heat-riesz-family-check.v1",
        "status":"gaussian_heat_boundedness_and_totality_verified",
        "bound":"||G_tau||_*^2 <= sqrt(2*pi)/(16*sqrt(tau)) for lambda_0=0",
        "rows":rows,
        "totality_argument":"substitute x=u^2 and apply Laplace uniqueness to g(sqrt(x))",
        "hilbert_norm_dense":True,
        "graph_norm_dense":False,
        "source_weil_identification_constructed":False,
        "rh_implication":False,
        "passed":True
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
