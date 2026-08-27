"""Audit the quarter resonances along the source dimensional regulator line."""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path

from exponent_adapter_quarter_divisor import rank_at


ROOT = Path(__file__).resolve().parents[3]
RESULTS = ROOT / "research" / "benincasa" / "results"


def ranks(packet: dict, gamma: Fraction) -> list[int]:
    source = rank_at(packet, gamma.numerator, gamma.denominator, 720)
    augmented = rank_at(packet, gamma.numerator, gamma.denominator, 756)
    return [source, augmented, augmented - source]


def main() -> None:
    points = {
        "physical": Fraction(-1, 2),
        "first_quarter": Fraction(-5, 4),
        "intervening_half": Fraction(-3, 2),
        "second_quarter": Fraction(-7, 4),
        "source_drop": Fraction(-2, 1),
    }
    expected = {
        "physical": [479, 505, 26],
        "first_quarter": [479, 500, 21],
        "intervening_half": [479, 498, 19],
        "second_quarter": [479, 498, 19],
        "source_drop": [477, 503, 26],
    }
    observed = {}
    for prime in (32003, 32009):
        packet = json.loads(
            (RESULTS / f"exponent_adapter_full_pencil_{prime}.json").read_text()
        )
        prime_observed = {name: ranks(packet, gamma) for name, gamma in points.items()}
        assert prime_observed == expected, (prime, prime_observed)
        observed[str(prime)] = prime_observed

    epsilon = {name: gamma + Fraction(1, 2) for name, gamma in points.items()}
    assert epsilon["physical"] == 0
    assert epsilon["first_quarter"] == Fraction(-3, 4)
    assert epsilon["second_quarter"] == Fraction(-5, 4)
    assert epsilon["first_quarter"] < Fraction(-1, 2)
    assert epsilon["second_quarter"] < Fraction(-1, 2)

    output = {
        "status": "pass",
        "source_regulator_relation": "gamma=epsilon-1/2",
        "literal_syzygy_boundary_chamber": "Re(epsilon)>-1/2",
        "epsilon_values": {name: str(value) for name, value in epsilon.items()},
        "rank_convention": "[rank(M), rank([M;L]), relative_rank]",
        "two_prime_ranks": observed,
        "ordered_real_gamma_path": [
            "-1/2 physical",
            "-5/4 quarter relative drop",
            "-3/2 established relative drop",
            "-7/4 quarter relative drop",
            "-2 source-module drop",
        ],
        "classification": (
            "The source dimensional regulator types the quarter fibers, but both "
            "lie outside the literal relative-boundary chamber. They are "
            "meromorphic regulator-plane resonances, not physical epsilon=0 support."
        ),
    }
    destination = RESULTS / "exponent_adapter_regulator_path.json"
    destination.write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
