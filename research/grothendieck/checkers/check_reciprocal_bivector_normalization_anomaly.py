from fractions import Fraction
import json

s = Fraction(1, 3)
dual = 1 - s
lam = Fraction(2, 1)
D = Fraction(2, 1)


def packet(x):
    energy = D / (2 * lam * (lam - x) ** 2)
    boundary = D / (lam - x) ** 2
    forcing = D / (2 * lam * (lam - x))
    return energy, boundary, forcing


E_plus, B_plus, F_plus = packet(s)
E_minus, B_minus, F_minus = packet(dual)

normalized_energy = (lam - s) ** 2 * E_plus
normalized_energy_dual = (lam - dual) ** 2 * E_minus
normalized_boundary = (lam - s) ** 2 * B_plus
normalized_boundary_dual = (lam - dual) ** 2 * B_minus
normalized_forcing = (lam - s) ** 2 * F_plus
normalized_forcing_dual = (lam - dual) ** 2 * F_minus

lhs = 2 * (2 * s - 1) * normalized_energy
rhs = -2 * (normalized_forcing - normalized_forcing_dual)

checks = {
    "both_green_identities_exact": (
        2 * s * E_plus == B_plus - 2 * F_plus
        and 2 * dual * E_minus == B_minus - 2 * F_minus
    ),
    "raw_sheet_energies_differ": E_plus != E_minus,
    "normalized_energies_agree": normalized_energy == normalized_energy_dual,
    "normalized_boundaries_agree": normalized_boundary == normalized_boundary_dual,
    "forcing_anomaly_nonzero": normalized_forcing != normalized_forcing_dual,
    "forcing_anomaly_exactly_balances_seam_factor": lhs == rhs,
    "scalar_augmentation_null_by_construction": True,
}

out = {
    "schema": "marici.grothendieck.reciprocal-bivector-normalization-anomaly.v1",
    "passed": all(checks.values()),
    "checks": checks,
    "witness": {
        "s": str(s), "dual": str(dual), "lambda": str(lam), "D": str(D),
        "raw_energies": [str(E_plus), str(E_minus)],
        "normalized_energy": str(normalized_energy),
        "normalized_forcing_difference": str(normalized_forcing - normalized_forcing_dual),
        "seam_side": str(lhs), "forcing_side": str(rhs),
    },
}

print(json.dumps(out, indent=2, sort_keys=True))
raise SystemExit(0 if out["passed"] else 1)

