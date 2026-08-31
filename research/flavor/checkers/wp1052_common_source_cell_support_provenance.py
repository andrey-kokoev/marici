import json
import math
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
Q = Fraction(1, 4)
H = Fraction(1, 2)


def atom(name, cells, outcome, weight):
    return {
        "name": name,
        "cells": frozenset(cells),
        "outcome": outcome,
        "weight": Fraction(weight),
    }


# Minimal common-source support cell.  Every atom carries detector/monitor
# provenance and a detected/null outcome label.  The shared X atoms are counted
# in both typed cells, which is exactly what makes them cross-cell amplitudes.
shared_cell = [
    atom("F_det", {"detector"}, "detected", Q),
    atom("F_null", {"detector"}, "null", Q),
    atom("R_det", {"monitor"}, "detected", Q),
    atom("R_null", {"monitor"}, "null", Q),
    atom("X_det", {"detector", "monitor"}, "detected", Q),
    atom("X_null", {"detector", "monitor"}, "null", Q),
]

# A scalar proxy can declare the same support and monitor records while having
# no atom with both detector and monitor provenance.
declared_proxy = [
    atom("F_det", {"detector"}, "detected", H),
    atom("F_null", {"detector"}, "null", H),
    atom("R_det", {"monitor"}, "detected", H),
    atom("R_null", {"monitor"}, "null", H),
]


def frac_sqrt(x):
    n = math.isqrt(x.numerator)
    d = math.isqrt(x.denominator)
    assert n * n == x.numerator and d * d == x.denominator
    return Fraction(n, d)


def derive_cell(cell):
    assert cell
    for a in cell:
        assert a["cells"] <= {"detector", "monitor"} and a["cells"]
        assert a["outcome"] in {"detected", "null"}
        assert a["weight"] >= 0

    def total(pred):
        return sum((a["weight"] for a in cell if pred(a)), Fraction(0))

    alpha = total(lambda a: "detector" in a["cells"])
    beta = total(lambda a: "monitor" in a["cells"])
    cross = total(lambda a: a["cells"] == {"detector", "monitor"})
    det_seen = total(lambda a: "detector" in a["cells"] and a["outcome"] == "detected")
    det_null = total(lambda a: "detector" in a["cells"] and a["outcome"] == "null")
    mon_seen = total(lambda a: "monitor" in a["cells"] and a["outcome"] == "detected")
    mon_null = total(lambda a: "monitor" in a["cells"] and a["outcome"] == "null")
    cross_seen = total(lambda a: a["cells"] == {"detector", "monitor"} and a["outcome"] == "detected")
    cross_null = total(lambda a: a["cells"] == {"detector", "monitor"} and a["outcome"] == "null")

    detector_null_complete = det_seen + det_null == alpha
    monitor_null_complete = mon_seen + mon_null == beta
    cross_null_complete = cross_seen + cross_null == cross
    null_complete = detector_null_complete and monitor_null_complete and cross_null_complete

    assert alpha > 0 and beta > 0
    c = cross / frac_sqrt(alpha * beta) if cross else Fraction(0)
    eta = mon_seen / beta
    sigma = Fraction(1) if cross > 0 else Fraction(0)
    provenance_ok = cross > 0 and all(
        a["cells"] == {"detector", "monitor"} and a["outcome"] in {"detected", "null"}
        for a in cell
        if a["name"].startswith("X_")
    )

    return {
        "alpha": alpha,
        "beta": beta,
        "cross": cross,
        "c": c,
        "eta": eta,
        "sigma": sigma,
        "detector_null_complete": detector_null_complete,
        "monitor_null_complete": monitor_null_complete,
        "cross_null_complete": cross_null_complete,
        "null_complete": null_complete,
        "provenance_ok": provenance_ok,
    }


def wp1051_rows(derived, B, L, g, nu, d):
    alpha = derived["alpha"]
    beta = derived["beta"]
    c = derived["c"]
    eta = derived["eta"]
    sigma = derived["sigma"]
    return {
        "B": B,
        "S": B + alpha * L * g * g,
        "D": Fraction(4) * nu * d * c * sigma * L * g,
        "Vref": nu,
        "epoch": d,
        "M": eta * c * beta,
        "N": eta * beta,
        "alpha": alpha,
        "beta": beta,
        "c": c,
        "eta": eta,
        "sigma": sigma,
    }


