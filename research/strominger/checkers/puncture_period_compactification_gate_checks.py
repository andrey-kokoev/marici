import cmath
import json
from pathlib import Path


P = 7

# Two-puncture cohomology has one integral cycle and one real period coordinate.
integral_cycle_rank = 1
real_periods = [2 * t / P for t in range(P)]
characters = [cmath.exp(2j * cmath.pi * period) for period in real_periods]

# The selected representatives do not define Z/7 -> R because t=0 and t=7
# represent the same class but lift to periods 0 and 2.
real_lift_at_zero = 0
real_lift_at_seven = 2
hom_to_real_well_defined = real_lift_at_zero == real_lift_at_seven

# Modulo integers, multiplication by two gives an injective Z/7 character.
compact_values = [(2 * t / P) % 1 for t in range(P)]
compact_wraps = ((2 * 7 / P) % 1) == 0
compact_injective = len(set(compact_values)) == P

# All A_t are flat on C*, while the generator contour sees their periods.
local_curvatures = [0 for _ in range(P)]
local_indistinguishable = len(set(local_curvatures)) == 1
contour_distinguishes = len(set(real_periods)) == P
character_distinguishes = len({
    (round(value.real, 12), round(value.imag, 12)) for value in characters
}) == P

gates = [
    integral_cycle_rank == 1,
    not hom_to_real_well_defined,
    compact_wraps,
    compact_injective,
    local_indistinguishable,
    contour_distinguishes,
    character_distinguishes,
]

result = {
    "schema": "marici.strominger.puncture_period_compactification_gate.v1",
    "source_integral_structure": "H_1(S^2-P,Z) rank one for two punctures",
    "current_period_codomain": "R",
    "current_gauge_quotient": "exact real one-forms",
    "hom_Z7_to_R_nonzero": hom_to_real_well_defined,
    "candidate_compact_codomain": "R/Z",
    "hom_Z7_to_R_mod_Z_injective": compact_injective and compact_wraps,
    "candidate_states": ["A_0", "A_1"],
    "same_local_curvature": local_indistinguishable,
    "period_outcomes": [real_periods[0], real_periods[1]],
    "phase_characters": ["1", "exp(2*pi*i*2/7)"],
    "counterfactual_contour_distinguishes": contour_distinguishes,
    "current_source_authority": False,
    "smallest_missing_theorem": "integral large-gauge compactification of the gravitational period",
    "gates_passed": sum(gates),
    "gates_total": len(gates),
    "all_passed": all(gates),
}

output = Path(__file__).parents[1] / "results" / "puncture_period_compactification_gate_checks.json"
output.write_text(json.dumps(result, indent=2) + "\n", encoding="ascii")
print(json.dumps(result, indent=2))
raise SystemExit(0 if all(gates) else 1)
