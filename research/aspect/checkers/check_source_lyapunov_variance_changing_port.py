import json

import sympy as sp


a, b, c, r = sp.symbols("a b c r", real=True)
G = sp.Matrix([[a, b], [b, c]])
I = sp.eye(2)
J = sp.Matrix([[0, -1], [1, 0]])

fourier_residual = sp.simplify(J * G * J.T - G)
lyapunov_residual = sp.simplify(I * G + G * I - I)
solution = sp.solve(list(lyapunov_residual), [a, b, c], dict=True)

scaled = r * I
scaled_fourier = sp.simplify(J * scaled * J.T - scaled)
scaled_lyapunov = sp.simplify(I * scaled + scaled * I - I)

checks = {
    "fourier_leaves_scalar_family": scaled_fourier == sp.zeros(2),
    "lyapunov_has_unique_symmetric_solution": solution
    == [{a: sp.Rational(1, 2), b: 0, c: sp.Rational(1, 2)}],
    "selected_covariance_is_fourier_invariant": fourier_residual.subs(solution[0])
    == sp.zeros(2),
    "hostile_rescaling_residual_is_exact": scaled_lyapunov
    == (2 * r - 1) * I,
    "hostile_rescaling_passes_only_at_half": sp.solve(
        list(scaled_lyapunov), [r], dict=True
    )
    == [{r: sp.Rational(1, 2)}],
}

result = {
    "schema": "marici.aspect.source-lyapunov-variance-changing-port.v1",
    "status": "pass" if all(checks.values()) else "fail",
    "checks": checks,
    "solution": {str(k): str(v) for k, v in solution[0].items()},
    "hostile_residual": str(scaled_lyapunov),
    "interpretation": (
        "Fourier symmetry removes anisotropy but the source Lyapunov law "
        "selects the remaining covariance scale and changes variance E'->E."
    ),
}

print(json.dumps(result, indent=2))
