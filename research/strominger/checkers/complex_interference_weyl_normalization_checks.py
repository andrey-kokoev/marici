import cmath
import json
from pathlib import Path


P = 7

# Additive complex coefficients contain no nonzero element killed by seven.
complex_additive_torsion = (7 * complex(1, 0) == 0)

# A normalized interferometer can display the desired discriminant character.
omega_tau_locked = 2 * cmath.pi
locked_phases = [
    cmath.exp(1j * omega_tau_locked * (2 * t / P)) for t in range(P)
]
locked_distinct = len({
    (round(z.real, 12), round(z.imag, 12)) for z in locked_phases
}) == P
locked_generator_is_expected = abs(
    locked_phases[1] - cmath.exp(2j * cmath.pi * 2 / P)
) < 1e-12

# Changing the authorized probe frequency changes the apparent character.
other_omega_tau = cmath.pi
other_generator = cmath.exp(1j * other_omega_tau * 2 / P)
frequency_dependence = abs(other_generator - locked_phases[1]) > 1e-12

# One frequency aliases real delays separated by its period.
delay = 0.37
instrument_period = 2 * cmath.pi / other_omega_tau
single_port_aliases = abs(
    cmath.exp(1j * other_omega_tau * delay)
    - cmath.exp(1j * other_omega_tau * (delay + instrument_period))
) < 1e-12

# Two incommensurate frequencies already remove that particular alias.
second_omega_tau = cmath.sqrt(2)
second_port_separates = abs(
    cmath.exp(1j * second_omega_tau * delay)
    - cmath.exp(1j * second_omega_tau * (delay + instrument_period))
) > 1e-12

gates = [
    not complex_additive_torsion,
    locked_distinct,
    locked_generator_is_expected,
    frequency_dependence,
    single_port_aliases,
    second_port_separates,
]

result = {
    "schema": "marici.strominger.complex_interference_weyl_normalization.v1",
    "complex_additive_coefficients_supply_Z7": False,
    "multiplicative_phase_codomain": "U(1)",
    "normalized_phase_displays_Z7": locked_distinct,
    "generator_character": "exp(2*pi*i*2/7)",
    "depends_on_probe_normalization": frequency_dependence,
    "one_phase_port_aliases_real_delays": single_port_aliases,
    "additional_frequency_can_separate_alias": second_port_separates,
    "source_authorized_interference_phase": True,
    "source_authorized_discriminant_frequency_lock": False,
    "smallest_missing_constructor": "DiscriminantInterferometerLock",
    "gates_passed": sum(gates),
    "gates_total": len(gates),
    "all_passed": all(gates),
}

output = (
    Path(__file__).parents[1]
    / "results"
    / "complex_interference_weyl_normalization_checks.json"
)
output.write_text(json.dumps(result, indent=2) + "\n", encoding="ascii")
print(json.dumps(result, indent=2))
raise SystemExit(0 if all(gates) else 1)
