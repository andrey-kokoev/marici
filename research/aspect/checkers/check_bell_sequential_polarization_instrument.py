from __future__ import annotations

import json
from fractions import Fraction as F
from pathlib import Path


Matrix = list[list[F]]


def mm(a: Matrix, b: Matrix) -> Matrix:
    return [[sum((a[i][k] * b[k][j] for k in range(len(b))), F(0)) for j in range(len(b[0]))] for i in range(len(a))]


def add(*matrices: Matrix) -> Matrix:
    return [[sum((m[i][j] for m in matrices), F(0)) for j in range(len(matrices[0][0]))] for i in range(len(matrices[0]))]


def kron(a: Matrix, b: Matrix) -> Matrix:
    return [[a[i // len(b)][j // len(b[0])] * b[i % len(b)][j % len(b[0])] for j in range(len(a[0]) * len(b[0]))] for i in range(len(a) * len(b))]


def tr(a: Matrix) -> F:
    return sum((a[i][i] for i in range(len(a))), F(0))


def instrument(rho: Matrix, projector: Matrix, on_alice: bool = True) -> Matrix:
    identity = [[F(1), F(0)], [F(0), F(1)]]
    k = kron(projector, identity) if on_alice else kron(identity, projector)
    return mm(mm(k, rho), k)


def partial_trace_alice(rho: Matrix) -> Matrix:
    return [[sum((rho[2 * a + b][2 * a + bp] for a in range(2)), F(0)) for bp in range(2)] for b in range(2)]


def encode(value: F) -> str:
    return str(value)


def main() -> None:
    z_plus = [[F(1), F(0)], [F(0), F(0)]]
    z_minus = [[F(0), F(0)], [F(0), F(1)]]
    x_plus = [[F(1, 2), F(1, 2)], [F(1, 2), F(1, 2)]]
    x_minus = [[F(1, 2), F(-1, 2)], [F(-1, 2), F(1, 2)]]
    zero4 = [[F(0) for _ in range(4)] for _ in range(4)]

    # |psi-> = (|01> - |10>)/sqrt(2); its density matrix is rational.
    rho = [row[:] for row in zero4]
    rho[1][1] = rho[2][2] = F(1, 2)
    rho[1][2] = rho[2][1] = F(-1, 2)
    assert tr(rho) == 1

    alice_z_plus = instrument(rho, z_plus)
    alice_z_minus = instrument(rho, z_minus)
    assert tr(alice_z_plus) == tr(alice_z_minus) == F(1, 2)

    # Conditioned on Alice Z+, Bob Z- is certain and Bob Z+ is impossible.
    joint_plus_minus = tr(instrument(alice_z_plus, z_minus, on_alice=False))
    joint_plus_plus = tr(instrument(alice_z_plus, z_plus, on_alice=False))
    assert joint_plus_minus == F(1, 2)
    assert joint_plus_plus == 0

    nonselective_alice_z = add(alice_z_plus, alice_z_minus)
    bob_after = partial_trace_alice(nonselective_alice_z)
    maximally_mixed = [[F(1, 2), F(0)], [F(0), F(1, 2)]]
    assert bob_after == maximally_mixed

    # Z then Z is repeatable.
    zz_same = tr(instrument(alice_z_plus, z_plus)) / tr(alice_z_plus)
    zz_flip = tr(instrument(alice_z_plus, z_minus)) / tr(alice_z_plus)
    assert zz_same == 1 and zz_flip == 0

    # Insert an unread X measurement between the two Z measurements.
    after_x_unread = add(instrument(alice_z_plus, x_plus), instrument(alice_z_plus, x_minus))
    zxz_same = tr(instrument(after_x_unread, z_plus)) / tr(alice_z_plus)
    zxz_flip = tr(instrument(after_x_unread, z_minus)) / tr(alice_z_plus)
    assert zxz_same == zxz_flip == F(1, 2)

    result = {
        "schema": "marici.aspect.bell-sequential-polarization-instrument.v1",
        "status": "pass",
        "alice_first_z_probabilities": [encode(tr(alice_z_plus)), encode(tr(alice_z_minus))],
        "conditional_bob_opposite_probability": encode(joint_plus_minus / tr(alice_z_plus)),
        "conditional_bob_same_probability": encode(joint_plus_plus),
        "bob_nonselective_reduced_state": [[encode(x) for x in row] for row in bob_after],
        "zz_repeat_probability": encode(zz_same),
        "zxz_repeat_probability": encode(zxz_same),
        "zxz_flip_probability": encode(zxz_flip),
        "local_sequential_test_excludes_invasive_hidden_memory": False,
        "classical_comparison_required_for_joint_correlators": True,
        "claim_boundary": "finite exact two-basis polarization instrument",
    }
    output = Path(__file__).parents[1] / "results" / "bell_sequential_polarization_instrument.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
