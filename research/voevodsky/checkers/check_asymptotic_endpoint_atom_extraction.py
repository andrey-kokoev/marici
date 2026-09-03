from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


CONTRACT = Path("research/voevodsky/asymptotic-endpoint-atom-extraction-v1.json")


def moments(atoms: list[tuple[sp.Rational, sp.Rational]], count: int) -> list[sp.Rational]:
    return [sum(weight * point**n for point, weight in atoms) for n in range(count)]


def hankel(sequence: list[sp.Rational], size: int) -> sp.Matrix:
    return sp.Matrix(size, size, lambda i, j: sequence[i + j])


def main() -> None:
    contract = json.loads(CONTRACT.read_text(encoding="utf-8"))
    Y = sp.Rational(2)
    c = sp.Rational(3)
    interior = [(sp.Rational(0), sp.Rational(5)), (sp.Rational(1), sp.Rational(7))]
    atoms = [(Y, c), *interior]
    sequence = moments(atoms, 20)

    # Exact normalized moments approach c; the residual is explicitly geometric.
    for n in range(10):
        normalized = sp.simplify(sequence[n] / Y**n)
        expected = c + sum(weight * (point / Y) ** n for point, weight in interior)
        assert normalized == expected

    residual_sequence = [sp.simplify(value - c * Y**n) for n, value in enumerate(sequence)]
    residual_expected = moments(interior, 20)
    assert residual_sequence == residual_expected
    for size in range(1, 10):
        assert hankel(residual_sequence, size).is_positive_semidefinite

    # Even asymptotics alone cannot distinguish the two endpoints.
    split_atoms = [(Y, sp.Rational(2)), (-Y, sp.Rational(1)), *interior]
    split = moments(split_atoms, 20)
    even_limit_target = sp.Rational(3)
    odd_limit_target = sp.Rational(1)
    for n in range(1, 8):
        even_normalized = sp.simplify(split[2 * n] / Y ** (2 * n))
        odd_normalized = sp.simplify(split[2 * n + 1] / Y ** (2 * n + 1))
        assert even_normalized - even_limit_target == sum(
            weight * (point / Y) ** (2 * n) for point, weight in interior
        )
        assert odd_normalized - odd_limit_target == sum(
            weight * (point / Y) ** (2 * n + 1) for point, weight in interior
        )

    result = {
        "schema":"marici.voevodsky.asymptotic-endpoint-atom-extraction-check.v1",
        "status":"endpoint_atom_extraction_fixture_verified",
        "full_sequence_endpoint_mass_extraction":True,
        "endpoint_subtraction_residual_PSD_ranks_checked":9,
        "even_only_sign_ambiguity_exhibited":True,
        "source_remainder_hankel_PSD":False,
        "source_decay_to_moment_asymptotic":False,
        "rh_implication":False,
        "acceptance_test":contract["acceptance_test"],
        "passed":True
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
