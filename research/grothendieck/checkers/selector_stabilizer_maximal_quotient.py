"""Exact selector stabilizers and coordinate-branch quotient descent."""

import json
from pathlib import Path


def stab(selector):
    return [k for k in range(32)
            if all(selector(x ^ k) == selector(x) for x in range(32))]


def descends(selector, branch_mask):
    return all(selector(x) == selector(x ^ k)
               for x in range(32)
               for k in range(32) if (k & ~branch_mask) == 0)


def main():
    selectors = {
        "delta_0": lambda x: int(x == 0),
        "constant_trace": lambda x: 1,
        "total_parity_character": lambda x: (-1) ** x.bit_count(),
        "first_coordinate": lambda x: x & 1,
        "two_coordinate_coset_indicator": lambda x: int((x & 3) == 0),
    }
    rows = []
    checks = 0
    for name, selector in selectors.items():
        stabilizer = stab(selector)
        admitted = []
        for branch_mask in range(32):
            direct = descends(selector, branch_mask)
            subgroup = [k for k in range(32) if (k & ~branch_mask) == 0]
            predicted = all(k in stabilizer for k in subgroup)
            assert direct == predicted
            checks += 32 * len(subgroup)
            if direct:
                admitted.append(branch_mask)
        rows.append({"selector": name, "stabilizer_size": len(stabilizer),
                     "stabilizer": stabilizer,
                     "admitted_coordinate_branch_masks": admitted})
    delta = next(x for x in rows if x["selector"] == "delta_0")
    trace = next(x for x in rows if x["selector"] == "constant_trace")
    assert delta["stabilizer_size"] == 1 and delta["admitted_coordinate_branch_masks"] == [0]
    assert trace["stabilizer_size"] == 32 and len(trace["admitted_coordinate_branch_masks"]) == 32
    result = {"theorem": "selector descends iff quotient kernel lies in its right stabilizer",
              "selectors": rows, "exact_checks": checks, "status": "pass"}
    out = Path(__file__).parents[1] / "results" / "selector-stabilizer-maximal-quotient.json"
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
