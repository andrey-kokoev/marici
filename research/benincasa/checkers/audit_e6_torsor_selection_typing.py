#!/usr/bin/env python3
"""Audit whether existing source maps select the global e6 torsor residue."""

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
BEN = ROOT / "research" / "benincasa"
OUT = BEN / "results" / "e6_torsor_selection_typing.json"


def main() -> None:
    gluing = json.loads((BEN / "enhanced-conductor-unimodular-gluing.json").read_text(encoding="utf-8"))
    top = json.loads((BEN / "total-energy-conductor-specialization.json").read_text(encoding="utf-8"))
    torsor = json.loads((BEN / "results" / "e6_global_logarithmic_torsor.json").read_text(encoding="utf-8"))

    assert gluing["primitive_conductor_basis"] == ["g101", "g110", "g111_tilde"]
    assert gluing["point_order"] == ["++", "+-", "-+", "--"]
    assert gluing["pairing"]["normalized_incidence_matrix"] == "K"
    assert top["source"]["generic_cycle_basis"] == ["g101", "g110", "g111_top"]
    assert top["specialization_graph"]["primitive_kernel"] == "Z*g111_top"
    assert torsor["residues_normalized_by_C2"] == {"v=0": "1", "v=2": "-1"}

    packet = {
        "schema": "marici.benincasa.e6_torsor_selection_typing.v1",
        "status": "pass",
        "candidate_base_soft_lattice": {
            "basis": ["s3={v=0}={X3=0}", "s2={v=2}={X2=0}"],
            "primitive_divisor_vector": [1, -1],
            "rational_function": "X3/X2=-v/(v-2)",
        },
        "existing_fiber_endpoint_lattice": {
            "basis": ["p_minus={r=-1}", "p_plus={r=1}"],
            "primitive_boundary_vector": [-1, 1],
            "provenance": "Entry 304 oriented Leray interval",
        },
        "existing_conductor_map": {
            "domain": ["g101", "g110", "g111_tilde"],
            "target": ["delta", "epsilon", "epsilon*delta"],
            "matrix": gluing["J"],
            "base_soft_target_present": False,
        },
        "infinity_gysin_on_e6": "zero",
        "hom_diagonal_connection": "zero; fixes no extension residue",
        "typed_map_fiber_endpoints_to_base_soft_divisors": False,
        "conclusion": "the equal primitive vectors are an untyped rank match; existing maps do not yet select the candidate e6 torsor",
        "required_constructor": "source-derived specialization/relative-chain map from the oriented exceptional endpoint interval to the ordered base-soft divisor pair",
        "new_carrier_datum": False,
    }
    OUT.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(packet, indent=2))


if __name__ == "__main__":
    main()
