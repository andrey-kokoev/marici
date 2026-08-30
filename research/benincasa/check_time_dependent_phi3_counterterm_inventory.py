#!/usr/bin/env python3
"""One-loop power-counting inventory for the action parent of the triangle."""

from __future__ import annotations

import json
from pathlib import Path


def one_loop_phi3(V: int) -> dict[str, int]:
    # At L=1, I=V.  Cubic incidence then gives E=3V-2I=V.
    I = V
    E = V
    omega = 4 - 2 * E
    return {"vertices": V, "internal_lines": I, "external_legs": E, "omega": omega}


graphs = [one_loop_phi3(V) for V in (1, 2, 3)]
by_external = {item["external_legs"]: item for item in graphs}

checks = {
    "one_point_is_power_divergent_before_regulator_specific_cancellations": (
        by_external[1]["omega"] == 2
    ),
    "two_point_is_logarithmic_and_momentum_degree_zero": (
        by_external[2]["omega"] == 0
    ),
    "three_point_triangle_is_uv_convergent": by_external[3]["omega"] == -2,
    "no_one_loop_wavefunction_counterterm_from_two_point_power_counting": (
        by_external[2]["omega"] < 2
    ),
    "no_one_loop_vertex_counterterm_from_triangle": by_external[3]["omega"] < 0,
}

packet = {
    "schema": "marici.benincasa.time-dependent-phi3-counterterm-inventory.v1",
    "status": "passed" if all(checks.values()) else "failed",
    "checks": checks,
    "parent_action_source": {
        "paper": "Arkani-Hamed, Benincasa, Postnikov, arXiv:1709.02813",
        "equation": 1,
        "action": (
            "S=int d^d x d eta [1/2 (partial phi)^2 "
            "- sum_{k>=3} lambda_k(eta) phi^k/k!]"
        ),
        "triangle_specialization": "k=3 at all three labelled sites",
    },
    "dimension": 4,
    "formula": "omega=4L-2I=4-E-V; at one-loop phi^3, V=I=E, so omega=4-2E",
    "one_loop_graphs": graphs,
    "inherited_counterterm_candidates": {
        "one_point": {
            "role": "background/tadpole condition",
            "status": "requires regulator and zero-one-point normalization audit",
        },
        "two_point": {
            "role": "local mass/conformal-weight counterterm",
            "status": "requires source normalization preserving the declared free state",
        },
        "three_point": {
            "role": "vertex counterterm",
            "status": "absent at one loop by power counting",
        },
        "field_strength": {
            "role": "external-leg residue",
            "status": "absent at one loop because the two-point divergence has degree zero",
        },
    },
    "rank7_frontier": (
        "Only the fixed one- and two-point counterterm insertions can modify the "
        "finite three-site readout. Their labelled insertion matrices remain to be "
        "derived; no three-point subtraction parameter exists."
    ),
    "comparison_source_warning": (
        "arXiv:2603.08794 supplies a general de Sitter EFT renormalization architecture "
        "but its derivatively coupled massless IR-safe EFT is not automatically the "
        "conformally coupled polynomial model. It is methodology, not direct authority."
    ),
    "new_carrier_support": False,
}

output = Path(__file__).with_name("time-dependent-phi3-counterterm-inventory.json")
output.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
print(json.dumps(packet, indent=2))

if packet["status"] != "passed":
    raise SystemExit(1)
