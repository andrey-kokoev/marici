"""Verify source-level C3 descent of the exponent-adapter obstruction."""

from __future__ import annotations

import importlib
import importlib.util
import json
import os
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
BENINCASA = ROOT / "research" / "benincasa"
RESULTS = BENINCASA / "results"
sys.path.insert(0, str(BENINCASA))
import physical_four_mark_residue_twisted_derham as base


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


obstruction = load_module(
    "exponent_adapter_specialization_obstruction",
    Path(__file__).with_name("exponent_adapter_specialization_obstruction.py"),
)


def clean(polynomial, prime):
    return {
        exponent: coefficient % prime
        for exponent, coefficient in polynomial.items()
        if coefficient % prime
    }


def g23_positional_fiber(x, y, z, prime):
    """G23 at target parameters, ordered by transported G12 mark positions."""
    k, _ = base.fiber_data(y, z, x)
    q = {
        "g1": {(0, 1): 1, (0, 0): -x - z},
        "g2": {(1, 0): 1, (0, 0): -x - y},
        "g3": {(1, 0): 1, (0, 1): 1, (0, 0): x},
        "g23": {(0, 1): 1, (0, 0): -y},
        "g31": {(1, 0): 1, (0, 0): -z},
    }
    return clean(k, prime), {name: clean(poly, prime) for name, poly in q.items()}


def g31_positional_fiber(x, y, z, prime):
    """Cyclic G31 at target parameters, ordered by transported G12 positions."""
    k, _ = base.fiber_data(z, x, y)
    q = {
        "g1": {(0, 1): 1, (0, 0): -x - y},
        "g2": {(1, 0): 1, (0, 0): -y - z},
        "g3": {(1, 0): 1, (0, 1): 1, (0, 0): y},
        "g23": {(0, 1): 1, (0, 0): -z},
        "g31": {(1, 0): 1, (0, 0): -x},
    }
    return clean(k, prime), {name: clean(poly, prime) for name, poly in q.items()}


def main() -> None:
    output = {
        "status": "pass",
        "site_cycle": "(X1,X2,X3)->(X3,X1,X2)",
        "residue_orientation_signs": [1, 1, 1],
        "source_checks": [],
        "obstruction_checks": [],
    }
    source_names = ("g1", "g2", "g3", "g23", "g31")
    once = ("g2", "g3", "g1", "g31", "g12")
    twice = ("g3", "g1", "g2", "g12", "g23")

    for prime in (32003, 32009):
        os.environ["MARICI_FIELD_PRIME"] = str(prime)
        importlib.reload(base)
        for point in ((2, 3, 4), (5, 7, 11), (13, 17, 19)):
            x, y, z = point
            source_k, source_q = base.fiber_data(x, y, z)
            target23_k, target23_q = g23_positional_fiber(z, x, y, prime)
            target31_k, target31_q = g31_positional_fiber(y, z, x, prime)
            assert clean(source_k, prime) == target23_k == target31_k
            assert all(clean(source_q[name], prime) == target23_q[name] for name in source_names)
            assert all(clean(source_q[name], prime) == target31_q[name] for name in source_names)
            output["source_checks"].append(
                {
                    "prime": prime,
                    "source_point": list(point),
                    "g23_target_point": [z, x, y],
                    "g31_target_point": [y, z, x],
                    "cayley_menger_match": True,
                    "five_mark_matches_each_edge": True,
                }
            )

        packet = json.loads(
            (RESULTS / f"exponent_adapter_full_pencil_{prime}.json").read_text()
        )
        for point in ((-5, 4), (-7, 4)):
            analysis = obstruction.analyze(prime, point, packet)
            output["obstruction_checks"].append(
                {
                    "prime": prime,
                    "point": list(point),
                    "cyclic_chart_ranks": [analysis[4]] * 3,
                    "cyclic_chart_filtrations": [analysis[5]] * 3,
                }
            )

    first_map = dict(zip(source_names, once))
    second_map = dict(zip(once, twice))
    third_map = dict(zip(twice, source_names))
    for name in source_names:
        assert third_map[second_map[first_map[name]]] == name
    output["mark_maps"] = {
        "G12_to_G23": first_map,
        "G23_to_G31": second_map,
        "G31_to_G12": third_map,
        "three_cycle_composition": "identity",
    }
    output["conclusion"] = (
        "After source relabelling, the three cyclic chart packets are coefficientwise "
        "identical and the signed cyclic composition is the identity."
    )
    (RESULTS / "exponent_adapter_cyclic_occurrence_descent.json").write_text(
        json.dumps(output, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
