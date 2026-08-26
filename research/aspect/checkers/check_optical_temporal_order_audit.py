from __future__ import annotations

import json
from fractions import Fraction as F
from pathlib import Path


Matrix = list[list[F]]


def mm(a: Matrix, b: Matrix) -> Matrix:
    return [[sum((a[i][k] * b[k][j] for k in range(len(b))), F(0)) for j in range(len(b[0]))] for i in range(len(a))]


def add(*matrices: Matrix) -> Matrix:
    return [[sum((m[i][j] for m in matrices), F(0)) for j in range(len(matrices[0][0]))] for i in range(len(matrices[0]))]


def sub(a: Matrix, b: Matrix) -> Matrix:
    return [[a[i][j] - b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def kron(a: Matrix, b: Matrix) -> Matrix:
    return [[a[i // len(b)][j // len(b[0])] * b[i % len(b)][j % len(b[0])] for j in range(len(a[0]) * len(b[0]))] for i in range(len(a) * len(b))]


def tr(a: Matrix) -> F:
    return sum((a[i][i] for i in range(len(a))), F(0))


def selective(rho: Matrix, projector: Matrix) -> Matrix:
    return mm(mm(projector, rho), projector)


def dephase(rho: Matrix, plus: Matrix, minus: Matrix) -> Matrix:
    return add(selective(rho, plus), selective(rho, minus))


def lift_channel(rho: Matrix, plus: Matrix, minus: Matrix, first_port: bool) -> Matrix:
    identity = [[F(1), F(0)], [F(0), F(1)]]
    kp = kron(plus, identity) if first_port else kron(identity, plus)
    km = kron(minus, identity) if first_port else kron(identity, minus)
    return add(mm(mm(kp, rho), kp), mm(mm(km, rho), km))


def encode_matrix(a: Matrix) -> list[list[str]]:
    return [[str(x) for x in row] for row in a]


def main() -> None:
    h = [[F(1), F(0)], [F(0), F(0)]]
    v = [[F(0), F(0)], [F(0), F(1)]]
    d = [[F(1, 2), F(1, 2)], [F(1, 2), F(1, 2)]]
    a = [[F(1, 2), F(-1, 2)], [F(-1, 2), F(1, 2)]]
    mixed = [[F(1, 2), F(0)], [F(0), F(1, 2)]]

    hdv = selective(selective(h, d), v)
    hvd = selective(selective(h, v), d)
    assert tr(hdv) == F(1, 4)
    assert tr(hvd) == 0

    h_then_d = selective(selective(mixed, h), d)
    d_then_h = selective(selective(mixed, d), h)
    assert tr(h_then_d) == tr(d_then_h) == F(1, 4)
    assert h_then_d != d_then_h
    downstream_h_after_hd = tr(selective(h_then_d, h)) / tr(h_then_d)
    downstream_h_after_dh = tr(selective(d_then_h, h)) / tr(d_then_h)
    assert downstream_h_after_hd == F(1, 2)
    assert downstream_h_after_dh == 1

    # Observable N = (3/5) X + (4/5) Z and its exact projectors.
    n_plus = [[F(9, 10), F(3, 10)], [F(3, 10), F(1, 10)]]
    n_minus = [[F(1, 10), F(-3, 10)], [F(-3, 10), F(9, 10)]]
    assert mm(n_plus, n_plus) == n_plus
    assert mm(n_minus, n_minus) == n_minus
    assert mm(n_plus, n_minus) == [[F(0), F(0)], [F(0), F(0)]]

    z_then_n = dephase(dephase(h, h, v), n_plus, n_minus)
    n_then_z = dephase(dephase(h, n_plus, n_minus), h, v)
    # Match Nima's composition convention: D_Z D_N - D_N D_Z.
    residual = sub(n_then_z, z_then_n)
    expected_residual = [[F(0), F(-6, 25)], [F(-6, 25), F(0)]]
    assert residual == expected_residual

    basis_checks = 0
    for row in range(4):
        for col in range(4):
            unit = [[F(0) for _ in range(4)] for _ in range(4)]
            unit[row][col] = F(1)
            first_then_second = lift_channel(lift_channel(unit, h, v, True), n_plus, n_minus, False)
            second_then_first = lift_channel(lift_channel(unit, n_plus, n_minus, False), h, v, True)
            assert first_then_second == second_then_first
            basis_checks += 1

    result = {
        "schema": "marici.aspect.optical-temporal-order-audit.v1",
        "status": "pass",
        "crossed_h_d_v_probability": "1/4",
        "crossed_h_v_d_probability": "0",
        "equal_scalar_word_probability": "1/4",
        "equal_scalar_continuations_equal": False,
        "downstream_h_probability_after_h_then_d": str(downstream_h_after_hd),
        "downstream_h_probability_after_d_then_h": str(downstream_h_after_dh),
        "same_carrier_dephasing_commutes": False,
        "same_carrier_order_residual": encode_matrix(residual),
        "independent_port_basis_commutation_checks": basis_checks,
        "independent_ports_commute": True,
        "verdict": "Order is removable only with continuation-level commutation; scalar equality is insufficient.",
        "claim_boundary": "finite exact ideal-polarization order audit",
    }
    output = Path(__file__).parents[1] / "results" / "optical_temporal_order_audit.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
