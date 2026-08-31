import itertools
import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# Minimal anomaly-free SU(6) chiral family from WP775: 15 + 2*bar6.
assert 2 + 2 * (-1) == 0  # A(15)+2 A(bar6)=0

branches = [
    {"id": "15_to_6", "parent": "15", "dim": 6, "port": None},
    {"id": "15_to_8", "parent": "15", "dim": 8, "port": None},
    {"id": "15_to_1", "parent": "15", "dim": 1, "port": None},
    {"id": "bar6a_to_4", "parent": "bar6a", "dim": 4, "port": None},
    {"id": "bar6a_to_2", "parent": "bar6a", "dim": 2, "port": "p1"},
    {"id": "bar6b_to_4", "parent": "bar6b", "dim": 4, "port": None},
    {"id": "bar6b_to_2", "parent": "bar6b", "dim": 2, "port": "p2"},
]
full_degree = sum(b["dim"] for b in branches)
assert full_degree == 27
assert [b["dim"] for b in branches] == [6, 8, 1, 4, 2, 4, 2]

# Enumerate exact localization subsets that leave C=23 in the bulk.  C alone
# is not enough: removing both doublets also leaves 23 but destroys k=2.
c23_options = []
for mask in range(1 << len(branches)):
    boundary = [b for i, b in enumerate(branches) if mask & (1 << i)]
    removed = sum(b["dim"] for b in boundary)
    if full_degree - removed != 23:
        continue
    retained_ports = [b["port"] for b in branches if b["port"] and b not in boundary]
    c23_options.append({
        "boundary": [b["id"] for b in boundary],
        "bulk_C": full_degree - removed,
        "retained_ports": retained_ports,
        "k": len(retained_ports),
    })

assert len(c23_options) == 3
port_retaining = [o for o in c23_options if o["k"] == 2]
port_destroying = [o for o in c23_options if o["k"] != 2]
assert [o["boundary"] for o in port_retaining] == [["bar6a_to_4"], ["bar6b_to_4"]]
assert [o["boundary"] for o in port_destroying] == [["bar6a_to_2", "bar6b_to_2"]]

candidate = port_retaining[0]
C = candidate["bulk_C"]
k = candidate["k"]
assert (C, k) == (23, 2)

# The same localized cell preserves a positive SU(6) spectral index and hits
# the WP1036 capacity point.
N_V = 35
kappa = 2 + N_V - C
assert kappa == 14
h_pi2_coefficient = Fraction(C * 12, 1367 * k)
assert h_pi2_coefficient == Fraction(138, 1367)

# Exact adjacent localization classes.
def localized(dimensions_removed):
    bulk = full_degree - sum(dimensions_removed)
    return {
        "bulk_C": bulk,
        "kappa": 2 + N_V - bulk,
        "h_pi2_coefficient": str(Fraction(bulk * 12, 1367 * 2)),
    }

adjacent = {
    "full_family_bulk": localized([]),
    "one_2_boundary": localized([2]),
    "one_4_boundary": localized([4]),
    "both_4s_boundary": localized([4, 4]),
}
assert adjacent["full_family_bulk"]["bulk_C"] == 27
assert adjacent["one_2_boundary"]["bulk_C"] == 25
assert adjacent["one_4_boundary"]["bulk_C"] == 23
assert adjacent["both_4s_boundary"]["bulk_C"] == 19

result = {
    "schema": "marici.flavor.wp1056.v1",
    "status": "PASS",
    "question": "Can the existing minimal anomaly-free SU(6) family derive C=23 and k=2 from one representation localization cell?",
    "family": {
        "representation": "15+2*bar6",
        "anomaly": "A(15)+2A(bar6)=2+2(-1)=0",
        "subgroup_branches": branches,
        "full_degree": full_degree,
    },
    "c23_localization_options": c23_options,
    "selected_cell": {
        "law": "exactly one SU(4)-quartet branch is boundary; every other branch is bulk",
        "bulk_C": C,
        "retained_doublet_ports": candidate["retained_ports"],
        "k": k,
        "spectral_index_kappa": kappa,
        "h_pi2_coefficient": str(h_pi2_coefficient),
    },
    "joint_selection": {
        "C23_alone_insufficient": True,
        "port_destroying_C23_option": port_destroying,
        "port_retaining_C23_options": port_retaining,
    },
    "adjacent_localization_classes": adjacent,
    "classification": "conditional anomaly-localization constructor: the SU(6) family branches to degree 27; one boundary quartet leaves C=23 bulk atoms and the two bar6 doublets as k=2 ports with kappa=14",
    "remaining_gate": "derive the one-quartet boundary localization law and resolve the symmetric choice between the two quartets; then derive the common pole clock, mass scale, and the WP802 12*pi^2/1367 interface from the same source",
    "claim_boundary": "exact representation branching and finite localization enumeration; does not prove the boundary law, chiral Standard Model embedding, or physical16 instrument",
    "disposition": "productive: the representation direction now has an anomaly-complete SU(6) candidate that derives C=23 and k=2 jointly, superseding the ungrounded SU(12) numeral identification",
}

(ROOT / "results" / "wp1056_su6_localized_quartet_pole_cell.json").write_text(json.dumps(result, indent=2) + "\n")
print("WP1056 PASS:", C, k, kappa, h_pi2_coefficient, len(c23_options))
