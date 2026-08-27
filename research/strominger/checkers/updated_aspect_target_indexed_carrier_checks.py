import json
from collections import Counter
from pathlib import Path


P = 7
PLANE = [(x, y) for x in range(P) for y in range(P)]


def ell(x, y):
    return (3 * x - 2 * y) % P


def ell_x(x, y):
    return (3 * y - 2 * x) % P


def q_minus(x, y):
    return (ell(x, y) - ell_x(x, y)) % P


def q_plus(x, y):
    return (ell(x, y) + ell_x(x, y)) % P


odd_kernel = [v for v in PLANE if q_minus(*v) == 0]
joint_kernel = [v for v in PLANE if ell(*v) == 0 and ell_x(*v) == 0]
odd_image = {q_minus(*v) for v in PLANE}
joint_image = {(ell(*v), ell_x(*v)) for v in PLANE}
parity_image = {(q_plus(*v), q_minus(*v)) for v in PLANE}

phase_domain = [(a, b) for a in range(P) for b in range(P)]
phase_values = [(3 * a * b) % P for a, b in phase_domain]
phase_fibers = Counter(phase_values)

gates = [
    len(odd_kernel) == 7,
    len(odd_image) == 7,
    joint_kernel == [(0, 0)],
    len(joint_image) == 49,
    len(parity_image) == 49,
    len(phase_domain) == 49,
    len(set(phase_values)) == 7,
    phase_fibers[0] == 13,
    all(phase_fibers[value] == 6 for value in range(1, P)),
    len(joint_image) == len(phase_domain),
    max(phase_fibers.values()) > 1,
]

result = {
    "schema": "marici.strominger.updated_aspect_target_indexed_carrier.v1",
    "fiber_gate": {
        "odd_target_kernel_order": len(odd_kernel),
        "odd_target_minimal_quotient_order": len(odd_image),
        "joint_target_kernel_order": len(joint_kernel),
        "joint_target_minimal_quotient_order": len(joint_image),
    },
    "arity_gate": {
        "unary_joint_chart_carrier_order": len(joint_image),
        "binary_primal_dual_domain_order": len(phase_domain),
        "phase_output_order": len(set(phase_values)),
        "same_cardinality_does_not_identify_types": True,
        "phase_fiber_sizes": dict(sorted(phase_fibers.items())),
        "phase_pairing_faithful_on_pairs": False,
    },
    "authority_gate": {
        "mathematical_linking_pairing_exists": True,
        "dual_physical_germ_authorized": False,
        "executable_phase_coupling_authorized": False,
        "realization_section_follows_from_descent": False,
    },
    "smallest_missing_constructor": "source-derived dual marked germ plus native binary phase coupling",
    "gates_passed": sum(gates),
    "gates_total": len(gates),
    "all_passed": all(gates),
}

output = Path(__file__).parents[1] / "results" / "updated_aspect_target_indexed_carrier_checks.json"
output.write_text(json.dumps(result, indent=2) + "\n", encoding="ascii")
print(json.dumps(result, indent=2))
raise SystemExit(0 if all(gates) else 1)
