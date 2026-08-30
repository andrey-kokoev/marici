"""Test whether quarter rank drops persist on their integral Kummer orbits."""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path

from exponent_adapter_quarter_divisor import rank_at


ROOT = Path(__file__).resolve().parents[3]
RESULTS = ROOT / "research" / "benincasa" / "results"


ORBITS = {
    "minus_i": [Fraction(-9, 4), Fraction(-5, 4), Fraction(-1, 4), Fraction(3, 4)],
    "plus_i": [Fraction(-11, 4), Fraction(-7, 4), Fraction(-3, 4), Fraction(1, 4)],
}


def rank_pair(packet: dict, gamma: Fraction) -> list[int]:
    return [
        rank_at(packet, gamma.numerator, gamma.denominator, 720),
        rank_at(packet, gamma.numerator, gamma.denominator, 756),
    ]


def main() -> None:
    all_ranks = {}
    for prime in (32003, 32009):
        packet = json.loads(
            (RESULTS / f"exponent_adapter_full_pencil_{prime}.json").read_text()
        )
        prime_ranks = {
            character: {str(gamma): rank_pair(packet, gamma) for gamma in orbit}
            for character, orbit in ORBITS.items()
        }
        assert prime_ranks["minus_i"] == {
            "-9/4": [479, 505],
            "-5/4": [479, 500],
            "-1/4": [479, 505],
            "3/4": [479, 505],
        }
        assert prime_ranks["plus_i"] == {
            "-11/4": [479, 505],
            "-7/4": [479, 498],
            "-3/4": [479, 505],
            "1/4": [479, 505],
        }
        all_ranks[str(prime)] = prime_ranks

    output = {
        "status": "pass",
        "rank_convention": "[rank(M), rank([M;L])]",
        "two_prime_integral_orbits": all_ranks,
        "same_inertia_rank_drop_persists": False,
        "classification": (
            "The quarter defects are resonances of the selected meromorphic "
            "pole-depth lattice, not support invariants of the underlying "
            "order-four Kummer local systems."
        ),
    }
    destination = RESULTS / "exponent_adapter_integral_orbit.json"
    destination.write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
