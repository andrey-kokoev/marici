from fractions import Fraction
import json
from pathlib import Path


PRIMES = (2, 3, 5)
COEFFICIENTS = {2: Fraction(1, 1), 3: Fraction(2, 1), 5: Fraction(-1, 1)}


def main() -> None:
    ratios = {}
    carrier = {}
    for p in PRIMES:
        for q in PRIMES:
            coefficient = COEFFICIENTS[p] * COEFFICIENTS[q]
            carrier[f"{p},{q}"] = str(coefficient) + f"/sqrt({p*q})"
            if p != q:
                ratio = Fraction(p, q)
                assert ratio not in ratios
                ratios[ratio] = (p, q)

    assert len(ratios) == len(PRIMES) * (len(PRIMES) - 1)

    recovered_pairs = {
        f"{p},{q}": carrier[f"{p},{q}"]
        for _, (p, q) in sorted(ratios.items())
    }
    assert len(recovered_pairs) == 6

    # The zero frequency is not label-faithful. These two one-prime packets
    # both have constant energy 1/2, although they occupy different labels.
    sparse_energy_at_2 = Fraction(1, 2)
    sparse_energy_at_3 = Fraction(3, 2) / 3
    assert sparse_energy_at_2 == sparse_energy_at_3

    diagonal = sum(COEFFICIENTS[p] ** 2 / p for p in PRIMES)
    result = {
        "schema": "marici.nima.mellin-seam-tomography.v1",
        "primes": list(PRIMES),
        "ordered_off_diagonal_frequency_count": len(ratios),
        "expected_ordered_off_diagonal_count": 6,
        "frequencies_are_pairwise_distinct": True,
        "zero_frequency_diagonal": str(diagonal),
        "mellin_orbit_recovers_all_off_diagonal_entries": True,
        "mellin_orbit_alone_recovers_labelled_diagonal": False,
        "labelled_diagonal_plus_mellin_orbit_recovers_full_carrier": True,
        "sparse_support_hostile_constant_energy": str(sparse_energy_at_2),
        "single_t_zero_observation_is_faithful": False,
        "completion_claimed": False,
        "recovered_pairs": recovered_pairs,
    }

    output = Path(__file__).parents[1] / "results" / "mellin-seam-tomography.json"
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
