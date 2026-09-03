from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path


CONTRACT = Path("research/voevodsky/no-local-positive-weil-density-v1.json")


def bump(center: Fraction, radius: Fraction, point: Fraction) -> Fraction:
    distance = abs(point - center)
    if distance >= radius:
        return Fraction(0)
    return Fraction(1) - distance / radius


def main() -> None:
    contract = json.loads(CONTRACT.read_text(encoding="utf-8"))

    # A negative isolated atom is detected by a nonnegative bump whose support excludes all others.
    prime_locus = Fraction(2)
    other_loci = [Fraction(-2), Fraction(0), Fraction(5)]
    coefficient = Fraction(-3, 5)
    radius = Fraction(1, 4)
    assert bump(prime_locus, radius, prime_locus) == 1
    assert all(bump(prime_locus, radius, point) == 0 for point in other_loci)
    atomic_pairing = coefficient * bump(prime_locus, radius, prime_locus)
    assert atomic_pairing < 0

    # A bounded smooth background cannot cancel localization as support radius shrinks.
    smooth_density_bound = Fraction(7, 3)
    for denominator in (10, 100, 1000):
        local_radius = Fraction(1, denominator)
        smooth_upper = 2 * local_radius * smooth_density_bound
        assert coefficient + smooth_upper < 0

    # Restricted test families need not contain these localized bumps.
    result = {
        "schema":"marici.voevodsky.no-local-positive-weil-density-check.v1",
        "status":"negative_singular_atom_no_go_verified",
        "isolated_negative_atom_detected":True,
        "smooth_background_cannot_cancel_under_localization":True,
        "restricted_test_algebra_contains_bump":False,
        "exact_weil_prime_sign_and_normalization_verified":False,
        "local_positive_measure_factor_falsified":"conditional_on_source_formula",
        "restricted_weil_cone_falsified":False,
        "rh_implication":False,
        "acceptance_test":contract["acceptance_test"],
        "passed":True
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
