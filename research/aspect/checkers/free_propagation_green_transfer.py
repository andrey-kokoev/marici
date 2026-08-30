"""Exact checks for paraxial propagation and finite Green transfer."""

from fractions import Fraction as F
import json
from pathlib import Path


def mm(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


def sub(a, b):
    return [[a[i][j] - b[i][j] for j in range(len(a[0]))]
            for i in range(len(a))]


def tr(a):
    return [list(row) for row in zip(*a)]


def det2(a):
    return a[0][0] * a[1][1] - a[0][1] * a[1][0]


def nz(a):
    return sum(v != 0 for row in a for v in row)


def main():
    L1, L2, focal = F(2), F(3), F(5)
    P1 = [[F(1), L1], [F(0), F(1)]]
    P2 = [[F(1), L2], [F(0), F(1)]]
    Psum = [[F(1), L1 + L2], [F(0), F(1)]]
    lens = [[F(1), F(0)], [-F(1, 5), F(1)]]
    order_residual = sub(mm(lens, P1), mm(P1, lens))

    K = [[F(2), F(-1)], [F(-1), F(2)]]
    G = [[F(2, 3), F(1, 3)], [F(1, 3), F(2, 3)]]
    Knr = [[F(2), F(-2)], [F(-1), F(2)]]
    Gnr = [[F(1), F(1)], [F(1, 2), F(1)]]
    identity = [[F(1), F(0)], [F(0), F(1)]]
    reciprocal_residual = sub(G, tr(G))
    directed_reciprocity_residual = sub(Gnr, tr(Gnr))

    retain, leak = F(3, 5), F(4, 5)
    loss_dilation = [[retain, leak], [-leak, retain]]
    loss_residual = sub(mm(tr(loss_dilation), loss_dilation), identity)

    detector = [[F(1), F(0)]]
    field_a = [[F(1)], [F(1)]]
    field_b = [[F(1)], [F(-1)]]
    same_scalar = mm(detector, field_a) == mm(detector, field_b)

    Kres = [[F(1), F(-1)], [F(-1), F(1)]]
    checks = {
        "free_propagation_composes_additively": mm(P2, P1) == Psum,
        "paraxial_maps_preserve_oriented_area": det2(P1) == det2(lens) == 1,
        "lens_propagation_order_is_detectable": nz(order_residual) > 0,
        "reciprocal_green_is_exact_inverse": mm(K, G) == identity and mm(G, K) == identity,
        "reciprocal_green_is_symmetric": nz(reciprocal_residual) == 0,
        "directed_green_is_inverse_but_not_reciprocal": mm(Knr, Gnr) == identity and nz(directed_reciprocity_residual) > 0,
        "loss_dilation_preserves_total_intensity": nz(loss_residual) == 0 and retain * retain + leak * leak == 1,
        "single_detector_row_has_field_kernel": same_scalar and field_a != field_b,
        "resonant_operator_has_no_full_inverse": det2(Kres) == 0,
    }
    result = {
        "schema": "marici.aspect.free_propagation_green_transfer.v1",
        "status": "pass" if all(checks.values()) else "fail",
        "exact_arithmetic": True,
        "checks": checks,
        "residuals": {
            "lens_propagation_commutator": [[str(v) for v in row] for row in order_residual],
            "reciprocal_transpose_nonzero_entries": nz(reciprocal_residual),
            "directed_transpose_residual": [[str(v) for v in row] for row in directed_reciprocity_residual],
            "retained_probability": str(retain * retain),
            "environment_probability": str(leak * leak),
            "resonant_determinant": str(det2(Kres)),
        },
        "typed_maps": {
            "paraxial": "R^2->R^2 in declared longitudinal frame",
            "green": "source C^2->field C^2 at frozen frequency and boundary condition",
            "detector": "field R^2->scalar R",
            "loss_dilation": "retained+environment R^2->R^2",
        },
        "completion_missing": [
            "frequency domain", "radiation condition", "function spaces",
            "convergence mode", "uniform resolvent bound", "infinite-time limit",
        ],
    }
    out = Path(__file__).parents[1] / "results" / "free_propagation_green_transfer.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    if result["status"] != "pass":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
