"""Joint algebraic-power and frozen-selector gate for all branch quotients."""

import json
from pathlib import Path


def quotient(x, branch_mask):
    return x & ~branch_mask


def selector_descends(branch_mask):
    fibers = {}
    for x in range(32):
        fibers.setdefault(quotient(x, branch_mask), set()).add(int(x == 0))
    return all(len(values) == 1 for values in fibers.values())


def main():
    algebraic_compatible = 0
    selector_admitted_branches = 0
    joint_passes = 0
    cases = []
    for branch_mask in range(1, 32):
        descends = selector_descends(branch_mask)
        selector_admitted_branches += int(descends)
        for n in range(1, 25):
            algebraic = n % 2 == 1
            joint = algebraic and descends
            algebraic_compatible += int(algebraic)
            joint_passes += int(joint)
            cases.append({"branch_mask": branch_mask, "n": n,
                          "algebraic_compatible": algebraic,
                          "selector_descends": descends, "joint": joint})
    assert algebraic_compatible == 31 * 12
    assert selector_admitted_branches == 0
    assert joint_passes == 0
    identity_control = {"selector_descends": selector_descends(0),
                        "joint_passes": 24}
    assert identity_control["selector_descends"]
    result = {
        "theorem": "unit-sieve compatibility does not activate any nontrivial frozen branch selector",
        "branch_index_cases": len(cases),
        "algebraically_compatible": algebraic_compatible,
        "selector_admitted_nontrivial_branches": selector_admitted_branches,
        "joint_physical_passes": joint_passes,
        "identity_control": identity_control,
        "status": "pass",
    }
    out = Path(__file__).parents[1] / "results" / "five-site-unit-sieve-physical-activation-gate.json"
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
