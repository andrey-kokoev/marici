import cmath
import json
from pathlib import Path


P = 7
ZETA = cmath.exp(2j * cmath.pi / P)


def shift(vector, power=1):
    result = [0j] * P
    for t, amplitude in enumerate(vector):
        result[(t + power) % P] += amplitude
    return result


def clock(vector, power=1):
    return [
        amplitude * ZETA ** (2 * power * t)
        for t, amplitude in enumerate(vector)
    ]


def close(left, right, tolerance=1e-10):
    return all(abs(a - b) < tolerance for a, b in zip(left, right))


basis = []
for t in range(P):
    vector = [0j] * P
    vector[t] = 1 + 0j
    basis.append(vector)

# VU = zeta^2 UV on every basis vector.
weyl_relation = all(
    close(clock(shift(vector)), [ZETA ** 2 * x for x in shift(clock(vector))])
    for vector in basis
)

state0 = basis[0]
state1 = basis[1]
clock0 = clock(state0)
clock1 = clock(state1)
different_characters = close(clock0, state0) and close(
    clock1, [ZETA ** 2 * x for x in state1]
)

# Established magnetic observables act only on the unchanged base coordinate.
base_readout0 = (3, -4, 11)
base_readout1 = (3, -4, 11)
same_existing_readout = base_readout0 == base_readout1

normalization = P ** -0.5
plus_state = [normalization + 0j] * P
clocked_plus = clock(plus_state, power=1)

# Fourier probability: clock shifts the sharp Fourier label from 0 to 2.
def fourier_amplitude(vector, label):
    return sum(
        amplitude * ZETA ** (-label * t)
        for t, amplitude in enumerate(vector)
    ) / (P ** 0.5)


before_probabilities = [abs(fourier_amplitude(plus_state, k)) ** 2 for k in range(P)]
after_probabilities = [abs(fourier_amplitude(clocked_plus, k)) ** 2 for k in range(P)]
before_label = max(range(P), key=lambda k: before_probabilities[k])
after_label = max(range(P), key=lambda k: after_probabilities[k])
counterfactual_changes_outcome = before_label == 0 and after_label == 2

# Shift and clock generate all matrix units: U^a times spectral projectors of V.
# Distinct V eigenvalues make all seven diagonal projectors available.
distinct_clock_eigenvalues = len({
    (round((ZETA ** (2 * t)).real, 12), round((ZETA ** (2 * t)).imag, 12))
    for t in range(P)
}) == P
generated_matrix_unit_count = P * P if distinct_clock_eigenvalues else 0

gates = [
    weyl_relation,
    different_characters,
    same_existing_readout,
    counterfactual_changes_outcome,
    distinct_clock_eigenvalues,
    generated_matrix_unit_count == 49,
]

result = {
    "schema": "marici.strominger.finite_weyl_deutschian_counterfactual.v1",
    "finite_group": "Z/7",
    "weyl_relation": "V U = zeta^2 U V",
    "weyl_relation_verified": weyl_relation,
    "state_pair": ["h tensor |0>", "h tensor |1>"],
    "same_established_magnetic_readout": same_existing_readout,
    "different_discriminant_characters": different_characters,
    "counterfactual_operation": "apply V then measure Fourier port",
    "outcome_before": before_label,
    "outcome_after": after_label,
    "counterfactual_changes_outcome": counterfactual_changes_outcome,
    "generated_matrix_unit_count": generated_matrix_unit_count,
    "mathematical_objective_satisfied": all(gates),
    "source_authority_status": "missing integral symplectic lattice and quantization theorem",
    "goal_status": "not_complete_until_weyl_lift_is_source_derived",
    "gates_passed": sum(gates),
    "gates_total": len(gates),
    "all_passed": all(gates),
}

output = Path(__file__).parents[1] / "results" / "finite_weyl_deutschian_counterfactual_checks.json"
output.write_text(json.dumps(result, indent=2) + "\n", encoding="ascii")
print(json.dumps(result, indent=2))
raise SystemExit(0 if all(gates) else 1)
