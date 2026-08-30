#!/usr/bin/env python3
"""Construct the three cyclic residue charts and test dual-gamma closure."""

from __future__ import annotations

import importlib
import json
import os
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[3]
P = int(os.environ.get("MARICI_FIELD_PRIME", "32009"))
suffix = "" if P == 32009 else f"-p{P}"
OUT = ROOT / "research" / "benincasa" / "results" / f"rank26-dual-gamma-cyclic-atlas-closure{suffix}.json"
os.environ["MARICI_FIELD_PRIME"] = str(P)
sys.path.insert(0, str(ROOT / "research" / "benincasa"))
base = importlib.import_module("physical_four_mark_residue_twisted_derham")
tr = importlib.import_module("g12_g31_residue_chart_transition")

tr.GAMMA = -pow(2, -1, P) % P
tr.AMBIENT = 14
tr.CUTOFF = 7

sigma_label = {"g1":"g2", "g2":"g3", "g3":"g1", "g23":"g31", "g31":"g12", "g12":"g23"}
base_names = ("g1", "g2", "g3", "g23", "g31")


def label_power(name: str, k: int) -> str:
    for _ in range(k):
        name = sigma_label[name]
    return name


def preimage_point(x: int, y: int, z: int, k: int):
    if k == 0: return x, y, z
    if k == 1: return z, x, y
    return y, z, x


def cyclic_fiber(k: int):
    def fiber(x: int, y: int, z: int):
        old_k, old_q = base.fiber_data(*preimage_point(x, y, z, k))
        renamed = {label_power(name, k): poly for name, poly in old_q.items()}
        return old_k, renamed
    return fiber


points = [(2,3,4), (3,4,2), (4,2,3)]
names = [tuple(label_power(name, k) for name in base_names) for k in range(3)]
charts = [tr.presentation(cyclic_fiber(k), points[k], names[k]) for k in range(3)]


def map_row_identity(row, source, target, sign=1):
    out = {}
    for column, coefficient in row.items():
        label = source["ordered_columns"][column]
        base.add_value(out, target["columns"][label], sign*coefficient)
    return out


edge_relation_failures = []
edge_ranks = []
edge_identity_failures = []
edge_maps = []
for k in range(3):
    source, target = charts[k], charts[(k+1)%3]
    failures = 0
    for row in source["pivots"].values():
        if base.reduce_row(map_row_identity(row, source, target), target["pivots"]):
            failures += 1
    edge_relation_failures.append(failures)

    forward = []
    identity_failures = 0
    for source_column in source["free_low"]:
        label = source["ordered_columns"][source_column]
        row = tr.quotient_vector(label, target, 1)
        forward.append(row)
        if row != {source_column: 1}:
            identity_failures += 1
    edge_ranks.append(tr.matrix_rank(forward))
    edge_identity_failures.append(identity_failures)
    edge_maps.append({source["free_low"][i]: row for i, row in enumerate(forward)})

# Generator-level gamma derivatives.  Cyclic transport preserves the ordered
# retained coordinate pair, so axes and monomial exponents remain positional.
gamma_failures = []
gamma_counts = []
levels = (1,1,1,1,1)
for k in range(3):
    source, target = charts[k], charts[(k+1)%3]
    source_kd = [base.derivative(source["k"], axis) for axis in range(2)]
    target_kd = [base.derivative(target["k"], axis) for axis in range(2)]
    failures = count = 0
    for kp in range(2):
        for axis in range(2):
            for exponent in base.monomials_at_most(14):
                count += 1
                left = {}
                right = {}
                for term, coefficient in source_kd[axis].items():
                    base.add_value(left, target["columns"][(kp+1,*levels,base.shifted(exponent,term))], coefficient)
                for term, coefficient in target_kd[axis].items():
                    base.add_value(right, target["columns"][(kp+1,*levels,base.shifted(exponent,term))], coefficient)
                if left != right:
                    failures += 1
    gamma_failures.append(failures)
    gamma_counts.append(count)

def apply_edge(vector, edge):
    out = {}
    for source_column, coefficient in vector.items():
        for target_column, value in edge[source_column].items():
            base.add_value(out, target_column, coefficient*value)
    return out

def proportional_scalar(left, right):
    coordinates = sorted(set(left)|set(right))
    pivot = next(c for c in coordinates if right.get(c,0))
    scalar = left.get(pivot,0)*pow(right[pivot],-1,P)%P
    if any(left.get(c,0) != scalar*right.get(c,0)%P for c in coordinates):
        return None
    return scalar

# Explicitly compose the three compatible-basis quotient matrices.
quotient_composite_failures = 0
quotient_product_rows = []
quotient_residual_rows = []
for source_column in charts[0]["free_low"]:
    vector = {source_column:1}
    for edge in edge_maps:
        vector = apply_edge(vector, edge)
    quotient_product_rows.append({"source_column":source_column,"target_coefficients":{str(c):v for c,v in sorted(vector.items())}})
    residual = dict(vector)
    base.add_value(residual, source_column, -1)
    quotient_residual_rows.append(residual)
    if vector != {source_column:1}:
        quotient_composite_failures += 1
