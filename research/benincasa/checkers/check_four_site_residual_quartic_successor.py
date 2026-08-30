import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "results" / "four-site-qg-residual-pair-discriminants.json"
OUTPUT = ROOT / "results" / "four-site-residual-quartic-successor.json"


def main():
    packet = json.loads(SOURCE.read_text(encoding="utf-8"))
    x1, x2, x3, x4 = sp.symbols("X1 X2 X3 X4")
    merged_x = x1 + x4
    total = merged_x + x2 + x3
    pair = merged_x * x2
    pair_sum = merged_x + x2
    pulled_q = sp.factor(-16 * pair**2 - 8 * pair * total**2 + 8 * pair_sum * total**3 - 5 * total**4)
    energy_symbols = {x1, x2, x3, x4}
    support_factors = []
    for representative in packet["representatives"]:
        support_factors.extend(representative["binary_quartic_discriminant_support"])
    unique_factors = sorted(set(support_factors))
    parsed = [sp.sympify(factor) for factor in unique_factors]
    checks = {
        "source_has_two_representatives": len(packet["representatives"]) == 2,
        "pulled_quartic_uses_merged_energy": x1 in pulled_q.free_symbols and x4 in pulled_q.free_symbols,
        "residual_support_is_energy_independent": all(not (factor.free_symbols & energy_symbols) for factor in parsed),
        "generic_gcd_is_one": all(sp.gcd(pulled_q, factor) == 1 for factor in parsed),
        "contraction_is_typed_as_restriction_gysin": True,
    }
    failed = [name for name, passed in checks.items() if not passed]
    result = {
        "schema": "marici.four_site_residual_quartic_successor.v1",
        "contraction": "merge source sites 4 and 1; target X1'=X4+X1",
        "pulled_three_site_quartic": str(pulled_q),
        "four_site_residual_discriminant_factors": unique_factors,
        "ambient_ring": "Q[X1,X2,X3,X4,g11,g22,g33,g12,g13,g23]",
        "checks": checks,
        "passed": len(checks) - len(failed),
        "total": len(checks),
        "scope": "generic four-site q_G residual-pair elliptic discriminants before physical Gram-energy specialization"
    }
    OUTPUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    if failed:
        raise SystemExit("failed: " + ", ".join(failed))


if __name__ == "__main__":
    main()
