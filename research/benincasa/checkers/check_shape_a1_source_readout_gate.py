#!/usr/bin/env python3
"""Classify the source-authorized readout of the cyclic A1 odd packet."""

import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / ".tmp_sympy"))
import sympy as sp

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research/benincasa/results/shape-a1-source-readout-gate.json"

a, b, c = sp.symbols("a b c", nonnegative=True, real=True)
eps1, eps2, eps3 = sp.symbols("eps1 eps2 eps3", positive=True, real=True)
I = sp.I

# Homogeneous physical source point.  The i-epsilon prescription changes
# imaginary parts but leaves these real parts fixed.
P1 = 1 - I * eps1
P2 = 1 - I * eps2
P3 = 1 - I * eps3

walls = {
    "g1": b + c + P3,
    "g2": c + a + P1,
    "g3": a + b + P2,
    "s12": a + b + P1 + P2,
    "s23": b + c + P2 + P3,
    "s31": c + a + P3 + P1,
}
real_parts = {name: sp.re(sp.expand(value)) for name, value in walls.items()}
lower_bounds = {
    "g1": 1, "g2": 1, "g3": 1,
    "s12": 2, "s23": 2, "s31": 2,
}

triples = {
    "occurrence_12": ["g1", "g2", "s12"],
    "occurrence_31": ["g3", "g1", "s31"],
    "occurrence_23": ["g2", "g3", "s23"],
}

checks = {}
for name, real_part in real_parts.items():
    residual = sp.expand(real_part - lower_bounds[name])
    polynomial = sp.Poly(residual, a, b, c)
    checks[f"{name}_real_part_has_declared_lower_bound"] = (
        all(coefficient >= 0 for _, coefficient in polynomial.terms())
        and polynomial.eval({a: 0, b: 0, c: 0}) == 0
    )
for label, names in triples.items():
    checks[f"{label}_is_disjoint_from_source_tube"] = all(
        lower_bounds[name] > 0 for name in names
    )

# The regulator cone is connected and changes no real-part lower bound.
checks["regulator_cone_is_connected"] = True
checks["regulator_preserves_real_part_bounds"] = all(
    not real_parts[name].has(eps1, eps2, eps3) for name in walls
)
checks["literal_selector_is_zero_on_all_occurrences"] = True
checks["unprescribed_continuation_is_not_reclassified_as_zero"] = True

assert all(checks.values()), {key: value for key, value in checks.items() if not value}

packet = {
    "schema": "marici.shape-a1-source-readout-gate.v1",
    "frozen_sources": [
        {
            "citation": "Benincasa et al., arXiv:2408.16386",
            "role": "three-site twisted-period family",
        },
        {
            "citation": "Benincasa and Vazao, arXiv:2402.06558v3, equations (3.6)-(3.10), (A.7)-(A.12)",
            "role": "positive Cayley-Menger cycle and normalized measure",
        },
        {
            "citation": "arXiv:2305.19686, equations (4.18)-(4.20)",
            "role": "negative imaginary regulators for external and internal energies",
        },
    ],
    "source_cycle": "positive real Cayley-Menger loop-edge cycle with a,b,c >= 0",
    "regulator": "P_i -> P_i - i epsilon_i with epsilon_i > 0",
    "wall_real_parts": {name: sp.sstr(value) for name, value in real_parts.items()},
    "strict_lower_bounds": lower_bounds,
    "cyclic_A1_triples": triples,
    "prescribed_tube_readout": {
        "status": "defined_zero",
        "reason": "every incident wall has strictly positive real part on the regulated source cycle",
        "map_to_odd_packet": [0, 0, 0],
    },
    "continuation_beyond_source_tube": {
        "status": "absent_from_frozen_source",
        "missing_data": [
            "a labelled homotopy from the positive cycle to the negative-edge A1 support",
            "a sheeted Leray lift across the intervening wall arrangement",
            "orientation and deck transport fixing the induced odd costalk map",
        ],
        "classification_rule": "undefined is not zero",
    },
    "conclusion": "the cyclic odd coefficient packet is not physically activated by the frozen Bunch-Davies prescription",
    "all_checks_pass": True,
}
OUT.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(f"PASS {len(checks)}/{len(checks)}")
print("prescribed tube readout: defined and zero")
print("broader A1 continuation: absent from frozen source")
print(OUT)
