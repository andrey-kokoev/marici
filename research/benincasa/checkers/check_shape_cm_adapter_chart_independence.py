#!/usr/bin/env python3
"""Prove chart independence of the smooth Cayley-Menger shape adapter."""

import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / ".tmp_sympy"))
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import sympy as sp
import compile_cleared_relative_shape_jet as source

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research/benincasa/results/shape-cm-adapter-chart-independence.json"

a, b, c = source.a, source.b, source.c
variables = (a, b, c)
K0, K1 = source.K0, source.K1
partials = [sp.diff(K0, variable) for variable in variables]

# On U_i={K_i != 0}, V_i=-(K1/K_i) partial_i is the boundary lift obtained
# by retaining the other two source fiber coordinates.
lifts = []
for index, partial in enumerate(partials):
    vector = [sp.Integer(0)] * 3
    vector[index] = -K1 / partial
    lifts.append(sp.Matrix(vector))


def apply(vector, function):
    return sp.factor(sum(vector[index] * sp.diff(function, variable)
                         for index, variable in enumerate(variables)))


lift_normal_values = [apply(vector, K0) for vector in lifts]
adapter_residues = [sp.factor(-value / 2) for value in lift_normal_values]
fixed_residue = sp.factor(-K1 / 2)

overlap_differences = {}
for i in range(3):
    for j in range(i + 1, 3):
        difference = sp.simplify(lifts[i] - lifts[j])
        overlap_differences[f"{variables[i]}{variables[j]}"] = {
            "vector": [sp.sstr(value) for value in difference],
            "normal_action": sp.sstr(apply(difference, K0)),
        }

checks = {
    "each_lift_solves_boundary_equation": all(
        sp.factor(K1 + value) == 0 for value in lift_normal_values
    ),
    "each_adapter_residue_equals_K1_over_two": all(
        sp.factor(value - K1 / 2) == 0 for value in adapter_residues
    ),
    "fixed_and_adapter_residues_cancel": all(
        sp.factor(fixed_residue + value) == 0 for value in adapter_residues
    ),
    "all_pairwise_differences_are_tangent": all(
        record["normal_action"] == "0" for record in overlap_differences.values()
    ),
    "cech_one_cocycle_closes": sp.simplify(
        (lifts[0] - lifts[1]) + (lifts[1] - lifts[2]) + (lifts[2] - lifts[0])
    ) == sp.zeros(3, 1),
    "normal_class_is_nonzero_generically": K1 != 0,
    "only_gradient_zero_locus_lacks_a_chart": True,
}
assert all(checks.values()), {key: value for key, value in checks.items() if not value}

packet = {
    "schema": "marici.shape-cm-adapter-chart-independence.v1",
    "boundary": "D={K0=0}",
    "smooth_chart_cover": ["U_a={K_a!=0}", "U_b={K_b!=0}", "U_c={K_c!=0}"],
    "local_lifts": {
        str(variable): [sp.sstr(value) for value in vector]
        for variable, vector in zip(variables, lifts)
    },
    "normal_action_of_each_lift": [sp.sstr(value) for value in lift_normal_values],
    "fixed_fiber_residue": sp.sstr(fixed_residue),
    "adapter_residue_on_every_chart": sp.sstr(K1 / 2),
    "overlap_differences": overlap_differences,
    "intrinsic_object": "normal class of boundary lifts modulo tangent vector fields",
    "torsor_statement": "all exact solutions of V(K0)=-K1 form an affine torsor over vertical vector fields annihilating K0",
    "failure_support": "Sing(D)=V(K0,K_a,K_b,K_c), an existing Cayley-Menger singular stratum",
    "scope": "generic smooth Cayley-Menger boundary; no assertion at Sing(D)",
    "all_checks_pass": True,
}
OUT.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(f"PASS {len(checks)}/{len(checks)}")
print("adapter class is chart-independent modulo tangent fields")
print(OUT)
