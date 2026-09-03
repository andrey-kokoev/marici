from __future__ import annotations

import json
import math


def H(t: float) -> float:
    # Decaying fixture for the sourced asymptotic H(t)->0.
    return math.exp(-t)


def K_H(a: float, b: float, h: float) -> float:
    return H(a + b) - H(a + b + h)


def K_R(a: float, b: float, h: float) -> float:
    alpha = math.exp(h / 4) - 1
    return K_H(a, b, h) + alpha * math.exp((a + b) / 4)


def main() -> None:
    h = 1.0
    alpha = math.exp(h / 4) - 1
    parameters = [4.0, 16.0, 64.0, 256.0]
    norm_upper = [
        math.exp(-a / 4) * (math.sqrt(math.pi) * math.sqrt(a) / (2 ** 2.5)) ** 0.5
        for a in parameters
    ]
    corrected_values = [math.exp(-a / 2) * K_R(a, a, h) for a in parameters]
    raw_values = [math.exp(-a / 2) * K_H(a, a, h) for a in parameters]
    assert norm_upper[-1] < 1e-20
    assert abs(corrected_values[-1] - alpha) < 1e-14
    assert abs(raw_values[-1]) < 1e-100

    result = {
        "schema":"marici.voevodsky.endpoint-form-nonclosability-check.v2",
        "status":"endpoint_corrected_remainder_form_nonclosable",
        "null_sequence":"f_a=exp(-a/4) g_a",
        "order_norm_upper_bounds":norm_upper,
        "corrected_remainder_form_values":corrected_values,
        "raw_completed_heat_form_values":raw_values,
        "limit_corrected_value":alpha,
        "raw_completed_heat_form_closability_proved":False,
        "endpoint_corrected_remainder_form_closable":False,
        "rh_implication":False,
        "passed":True
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
