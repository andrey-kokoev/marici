"""Exact WP598 abelian-shaping overlap no-go."""

import json
from pathlib import Path

import sympy as sp


q_phi, q_psi = sp.symbols("q_phi q_psi", integer=True)
alpha, beta, eta = sp.symbols("alpha beta eta", real=True)

# A dagger reverses every additive abelian charge.  The overlap and its
# conjugate therefore have opposite charges for arbitrary charge assignments.
overlap_charge = -q_phi + q_psi
conjugate_overlap_charge = q_phi - q_psi
modulus_square_charge = sp.simplify(
    overlap_charge + conjugate_overlap_charge
)

# On the real angular slice, the invariant is the same overlap term that
# obstructs WP597.
overlap_modulus_real_slice = sp.cos(alpha - beta) ** 2
angular_gradient = sp.simplify(
    sp.Matrix(
        [
            sp.diff(eta * overlap_modulus_real_slice / 2, alpha),
            sp.diff(eta * overlap_modulus_real_slice / 2, beta),
        ]
    ).subs({alpha: 0, beta: sp.pi / 4})
)

finite_charge_census = []
for order in range(2, 13):
    all_neutral = all(
        int(modulus_square_charge.subs({q_phi: a, q_psi: b})) % order == 0
        for a in range(order)
        for b in range(order)
    )
    finite_charge_census.append(
        {"cyclic_order": order, "all_charge_pairs_leave_overlap_neutral": all_neutral}
    )

checks = {
    "overlap_modulus_has_identically_zero_additive_charge": (
        modulus_square_charge == 0
    ),
    "all_cyclic_charge_assignments_through_order_twelve_fail_to_forbid_it": all(
        item["all_charge_pairs_leave_overlap_neutral"]
        for item in finite_charge_census
    ),
    "real_slice_reproduces_wp597_angle_dependence": (
        overlap_modulus_real_slice == sp.cos(alpha - beta) ** 2
    ),
    "neutral_overlap_still_moves_axis_diagonal_candidate": angular_gradient
    == sp.Matrix([eta / 2, -eta / 2]),
    "deliberate_eta_one_witness_is_nonzero": angular_gradient.subs(eta, 1)
    == sp.Matrix([sp.Rational(1, 2), sp.Rational(-1, 2)]),
}

if not all(checks.values()):
    raise SystemExit(f"WP598 check failed: {checks}")

result = {
    "work_package": "WP598",
    "status": "PASS",
    "checks": {key: bool(value) for key, value in checks.items()},
    "domain": "two fields or multiplets with arbitrary additive charges under any product of abelian phase symmetries; renormalizable Hermitian scalar grammar",
    "charge_identity": "charge(|phi^dagger psi|^2)=(-q_phi+q_psi)+(q_phi-q_psi)=0",
    "finite_census": finite_charge_census,
    "classification": "abelian phase-shaping no-go for the WP597 overlap obstruction",
    "smallest_exact_falsifier": "for arbitrary q_phi and q_psi the overlap modulus has charge zero, and eta=1 gives gradient (1/2,-1/2)",
    "surviving_architecture_gate": "use a non-abelian product-selection rule, source-derived sequestering or locality, or a representation for which the dangerous singlet is absent; then enumerate the complete invariant ring",
    "instrument_gate": "unchanged: the protecting constructor and CP-odd physical16 portal must share a calibrated executable readout",
}

out = (
    Path(__file__).resolve().parents[1]
    / "results"
    / "wp598_abelian_shaping_overlap_no_go.json"
)
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
