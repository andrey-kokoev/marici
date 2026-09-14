#!/usr/bin/env python3
"""Construct the first endpoint-to-conormal mate in the primitive fine frame.

The integral fully-marked endpoint detector annihilates incoming boundaries;
its value multiplies the closed normalized conormal top column.  This is a
strict map of the selected homogeneous chain complexes.  It does not claim a
native-operation-linear extension to the other fine weights.
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
        lam = m.es(
            m.es(m.GAMMA, m.ex({i: 1 for i in range(6)})),
            m.ex({9 + i: 1 for i in labels}),
        )
        top_p = tuple(range(7))

        for side, endpoint_labels, face in (
            ("plus", m.OD, m.VP),
            ("minus", m.EV, m.VM),
        ):
            D = m.dual_koszul(endpoint_labels)
            S = m.tensor_model(P, D)
            endpoint_frame = m.ex({9 + i: 1 for i in endpoint_labels})
            ll = m.ea(lam, endpoint_frame)
            # The determinant frame is carried by the external Hom shift ll;
            # adding it to the source weights as well would count it twice.
            g, d, cf = m.bare_hom(S, ll, ())
            gv, dv = m.bare_section(g, d, "V")
            residual, inclusions, _ = m.sdr_cycles(gv, dv)
            survivors = [state for state in residual if gv[state] == -4]
            check(len(survivors) == 1, "unique_endpoint_primitive")
            cycle = inclusions[survivors[0]]

            endpoint_source_state = (top_p, ())
            endpoint_target_state = (face, face)
            distinguished = (endpoint_source_state, endpoint_target_state)
            value = cycle.get(distinguished, 0)
            check(abs(value) == 1, "endpoint_detector_is_unit_normalized")
            normalized_cycle = m.scale(cycle, value)
            check(normalized_cycle.get(distinguished) == 1,
                  "normalized_endpoint_primitive_value_one")

            # The distinguished coefficient annihilates every boundary entering
            # the primitive degree.  This makes it a well-defined integral
            # functional on H^{-4} in the selected fine frame.
            incoming = [state for state in gv if gv[state] == -5]
            for state in incoming:
                check(dv[state].get(distinguished, 0) == 0,
                      "endpoint_detector_annihilates_boundary")

            # The conormal output is the unique source state in unshifted
            # degree seven (actual degree three after [-4]).
            conormal_state = (top_p, ())
            degree_seven = [state for state, degree in S[0].items()
                            if degree == 7]
            check(degree_seven == [conormal_state],
                  "unique_normalized_conormal_output")
            incoming_conormal = [state for state, degree in S[0].items()
                                  if degree == 8]
            check(not incoming_conormal, "conormal_output_is_closed")

            records.append({
                "T": list(labels),
                "endpoint": side,
                "endpoint_hom_degree": -4,
                "endpoint_detector_column": repr(distinguished),
                "endpoint_detector_value": 1,
                "endpoint_boundary_columns_tested": len(incoming),
                "conormal_source_state": repr(conormal_state),
                "conormal_actual_source_degree": 3,
                "mate_degree_displacement": 0,
                "primitive_cohomology_map": "[nu_sigma] -> [1 mod (t_T, endpoint t_i)]",
            })

    payload = {
        "status": "primitive_fine_frame_chain_mate_constructed_operation_extension_open",
        "checks": checks,
        "cases": records,
        "construction": {
            "input": "integral detector of the fully marked endpoint H^{-4} class",
            "output": "normalized unique conormal top column in H^0 Hom(P^G,K[3])",
            "formula": "z maps to detector(z) times (top^vee tensor v)",
            "degree_displacement": 0,
        },
        "not_constructed": [
            "an extension beyond the selected primitive homogeneous frame",
            "the nine mixed-weight operation intertwiners",
            "a native-ring geometric target mate",
            "determinant-line identification outside the selected fine frames",
        ],
    }
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "status": payload["status"],
        "checks": checks,
        "cases": len(records),
        "output": str(output),
    }, indent=2))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output", type=Path,
        default=ROOT / "research/voevodsky/endpoint-to-conormal-cohomology-mate.json",
    )
    main(parser.parse_args().output)
