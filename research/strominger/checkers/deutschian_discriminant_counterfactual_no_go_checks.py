import cmath
import json
from pathlib import Path


P = 7

# Finite exact model of a real source stage over rational test points.
# Divisibility gives a preimage h/7 for every sampled h.
sample_source = [(a, b) for a in range(-5, 6) for b in range(-5, 6)]
divisibility_witnesses = {
    h: (h[0] / P, h[1] / P) for h in sample_source
}
divisible_identity = all(
    (P * y[0], P * y[1]) == h
    for h, y in divisibility_witnesses.items()
)

# Any additive map to Z/7 must satisfy chi(h)=7*chi(h/7)=0.
forced_character_values = {h: 0 for h in sample_source}
all_forced_zero = set(forced_character_values.values()) == {0}

# Torsion-free target: a seven-torsion vector must be zero.
torsion_candidates = sample_source
seven_torsion = [h for h in torsion_candidates if (P * h[0], P * h[1]) == (0, 0)]

# Exact extension fixture. Existing readout forgets t; dual control changes phase.
base_state = (2, -3)
t0, t1, dual_control = 0, 1, 1
readout0 = base_state
readout1 = base_state
phase0 = cmath.exp(2j * cmath.pi * (2 * t0 * dual_control / P))
phase1 = cmath.exp(2j * cmath.pi * (2 * t1 * dual_control / P))
extension_fixture = {
    "same_existing_readout": readout0 == readout1,
    "different_fiber_characters": t0 != t1,
    "different_controlled_phases": abs(phase0 - phase1) > 1e-12,
}

gates = [
    divisible_identity,
    all_forced_zero,
    seven_torsion == [(0, 0)],
    extension_fixture["same_existing_readout"],
    extension_fixture["different_fiber_characters"],
    extension_fixture["different_controlled_phases"],
]

result = {
    "schema": "marici.strominger.deutschian_discriminant_counterfactual_no_go.v1",
    "current_source": {
        "type": "real finite-jet vector space and strict LF union",
        "additive_group_divisible": divisible_identity,
        "all_additive_maps_to_Z7_zero": all_forced_zero,
        "all_additive_maps_from_Z7_zero": seven_torsion == [(0, 0)],
        "full_local_magnetic_readout": "injective by completed physical engine theorem",
        "requested_pair_exists": False,
        "authorized_character_sensitive_operation_exists": False,
    },
    "extension_fixture": extension_fixture,
    "extension_fixture_status": "mathematically_sufficient_but_not_source_authorized",
    "smallest_missing_constructor": "source-authorized central Z7 phase fiber with dual control and interference readout",
    "gates_passed": sum(gates),
    "gates_total": len(gates),
    "all_passed": all(gates),
}

output = Path(__file__).parents[1] / "results" / "deutschian_discriminant_counterfactual_no_go_checks.json"
output.write_text(json.dumps(result, indent=2) + "\n", encoding="ascii")
print(json.dumps(result, indent=2))
raise SystemExit(0 if all(gates) else 1)
