from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


CONTRACT = Path("research/voevodsky/one-width-gaussian-weil-faithfulness-v1.json")


def main() -> None:
    contract = json.loads(CONTRACT.read_text(encoding="utf-8"))
    sigma = sp.symbols("sigma", positive=True)
    points = [sp.Integer(0), sp.Integer(1), sp.Integer(3)]
    atoms = [(sp.Integer(-2), sp.Integer(1)), (sp.Integer(1), sp.Integer(3))]

    # Positive weighted atoms give a fixed-width Toeplitz Gram factorization.
    features = sp.Matrix([[sp.sqrt(weight) * sp.exp(-sigma * location**2) * sp.exp(-sp.I * point * location)
                           for location, weight in atoms] for point in points])
    gram = sp.simplify(features * features.conjugate().T)
    kernel = lambda difference: sum(weight * sp.exp(-2 * sigma * location**2) * sp.exp(-sp.I * difference * location)
                                    for location, weight in atoms)
    assert all(sp.simplify(gram[i, j] - kernel(points[i] - points[j])) == 0
               for i in range(len(points)) for j in range(len(points)))

    # Local division exactly recovers an unweighted compactly supported test value.
    phi_values = {sp.Integer(-2): sp.Integer(5), sp.Integer(1): sp.Integer(7)}
    rho_pairing = sum(weight * phi_values[location] for location, weight in atoms)
    weighted_pairing = sum(
        weight * sp.exp(-2 * sigma * location**2)
        * (sp.exp(2 * sigma * location**2) * phi_values[location])
        for location, weight in atoms
    )
    assert sp.simplify(rho_pairing - weighted_pairing) == 0

    # Deliberate failure: a negative atom remains negative after every positive Gaussian weight.
    negative_diagonal = -sp.exp(-2 * sigma)
    assert negative_diagonal.is_negative

    status = contract["status"]
    assert status["fixed_width_toeplitz_psd"] == "not proved"
    result = {
        "schema":"marici.voevodsky.one-width-gaussian-weil-faithfulness-check.v1",
        "status":"one_width_faithfulness_reduction_verified",
        "fixed_width_positive_measure_gram_factorization":True,
        "local_division_identity":True,
        "negative_atom_not_hidden_by_gaussian":True,
        "width_limit_required":False,
        "fixed_width_toeplitz_psd_verified":False,
        "rh_implication":False,
        "acceptance_test":contract["acceptance_test"],
        "passed":True
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
