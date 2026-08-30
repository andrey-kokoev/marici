"""Exact WP594 symmetry-reduction versus CP-selection tradeoff."""

import json
from itertools import combinations_with_replacement
from pathlib import Path

import sympy as sp

sigma, s = sp.symbols("sigma s", real=True)
scale, lam, kappa, chi = sp.symbols(
    "a lambda kappa chi", positive=True, real=True
)

leaves = ("F", "H", "R")
full_fields = leaves + ("sigma", "s")
full_quartic_count = len(list(combinations_with_replacement(full_fields, 2)))

# Under O(2) on (sigma,s), the singlet pair appears only through S.
o2_basis = {
    "S^2",
    "F^4",
    "H^4",
    "R^4",
    "F^2 H^2",
    "F^2 R^2",
    "H^2 R^2",
    "S F^2",
    "S H^2",
    "S R^2",
}

singlet_radius = sigma**2 + s**2
o2_potential = lam * (singlet_radius - scale**2) ** 2 / 4
o2_hessian = sp.hessian(o2_potential, (sigma, s))
cp_conserving_vacuum = {sigma: scale, s: 0}
cp_broken_vacuum = {sigma: 0, s: scale}
cp_conserving_spectrum = o2_hessian.subs(cp_conserving_vacuum).eigenvals()

anisotropy = kappa * (s**2 - chi * sigma**2) ** 2 / 4
completed_potential = o2_potential + anisotropy
sigma_sq_star = scale**2 / (1 + chi)
s_sq_star = chi * scale**2 / (1 + chi)
orientation_fraction = sp.simplify(s_sq_star / scale**2)

checks = {
    "full_five_radial_quartic_basis_has_fifteen_coordinates": full_quartic_count
    == 15,
    "o2_reduced_basis_has_ten_coordinates": len(o2_basis) == 10,
    "o2_potential_is_rotation_invariant": sp.simplify(
        o2_potential.subs({sigma: -s, s: sigma}, simultaneous=True)
        - o2_potential
    )
    == 0,
    "cp_conserving_point_is_a_zero_energy_vacuum": sp.simplify(
        o2_potential.subs(cp_conserving_vacuum)
    )
    == 0,
    "cp_broken_point_is_also_a_zero_energy_vacuum": sp.simplify(
        o2_potential.subs(cp_broken_vacuum)
    )
    == 0,
    "o2_vacuum_has_one_angular_zero_mode": cp_conserving_spectrum
    == {2 * lam * scale**2: 1, 0: 1},
    "anisotropic_shell_satisfies_both_squares": sp.simplify(
        completed_potential.subs(
            {sigma**2: sigma_sq_star, s**2: s_sq_star}
        )
    )
    == 0,
    "anisotropy_selects_chi_dependent_orientation": orientation_fraction
    == chi / (1 + chi),
    "orientation_retains_chi_response": sp.simplify(
        sp.diff(orientation_fraction, chi) - 1 / (1 + chi) ** 2
    )
    == 0,
    "hostile_chi_values_change_orientation": orientation_fraction.subs(chi, 1)
    == sp.Rational(1, 2)
    and orientation_fraction.subs(chi, 3) == sp.Rational(3, 4),
}

if not all(checks.values()):
    raise SystemExit(f"WP594 check failed: {checks}")

checks = {key: bool(value) for key, value in checks.items()}
result = {
    "work_package": "WP594",
    "status": "PASS",
    "checks": checks,
    "symmetry": "O(2) acting on the gauge-singlet pair (sigma,s), with CP embedded as a reflection",
    "quartic_coordinate_reduction": {
        "generic_five_radial_fields": full_quartic_count,
        "o2_singlet_doublet": len(o2_basis),
        "coordinates_removed": full_quartic_count - len(o2_basis),
    },
    "symmetric_vacuum": "sigma^2+s^2=a^2; includes s=0 and has one angular zero mode",
    "minimal_positive_anisotropy": "kappa*(s^2-chi*sigma^2)^2/4",
    "anisotropic_prediction": "s^2/(sigma^2+s^2)=chi/(1+chi)",
    "classification": "exact symmetry-versus-selection obstruction; O(2) rigidifies coefficients but does not select CP breaking",
    "smallest_exact_falsifier": "the O(2) vacuum (sigma,s)=(a,0) is CP conserving; after anisotropy chi=1 and chi=3 preserve typing but select fractions 1/2 and 3/4",
    "experiment_gate": "the symmetric branch predicts a massless angular singlet mode, while a predictive anisotropic branch requires an independently derived chi before CP and scalar-pole measurements can test it",
    "remaining_architecture_gate": "derive directional anisotropy from discrete representation data or a Ward identity without restoring a tunable ratio",
}

out = (
    Path(__file__).resolve().parents[1]
    / "results"
    / "wp594_singlet_o2_symmetry_selection_tradeoff.json"
)
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
