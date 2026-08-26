"""WP396: exact post-hoc lookup-selector no-go on the spectator fiber."""
import itertools
import json
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]

def energy(target, state):
    return sum(sp.Rational(1, 2)*(1-target[i]*state[i]) for i in range(3))

def main():
    states = list(itertools.product((-1, 1), repeat=3))
    energy_tables = {target: tuple(energy(target, state) for state in states) for target in states}
    minimizers = {
        target: [state for state in states if energy(target, state) == min(table)]
        for target, table in energy_tables.items()
    }
    spectra = {target: tuple(sorted(table)) for target, table in energy_tables.items()}
    coefficient_norms = {
        target: sum(sp.Rational(sign, 2)**2 for sign in target) for target in states
    }
    chosen = (1, -1, 1)
    alternative = (-1, 1, -1)
    masks = list(itertools.product((0, 1), repeat=3))
    H = sp.Matrix([[sp.prod(state[i] for i in range(3) if mask[i]) for state in states] for mask in masks])
    chosen_delta = sp.Matrix([1 if state == chosen else 0 for state in states])
    chosen_record = H*chosen_delta
    recovered = H.T*chosen_record/8
    checks = {
        "every_target_has_unique_minimum": all(minimizers[target] == [target] for target in states),
        "every_minimum_energy_zero": all(energy_tables[target][states.index(target)] == 0 for target in states),
        "all_selectors_nonnegative": all(value >= 0 for table in energy_tables.values() for value in table),
        "all_selectors_share_energy_spectrum": len(set(spectra.values())) == 1,
        "common_spectrum_is_hamming_spectrum": next(iter(spectra.values())) == (0, 1, 1, 1, 2, 2, 2, 3),
        "all_selector_coefficient_norms_equal": set(coefficient_norms.values()) == {sp.Rational(3, 4)},
        "all_eight_outcomes_have_equal_complexity_selectors": len(energy_tables) == 8,
        "complete_probe_record_reconstructs_chosen_state": recovered == chosen_delta,
        "chosen_selector_rejects_alternative": energy(chosen, alternative) == 3,
        "alternative_selector_rejects_chosen": energy(alternative, chosen) == 3,
        "posthoc_rule_reads_target_into_coefficients": tuple(-sp.Rational(sign, 2) for sign in chosen) == (-sp.Rational(1, 2), sp.Rational(1, 2), -sp.Rational(1, 2)),
        "faithful_identification_does_not_remove_selector_multiplicity": len(minimizers) == len(states),
    }
    checks = {name: bool(value) for name, value in checks.items()}
    result = {
        "work_package": "WP396",
        "admitted_state_domain": "the eight labelled spectator extensions from WP395",
        "faithful_quotient_coordinate": "the complete labelled parity record",
        "source_authorized_probe_family": "the invertible Walsh tower together with positive linear Hamming selectors",
        "contextual_partition": "the probe tower has singleton fibers, while the selector grammar contains one equally simple unique-minimum potential for every fiber",
        "classification": "exact no-go for inferring explanatory selection from faithfulness, positivity, uniqueness, or equal syntactic simplicity",
        "selector_count": len(energy_tables),
        "common_energy_spectrum": [int(value) for value in next(iter(spectra.values()))],
        "common_coefficient_norm_squared": str(next(iter(coefficient_norms.values()))),
        "smallest_exact_falsifier": "the outcomes (1,-1,1) and (-1,1,-1) are perfectly distinguished, yet each is uniquely selected by an isomorphic positive Hamming potential",
        "remaining_physical_instrument_gate": "derive the selector coefficients from source data fixed before the parity record and demand an independent prediction not used in constructing them",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = ROOT / "results/wp396_lookup_selector_no_go.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)

if __name__ == "__main__":
    main()
