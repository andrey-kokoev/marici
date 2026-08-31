import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# SU(4) cubic anomaly coefficients for the WP1056 branches.  Normalize
# A(4)=1, A(bar4)=-1.  For SU(4), A(6)=0, and for (4,2) the coefficient is
# dim(2) A(4)=2.  SU(2) has no perturbative cubic anomaly.
branches = [
    {"id": "15_to_6", "dim": 6, "A_SU4": 0, "port": None},
    {"id": "15_to_8", "dim": 8, "A_SU4": 2, "port": None},
    {"id": "15_to_1", "dim": 1, "A_SU4": 0, "port": None},
    {"id": "bar6a_to_4", "dim": 4, "A_SU4": -1, "port": None},
    {"id": "bar6a_to_2", "dim": 2, "A_SU4": 0, "port": "p1"},
    {"id": "bar6b_to_4", "dim": 4, "A_SU4": -1, "port": None},
    {"id": "bar6b_to_2", "dim": 2, "A_SU4": 0, "port": "p2"},
]
assert sum(b["A_SU4"] for b in branches) == 0
by_id = {b["id"]: b for b in branches}


def inflow(boundary_ids, endpoint=0):
    boundary = [by_id[i] for i in boundary_ids]
    bulk = [b for b in branches if b["id"] not in set(boundary_ids)]
    b_anomaly = sum(b["A_SU4"] for b in boundary)
    B = sum(b["A_SU4"] for b in bulk)
    assert b_anomaly + B == 0
    b0, bpi = (b_anomaly, 0) if endpoint == 0 else (0, b_anomaly)
    k = Fraction(-b0) - Fraction(B, 2)
    A0 = b0 + Fraction(B, 2) + k
    Api = bpi + Fraction(B, 2) - k
    assert A0 == 0 and Api == 0
    return {
        "boundary": list(boundary_ids),
        "endpoint": endpoint,
        "boundary_A_SU4": b_anomaly,
        "bulk_A_SU4": B,
        "k_SU4_CS": k,
        "retained_ports": [b["port"] for b in bulk if b["port"]],
    }

quartet = inflow(["bar6a_to_4"])
quartet_reflected = inflow(["bar6a_to_4"], endpoint=1)
doublet_pair = inflow(["bar6a_to_2", "bar6b_to_2"])
bifundamental8 = inflow(["15_to_8"])

assert quartet["k_SU4_CS"] == Fraction(1, 2)
assert quartet_reflected["k_SU4_CS"] == Fraction(-1, 2)
assert doublet_pair["k_SU4_CS"] == 0
assert bifundamental8["k_SU4_CS"] == -1
assert len(quartet["retained_ports"]) == 2
assert len(doublet_pair["retained_ports"]) == 0

integral_lattice_admits_quartet = quartet["k_SU4_CS"].denominator == 1
integral_lattice_admits_doublet_pair = doublet_pair["k_SU4_CS"].denominator == 1
half_integral_lattice_admits_quartet = quartet["k_SU4_CS"].denominator in (1, 2)
assert not integral_lattice_admits_quartet
assert integral_lattice_admits_doublet_pair
assert half_integral_lattice_admits_quartet

result = {
    "schema": "marici.flavor.wp1066.v1",
    "status": "PASS",
    "question": "Does the non-Abelian SU(4) cubic anomaly constrain WP1056's one-quartet localization?",
    "anomaly_normalization": "A(4)=1, A(bar4)=-1, A_SU4(6)=0, A_SU4(4,2)=2; total 15+2bar6 anomaly is zero",
    "selected_quartet": {k: (str(v) if isinstance(v, Fraction) else v) for k, v in quartet.items()},
    "reflected_quartet": {k: (str(v) if isinstance(v, Fraction) else v) for k, v in quartet_reflected.items()},
    "c23_port_destroying_hostile": {k: (str(v) if isinstance(v, Fraction) else v) for k, v in doublet_pair.items()},
    "adjacent_bifundamental8": {k: (str(v) if isinstance(v, Fraction) else v) for k, v in bifundamental8.items()},
    "lattice_gate": {
        "integral_SU4_CS_admits_quartet": integral_lattice_admits_quartet,
        "integral_SU4_CS_admits_doublet_pair": integral_lattice_admits_doublet_pair,
        "half_integral_SU4_CS_admits_quartet": half_integral_lattice_admits_quartet,
    },
    "classification": "non-Abelian inflow gate: the one-quartet (C,k)=(23,2) cell requires half-integral SU(4) Chern-Simons level 1/2, while the port-destroying C=23 doublet-pair cell is integral-level compatible",
    "remaining_gate": "derive a shifted/half-integral SU(4) Chern-Simons class and endpoint orientation from the UV compactification, and compute the complete mixed/gravitational anomaly lattice",
    "claim_boundary": "computes the SU(4) cubic channel only; WP1057's linear U(1) result remains separate and does not remove this constraint",
    "disposition": "productive: the localization blocker is sharpened from an unfixed integer cofiber to a concrete shifted-quantization requirement",
}

(ROOT / "results" / "wp1066_localized_quartet_nonabelian_inflow_gate.json").write_text(json.dumps(result, indent=2) + "\n")
print("WP1066 PASS:", quartet["k_SU4_CS"], doublet_pair["k_SU4_CS"], bifundamental8["k_SU4_CS"])
