"""WP260: exact audit of commutator-gradient flavor alignment."""

import json
from itertools import combinations
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]


def dagger(matrix):
    return matrix.conjugate().T


def hs_norm2(matrix):
    return sp.simplify(sp.trace(dagger(matrix) * matrix))


def channel(projectors, eigenvalues, matrix, powers):
    result = sp.zeros(3)
    for i, projector_i in enumerate(projectors):
        for j, projector_j in enumerate(projectors):
            gap2 = (eigenvalues[i] - eigenvalues[j]) ** 2
            result += sp.Rational(1, 2) ** (powers * gap2) * projector_i * matrix * projector_j
    return sp.simplify(result)


def main():
    eigenvalues = [0, 1, 2]
    hu = sp.diag(*eigenvalues)
    projectors = [sp.diag(1, 0, 0), sp.diag(0, 1, 0), sp.diag(0, 0, 1)]
    hd = sp.Matrix([[4, 1, 2], [1, 5, 3], [2, 3, 9]])
    q = sp.Matrix([[sp.Rational(3, 5), sp.Rational(4, 5), 0],
                   [-sp.Rational(4, 5), sp.Rational(3, 5), 0], [0, 0, 1]])

    phi_1 = channel(projectors, eigenvalues, hd, 1)
    phi_2 = channel(projectors, eigenvalues, hd, 2)
    composed = channel(projectors, eigenvalues, phi_1, 1)
    pinched = sum((projector * hd * projector for projector in projectors), sp.zeros(3))

    generator = sp.zeros(3)
    for i, projector_i in enumerate(projectors):
        for j, projector_j in enumerate(projectors):
            generator -= (eigenvalues[i] - eigenvalues[j]) ** 2 * projector_i * hd * projector_j
    double_commutator = -(hu * (hu * hd - hd * hu) - (hu * hd - hd * hu) * hu)

    kernel = sp.Matrix([[sp.Rational(1, 2) ** ((a - b) ** 2) for b in eigenvalues] for a in eigenvalues])
    principal_minors = []
    for size in (1, 2, 3):
        for indices in combinations(range(3), size):
            principal_minors.append(sp.factor(kernel.extract(indices, indices).det()))

    transformed_projectors = [q * projector * dagger(q) for projector in projectors]
    covariance = channel(transformed_projectors, eigenvalues, q * hd * dagger(q), 1) - q * phi_1 * dagger(q)
    commutator_before = hu * hd - hd * hu
    commutator_after = hu * phi_1 - phi_1 * hu
    finite_map_determinant = sp.prod(
        sp.Rational(1, 2) ** ((eigenvalues[i] - eigenvalues[j]) ** 2)
        for i in range(3) for j in range(3)
    )

    checks = {
        "gradient_generator_is_double_commutator": generator == double_commutator,
        "finite_channel_is_full_weak_basis_covariant": covariance == sp.zeros(3),
        "schur_kernel_is_positive_definite": all(minor > 0 for minor in principal_minors),
        "semigroup_composition_exact": composed == phi_2,
        "commutator_energy_strictly_decreases": hs_norm2(commutator_after) < hs_norm2(commutator_before),
        "finite_time_map_is_invertible": finite_map_determinant > 0,
        "finite_time_image_not_dimension_reducing": finite_map_determinant != 0,
        "asymptotic_image_is_proper_commutant": pinched != hd and hu * pinched == pinched * hu,
        "asymptotic_fixed_locus_erases_mixing": any(pinched[i, j] == 0 and hd[i, j] != 0 for i in range(3) for j in range(3)),
        "deliberate_finite_time_selector_claim_fails": phi_1 != pinched,
    }
    checks = {name: bool(value) for name, value in checks.items()}
    result = {
        "work_package": "WP260",
        "admitted_state_domain": "nondegenerate Hermitian Yukawa-Gram pairs with a candidate dynamical flavon interpretation",
        "faithful_quotient_coordinate": "physical16 modulo simultaneous full weak-basis conjugation",
        "candidate_source_geometry": "commutator energy ||[H_u,H_d]||_HS^2 / 2",
        "candidate_operation": "dH_d/dt = -[H_u,[H_u,H_d]]",
        "finite_time_test": "t = log(2)",
        "positive_kernel_exact": [[str(value) for value in kernel.row(i)] for i in range(3)],
        "positive_kernel_principal_minors_exact": [str(value) for value in principal_minors],
        "finite_map_determinant_exact": str(finite_map_determinant),
        "commutator_energy_before_exact": str(hs_norm2(commutator_before)),
        "commutator_energy_after_exact": str(hs_norm2(commutator_after)),
        "contextual_partition": "every finite-time map is injective on the ambient Hermitian space and preserves Gram-pair distinctions; only the infinite-time limit collapses them onto the commuting locus",
        "classification": "weak-basis-descending positive finite-time transport with no proper-subspace or point image, not a rigidifier; its asymptotic mathematical selector is uninstrumented and empirically selects trivial mixing",
        "first_nonfaithful_arrow": "finite executable evolution -> infinite-time pinching limit",
        "smallest_exact_falsifier": "at t=log(2) the channel determinant is nonzero, so its image is not proper; one nonzero CKM mixing entry falsifies the proposed asymptotic fixed-point law",
        "remaining_physical_instrument_gate": "derive a dynamical flavon substrate, finite-time stopping/stabilization law, and nontrivial-mixing fixed locus from one source action before flavor readout",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = ROOT / "results/wp260_commutator_gradient_selector.json"
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
