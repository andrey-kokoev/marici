"""Exact WP453 hostile physical16 fiber for the WP448 current kernel."""

import json
from pathlib import Path

import sympy as sp


root = Path(__file__).resolve().parents[1]
wp448 = json.loads((root / "results" / "wp448_triplet_pole_residue_packet.json").read_text(encoding="utf-8"))
wp450 = json.loads((root / "results" / "wp450_messenger_word_grammar.json").read_text(encoding="utf-8"))
I = sp.I
lambdas = [
    sp.Matrix([[0, 1, 0], [1, 0, 0], [0, 0, 0]]),
    sp.Matrix([[0, -I, 0], [I, 0, 0], [0, 0, 0]]),
    sp.diag(1, -1, 0),
    sp.Matrix([[0, 0, 1], [0, 0, 0], [1, 0, 0]]),
    sp.Matrix([[0, 0, -I], [0, 0, 0], [I, 0, 0]]),
    sp.Matrix([[0, 0, 0], [0, 0, 1], [0, 1, 0]]),
    sp.Matrix([[0, 0, 0], [0, 0, -I], [0, I, 0]]),
    sp.diag(1, 1, -2)/sp.sqrt(3),
]
T = [matrix/2 for matrix in lambdas]
K_inverse = sp.Matrix([[sp.sympify(x) for x in row] for row in wp448["zero_momentum_kernel"]])

c = 1/sp.sqrt(2)
W = sp.Matrix([[c, 0, c], [0, 1, 0], [-c, 0, c]])
Y_u = sp.diag(1, 2, 3)
Y_d = sp.diag(4, 5, 6)
Y_u_rotated = sp.simplify(W*Y_u*W.conjugate().T)
Y_d_rotated = sp.simplify(W*Y_d*W.conjugate().T)

def delta_f_two_coefficient(diagonalizer, i, j):
    mass_generators = [sp.simplify(diagonalizer.conjugate().T*generator*diagonalizer) for generator in T]
    transition = sp.Matrix([generator[i, j] for generator in mass_generators])
    return sp.simplify((transition.T*K_inverse*transition)[0])


coefficient_original = delta_f_two_coefficient(sp.eye(3), 0, 1)
coefficient_rotated = delta_f_two_coefficient(W, 0, 1)
ckm_original = sp.eye(3)
ckm_rotated = sp.simplify(W.conjugate().T*W)

checks = {
    "wp448_dependency_passed": wp448["passed"],
    "wp450_universal_word_capacity_passed": wp450["passed"],
    "hostile_rotation_is_unitary": W.conjugate().T*W == sp.eye(3),
    "up_spectra_are_identical": Y_u.charpoly().as_expr() == Y_u_rotated.charpoly().as_expr(),
    "down_spectra_are_identical": Y_d.charpoly().as_expr() == Y_d_rotated.charpoly().as_expr(),
    "ckm_records_are_identical": ckm_original == ckm_rotated,
    "original_deltaF2_coefficient_vanishes": coefficient_original == 0,
    "rotated_deltaF2_coefficient_is_nonzero": coefficient_rotated == -sp.Rational(1, 6),
    "current_readout_separates_the_hostile_pair": coefficient_original != coefficient_rotated,
}
checks = {name: bool(value) for name, value in checks.items()}

result = {
    "work_package": "WP453",
    "admitted_domain": "WP447 fixed flavon vacuum plus WP450 universal degree-two messenger coefficient family.",
    "physical16_projection": "Quark singular spectra and relative up/down mixing, invariant under common conjugation of both Yukawas.",
    "hostile_pair": "(Y_u,Y_d) and (W Y_u W^dagger, W Y_d W^dagger) at fixed flavon vacuum, with W a 1-3 pi/4 rotation.",
    "shared_standard_model_record": {"up_eigenvalues": [1, 2, 3], "down_eigenvalues": [4, 5, 6], "CKM": "I"},
    "deltaF2_current_coefficients_before_common_factor": {"original_12": str(coefficient_original), "rotated_12": str(coefficient_rotated)},
    "current_common_factor": "-1/(2 mu^2)",
    "contextual_partition": "The WP448 current family strictly refines the Standard Model physical16 projection by resolving common Yukawa orientation relative to the flavon vacuum.",
    "selector_classification": "Current probe, not selector: it distinguishes extended-theory points but does not choose one.",
    "instrument": "Neutral-meson mixing is the relevant physical instrument class after flavor labels and hadronic matching are supplied.",
    "smallest_exact_falsifier": "Equality of the two exact Delta-F=2 coefficients for the hostile pair.",
    "remaining_gate": "Select or measure the messenger-coefficient orientation and perform RG/hadronic matching before applying calibrated neutral-meson limits.",
    "checks": checks,
    "passed": all(checks.values()),
}

out = root / "results" / "wp453_current_orientation_fiber.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)
