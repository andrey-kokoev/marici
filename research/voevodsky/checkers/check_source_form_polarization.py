from __future__ import annotations

import json
import sympy as sp


def main() -> None:
    I = sp.I
    H = sp.Matrix([[3, 1 + 2 * I], [1 - 2 * I, -1]])
    x = sp.Matrix([1 + I, 2 - I])
    y = sp.Matrix([2, -1 + I])

    def B(a: sp.Matrix, b: sp.Matrix):
        return (sp.conjugate(a).T * H * b)[0]

    def q(a: sp.Matrix):
        return sp.simplify(B(a, a))

    polarized = sp.simplify(sum(
        (-I) ** k * q(x + I ** k * y) for k in range(4)
    ) / 4)
    assert sp.simplify(polarized - B(x, y)) == 0

    result = {
        "schema":"marici.voevodsky.source-form-polarization-check.v1",
        "status":"complex_hermitian_polarization_verified",
        "convention":"conjugate-linear first variable, linear second variable",
        "polarized_kernel_independent_input":False,
        "joint_quadratic_form_on_linear_span_required":True,
        "shared_regularization_required":True,
        "closability_proved":False,
        "rh_implication":False,
        "passed":True
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
