"""Exact checks for reciprocal and Faraday-type Jones scattering."""

from fractions import Fraction as F
import json
from pathlib import Path


def mm(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


def tr(a):
    return [list(row) for row in zip(*a)]


def sub(a, b):
    return [[a[i][j] - b[i][j] for j in range(len(a[0]))]
            for i in range(len(a))]


def eye(n):
    return [[F(i == j) for j in range(n)] for i in range(n)]


def nz(a):
    return sum(v != 0 for row in a for v in row)


def block_scattering(U, V):
    z = [[F(0), F(0)], [F(0), F(0)]]
    return [z[0] + V[0], z[1] + V[1], U[0] + z[0], U[1] + z[1]]


def block2(A, L):
    return [A[0] + L[0], A[1] + L[1],
            [-v for v in L[0]] + A[0], [-v for v in L[1]] + A[1]]


def main():
    R = [[F(3, 5), F(-4, 5)], [F(4, 5), F(3, 5)]]
    reciprocal_reverse = tr(R)
    faraday_reverse = R
    S_recip = block_scattering(R, reciprocal_reverse)
    S_faraday = block_scattering(R, faraday_reverse)

    reciprocal_residual = sub(S_recip, tr(S_recip))
    faraday_reciprocity_residual = sub(S_faraday, tr(S_faraday))
    faraday_unitarity_residual = sub(mm(tr(S_faraday), S_faraday), eye(4))
    reciprocal_round_trip = mm(reciprocal_reverse, R)
    faraday_round_trip = mm(faraday_reverse, R)

    A = [[F(3, 5), F(0)], [F(0), F(1)]]
    L = [[F(4, 5), F(0)], [F(0), F(0)]]
    dilation = block2(A, L)
    dilation_residual = sub(mm(tr(dilation), dilation), eye(4))
    order_residual = sub(mm(R, A), mm(A, R))

    analyzer = [[F(1), F(0)]]
    jones_a = [[F(1)], [F(1)]]
    jones_b = [[F(1)], [F(-1)]]
    same_scalar = mm(analyzer, jones_a) == mm(analyzer, jones_b)

    checks = {
        "jones_rotation_preserves_norm": mm(tr(R), R) == eye(2),
        "reciprocal_scattering_is_symmetric": nz(reciprocal_residual) == 0,
        "reciprocal_round_trip_cancels": reciprocal_round_trip == eye(2),
        "faraday_scattering_is_lossless": nz(faraday_unitarity_residual) == 0,
        "faraday_scattering_is_not_reciprocal": nz(faraday_reciprocity_residual) > 0,
        "faraday_round_trip_does_not_cancel": faraday_round_trip != eye(2),
        "polarization_loss_dilation_is_orthogonal": nz(dilation_residual) == 0,
        "single_analyzer_row_is_not_faithful": same_scalar and jones_a != jones_b,
        "rotation_and_anisotropic_loss_do_not_commute": nz(order_residual) > 0,
    }
    result = {
        "schema": "marici.aspect.nonreciprocal_polarization_scattering.v1",
        "status": "pass" if all(checks.values()) else "fail",
        "exact_arithmetic": True,
        "checks": checks,
        "residuals": {
            "faraday_reciprocity": [[str(v) for v in row] for row in faraday_reciprocity_residual],
            "faraday_round_trip_minus_identity": [[str(v) for v in row] for row in sub(faraday_round_trip, eye(2))],
            "rotation_loss_commutator": [[str(v) for v in row] for row in order_residual],
            "loss_dilation_nonzero_entries": nz(dilation_residual),
            "H_retained_probability": "9/25",
            "H_environment_probability": "16/25",
        },
        "typed_boundary": {
            "ports": "left and right Jones C^2 in one laboratory basis and energy metric",
            "complete_scattering": "C^4->C^4",
            "analyzer": "Jones C^2->scalar C",
            "loss_completion": "retained+environment C^4->C^4",
        },
        "completion_missing": [
            "dispersion", "microscopic magneto-optic source", "continuum modes",
            "quantum noise", "Kramers-Kronig causal completion",
        ],
    }
    out = Path(__file__).parents[1] / "results" / "nonreciprocal_polarization_scattering.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    if result["status"] != "pass":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
