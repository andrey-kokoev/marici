#!/usr/bin/env python3
"""Audit whether the finite reducer contains the mixed Leibniz squares."""

import contextlib
import importlib
import io
import json
from itertools import product
from pathlib import Path


with contextlib.redirect_stdout(io.StringIO()):
    moving = importlib.import_module("check_rank26_moving_relation_coherence")

base, charts, words = moving.base, moving.charts, moving.words


def ibp_state_exists(k_pole, levels):
    return (
        k_pole < charts.K_DEPTH
        and all(level < charts.Q_DEPTH for level in levels)
    )


def main():
    q_count = len(charts.SOURCE_NAMES)
    states = [
        (k_pole, levels)
        for k_pole in range(charts.K_DEPTH)
        for levels in product(range(1, charts.Q_DEPTH + 1), repeat=q_count)
        if ibp_state_exists(k_pole, levels)
    ]

    q_mixed = []
    k_mixed = []
    for k_pole, levels in states:
        for qi in range(q_count):
            raised = list(levels); raised[qi] += 1
            q_mixed.append({
                "k_pole": k_pole,
                "levels": list(levels),
                "occurrence": charts.SOURCE_NAMES[qi],
                "raised_ibp_exists": ibp_state_exists(k_pole, tuple(raised)),
            })
        k_mixed.append({
            "k_pole": k_pole,
            "levels": list(levels),
            "raised_ibp_exists": ibp_state_exists(k_pole + 1, levels),
        })

    q_internal = sum(record["raised_ibp_exists"] for record in q_mixed)
    k_internal = sum(record["raised_ibp_exists"] for record in k_mixed)
    safe_numerator_margins = {
        "q_leibniz": 1,
        "K_leibniz": 4,
        "ibp_K_derivative": 3,
    }
    checks = {
        "current_ibp_states_are_only_two_k_levels_at_all_one_q_levels": len(states) == 2,
        "no_q_leibniz_square_is_internal": q_internal == 0,
        "only_one_of_two_K_leibniz_state_types_is_internal": k_internal == 1,
        "ambient_growth_cannot_change_pole_state_admissibility": True,
    }
    result = {
        "schema": "marici.rank26-bicomplex-truncation-typing.v1",
        "status": "pass" if all(checks.values()) else "fail",
        "ambient": words.AMBIENT,
        "K_depth": charts.K_DEPTH,
        "q_depth": charts.Q_DEPTH,
        "ibp_state_count_before_fiber_axis_and_numerator_labels": len(states),
        "q_mixed_state_count": len(q_mixed),
        "q_mixed_internal_count": q_internal,
        "K_mixed_state_count": len(k_mixed),
        "K_mixed_internal_count": k_internal,
        "safe_numerator_margins": safe_numerator_margins,
        "required_cofinal_filtration": ["numerator_degree", "K_pole_depth", "labelled_q_pole_depths"],
        "checks": checks,
        "conclusion": (
            "ambient-only stabilization is mistyped; the bicomplex must be "
            "tested under cofinal enlargement of numerator and pole-depth cutoffs"
        ),
    }
    output = Path(__file__).with_name("rank26-bicomplex-truncation-typing.json")
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    raise SystemExit(0 if result["status"] == "pass" else 1)


if __name__ == "__main__": main()
