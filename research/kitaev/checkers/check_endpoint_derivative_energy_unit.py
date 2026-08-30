#!/usr/bin/env python3
import hashlib
import json
from pathlib import Path

from sympy import Rational, diff, integrate, symbols

ROOT = Path(__file__).resolve().parents[3]
RESULT = ROOT / "research/kitaev/results/endpoint-derivative-energy-unit.json"


def affine_fixture(a, x):
    u = 1 - a * x
    energy = integrate(diff(u, x) ** 2, (x, 0, 1))
    return u, energy


def main():
    x = symbols("x", real=True)
    safe, safe_energy = affine_fixture(Rational(1, 2), x)
    assert safe.subs(x, 0) == 1
    assert safe.subs(x, 1) == Rational(1, 2)
    assert safe_energy == Rational(1, 4)

    threshold, threshold_energy = affine_fixture(1, x)
    assert threshold_energy == 1
    assert threshold.subs(x, 1) == 0

    collapse = []
    for n in (2, 4, 8, 16):
        a = 1 - Rational(1, n)
        u, energy = affine_fixture(a, x)
        endpoint = u.subs(x, 1)
        assert energy == a ** 2 < 1
        assert endpoint == Rational(1, n)
        collapse.append({"cutoff": n, "path_energy": str(energy),
                         "terminal_value": str(endpoint), "inverse_norm": n})

    payload = {
        "schema": "marici.kitaev.endpoint_derivative_energy_unit.v1",
        "status": "pass",
        "safe_fixture": {"path_length": 1, "energy": str(safe_energy),
                         "unit_lower_bound": "1/2", "inverse_norm_bound": 2},
        "sharp_threshold": {"path_length_times_energy": "1",
                            "terminal_zero": True},
        "nonuniform_completion_hostile": collapse,
        "disconnected_hostile": {"anchored_component_value": 1,
                                 "unanchored_component_value": 0,
                                 "derivative_energy": 0,
                                 "path_coverage": False},
        "typing_gate": "bulk_energy_requires_a_source_derived_trace_to_path_energy",
        "checker_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
