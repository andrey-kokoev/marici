import itertools
import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# SU(6) -> SU(4)xSU(2)xU(1) branch data.  The U(1) charges are fixed by
# tracelessness: 6=(4,1)_1+(1,2)_-2 and 15=(6,1)_2+(4,2)_-1+(1,1)_-4.
branches = [
    {"id": "15_to_6", "dim": 6, "q": Fraction(2), "port": None},
    {"id": "15_to_8", "dim": 8, "q": Fraction(-1), "port": None},
    {"id": "15_to_1", "dim": 1, "q": Fraction(-4), "port": None},
    {"id": "bar6a_to_4", "dim": 4, "q": Fraction(-1), "port": None},
    {"id": "bar6a_to_2", "dim": 2, "q": Fraction(2), "port": "p1"},
    {"id": "bar6b_to_4", "dim": 4, "q": Fraction(-1), "port": None},
    {"id": "bar6b_to_2", "dim": 2, "q": Fraction(2), "port": "p2"},
]
assert sum(b["dim"] for b in branches) == 27
assert sum((b["dim"] * b["q"] for b in branches), Fraction(0)) == 0
by_id = {b["id"]: b for b in branches}


def localization(boundary_ids, endpoint=0):
    boundary = [by_id[i] for i in boundary_ids]
    bulk = [b for b in branches if b["id"] not in set(boundary_ids)]
    B = sum((b["dim"] * b["q"] for b in bulk), Fraction(0))
    b_boundary = sum((b["dim"] * b["q"] for b in boundary), Fraction(0))
    assert B + b_boundary == 0
    b0, bpi = (b_boundary, Fraction(0)) if endpoint == 0 else (Fraction(0), b_boundary)
    k_inflow = -b0 - B / 2
    A0 = b0 + B / 2 + k_inflow
    Api = bpi + B / 2 - k_inflow
    assert A0 == 0 and Api == 0
    ports = [b["port"] for b in bulk if b["port"]]
    C = sum(b["dim"] for b in bulk)
    return {
        "boundary": list(boundary_ids),
        "endpoint": endpoint,
        "bulk_U1_anomaly_B": B,
        "boundary_U1_anomaly": b_boundary,
        "inflow_level": k_inflow,
        "bulk_C": C,
        "retained_ports": ports,
        "k_ports": len(ports),
        "kappa": 2 + 35 - C,
    }


# The three C=23 localization classes from WP1056 have different inflow data.
c23 = [
    localization(["bar6a_to_4"]),
    localization(["bar6b_to_4"]),
    localization(["bar6a_to_2", "bar6b_to_2"]),
]
assert [x["inflow_level"] for x in c23] == [Fraction(2), Fraction(2), Fraction(-4)]
assert [x["k_ports"] for x in c23] == [2, 2, 0]

selected = c23[0]
assert selected["bulk_C"] == 23 and selected["k_ports"] == 2
assert selected["kappa"] == 14
h_pi2_coefficient = Fraction(selected["bulk_C"] * 12, 1367 * selected["k_ports"])
assert h_pi2_coefficient == Fraction(138, 1367)

# Endpoint reflection changes the sign of the required half-integral class.
opposite_endpoint = localization(["bar6a_to_4"], endpoint=1)
assert opposite_endpoint["inflow_level"] == Fraction(-2)

# Integral-CS admission permits both the port-retaining quartet cell and the
# port-destroying doublet-pair cell, but at different levels.  Linear U(1)
# inflow therefore does not select the localization by itself.
integral_lattice_admits = selected["inflow_level"].denominator == 1
doublet_pair_integral_admits = c23[2]["inflow_level"].denominator == 1
assert integral_lattice_admits and doublet_pair_integral_admits

adjacent = {
    "one_doublet_boundary": localization(["bar6a_to_2"]),
    "one_bifundamental8_boundary": localization(["15_to_8"]),
    "one_singlet_boundary": localization(["15_to_1"]),
}
assert adjacent["one_doublet_boundary"]["inflow_level"] == -2
assert adjacent["one_doublet_boundary"]["bulk_C"] == 25
assert adjacent["one_bifundamental8_boundary"]["inflow_level"] == 4
assert adjacent["one_bifundamental8_boundary"]["bulk_C"] == 19
assert adjacent["one_singlet_boundary"]["inflow_level"] == 2
assert adjacent["one_singlet_boundary"]["bulk_C"] == 26

result = {
    "schema": "marici.flavor.wp1057.v1",
    "status": "PASS",
    "question": "What anomaly-inflow class does WP1056's one-quartet localization law require?",
    "branch_charge_law": "SU(6)->SU(4)xSU(2)xU(1), with 6=(4,1)_1+(1,2)_-2 and 15=(6,1)_2+(4,2)_-1+(1,1)_-4",
    "c23_localization_inflow": [
        {k: (str(v) if isinstance(v, Fraction) else v) for k, v in x.items()}
        for x in c23
    ],
    "selected_quartet_cell": {
        **{k: (str(v) if isinstance(v, Fraction) else v) for k, v in selected.items()},
        "h_pi2_coefficient": str(h_pi2_coefficient),
    },
    "opposite_endpoint": {k: (str(v) if isinstance(v, Fraction) else v) for k, v in opposite_endpoint.items()},
    "inflow_lattice_gate": {
        "integral_CS_lattice_admits_quartet": integral_lattice_admits,
        "integral_CS_lattice_admits_doublet_pair": doublet_pair_integral_admits,
        "required_class": "k_inflow=2 for one boundary quartet at endpoint 0; -2 at the reflected endpoint; the port-destroying doublet-pair cell has -4",
    },
    "adjacent_localizations": {
        name: {k: (str(v) if isinstance(v, Fraction) else v) for k, v in value.items()}
        for name, value in adjacent.items()
    },
    "classification": "conditional anomaly-inflow cofiber: the one-quartet (C,k)=(23,2) cell has integral level 2, while the port-destroying C=23 doublet-boundary cell has level -4; linear U(1) inflow distinguishes but does not select between them without a fixed CS class",
    "remaining_gate": "derive the complete Chern-Simons level vector and endpoint orientation from the UV compactification; then derive the common pole clock and mass scale",
    "claim_boundary": "exact U(1) linear-anomaly inflow for the SU(6) branch packet; non-Abelian, mixed, and gravitational anomaly lattices are not computed here",
    "disposition": "productive: the missing localization law is sharpened to a concrete fixed-inflow requirement with exact quartet-versus-doublet-pair levels",
}

(ROOT / "results" / "wp1057_localized_quartet_inflow_gate.json").write_text(json.dumps(result, indent=2) + "\n")
print("WP1057 PASS:", selected["inflow_level"], selected["bulk_C"], selected["k_ports"], h_pi2_coefficient)