shared = derive_cell(shared_cell)
assert shared == {
    "alpha": 1,
    "beta": 1,
    "cross": H,
    "c": H,
    "eta": H,
    "sigma": 1,
    "detector_null_complete": True,
    "monitor_null_complete": True,
    "cross_null_complete": True,
    "null_complete": True,
    "provenance_ok": True,
}

B = Fraction(0)
L = Fraction(4)
g = Fraction(1)
nu = Fraction(1)
d = Fraction(1)
shared_rows = wp1051_rows(shared, B, L, g, nu, d)
assert shared_rows == {
    "B": 0,
    "S": 4,
    "D": 8,
    "Vref": 1,
    "epoch": 1,
    "M": Q,
    "N": H,
    "alpha": 1,
    "beta": 1,
    "c": H,
    "eta": H,
    "sigma": 1,
}

proxy = derive_cell(declared_proxy)
assert proxy["alpha"] == 1 and proxy["beta"] == 1 and proxy["eta"] == H
assert proxy["cross"] == 0 and proxy["c"] == 0 and proxy["sigma"] == 0
assert proxy["null_complete"] and not proxy["provenance_ok"]

# Declared scalar overlap can mimic the monitor records and fake the science
# row, but the atom-derived rows expose the missing cross provenance.
proxy_declared = dict(proxy)
proxy_declared["c"] = H
proxy_declared["sigma"] = Fraction(1)
proxy_declared_rows = wp1051_rows(proxy_declared, B, L, g, nu, d)
proxy_derived_rows = wp1051_rows(proxy, B, L, g, nu, d)
assert proxy_declared_rows["M"] == shared_rows["M"] == Q
assert proxy_declared_rows["N"] == shared_rows["N"] == H
assert proxy_declared_rows["D"] == shared_rows["D"] == 8
assert proxy_derived_rows["D"] == 0

result = {
    "schema": "marici.flavor.wp1052.v1",
    "status": "PASS",
    "question": "Can detector and monitor cell supports be derived from one typed physical16 source cell rather than declared as separate instrument coordinates?",
    "shared_cell_atoms": [
        {"name": a["name"], "cells": sorted(a["cells"]), "outcome": a["outcome"], "weight": str(a["weight"])}
        for a in shared_cell
    ],
    "derived_shared_cell": {k: (str(v) if isinstance(v, Fraction) else v) for k, v in shared.items()},
    "wp1051_rows_from_common_source": {k: str(v) for k, v in shared_rows.items()},
    "declared_overlap_proxy": {
        "atoms": [
            {"name": a["name"], "cells": sorted(a["cells"]), "outcome": a["outcome"], "weight": str(a["weight"])}
            for a in declared_proxy
        ],
        "derived": {k: (str(v) if isinstance(v, Fraction) else v) for k, v in proxy.items()},
        "declared_rows": {k: str(v) for k, v in proxy_declared_rows.items()},
        "derived_rows": {k: str(v) for k, v in proxy_derived_rows.items()},
    },
    "classification": "conditional common-source support constructor: finite atom provenance derives detector support, monitor support, overlap, efficiency, same-cell certificate, and null completeness from one typed cell",
    "remaining_gate": "derive the atom weights and detector/monitor/cross/null labels from physical16 source dynamics; this packet supplies the minimal support-provenance algebra, not the physical action",
    "claim_boundary": "finite two-cell support algebra with exact branch weights; no continuum event space, detector dynamics, or numerical source selection is claimed",
    "disposition": "productive: WP1051's typed supports now have a minimal common-source provenance realization and a declared-overlap falsifier",
}

(ROOT / "results" / "wp1052_common_source_cell_support_provenance.json").write_text(json.dumps(result, indent=2) + "\n")
print("WP1052 PASS:", shared["alpha"], shared["beta"], shared["c"], shared["eta"], proxy_derived_rows["D"])
