"""WP361: exact authority audit for dimensional closure of the CP portal."""

import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]


def main():
    Q, M2, alpha, lam = sp.symbols("Q M2 alpha lambda", positive=True)
    U = sp.symbols("U", real=True, negative=True)
    J = sp.symbols("J", real=True)

    rho = Q / M2
    portal = lam * (J**2 - alpha * rho) ** 2
    shell = alpha * rho
    shell_via_U = -alpha / U
    response_alpha = sp.diff(shell, alpha)
    response_U = sp.diff(shell_via_U, U)
    q_mass_dimension = sp.Integer(2)
    m2_mass_dimension = sp.Integer(2)
    rho_mass_dimension = q_mass_dimension - m2_mass_dimension

    source_a = {Q: 1, M2: 4}
    source_b = {Q: 2, M2: 8}
    canonical_W = 3 * M2 / (4 * Q**2)
    rho_a, rho_b = sp.simplify(rho.subs(source_a)), sp.simplify(rho.subs(source_b))
    W_a, W_b = sp.simplify(canonical_W.subs(source_a)), sp.simplify(canonical_W.subs(source_b))

    checks = {
        "ratio_is_dimensionless_by_equal_source_dimensions": rho_mass_dimension == 0,
        "portal_is_nonnegative": portal.is_nonnegative,
        "ratio_equals_minus_inverse_quartic": sp.simplify(rho.subs(M2, -U * Q) + 1 / U) == 0,
        "shell_responds_to_dimensionless_matching": response_alpha == rho,
        "shell_responds_to_source_quartic": response_U == alpha / U**2,
        "source_hostile_pair_has_equal_ratio": rho_a == rho_b == sp.Rational(1, 4),
        "source_hostile_pair_has_distinct_sextic_coordinate": W_a == 3 and W_b == sp.Rational(3, 2) and W_a != W_b,
        "portal_collapses_hostile_source_pair": sp.simplify(shell.subs(source_a) - shell.subs(source_b)) == 0,
        "deliberate_unit_normalization_is_not_unique": (
            sp.simplify(shell.subs({Q: 1, M2: 4, alpha: 1}) - shell.subs({Q: 1, M2: 4, alpha: 2})) != 0
        ),
    }
    checks = {name: bool(value) for name, value in checks.items()}

    result = {
        "work_package": "WP361",
        "admitted_state_domain": "positive canonical source readouts Q and M2, negative canonical quartic U=-M2/Q, and positive dimensionless matching alpha",
        "faithful_quotient_coordinate": "full physical16 downstream and the WP359 source quotient (Q,M2) upstream; the portal factors through rho=Q/M2 and J^2",
        "source_authorized_probe_family": "dimensionally closed invariant portals lambda*(J^2-alpha*Q/M2)^2 for alpha>0",
        "contextual_partition": "source packets with equal Q/M2 and physical points with equal J^2 are contextually equivalent to the portal",
        "classification": "conditional codimension-one selector and shell rigidifier; neither numerical selector nor faithful source identifier",
        "rho": str(rho),
        "rho_via_canonical_quartic": str(-1 / U),
        "portal": str(portal),
        "selected_shell_J2": str(shell),
        "responses": {"d_J2_d_alpha": str(response_alpha), "d_J2_d_U": str(response_U)},
        "hostile_source_pair": {
            "source_a": {"Q": 1, "M2": 4, "rho": str(rho_a), "W": str(W_a)},
            "source_b": {"Q": 2, "M2": 8, "rho": str(rho_b), "W": str(W_b)},
        },
        "smallest_exact_falsifier": "alpha=1 and alpha=2 obey identical symmetry and dimensional gates but select distinct J^2 shells for the same Q/M2",
        "remaining_physical_instrument_gate": "derive alpha from microscopic matching or a Ward identity and jointly calibrate Q, M2, and J^2; dimensional analysis alone cannot grant unit normalization",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = ROOT / "results/wp361_dimensionless_portal_normalization.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
