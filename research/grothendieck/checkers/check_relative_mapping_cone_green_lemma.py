from fractions import Fraction
import json

a = Fraction(1, 3)
E = Fraction(2)
B = Fraction(5)

# Choose F so the direct identity holds off seam.
F = (B - 2 * a * E) / 2

direct_lhs = 2 * a * E
direct_rhs = B - 2 * F
dual_lhs = 2 * a * E
dual_rhs = -B + 2 * F
coupled_residual = direct_lhs + dual_lhs
coupled_boundary = direct_rhs + dual_rhs

checks = {
    "direct_off_seam_identity_can_hold": direct_lhs == direct_rhs,
    "same_packet_dual_identity_then_fails_off_seam": dual_lhs != dual_rhs,
    "oriented_boundary_packets_cancel": coupled_boundary == 0,
    "coupled_bulk_residual_is_four_a_E": coupled_residual == 4 * a * E,
    "positive_energy_forces_a_zero_if_both_identities_hold": E > 0 and coupled_residual != 0,
}

out = {
    "schema": "marici.grothendieck.relative-mapping-cone-green-lemma.v1",
    "passed": all(checks.values()),
    "checks": checks,
    "witness": {
        "a": str(a), "E": str(E), "B": str(B), "F": str(F),
        "direct_lhs": str(direct_lhs), "direct_rhs": str(direct_rhs),
        "dual_lhs": str(dual_lhs), "dual_rhs": str(dual_rhs),
        "coupled_bulk_residual": str(coupled_residual),
        "coupled_boundary": str(coupled_boundary),
    },
}

print(json.dumps(out, indent=2, sort_keys=True))
raise SystemExit(0 if out["passed"] else 1)

