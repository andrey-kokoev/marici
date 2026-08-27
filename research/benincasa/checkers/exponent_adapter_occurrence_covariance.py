"""Verify G12-to-G31 covariance of the exponent specialization obstruction."""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
RESULTS = ROOT / "research" / "benincasa" / "results"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


obstruction = load_module(
    "exponent_adapter_specialization_obstruction",
    Path(__file__).with_name("exponent_adapter_specialization_obstruction.py"),
)


def map_row(row, transport, prime):
    result = {}
    for source_column, coefficient in row.items():
        for target_column, value in transport[source_column].items():
            obstruction.add(result, target_column, coefficient * value, prime)
    return result


def dual_inclusion(left_constant, left_normal, right_constant, right_normal, prime):
    basis = obstruction.dual_basis(right_constant, right_normal, prime)
    constant_failures = normal_failures = 0
    for constant, normal in zip(left_constant, left_normal):
        remainder, normal_remainder = obstruction.reduce_dual(
            constant, normal, basis, prime
        )
        constant_failures += bool(remainder)
        normal_failures += bool(normal_remainder)
    return {
        "constant_failures": constant_failures,
        "first_normal_failures": normal_failures,
        "target_rank": len(basis),
    }


def main() -> None:
    points = ((-5, 4), (-7, 4))
    expected_obstruction = {
        (-5, 4): (5, [0, 0, 0, 0, 0, 2, 5, 5]),
        (-7, 4): (7, [0, 0, 0, 0, 0, 2, 6, 7]),
    }
    output = {"status": "pass", "transition": "G12 to G31 with residue sign -1", "checks": []}
    monomials = [(i, j) for i in range(8) for j in range(8 - i)]
    monomial_position = {monomial: index for index, monomial in enumerate(monomials)}

    for prime in (32003, 32009):
        source = json.loads(
            (RESULTS / f"exponent_adapter_full_pencil_{prime}.json").read_text()
        )
        target = json.loads(
            (RESULTS / f"exponent_adapter_g31_full_pencil_{prime}.json").read_text()
        )
        transport = [
            dict(row)
            for row in json.loads(
                (RESULTS / f"exponent_adapter_g12_g31_transport_{prime}.json").read_text()
            )
        ]
        assert len(obstruction.row_basis(transport, prime)) == 535

        for point in points:
            source_constant, source_normal = obstruction.load(source, *point, 756)
            target_constant, target_normal = obstruction.load(target, *point, 756)
            mapped_constant = [map_row(row, transport, prime) for row in source_constant]
            mapped_normal = [map_row(row, transport, prime) for row in source_normal]

            forward = dual_inclusion(
                mapped_constant[:720], mapped_normal[:720],
                target_constant[:720], target_normal[:720], prime,
            )
            reverse = dual_inclusion(
                target_constant[:720], target_normal[:720],
                mapped_constant[:720], mapped_normal[:720], prime,
            )
            assert forward["constant_failures"] == forward["first_normal_failures"] == 0
            assert reverse["constant_failures"] == reverse["first_normal_failures"] == 0

            low_failures = 0
            for source_index, monomial in enumerate(monomials):
                target_index = monomial_position[(monomial[1], monomial[0])]
                expected = {
                    column: -value % prime
                    for column, value in target_constant[720 + target_index].items()
                }
                low_failures += mapped_constant[720 + source_index] != expected
            assert low_failures == 0

            target_analysis = obstruction.analyze(prime, point, target)
            expected_rank, expected_filtration = expected_obstruction[point]
            assert target_analysis[4] == expected_rank
            assert target_analysis[5] == expected_filtration

            output["checks"].append(
                {
                    "prime": prime,
                    "point": list(point),
                    "transport_rank": 535,
                    "source_module_forward": forward,
                    "source_module_reverse": reverse,
                    "signed_low_row_failures": low_failures,
                    "target_obstruction_rank": target_analysis[4],
                    "target_obstruction_filtration": target_analysis[5],
                }
            )

    (RESULTS / "exponent_adapter_occurrence_covariance.json").write_text(
        json.dumps(output, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
