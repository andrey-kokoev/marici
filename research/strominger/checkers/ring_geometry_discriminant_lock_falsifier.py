import cmath
import json
from pathlib import Path


P = 7
L = 3.0
mode_numbers = [1, 2, 3]
mode_frequencies = [n / L for n in mode_numbers]

# Fix a nonzero normalized delay and vary the allowed real source amplitude.
base_delay = L
amplitudes = [0.0, 0.1, 0.25, 0.5, 1.0, 1.3]
phases = [
    cmath.exp(1j * mode_frequencies[0] * s * base_delay)
    for s in amplitudes
]

mu7 = [cmath.exp(2j * cmath.pi * t / P) for t in range(P)]


def in_mu7(z):
    return any(abs(z - root) < 1e-12 for root in mu7)


continuous_family_leaves_mu7 = any(not in_mu7(z) for z in phases)
multiple_ring_modes = len(mode_frequencies) > 1

# Seven desired phases can always be manufactured by fitted amplitudes.
fitted_amplitudes = [2 * cmath.pi * t / P for t in range(P)]
fitted_phases = [cmath.exp(1j * s) for s in fitted_amplitudes]
fitted_matches_mu7 = all(in_mu7(z) for z in fitted_phases)

# But the selected amplitudes are not closed under ordinary real scaling.
scaled_selected = 0.5 * fitted_amplitudes[1]
selected_subset_not_scalar_closed = not in_mu7(cmath.exp(1j * scaled_selected))

gates = [
    multiple_ring_modes,
    continuous_family_leaves_mu7,
    fitted_matches_mu7,
    selected_subset_not_scalar_closed,
]

result = {
    "schema": "marici.strominger.ring_geometry_discriminant_lock_falsifier.v1",
    "candidate_lock": "omega_n=n/L",
    "ring_supplies_unique_frequency": False,
    "linear_source_allows_continuous_amplitude_scaling": True,
    "fixed_mode_phase_confined_to_mu7": not continuous_family_leaves_mu7,
    "seven_phases_can_be_fitted": fitted_matches_mu7,
    "fitted_subset_closed_under_source_scalars": not selected_subset_not_scalar_closed,
    "affine_determinant_supplies_physical_amplitude_lattice": False,
    "smallest_missing_theorem": "QuantizedSpinMemoryComparison",
    "gates_passed": sum(gates),
    "gates_total": len(gates),
    "all_passed": all(gates),
}

output = (
    Path(__file__).parents[1]
    / "results"
    / "ring_geometry_discriminant_lock_falsifier.json"
)
output.write_text(json.dumps(result, indent=2) + "\n", encoding="ascii")
print(json.dumps(result, indent=2))
raise SystemExit(0 if all(gates) else 1)
