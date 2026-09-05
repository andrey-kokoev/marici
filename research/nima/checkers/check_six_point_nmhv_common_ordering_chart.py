from __future__ import annotations

import itertools
import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[3]
RESULT = ROOT / "research/nima/results/six-point-nmhv-common-ordering-chart.json"


def bracket(a, b):
    return sp.expand(a[0] * b[1] - a[1] * b[0])


def derive_tilde(order, lambdas, mus):
    out = {}
    n = len(order)
    for r, i in enumerate(order):
        prev, nxt = order[(r - 1) % n], order[(r + 1) % n]
        a = bracket(lambdas[i], lambdas[nxt])
        b = bracket(lambdas[nxt], lambdas[prev])
        c = bracket(lambdas[prev], lambdas[i])
        den = bracket(lambdas[prev], lambdas[i]) * bracket(lambdas[i], lambdas[nxt])
        out[i] = tuple(sp.cancel((a * mus[prev][d] + b * mus[i][d] + c * mus[nxt][d]) / den) for d in range(2))
    return out


def reconstruct_mus(order, lambdas, target_tilde):
    symbols = {(i, d): sp.Symbol(f"mu_{i}_{d}") for i in order for d in range(2)}
    solution = {}
    for d in range(2):
        equations = []
        n = len(order)
        for r, i in enumerate(order):
            prev, nxt = order[(r - 1) % n], order[(r + 1) % n]
            a = bracket(lambdas[i], lambdas[nxt])
            b = bracket(lambdas[nxt], lambdas[prev])
            c = bracket(lambdas[prev], lambdas[i])
            den = bracket(lambdas[prev], lambdas[i]) * bracket(lambdas[i], lambdas[nxt])
            equations.append(sp.Eq(a * symbols[(prev, d)] + b * symbols[(i, d)] + c * symbols[(nxt, d)], den * target_tilde[i][d]))
        equations.extend([sp.Eq(symbols[(order[0], d)], 0), sp.Eq(symbols[(order[1], d)], 0)])
        solved = sp.solve(equations, [symbols[(i, d)] for i in order], dict=True)
        if len(solved) != 1:
            raise AssertionError(f"ordering {order}, component {d}: expected unique gauge-fixed solution")
        solution.update(solved[0])
    return {i: tuple(sp.cancel(solution[symbols[(i, d)]]) for d in range(2)) for i in order}


def main():
    labels = tuple(range(1, 7))
    ts = {i: sp.Integer(i) for i in labels}
    lambdas = {i: (sp.Integer(1), ts[i]) for i in labels}
    mu_values = [(2, 17), (11, 5), (23, 31), (7, 29), (37, 13), (19, 41)]
    base_mus = {i: tuple(map(sp.Integer, mu_values[i - 1])) for i in labels}
    base_tilde = derive_tilde(labels, lambdas, base_mus)
    momentum_sum = tuple(sp.expand(sum(lambdas[i][a] * base_tilde[i][d] for i in labels)) for a in range(2) for d in range(2))

    checks = []
    for middle in itertools.permutations((2, 3, 4, 5)):
        order = (1,) + middle + (6,)
        mus = reconstruct_mus(order, lambdas, base_tilde)
        roundtrip = derive_tilde(order, lambdas, mus)
        residuals = [sp.cancel(roundtrip[i][d] - base_tilde[i][d]) for i in labels for d in range(2)]
        checks.append({
            "ordering": list(order),
            "all_tilde_spinors_roundtrip": all(value == 0 for value in residuals),
            "nonzero_adjacent_angle_brackets": all(bracket(lambdas[order[r]], lambdas[order[(r + 1) % 6]]) != 0 for r in range(6))
        })

    assertions = {
        "base_momenta_conserved": all(value == 0 for value in momentum_sum),
        "all_24_ddm_orderings_reconstructed": len(checks) == 24,
        "all_roundtrips_exact": all(c["all_tilde_spinors_roundtrip"] for c in checks),
        "all_adjacent_denominators_nonzero": all(c["nonzero_adjacent_angle_brackets"] for c in checks)
    }
    out = {
        "schema": "marici.nima.six_point_nmhv_common_ordering_chart.result.v1",
        "status": "passed" if all(assertions.values()) else "failed",
        "assertions": assertions,
        "base_momentum_sum": [str(x) for x in momentum_sum],
        "checks": checks,
        "claim_boundary": "Exact common bosonic kinematic chart for all 24 DDM orderings. This does not yet evaluate NMHV Grassmann components or prove KK, BCJ, or chain-level Jacobi descent."
    }
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    if out["status"] != "passed": raise SystemExit(1)


if __name__ == "__main__": main()
