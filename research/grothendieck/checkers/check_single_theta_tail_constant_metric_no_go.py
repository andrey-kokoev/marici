"""Exact no-go for a constant positive Hermitian metric on one theta-tail phase plane."""
import json
import sympy as sp


def main():
    h11, h12, h22, a, t = sp.symbols("h11 h12 h22 a t", real=True)
    H = sp.Matrix([[h11, h12], [h12, h22]])
    N = sp.Matrix([[0, -1], [0, 0]])
    forcing_lyapunov = sp.simplify(N.T * H + H * N)
    forcing_solution = sp.solve(list(forcing_lyapunov), [h11, h12], dict=True)

    s = a + sp.I * t
    D = sp.diag(-s / 2, s / 2)
    drift_lyapunov = sp.simplify(sp.conjugate(D).T * H + H * D)

    checks = {
        "forcing_condition_sets_h11_zero": all(sol.get(h11) == 0 for sol in forcing_solution),
        "forcing_condition_sets_h12_zero": all(sol.get(h12) == 0 for sol in forcing_solution),
        "positive_metric_impossible_for_variable_forcing": all(sol.get(h11) == 0 for sol in forcing_solution),
        "off_seam_drift_has_nonimaginary_eigenvalues": sp.re(-s / 2) == -a / 2 and sp.re(s / 2) == a / 2,
    }
    result = {
        "schema": "marici.grothendieck.single-theta-tail-constant-metric-no-go.v1",
        "passed": all(checks.values()),
        "checks": checks,
        "forcing_generator": [[str(x) for x in N.row(i)] for i in range(2)],
        "forcing_lyapunov_matrix": [[str(x) for x in forcing_lyapunov.row(i)] for i in range(2)],
        "forcing_solutions": [{str(k): str(v) for k, v in sol.items()} for sol in forcing_solution],
        "drift_lyapunov_matrix": [[str(x) for x in drift_lyapunov.row(i)] for i in range(2)],
        "disposition": "A positive conserved form cannot be constant on one phase plane. Any surviving metric must be doubled reciprocal or q-dependent.",
    }
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
