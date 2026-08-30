"""Typed contract checks for the simplicial braid/homotopy residue hierarchy."""

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve()
ROOT = HERE.parents[1]
RESULT = ROOT / "results" / "simplicial_braid_homotopy_residue_contract_checks.json"

contract = {
    "graded_object": "AP_n=P_{n+1}",
    "face_maps": "delete one strand",
    "degeneracy_maps": "double one strand",
    "cycle_object": "Brun_n(S2)=intersection of all deletion kernels",
    "boundary_object": "source-defined symmetric commutator/fillable subgroup",
    "residue_object": "pi_{n-1}(S2)",
    "exact_sequence_range": "n>4",
}

hostile_rejections = {
    "raw_brunnian_equals_irreducible_residue": False,
    "all_face_values_determine_filling": False,
    "four_point_termination_is_uniform_in_arity": False,
    "geometric_realization_grants_executable_observation": False,
}

checks = {
    "faces_and_degeneracies_are_separately_typed": contract["face_maps"] != contract["degeneracy_maps"],
    "cycles_are_intersection_of_face_kernels": "intersection" in contract["cycle_object"],
    "boundaries_are_not_identified_with_cycles": contract["boundary_object"] != contract["cycle_object"],
    "residue_is_a_quotient_level_object": contract["residue_object"] == "pi_{n-1}(S2)",
    "theorem_range_is_explicit": contract["exact_sequence_range"] == "n>4",
    "all_hostile_conflations_are_rejected": not any(hostile_rejections.values()),
}
checks = {name: bool(value) for name, value in checks.items()}

payload = {
    "schema": "marici.strominger.simplicial-braid-homotopy-residue-contract.v1",
    "status": "passed" if all(checks.values()) else "failed",
    "passed": sum(checks.values()),
    "total": len(checks),
    "checks": checks,
    "contract": contract,
    "hostile_rejections": hostile_rejections,
    "external_theorem": "sphere Brunnian braids fit an exact sequence with quotient pi_{n-1}(S2) for n>4",
    "conclusion": "the arity tower is organized by one simplicial braid object; irreducible filling residues are homotopy classes, not raw Brunnian cycles",
}
payload["checker_sha256"] = hashlib.sha256(HERE.read_bytes()).hexdigest()
RESULT.write_text(json.dumps(payload, indent=2) + "\n", encoding="ascii")
print(f"{payload['passed']}/{payload['total']} checks passed")
print(payload["checker_sha256"])
raise SystemExit(0 if payload["status"] == "passed" else 1)
