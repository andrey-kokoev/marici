"""Exact directional and holonomy tests for a four-port moving-fiber model."""

from fractions import Fraction as F
import json
from pathlib import Path


def mm(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


def sub(a, b):
    return [[a[i][j] - b[i][j] for j in range(len(a[0]))]
            for i in range(len(a))]


def eye(n):
    return [[F(i == j) for j in range(n)] for i in range(n)]


def power(a, n):
    out = eye(len(a))
    for _ in range(n):
        out = mm(out, a)
    return out


def nz(a):
    return sum(v != 0 for row in a for v in row)


def block4(ak, b, lower, ae):
    return [ak[0] + b[0], ak[1] + b[1], lower[0] + ae[0], lower[1] + ae[1]]


def main():
    z2 = [[F(0), F(0)], [F(0), F(0)]]
    ak = [[F(0), F(1)], [F(-1), F(0)]]
    ae = [[F(0), F(2)], [F(-2), F(0)]]
    extension = [[F(1), F(0)], [F(1), F(1)]]
    total = block4(ak, extension, z2, ae)
    forget = [[F(0), F(0), F(1), F(0)], [F(0), F(0), F(0), F(1)]]
    horizontal_residual = sub(mm(forget, total), mm(ae, forget))

    epsilon = F(1, 7)
    transport = [[F(i == j) + epsilon * total[i][j] for j in range(4)] for i in range(4)]
    elliptic_transport = [[F(i == j) + epsilon * ae[i][j] for j in range(2)] for i in range(2)]
    finite_horizontal_residual = sub(mm(forget, transport), mm(elliptic_transport, forget))

    marked_input = [[F(1)], [F(0)], [F(0)], [F(0)]]
    elliptic_input = [[F(0)], [F(0)], [F(1)], [F(0)]]
    marked_to_elliptic = mm(forget, mm(transport, marked_input))
    transported_elliptic = mm(transport, elliptic_input)
    elliptic_to_marked = transported_elliptic[:2]

    hostile_lower = [[F(1), F(0)], [F(0), F(0)]]
    hostile_total = block4(ak, extension, hostile_lower, ae)
    hostile_horizontal_residual = sub(mm(forget, hostile_total), mm(ae, forget))

    hk = [[F(0), F(-1)], [F(1), F(0)]]
    shear = [[F(1), F(1)], [F(0), F(1)]]

    p = [[F(0), F(-1)], [F(1), F(0)]]
    q = [[F(1), F(0)], [F(0), F(0)]]
    good = block4(p, q, z2, eye(2))
    bad = block4(eye(2), z2, hostile_lower, eye(2))
    good_gluing_residual = sub(mm(forget, good), forget)
    bad_gluing_residual = sub(mm(forget, bad), forget)

    checks = {
        "horizontal_forget_marks_identity_holds": nz(horizontal_residual) == 0,
        "first_order_transport_intertwines_exactly": nz(finite_horizontal_residual) == 0,
        "marked_kernel_does_not_flow_to_elliptic_quotient": nz(marked_to_elliptic) == 0,
        "elliptic_input_can_flow_into_marked_kernel": nz(elliptic_to_marked) > 0,
        "nonzero_lower_left_hostile_breaks_horizontality": nz(hostile_horizontal_residual) > 0,
        "kernel_holonomy_has_exact_order_four": power(hk, 4) == eye(2) and power(hk, 2) != eye(2),
        "generic_shear_fixture_is_not_order_four": power(shear, 4) != eye(2),
        "good_overlap_preserves_forget_marks_map": nz(good_gluing_residual) == 0,
        "bad_overlap_is_invertible_but_breaks_relative_gluing": nz(bad_gluing_residual) > 0,
    }

    result = {
        "schema": "marici.aspect.directional_double_triangle_moving_fiber_interferometer.v1",
        "status": "pass" if all(checks.values()) else "fail",
        "exact_arithmetic": True,
        "checks": checks,
        "residuals": {
            "horizontal_nonzero_entries": nz(horizontal_residual),
            "allowed_elliptic_to_marked_output": [str(row[0]) for row in elliptic_to_marked],
            "hostile_horizontal_nonzero_entries": nz(hostile_horizontal_residual),
            "good_gluing_nonzero_entries": nz(good_gluing_residual),
            "bad_gluing_nonzero_entries": nz(bad_gluing_residual),
        },
        "typed_boundary": {
            "verified": "directional triangularity, allowed reverse extension, kernel torsion fixture, and gluing hostile",
            "not_verified": "geometric double-triangle source connection or actual torsion",
            "power": "no finite-transport unitarity claim without dilation",
        },
    }
    out = Path(__file__).parents[1] / "results" / "directional_double_triangle_moving_fiber_interferometer.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    if result["status"] != "pass":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
