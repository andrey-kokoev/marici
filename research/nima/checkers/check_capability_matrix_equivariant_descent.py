#!/usr/bin/env python3
"""Audit the sheaf-like interpretation against exact cosmology chart data."""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
R = ROOT / "research" / "nima" / "results"
B = ROOT / "research" / "benincasa"
OUT = R / "capability_matrix_equivariant_descent.json"


def load(name):
    return json.loads((R / name).read_text())


def main():
    g31 = load("rank26_physical_jet_seven_plane_chart_transport_p32003.json")
    g23 = load("rank26_physical_jet_seven_plane_G12_to_G23_transport_p32003.json")
    cyc = load("rank26_cyclic_chart_order_three_closure_p32003.json")
    overlap = json.loads((B / "cross-sector-overlap-certificate.json").read_text())

    assert g31["passed"] and g31["planes_equal"]
    assert g23["passed"] and g23["planes_equal"]
    assert cyc["passed"] and cyc["order_three_identity_defect"] == 0
    assert not overlap["source_double_pole_G12_G23"]

    result = {
        "schema": "marici.capability-matrix-equivariant-descent.v1",
        "local_ambient_rank": 26,
        "local_annihilator_rank": 7,
        "g12_g31_annihilators_intertwined": True,
        "g12_g23_annihilators_intertwined": True,
        "cyclic_transition_product_identity": True,
        "source_open_overlap_exists": False,
        "ordinary_cech_sheaf_claim": False,
        "equivariant_groupoid_bundle_claim": True,
        "operational_capability_sheaf_claim": False,
        "verdict": "The coefficient matrices are local presentations of an equivariant descent object on the cyclic chart groupoid, not yet an ordinary sheaf of operational capabilities across sectors.",
    }
    OUT.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
