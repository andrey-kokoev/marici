"""Verify the S3 coherence relation for the quarter-obstruction source packet."""

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


def compose(left, right, item):
    return left(right(item))


def site_cycle(site: int) -> int:
    return {1: 2, 2: 3, 3: 1}[site]


def site_reflection(site: int) -> int:
    return {1: 1, 2: 3, 3: 2}[site]


def map_mark(mark: tuple[int, ...], site_map) -> tuple[int, ...]:
    return tuple(sorted(site_map(site) for site in mark))


def cycle_state(state):
    chart, i, j, sign = state
    return ((chart + 1) % 3, i, j, sign)


def reflection_state(state):
    chart, i, j, sign = state
    target_chart = {0: 2, 1: 1, 2: 0}[chart]
    return target_chart, j, i, -sign


def main() -> None:
    sites = (1, 2, 3)
    marks = ((1,), (2,), (3,), (1, 2), (2, 3), (1, 3))
    site_checks = 0
    mark_checks = 0
    for site in sites:
        assert compose(site_reflection, site_cycle, site_reflection(site)) == compose(
            site_cycle, site_cycle, site
        )
        assert site_cycle(site_cycle(site_cycle(site))) == site
        assert site_reflection(site_reflection(site)) == site
        site_checks += 1
    for mark in marks:
        left = map_mark(
            map_mark(map_mark(mark, site_reflection), site_cycle), site_reflection
        )
        right = map_mark(map_mark(mark, site_cycle), site_cycle)
        assert left == right
        mark_checks += 1

    low_states = [
        (chart, i, j, 1)
        for chart in range(3)
        for i in range(8)
        for j in range(8 - i)
    ]
    low_checks = 0
    for state in low_states:
        assert cycle_state(cycle_state(cycle_state(state))) == state
        assert reflection_state(reflection_state(state)) == state
        assert reflection_state(cycle_state(reflection_state(state))) == cycle_state(
            cycle_state(state)
        )
        low_checks += 1

    transport_ranks = {}
    obstruction_checks = []
    for prime in (32003, 32009):
        transport = [
            dict(row)
            for row in json.loads(
                (RESULTS / f"exponent_adapter_g12_g31_transport_{prime}.json").read_text()
            )
        ]
        transport_ranks[str(prime)] = len(obstruction.row_basis(transport, prime))
        assert transport_ranks[str(prime)] == 535
        packet = json.loads(
            (RESULTS / f"exponent_adapter_full_pencil_{prime}.json").read_text()
        )
        for point in ((-5, 4), (-7, 4)):
            analysis = obstruction.analyze(prime, point, packet)
            obstruction_checks.append(
                {
                    "prime": prime,
                    "point": list(point),
                    "rank": analysis[4],
                    "filtration": analysis[5],
                }
            )

    output = {
        "status": "pass",
        "presentation": "S3=<r,s | r^3=s^2=1, srs=r^-1>",
        "generators": {
            "r": "site cycle; chart cycle; retained exponents fixed; residue sign +1",
            "s": "site transposition 23; charts 0 and 2 exchanged; exponents swapped; residue sign -1",
        },
        "site_relation_checks": site_checks,
        "marked_subgraph_relation_checks": mark_checks,
        "signed_low_occurrence_relation_checks": low_checks,
        "reflection_transport_ranks": transport_ranks,
        "obstruction_checks": obstruction_checks,
        "conclusion": (
            "The reflected and cyclic source transports satisfy s r s = r^-1, "
            "including the residue sign, so the finite-field lifting obstruction "
            "carries a coherent S3 occurrence action."
        ),
    }
    (RESULTS / "exponent_adapter_s3_coherence.json").write_text(
        json.dumps(output, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
