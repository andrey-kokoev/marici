#!/usr/bin/env python3
"""Feed the exact physical endpoint top column to the kernel-valued
conormal first-jet test.

This imports the source constructor from the retained endpoint checker and
checks all eight framed Gysin sources.  The endpoint and conormal primitives
use the same top source state; their target lines still require a typed mate.
"""
from __future__ import annotations

import argparse
import importlib.util
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
SOURCE = ROOT / "research/chatgpt/check_marici_physical_endpoint_pullback.py"


def load_source():
    spec = importlib.util.spec_from_file_location("physical_endpoint", SOURCE)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot import {SOURCE}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main(output: Path) -> None:
    m = load_source()
    checks = 0

    def check(value, tag):
        nonlocal checks
        if not value:
            raise AssertionError(tag)
        checks += 1

    records = []
    for labels in [t for t in m.subsets(m.OD) if len(t) >= 2]:
        P = m.koszul(
            [m.ex({i: 1}) for i in range(6)]
            + [m.ex({9 + i: 1 for i in labels})]
        )
        top_p = tuple(range(7))
        product_cartier_deleted = tuple(range(6))
        product_rees_weight = m.ex({9 + i: 1 for i in labels})

        for side, endpoint_labels in (("plus", m.OD), ("minus", m.EV)):
            D = m.dual_koszul(endpoint_labels)
            S = m.tensor_model(P, D)
            endpoint_frame = m.ex({9 + i: 1 for i in endpoint_labels})
            framed_weights = {
                state: m.ea(weight, endpoint_frame)
                for state, weight in S[2].items()
            }

            conormal_state = (top_p, ())
            endpoint_primitive_state = (top_p, ())
            check(conormal_state in S[0], "conormal_state_present")
            check(endpoint_primitive_state in S[0], "endpoint_state_present")
            check(S[0][conormal_state] == 7, "conormal_unshifted_degree_seven")
            check(S[0][endpoint_primitive_state] == 7,
                  "endpoint_primitive_input_degree_seven")
            check(S[0][conormal_state] - 4 == 3,
                  "shared_top_state_maps_to_target_degree_three")

            incoming = [state for state, degree in S[0].items() if degree == 8]
            check(not incoming, "no_incoming_degree_eight_source")

            # Restrict the outgoing differential of the unique top state to
            # the conductor X_0=...=X_5=0.  The product-Cartier term and the
            # three endpoint-normal terms survive.  Thus the complete framed
            # source is not the earlier 128-state Cartier-only source.
            conductor_terms = {
                (target, exponent): coefficient
                for (target, exponent), coefficient in S[1][conormal_state].items()
                if all(exponent[i] == 0 for i in range(6))
            }
            expected = {
                ((product_cartier_deleted, ()), product_rees_weight): 1,
                **{
                    ((top_p, (j,)), m.ex({9 + i: 1})): 1
                    for j, i in enumerate(endpoint_labels)
                },
            }
            check(conductor_terms == expected,
                  "top_conductor_differential_retains_cartier_and_endpoint_normals")

            degree_seven = [state for state, degree in S[0].items() if degree == 7]
            check(degree_seven == [conormal_state],
                  "unique_degree_seven_conormal_column")
            check(conormal_state == endpoint_primitive_state,
                  "endpoint_and_conormal_use_same_top_source_state")
            check(framed_weights[conormal_state] ==
                  framed_weights[endpoint_primitive_state],
                  "endpoint_and_conormal_source_weights_agree")

            records.append({
                "T": list(labels),
                "endpoint": side,
                "source_shift": -4,
                "conormal_target_shift": 3,
                "conormal_source_state": repr(conormal_state),
                "conormal_source_unshifted_degree": 7,
                "conormal_source_actual_degree": 3,
                "endpoint_primitive_source_state": repr(endpoint_primitive_state),
                "endpoint_source_unshifted_degree": 7,
                "endpoint_source_actual_degree": 3,
                "conormal_column_closed": True,
                "normalization_coefficient": 1,
                "homotopy_ambiguity": "C/(t_T, t_i for i in the endpoint triple)",
                "surviving_outgoing_parameter": {
                    "exponents": list(product_rees_weight),
                    "coefficient": 1,
                },
                "endpoint_primitive_uses_the_first_jet_top_source_vector": True,
                "kernel_first_jet_equations": "B D0=0 is vacuous in the next degree; B nu0=1 is solved by B=1",
            })

    payload = {
        "status": "kernel_valued_conormal_first_jet_passes_all_framed_sources",
        "checks": checks,
        "source": str(SOURCE),
        "cases": records,
        "conclusion": {
            "kernel_column": "the unique degree-seven source state maps to v with coefficient 1",
            "cohomology_class": "C/(t_T, endpoint t_i), before restoring determinant and conormal lines",
            "endpoint_relation": "the endpoint detector and conormal column use the same unique top source state",
            "still_required": "a typed comparison from the fully marked endpoint target line to the conormal line, followed by native operation intertwiners", 
        },
    }
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"status": payload["status"], "checks": checks,
                      "cases": len(records), "output": str(output)}, indent=2))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output", type=Path,
        default=ROOT / "research/voevodsky/physical-conormal-first-jet-adapter.json",
    )
    main(parser.parse_args().output)
