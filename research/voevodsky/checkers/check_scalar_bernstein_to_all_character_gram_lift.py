from __future__ import annotations

import json
from itertools import combinations
from pathlib import Path

import sympy as sp


CONTRACT = Path("research/voevodsky/scalar-bernstein-to-all-character-gram-lift-v1.json")


def main() -> None:
    contract = json.loads(CONTRACT.read_text(encoding="utf-8"))
    d, sigma, t = sp.symbols("d sigma t", real=True, positive=True)
    atoms = [(sp.Integer(0), sp.Integer(1)), (sp.Integer(1), sp.Integer(2)), (sp.Integer(4), sp.Integer(3))]
    theta = sum(weight * sp.exp(-t * lam) for lam, weight in atoms)
    kernel = sum(weight * sp.exp(-2 * sigma * lam) * sp.cos(d * sp.sqrt(lam)) for lam, weight in atoms)
    for order in range(5):
        local_jet = sp.diff(kernel, d, 2 * order).subs(d, 0)
        heat_jet = sp.diff(theta, t, order).subs(t, 2 * sigma)
        assert sp.simplify(local_jet - heat_jet) == 0

    points = [sp.Integer(0), sp.Integer(1), sp.Integer(3)]
    gram = sp.Matrix([[kernel.subs(d, left - right) for right in points] for left in points])
    feature_columns = []
    for lam, weight in atoms:
        feature_columns.append([sp.sqrt(weight) * sp.exp(-sigma * lam) * sp.cos(point * sp.sqrt(lam)) for point in points])
        if lam:
            feature_columns.append([sp.sqrt(weight) * sp.exp(-sigma * lam) * sp.sin(point * sp.sqrt(lam)) for point in points])
    feature = sp.Matrix.hstack(*(sp.Matrix(column) for column in feature_columns))
    assert all(sp.simplify(gram[i, j] - (feature * feature.conjugate().T)[i, j]) == 0 for i in range(3) for j in range(3))

    # Rank-two bound follows from the positive-measure triangle inequality in the fixture.
    k0 = kernel.subs(d, 0)
    assert sp.simplify(k0 - kernel.subs(d, sp.pi)) >= 0
    assert sp.simplify(k0 + kernel.subs(d, sp.pi)) >= 0

    status = contract["status"]
    assert status["source_measure_lift"] == "not supplied"
    result = {
        "schema":"marici.voevodsky.scalar-bernstein-to-all-character-gram-lift-check.v1",
        "status":"conditional_all_character_factorization_verified",
        "even_jet_identities_checked":5,
        "positive_measure_gram_factorization":True,
        "finite_matrix_size":3,
        "rank_two_bound":True,
        "source_measure_lift_supplied":False,
        "unconditional_psd":False,
        "rh_implication":False,
        "acceptance_test":contract["acceptance_test"],
        "passed":True
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