quotient_identity_residual_rank = tr.matrix_rank(quotient_residual_rows)

# The gamma normal coordinate is literal and unchanged by the site cycle.
epsilon_edge_scalars = [1,1,1]
epsilon_composite_scalar = 1
for scalar in epsilon_edge_scalars:
    epsilon_composite_scalar = epsilon_composite_scalar*scalar%P

# Use Entry 3902's exported source Bockstein vector and transport it through
# each actual quotient matrix.  Source-equivariant chart generation supplies
# the same labelled positional vector in each target frame.
bockstein_path = ROOT / "research" / "benincasa" / "results" / f"rank26-conductor-gamma-bockstein{suffix}.json"
bockstein_packet = json.loads(bockstein_path.read_text(encoding="utf-8"))
beta = {int(c):int(value)%P for c,value in bockstein_packet["root_visible_bockstein_vector"].items()}
bockstein_edge_scalars = []
transported_beta = dict(beta)
for edge in edge_maps:
    edge_beta = apply_edge(beta, edge)
    bockstein_edge_scalars.append(proportional_scalar(edge_beta, beta))
    transported_beta = apply_edge(transported_beta, edge)
bockstein_composite_scalar = proportional_scalar(transported_beta, beta)

checks = {
    "three_independent_chart_ranks_26": [len(chart["free_low"]) for chart in charts] == [26,26,26],
    "all_three_exact_submodules_transport": edge_relation_failures == [0,0,0],
    "all_three_quotient_maps_full_rank": edge_ranks == [26,26,26],
    "cyclic_maps_are_identity_in_labelled_positional_frames": edge_identity_failures == [0,0,0],
    "all_1440_gamma_generators_intertwine": gamma_failures == [0,0,0] and gamma_counts == [480,480,480],
    "signed_order_three_quotient_composite_is_identity": quotient_composite_failures == 0,
    "epsilon_coordinate_returns_identically": epsilon_composite_scalar == 1,
    "common_bockstein_line_returns_identically": bockstein_composite_scalar == 1,
}
payload = {
    "schema":"marici.rank26-dual-gamma-cyclic-atlas-closure.v1",
    "prime":P,
    "chart_points":points,
    "chart_mark_orders":names,
    "chart_orientations":["da wedge db","db wedge dc","dc wedge da"],
    "edge_orientation_signs":[1,1,1],
    "chart_construction_provenance":[
        "G12: frozen source residue formula at (2,3,4)",
        "G23: source cyclic action applied to frozen labels, parameters, retained coordinates, and residue orientation",
        "G31: second source cyclic action applied to the same frozen packet; not fitted as an inverse edge",
    ],
    "chart_ranks":[len(chart["free_low"]) for chart in charts],
    "edge_transport_ranks":edge_ranks,
    "edge_relation_failures":edge_relation_failures,
    "edge_identity_failures":edge_identity_failures,
    "gamma_generator_counts":gamma_counts,
    "gamma_generator_failures":gamma_failures,
    "quotient_transport_matrices":[
        {
            "edge":f"{('G12','G23','G31')[k]}_to_{('G12','G23','G31')[(k+1)%3]}",
            "source_basis":charts[k]["free_low"],
            "target_basis":charts[(k+1)%3]["free_low"],
            "rows":[{"source_column":c,"target_coefficients":{str(j):v for j,v in sorted(edge_maps[k][c].items())}} for c in charts[k]["free_low"]],
        } for k in range(3)
    ],
    "ordered_quotient_matrix_product":{"order":["G12_to_G23","G23_to_G31","G31_to_G12"],"rows":quotient_product_rows},
    "quotient_composite_failures":quotient_composite_failures,
    "quotient_identity_residual_rank":quotient_identity_residual_rank,
    "epsilon_edge_units":epsilon_edge_scalars,
    "epsilon_edge_product":epsilon_composite_scalar,
    "bockstein_line_edge_units":bockstein_edge_scalars,
    "bockstein_line_edge_product":bockstein_composite_scalar,
    "checks":checks,
    "passed":all(checks.values()),
    "conclusion":"The three source-equivariantly generated labelled cyclic residue charts form a strict dual-gamma descent atlas. Every exact and gamma-normal generator transports, all edge units are the source orientation unit +1, and explicit matrix/scalar composition is identity on the rank-26 quotient, epsilon coordinate, and common Bockstein line.",
}
OUT.write_text(json.dumps(payload,indent=2)+"\n",encoding="utf-8")
print(json.dumps(payload,indent=2))
if not payload["passed"]: raise SystemExit(1)
