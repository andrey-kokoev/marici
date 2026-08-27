import json
from pathlib import Path


def fixed_points(n, action):
    return [x for x in range(n) if (action * x - x) % n == 0]


def coinvariant_order(n, action):
    image = {(action * x - x) % n for x in range(n)}
    return n // len(image)


rows = []
gates = []
for n in (3, 5, 7, 9, 11, 14):
    for coefficient_parity in (1, -1):
        combined_action = -coefficient_parity
        invariants = fixed_points(n, combined_action)
        coinvariants = coinvariant_order(n, combined_action)
        row = {
            "modulus": n,
            "coefficient_parity": coefficient_parity,
            "combined_action": combined_action,
            "invariant_order": len(invariants),
            "coinvariant_order": coinvariants,
        }
        rows.append(row)
        if n % 2 == 1:
            expected = n if coefficient_parity == -1 else 1
            gates.append(len(invariants) == expected)
            gates.append(coinvariants == expected)

# Magnetic affine frame and its canonical cokernel functional.
F = ((2, 7), (3, 7))
determinant = F[0][0] * F[1][1] - F[0][1] * F[1][0]
functional_annihilates_columns = all(
    (3 * F[0][j] - 2 * F[1][j]) % 7 == 0 for j in range(2)
)
gates.extend([determinant == -7, functional_annihilates_columns])

# Same frame and orbit, different coefficient action, different descent.
seven_rows = [row for row in rows if row["modulus"] == 7]
hostile_pair_changes_descent = {
    (row["invariant_order"], row["coinvariant_order"]) for row in seven_rows
} == {(1, 1), (7, 7)}
gates.append(hostile_pair_changes_descent)

result = {
    "schema": "marici.strominger.discriminant_orbit_local_system.v1",
    "affine_frame": F,
    "determinant": determinant,
    "functional_annihilates_columns_mod_7": functional_annihilates_columns,
    "descent_rows": rows,
    "hostile_pair_changes_descent": hostile_pair_changes_descent,
    "semantic_fields": {
        "bare_tensor_is_equivariantly_incomplete": True,
        "missing_constructor": "coefficient_involution",
        "survival_rule": "relative_character_is_trivial",
        "odd_primary_clean_dichotomy": True,
        "even_primary_exception": "two_torsion_can_survive_sign_descent",
    },
    "gates_passed": sum(gates),
    "gates_total": len(gates),
    "all_passed": all(gates),
}

output = Path(__file__).parents[1] / "results" / "discriminant_orbit_local_system_checks.json"
output.write_text(json.dumps(result, indent=2) + "\n", encoding="ascii")
print(json.dumps(result, indent=2))
raise SystemExit(0 if all(gates) else 1)
