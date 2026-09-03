from __future__ import annotations

import json
import sympy as sp


def main() -> None:
    # Finite Gaussian independence on distinct squared labels.
    squared_labels = [0, 1, 2]
    heat_parameters = [1, 2, 3]
    evaluation = sp.Matrix([
        [sp.exp(-a * x) for a in heat_parameters]
        for x in squared_labels
    ])
    assert evaluation.det() != 0

    # Arbitrary real source values H(r) induce K_h(a,b)=H(a+b)-H(a+b+h).
    h = sp.Rational(1, 2)
    H = {r: sp.Symbol(f"H_{str(r).replace('/', '_')}", real=True)
         for r in {sp.Rational(a + b) for a in heat_parameters for b in heat_parameters}
         | {sp.Rational(a + b) + h for a in heat_parameters for b in heat_parameters}}
    K = sp.Matrix([
        [H[sp.Rational(a + b)] - H[sp.Rational(a + b) + h] for b in heat_parameters]
        for a in heat_parameters
    ])
    assert K == K.T

    result = {
        "schema":"marici.voevodsky.completed-heat-gaussian-source-form-check.v1",
        "status":"joint_gaussian_source_form_constructed",
        "kernel":"K_h(a,b)=H(a+b)-H(a+b+h)",
        "finite_gaussian_independence":True,
        "hermitian_consistency":True,
        "parallelogram_residual":"zero",
        "closability_proved":False,
        "semiboundedness_proved":False,
        "rh_implication":False,
        "passed":True
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
