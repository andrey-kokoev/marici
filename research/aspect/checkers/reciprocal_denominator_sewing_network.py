"""Exact finite reciprocal denominator-sewing and Schur-jet checks."""

from fractions import Fraction as F
import json
from pathlib import Path


def eye(n):
    return [[F(i == j) for j in range(n)] for i in range(n)]


def tr(a):
    return [list(row) for row in zip(*a)]


def mm(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


def add(a, b):
    return [[a[i][j] + b[i][j] for j in range(len(a))] for i in range(len(a))]


def scale(q, a):
    return [[q * v for v in row] for row in a]


def minor(a, row, col):
    return [[a[i][j] for j in range(len(a)) if j != col]
            for i in range(len(a)) if i != row]


def det(a):
    if len(a) == 0:
        return F(1)
    if len(a) == 1:
        return a[0][0]
    return sum((F(-1) ** j) * a[0][j] * det(minor(a, 0, j))
               for j in range(len(a)))


def inv(a):
    d = det(a)
    n = len(a)
    cof = [[(F(-1) ** (i + j)) * det(minor(a, i, j)) for j in range(n)]
           for i in range(n)]
    return scale(F(1, 1) / d, tr(cof))


def trace(a):
    return sum(a[i][i] for i in range(len(a)))


def select(a, indices):
    return [[a[i][j] for j in indices] for i in indices]


def at(a0, a1, z):
    return add(a0, scale(z, a1))


def log_jet(a0, a1):
    return trace(mm(inv(a0), a1))


def schur_data(a0, a1, retained, boundary):
    ax0 = select(a0, retained)
    ax1 = select(a1, retained)
    b0 = [[a0[i][boundary]] for i in retained]
    c0 = [[a0[boundary][j] for j in retained]]
    e0 = a0[boundary][boundary]
    e1 = a1[boundary][boundary]
    ax0_inv = inv(ax0)
    mixed = mm(mm(mm(c0, ax0_inv), ax1), mm(ax0_inv, b0))[0][0]
    s0 = e0 - mm(mm(c0, ax0_inv), b0)[0][0]
    s1 = e1 + mixed
    return {"s0": s0, "s1": s1, "mixed": mixed, "diagonal_only": e1}


def addition(a0, a1, retained, boundary):
    enlarged = retained + [boundary]
    data = schur_data(a0, a1, retained, boundary)
    increment = log_jet(select(a0, enlarged), select(a1, enlarged)) - log_jet(
        select(a0, retained), select(a1, retained)
    )
    data["increment"] = increment
    data["schur_jet"] = data["s1"] / data["s0"]
    return data


def encode_map(values):
    return {key: str(value) for key, value in values.items()}


def main():
    q = [
        [F(3, 5), F(-4, 13), F(48, 65)],
        [F(4, 5), F(3, 13), F(-36, 65)],
        [F(0), F(12, 13), F(5, 13)],
    ]
    lam = [[F(1, 2), F(0), F(0)], [F(0), F(1, 4), F(0)], [F(0), F(0), F(1, 5)]]
    m0 = mm(mm(q, lam), tr(q))
    a0 = add(eye(3), m0)
    a1 = eye(3)

    dark_z = F(1, 2)
    numerator_dark = det(add(m0, scale(dark_z - F(1), eye(3))))
    denominator_at_dark = det(at(a0, a1, dark_z))

    sample_z = F(1, 3)
    elimination_checks = []
    orders = [(1, 2), (2, 1)]
    order_results = {}
    full_minus_base = log_jet(a0, a1) - log_jet(select(a0, [0]), select(a1, [0]))

    for order in orders:
        retained = [0]
        increments = []
        mixed_terms = []
        for boundary in order:
            data = addition(a0, a1, retained, boundary)
            increments.append(data["increment"])
            mixed_terms.append(data["mixed"])
            enlarged = retained + [boundary]
            ax = select(at(a0, a1, sample_z), retained)
            ay = select(at(a0, a1, sample_z), enlarged)
            sample_s = schur_data(at(a0, a1, sample_z), [[F(0)] * 3 for _ in range(3)], retained, boundary)["s0"]
            elimination_checks.append(det(ay) == det(ax) * sample_s)
            retained = enlarged
        order_results[str(order)] = {
            "increments": [str(x) for x in increments],
            "mixed_terms": [str(x) for x in mixed_terms],
            "sum": str(sum(increments)),
            "telescopes": sum(increments) == full_minus_base,
        }

    first = addition(a0, a1, [0], 1)
    reflected_sample = det(at(a0, scale(F(-1), a1), F(-2)))
    forward_reflected_argument = det(at(a0, a1, F(2)))

    checks = {
        "calibration_matrix_is_exactly_orthogonal": mm(tr(q), q) == eye(3),
        "network_is_reciprocal": tr(m0) == m0,
        "static_impedance_eigenvalues_are_positive": all(lam[i][i] > 0 for i in range(3)),
        "cayley_numerator_has_exact_right_sector_dark_zero": numerator_dark == 0,
        "denominator_is_nonzero_at_dark_zero": denominator_at_dark != 0,
        "boundary_elimination_preserves_determinants": all(elimination_checks),
        "schur_first_jet_equals_log_denominator_increment": first["increment"] == first["schur_jet"],
        "mixed_schur_derivative_is_nonzero": first["mixed"] != 0,
        "diagonal_only_derivative_is_wrong": first["diagonal_only"] / first["s0"] != first["increment"],
        "both_addition_orders_telescope": all(v["telescopes"] for v in order_results.values()),
        "local_increments_remember_addition_order": order_results["(1, 2)"]["increments"] != order_results["(2, 1)"]["increments"],
        "reflected_sector_obeys_Dminus_z_equals_Dplus_minus_z": reflected_sample == forward_reflected_argument,
    }

    result = {
        "schema": "marici.aspect.reciprocal_denominator_sewing_network.v1",
        "status": "pass" if all(checks.values()) else "fail",
        "exact_arithmetic": True,
        "checks": checks,
        "residuals": {
            "cayley_numerator_at_one_half": str(numerator_dark),
            "denominator_at_one_half": str(denominator_at_dark),
            "first_addition": encode_map(first),
            "full_minus_base_log_jet": str(full_minus_base),
            "orders": order_results,
        },
        "typed_boundary": {
            "verified": "finite reciprocal accretive denominator, Cayley dark zero, Schur bonding, and telescoping",
            "elimination": "algebraic Schur reduction, not physical multiport dilation",
            "completion_missing": "uniform cutoff bounds, nonzero limiting basepoint, theta sewing, and arithmetic current identity",
        },
    }
    out = Path(__file__).parents[1] / "results" / "reciprocal_denominator_sewing_network.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    if result["status"] != "pass":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
