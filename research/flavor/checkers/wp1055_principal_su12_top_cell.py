import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def principal_adjoint_cell(n):
    spins = list(range(1, n))
    dimensions = [2 * j + 1 for j in spins]
    assert sum(dimensions) == n * n - 1
    return spins, dimensions


def top_cell(n):
    spins, dimensions = principal_adjoint_cell(n)
    return {
        "parent_n": n,
        "spins": spins,
        "dimensions": dimensions,
        "adjoint_dimension": n * n - 1,
        "top_spin": spins[-1],
        "top_C": dimensions[-1],
    }


# Conditional parent/top-cell law: the WP1036 factor 12 is interpreted as an
# SU(12) parent, and the pole operator is the top principal-sl2 component.
parent = top_cell(12)
assert parent["dimensions"] == [3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23]
assert parent["adjoint_dimension"] == 143
assert parent["top_spin"] == 11
assert parent["top_C"] == 23

nilpotent_ports = ("E", "F")
k = len(nilpotent_ports)
assert k == 2
h_pi2_coefficient = Fraction(parent["top_C"] * parent["parent_n"], 1367 * k)
assert h_pi2_coefficient == Fraction(138, 1367)
normalized_response = Fraction(1, 2)

# The top-cell requirement selects n=12 uniquely in a broad bounded parent
# scan.  Merely containing spin 11 somewhere is insufficient: SU(13) contains
# it as a lower component, while its top cell has C=25.
unique_top_parents = [n for n in range(2, 31) if top_cell(n)["top_C"] == 23]
assert unique_top_parents == [12]

too_small = top_cell(11)
too_large = top_cell(13)
assert too_small["top_spin"] == 10 and too_small["top_C"] == 21
assert too_large["top_spin"] == 12 and too_large["top_C"] == 25
assert 23 in too_large["dimensions"]  # lower component: not the top-cell pole

result = {
    "schema": "marici.flavor.wp1055.v1",
    "status": "PASS",
    "question": "Can a parent representation derive WP1054's spin-11 pole cell rather than postulate j=11?",
    "principal_sl2_law": "su(n) adjoint = direct sum of principal-sl2 spins 1,2,...,n-1 with dimensions 3,5,...,2n-1",
    "selected_parent": parent,
    "conditional_port_arity": {"ports": list(nilpotent_ports), "k": k, "status": "two nilpotent incidence directions; physical port law remains open"},
    "capacity_match": {
        "formula": "h=C*parent_n*pi^2/(1367*k)",
        "h_pi2_coefficient": str(h_pi2_coefficient),
        "normalized_R1_over_R0_with_common_M2_1": str(normalized_response),
    },
    "parent_scan": {
        "range": [2, 30],
        "unique_parent_with_top_C_23": unique_top_parents,
        "too_small_parent": {"n": 11, "top_spin": too_small["top_spin"], "top_C": too_small["top_C"]},
        "too_large_parent": {"n": 13, "top_spin": too_large["top_spin"], "top_C": too_large["top_C"], "contains_C23_as_lower_component": True},
    },
    "classification": "conditional parent/top-cell constructor: SU(12) principal-sl2 adjoint has a unique top spin-11 component of dimension 23 and the two nilpotent incidence directions give k=2; the parent/top-cell law itself remains underived",
    "remaining_gate": "derive the SU(12) parent, the top principal-sl2 projection, and the physical meaning of the E/F two-port arity from the actual anomaly-complete source; then derive the common mass scale",
    "claim_boundary": "exact branching arithmetic and bounded parent scan; does not prove that WP1036's factor 12 is SU(12), that the pole operator is the top component, or that the nilpotent directions are physical detector ports",
    "disposition": "productive: WP1054's unexplained spin 11 now has a minimal parent-representation ancestry and a lower-component hostile",
}

(ROOT / "results" / "wp1055_principal_su12_top_cell.json").write_text(json.dumps(result, indent=2) + "\n")
print("WP1055 PASS:", parent["parent_n"], parent["top_spin"], parent["top_C"], k, h_pi2_coefficient)
