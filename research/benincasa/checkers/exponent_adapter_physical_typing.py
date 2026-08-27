"""Type the universal exponent adapter against the physical residue sector."""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path

from exponent_adapter_quarter_divisor import rank_at


ROOT = Path(__file__).resolve().parents[3]
RESULTS = ROOT / "research" / "benincasa" / "results"


def main() -> None:
    physical_gamma = Fraction(-1, 2)
    quarter_resonances = (Fraction(-5, 4), Fraction(-7, 4))

    ranks = {}
    for prime in (32003, 32009):
        packet = json.loads(
            (RESULTS / f"exponent_adapter_full_pencil_{prime}.json").read_text()
        )
        observed = (
            rank_at(packet, physical_gamma.numerator, physical_gamma.denominator, 720),
            rank_at(packet, physical_gamma.numerator, physical_gamma.denominator, 756),
        )
        assert observed == (479, 505), (prime, observed)
        ranks[str(prime)] = {
            "source_rank": observed[0],
            "augmented_rank": observed[1],
            "relative_rank": observed[1] - observed[0],
        }

    integer_shift_differences = [
        resonance - physical_gamma for resonance in quarter_resonances
    ]
    assert integer_shift_differences == [Fraction(-3, 4), Fraction(-5, 4)]
    assert all(value.denominator != 1 for value in integer_shift_differences)

    output = {
        "status": "pass",
        "adapter_convention": "K^(gamma-k_pole)",
        "source_simple_residue": "K^(-1/2)",
        "source_double_pole_descendant": "K^(-3/2)",
        "physical_base_gamma": "-1/2",
        "physical_ranks": ranks,
        "quarter_resonances": ["-5/4", "-7/4"],
        "differences_from_physical_gamma": ["-3/4", "-5/4"],
        "reachable_by_integer_exponent_shift": False,
        "scope": (
            "The quarter fibers are resonances of the analytic exponent family; "
            "the frozen physical residue sector does not occupy or reach them by "
            "the adapter's integral pole-depth shifts."
        ),
    }
    destination = RESULTS / "exponent_adapter_physical_typing.json"
    destination.write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
