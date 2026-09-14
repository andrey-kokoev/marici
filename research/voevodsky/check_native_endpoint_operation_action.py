#!/usr/bin/env python3
"""Construct the nine quadratic chain actions on the native endpoint bar.

This is the genuinely B-linear separated endpoint model.  It is not an action
on the literal ambient A-Hom, whose mixed weights are already known acyclic.
"""
from __future__ import annotations

import argparse
import importlib.util
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
SOURCE = ROOT / "research/chatgpt/check_marici_physical_change_of_rings.py"


def load_source():
    spec = importlib.util.spec_from_file_location("change_rings", SOURCE)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot import {SOURCE}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def total_weight(alpha):
    return sum(alpha)


def main(output: Path) -> None:
    m = load_source()
    checks = 0

    def check(value, tag):
        nonlocal checks
        if not value:
            raise AssertionError(tag)
        checks += 1

    max_weight = 4
    algebra = m.dual_integral_complex(m.bar_model(max_weight))
    generators = m.op_generators()
    quadratics = {
        key: m.raw_cochain(value)
        for key, value in generators.items()
        if sum(map(len, key)) == 2
    }
    check(len(quadratics) == 9, "nine_quadratic_operations")

    records = []
    for side_name, side in (("plus", m.OD), ("minus", m.EV)):
        endpoint = m.dual_integral_complex(m.bar_model(max_weight, side))
        sdr, _ = m.weight_sdr(endpoint)
        unit = {((), m.NZ): 1}
        images = []

        for key, operation in sorted(quadratics.items(), key=repr):
            check(not m.lin(algebra[1], operation), "quadratic_operation_closed")
            primitive_image = m.cup(operation, unit)
            check(not m.lin(endpoint[1], primitive_image),
                  "quadratic_primitive_image_closed")
            images.append(m.project_vec(primitive_image, sdr, endpoint[2]))

            tested_columns = 0
            for basis, degree in endpoint[0].items():
                if total_weight(endpoint[2][basis]) + 2 > max_weight:
                    continue
                vector = {basis: 1}
                acted = m.cup(operation, vector)
                # Quadratic operations have even cohomological degree, so the
                # chain-map equation has no additional Koszul sign.
                left = m.lin(endpoint[1], acted)
                right = m.cup(operation, m.lin(endpoint[1], vector))
                check(left == right, "quadratic_cup_action_chain_map")
                tested_columns += 1

            records.append({
                "endpoint": side_name,
                "operation": repr(key),
                "operation_degree": 2,
                "formula": "rho_r(h)=r cup h",
                "tested_source_columns": tested_columns,
                "primitive_image_terms": len(primitive_image),
            })

        check(m.linear_rank(images) == 9,
              "nine_primitive_operation_images_independent")

    payload = {
        "status": "nine_native_quadratic_chain_actions_constructed",
        "checks": checks,
        "source": str(SOURCE),
        "records": records,
        "scope": {
            "model": "RHom_B(B_sigma,C) native reduced bar, weights <= 4",
            "coefficient_extension": "tensor with the primitive endpoint line W_sigma",
            "action": "left cup composition by closed relative bar cochains",
            "literal_ambient_A_Hom": False,
            "actual_spatial_target_identification": False,
        },
        "next_gate": "intertwine these native bar actions with the conormal j35 orbit, including the precomposition/postcomposition mate and line transport",
    }
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "status": payload["status"],
        "checks": checks,
        "operation_endpoint_pairs": len(records),
        "output": str(output),
    }, indent=2))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output", type=Path,
        default=ROOT / "research/voevodsky/native-endpoint-operation-action.json",
    )
    main(parser.parse_args().output)
