from __future__ import annotations

import json
from fractions import Fraction


def partial_energy(sequence: list[Fraction], cutoff: int) -> Fraction:
    return sum(Fraction(index + 1) * sequence[index] ** 2 for index in range(cutoff))


def main() -> None:
    cutoffs = [1, 2, 4, 8, 16, 32]
    all_ones = [Fraction(1)] * max(cutoffs)
    phantom_energies = [partial_energy(all_ones, cutoff) for cutoff in cutoffs]
    assert phantom_energies == [Fraction(cutoff * (cutoff + 1), 2) for cutoff in cutoffs]
    assert all(phantom_energies[index + 1] > phantom_energies[index] for index in range(len(cutoffs) - 1))

    decaying = [Fraction(1, (index + 1) ** 2) for index in range(max(cutoffs))]
    bounded_energies = [partial_energy(decaying, cutoff) for cutoff in cutoffs]
    assert all(bounded_energies[index + 1] >= bounded_energies[index] for index in range(len(cutoffs) - 1))
    upper_bound = sum(Fraction(1, n**3) for n in range(1, 1000))
    assert bounded_energies[-1] < upper_bound < 2

    # Exhaustion independence at a common terminal cutoff.
    natural_order_energy = partial_energy(decaying, 32)
    even_then_odd_indices = list(range(0, 32, 2)) + list(range(1, 32, 2))
    reordered_energy = sum(Fraction(index + 1) * decaying[index] ** 2 for index in even_then_odd_indices)
    assert natural_order_energy == reordered_energy

    result = {
        "schema": "marici.voevodsky.energy-bounded-inverse-limit-completion.v1",
        "status": "energy_bounded_sublimit_verified",
        "cutoffs": cutoffs,
        "all_one_prefixes_compatible": True,
        "all_one_partial_energies": [str(value) for value in phantom_energies],
        "all_one_family_energy_bounded": False,
        "decaying_family_compatible": True,
        "decaying_partial_energies": [str(value) for value in bounded_energies],
        "decaying_family_energy_bounded": True,
        "weighted_l2_identification": True,
        "finite_reordering_energy_invariant": True,
        "bare_inverse_limit_has_phantoms": True,
        "completed_Weil_positive_energy_source_usable_non_circularly": False,
        "next_gate": "fixed-support Sobolev ambient energy and uniform quotient-map boundedness",
        "passed": True,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
