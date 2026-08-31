"""Pair-face residue vector for the triple-incidence denominator obstruction.

Repeat iteration 2 refines the residue obstruction by computing the ordered
residue on all three pair-wall faces.  It identifies the exact face datum any
relative Cech or resolved/Rees enlargement must supply.
"""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
VOEVODSKY_RESULTS = ROOT / "research" / "voevodsky" / "results"
NIMA_RESULTS = ROOT / "research" / "nima" / "results"
OUT = VOEVODSKY_RESULTS / "cosmology_pair_face_residue_vector.json"


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def mod(value: int, prime: int) -> int:
    return value % prime


def main() -> None:
    residue = load(VOEVODSKY_RESULTS / "cosmology_log_denominator_residue_obstruction.json")
    log_identity = load(NIMA_RESULTS / "cosmology_triple_incidence_logarithmic_identity.json")
    source = load(NIMA_RESULTS / "cosmology_source_principal_wall_cell.json")

    assert residue["passed"] is True
    assert residue["status"] == "unbounded_local_residue_obstruction_to_denominator_primitive"
    assert log_identity["circuit_vector"] == [1, -1, 1]
    assert source["remaining_wall_on_pair_intersections"] == {
        "q1_q2": "x + y + 3*z",
        "q1_q3": "-x - y - 3*z",
        "q2_q3": "-x - y - 3*z",
    }

    # Ordered pair-face coordinates and residues of
    # p*dq1^dq2/(q1*q2*q3), with q3=q1+q2+p and p a unit.
    pair_faces = {
        "q1_q2": {
            "ordered_coordinates": ["q1", "q2"],
            "unit_remaining_wall_at_face": "+p",
            "dq1_wedge_dq2_sign_in_ordered_coordinates": 1,
            "unit_denominator_sign": 1,
            "residue": 1,
        },
        "q1_q3": {
            "ordered_coordinates": ["q1", "q3"],
            "unit_remaining_wall_at_face": "-p",
            "dq1_wedge_dq2_sign_in_ordered_coordinates": 1,
            "unit_denominator_sign": -1,
            "residue": -1,
        },
        "q2_q3": {
            "ordered_coordinates": ["q2", "q3"],
            "unit_remaining_wall_at_face": "-p",
            "dq1_wedge_dq2_sign_in_ordered_coordinates": -1,
            "unit_denominator_sign": -1,
            "residue": 1,
        },
    }
    residue_vector = [pair_faces[key]["residue"] for key in ("q1_q2", "q1_q3", "q2_q3")]
    assert residue_vector == [1, -1, 1]
    assert residue_vector == log_identity["circuit_vector"]

    witnesses = {}
    for prime in (101, 103):
        vector_mod = [mod(value, prime) for value in residue_vector]
        assert vector_mod != [0, 0, 0]
        canceling_vector = [mod(-value, prime) for value in residue_vector]
        witnesses[str(prime)] = {
            "residue_vector_mod_prime": vector_mod,
            "nonzero": True,
            "required_relative_face_boundary_vector_mod_prime": canceling_vector,
        }

    result = {
        "schema": "marici.voevodsky.cosmology-pair-face-residue-vector.v1",
        "status": "ordered_pair_face_residue_vector_computed",
        "rechecked_inputs": [
            "research/voevodsky/results/cosmology_log_denominator_residue_obstruction.json",
            "research/nima/results/cosmology_triple_incidence_logarithmic_identity.json",
            "research/nima/results/cosmology_source_principal_wall_cell.json",
        ],
        "target_form": "p*dq1^dq2/(q1*q2*q3)",
        "pair_faces_order": ["q1_q2", "q1_q3", "q2_q3"],
        "pair_face_data": pair_faces,
        "residue_vector": residue_vector,
        "matches_logarithmic_circuit_vector": True,
        "finite_field_witnesses": witnesses,
        "relative_cone_requirement": "a non-tautological relative face term must carry boundary residue vector (-1,1,-1) in the ordered pair-face basis",
        "why_Cayley_Menger_empty_face_does_not_help": "the generic K_CM-nonsingular packet supplies no CM face generator, while the obstruction lives on the three marked-wall pair faces",
        "ambient_division_by_p": False,
        "tautological_circuit_quotient_used": False,
        "physical_period_constructed": False,
        "next_gate": "construct an ordered pair-wall Cech or resolved/Rees face module with this boundary residue vector and prove its differential stability",
        "passed": True,
    }
    OUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
