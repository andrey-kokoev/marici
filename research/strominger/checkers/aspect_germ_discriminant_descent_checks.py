import json
from pathlib import Path


MODULUS = 7


def invariants(action):
    return tuple(x for x in range(MODULUS) if (action * x - x) % MODULUS == 0)


def completed_packet(coefficient_parity):
    # Premature completion deliberately forgets coefficient_parity.
    return {
        "frame": ((2, 7), (3, 7)),
        "coefficient_group": "Z/7",
        "orbit": "free_C2_orbit",
        "reduced_generator": (1, -1),
    }


def target_descent(coefficient_parity):
    orbit_parity = -1
    diagonal_action = coefficient_parity * orbit_parity
    return invariants(diagonal_action)


plus_completed = completed_packet(1)
minus_completed = completed_packet(-1)
plus_descent = target_descent(1)
minus_descent = target_descent(-1)

same_completion_fiber = plus_completed == minus_completed
different_target_values = plus_descent != minus_descent
kernel_pair_descent_fails = same_completion_fiber and different_target_values

gates = [
    same_completion_fiber,
    plus_descent == (0,),
    minus_descent == tuple(range(7)),
    different_target_values,
    kernel_pair_descent_fails,
]

result = {
    "schema": "marici.strominger.aspect_germ_discriminant_descent.v1",
    "theorem_form": "target_factors_through_q_iff_constant_on_kernel_pair_of_q",
    "same_completion_fiber": same_completion_fiber,
    "plus_coefficient_parity": {
        "combined_action": -1,
        "invariants": plus_descent,
        "invariant_order": len(plus_descent),
    },
    "minus_coefficient_parity": {
        "combined_action": 1,
        "invariants": minus_descent,
        "invariant_order": len(minus_descent),
    },
    "kernel_pair_descent_fails": kernel_pair_descent_fails,
    "first_nonfaithful_arrow": "forget_coefficient_involution",
    "required_mate": "coefficient_parity_times_orbit_parity",
    "unresolved_source_calculation": "reflection_action_on_affine_discriminant_generator",
    "gates_passed": sum(gates),
    "gates_total": len(gates),
    "all_passed": all(gates),
}

output = Path(__file__).parents[1] / "results" / "aspect_germ_discriminant_descent_checks.json"
output.write_text(json.dumps(result, indent=2) + "\n", encoding="ascii")
print(json.dumps(result, indent=2))
raise SystemExit(0 if all(gates) else 1)
