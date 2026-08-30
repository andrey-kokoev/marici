"""Exact WP610 spectral-projector portal and permutation-support obstruction."""

import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
ensemble = json.loads(
    (ROOT / "results" / "wp108_fdm2_ensemble_certificate_boundary.json").read_text(
        encoding="utf-8"
    )
)

up_values = [sp.Integer(1), sp.Integer(4), sp.Integer(9)]
down_values = [sp.Integer(16), sp.Integer(25), sp.Integer(36)]
hu = sp.diag(*up_values)


def polynomial_projectors(matrix, eigenvalues):
    projectors = []
    identity = sp.eye(matrix.rows)
    for index, eigenvalue in enumerate(eigenvalues):
        projector = identity
        for other_index, other in enumerate(eigenvalues):
            if index != other_index:
                projector = projector * (matrix - other * identity) / (
                    eigenvalue - other
                )
        projectors.append(sp.simplify(projector))
    return projectors


up_projectors = polynomial_projectors(hu, up_values)

forward = sp.Matrix([[0, 1, 0], [0, 0, 1], [1, 0, 0]])
hd_permutation = forward * sp.diag(*down_values) * forward.T
down_permutation_projectors = polynomial_projectors(hd_permutation, down_values)
permutation_overlap = sp.Matrix(
    3,
    3,
    lambda i, j: sp.simplify(sp.trace(up_projectors[i] * down_permutation_projectors[j])),
)
permutation_commutator = sp.simplify(hu * hd_permutation - hd_permutation * hu)

omega = -sp.Rational(1, 2) + sp.I * sp.sqrt(3) / 2
fourier = sp.Matrix(
    [[omega ** (row * column) / sp.sqrt(3) for column in range(3)] for row in range(3)]
)
hd_fourier = sp.simplify(fourier * sp.diag(*down_values) * fourier.conjugate().T)
down_fourier_projectors = polynomial_projectors(hd_fourier, down_values)
fourier_overlap = sp.Matrix(
    3,
    3,
    lambda i, j: sp.simplify(sp.trace(up_projectors[i] * down_fourier_projectors[j])),
)
fourier_j = sp.simplify(
    sp.im(
        fourier[0, 0]
        * fourier[1, 1]
        * sp.conjugate(fourier[0, 1])
        * sp.conjugate(fourier[1, 0])
    )
)
fourier_commutator = sp.simplify(hu * hd_fourier - hd_fourier * hu)

# Exact common-left weak-basis covariance and overlap invariance.
q = sp.Matrix(
    [[sp.Rational(3, 5), sp.Rational(4, 5), 0],
     [-sp.Rational(4, 5), sp.Rational(3, 5), 0],
     [0, 0, 1]]
)
rotated_up_projectors = [sp.simplify(q * projector * q.T) for projector in up_projectors]
rotated_down_projectors = [
    sp.simplify(q * projector * q.T) for projector in down_fourier_projectors
]
rotated_overlap = sp.Matrix(
    3,
    3,
    lambda i, j: sp.simplify(
        sp.trace(rotated_up_projectors[i] * rotated_down_projectors[j])
    ),
)

checks = {
    "polynomial_up_projectors_are_rank_one_resolution": sum(
        up_projectors, sp.zeros(3)
    )
    == sp.eye(3)
    and all(projector.rank() == 1 for projector in up_projectors),
    "permutation_overlap_is_exact_matching": permutation_overlap == forward,
    "permutation_matching_forces_commuting_grams": permutation_commutator
    == sp.zeros(3),
    "fourier_overlap_has_full_one_third_support": fourier_overlap
    == sp.ones(3) / 3,
    "fourier_overlap_is_doubly_stochastic": all(
        sum(fourier_overlap[row, column] for column in range(3)) == 1
        for row in range(3)
    )
    and all(
        sum(fourier_overlap[row, column] for row in range(3)) == 1
        for column in range(3)
    ),
    "fourier_point_has_nonzero_cp_invariant": fourier_j == sp.sqrt(3) / 18,
    "fourier_grams_do_not_commute": fourier_commutator != sp.zeros(3),
    "overlap_is_weak_basis_invariant": rotated_overlap == fourier_overlap,
    "complete_fitted_ensemble_has_nonzero_j": ensemble["qualitative_prediction"]
    == {
        "claim": "J!=0",
        "passes": 1210,
        "total": 1210,
        "min_abs_J": 3.1413288219332114e-05,
    },
}

if not all(checks.values()):
    raise SystemExit(f"WP610 check failed: {checks}")

result = {
    "work_package": "WP610",
    "status": "PASS",
    "checks": {key: bool(value) for key, value in checks.items()},
    "admitted_state_domain": "nondegenerate ordered up- and down-type Yukawa Gram spectra on physical16",
    "faithful_port_coordinate": "W_ij=Tr(P_i^u P_j^d)=abs(V_ij)^2, measured by charged-current transitions",
    "descent": "spectral projectors transform by common weak-basis conjugation and W is invariant",
    "contextual_partition": "one charged-current overlap matrix records the relative spectral frames; exact permutation support is the commuting J=0 stratum",
    "hostile_physical_point": "the exact Fourier mixing point has W_ij=1/3 and J=sqrt(3)/18",
    "ensemble_result": "all 1210 stored fitted sheets have nonzero J, with minimum absolute J 3.1413288219332114e-05",
    "classification": "the spectral-projector portal is a physical readout and common-port instrument, but it falsifies rather than realizes exact anchored permutation support",
    "smallest_exact_falsifier": "one nonzero off-permutation charged-current overlap; nonzero J is a stronger invariant falsifier",
    "source_gate": "WP609's D and K must be additional source operations, not reinterpreted copies of the single Standard Model charged-current overlap",
    "alternating_carrier_gate": "mass ordering supplies port names but does not derive Nima's alternating cubic source carrier or distinguish its two orientation orbits dynamically",
    "remaining_instrument_gate": "resolve any new anchor and forward mediator channels independently while retaining the same spectral-projector port identities and temporal phase record",
}

out = ROOT / "results" / "wp610_spectral_projector_matching_obstruction.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
