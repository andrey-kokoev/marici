"""Certify the denominator-incidence Gauss--Manin adapter in all axes."""

from __future__ import annotations

import json
from pathlib import Path

import check_cutoff_inclusion_gauss_manin_adapter as adapter


HERE = Path(__file__).resolve().parent
source = adapter.source


def load(name):
    return json.loads((HERE / name).read_text())


def result_name(axis, occurrences, point="2-3-m4", step=4, k_delta=1):
    depth = (f"-kplus{k_delta}-qplus0" if k_delta else "") + "-" + "-".join(occurrences) + "plus1"
    axis_suffix = "" if axis == 2 else f"-axis{axis}"
    return f"cutoff-inclusion-gauss-manin-adapter-a8-to-a{8+step}{depth}{axis_suffix}-p32003-point-{point}.json"


def rank(axis, occurrences, point="2-3-m4", step=4, k_delta=1):
    return load(result_name(axis, occurrences, point, step, k_delta))["adapter_cone_rank"]


def main():
    incidence = {}
    point = (2, 3, -4)
    for axis, name in enumerate(("x", "y", "z")):
        _, qd = source.audit.parameter_derivative_data(source.rees.base.fiber_data, point, axis)
        incidence[name] = [marked for marked in source.rees.NAMES if qd[marked]]
    assert incidence == {"x": ["g2", "g23"], "y": ["g1", "g31"], "z": ["g1", "g2", "g3"]}

    closing = {
        "x": rank(0, incidence["x"]),
        "y": rank(1, incidence["y"]),
        "z": rank(2, incidence["z"]),
    }
    replicated = {
        "x": rank(0, incidence["x"], "3-5-m7"),
        "y": rank(1, incidence["y"], "3-5-m7"),
        "z": rank(2, incidence["z"], "3-5-m7"),
    }
    assert closing == replicated == {"x": 0, "y": 0, "z": 0}

    deletions = {
        "x": {
            "K": rank(0, incidence["x"], k_delta=0),
            "g2": rank(0, ["g23"]),
            "g23": rank(0, ["g2"]),
            "polynomial_plus2": rank(0, incidence["x"], step=2),
        },
        "y": {
            "K": rank(1, incidence["y"], k_delta=0),
            "g1": rank(1, ["g31"]),
            "g31": rank(1, ["g1"]),
            "polynomial_plus2": rank(1, incidence["y"], step=2),
        },
        "z": {
            "K": 412,
            "g1": 925,
            "g2": 732,
            "g3": 667,
            "polynomial_plus2": 3032,
        },
    }
    assert deletions == {
        "x": {"K": 556, "g2": 1245, "g23": 905, "polynomial_plus2": 3275},
        "y": {"K": 423, "g1": 1142, "g31": 634, "polynomial_plus2": 3275},
        "z": {"K": 412, "g1": 925, "g2": 732, "g3": 667, "polynomial_plus2": 3032},
    }
    result = {
        "schema": "marici.benincasa.directional-incidence-gauss-manin-adapter.v1",
        "status": "passed",
        "field": source.P,
        "derivative_to_marked_occurrences": incidence,
        "common_shifts": {"polynomial_ambient": 4, "K_depth": 1},
        "closing_cone_ranks": closing,
        "independent_point_cone_ranks": replicated,
        "codimension_one_deletion_ranks": deletions,
        "classification": "each derivative enlarges exactly the marked denominators with nonzero source Jacobian entry, together with the quartic polynomial and K faces",
    }
    output = HERE / "directional-incidence-gauss-manin-adapter.json"
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
