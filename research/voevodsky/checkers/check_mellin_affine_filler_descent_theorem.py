from __future__ import annotations

import json
from pathlib import Path


ROOT = Path("research/voevodsky/results")
FILES = {
    "ordinary": ROOT / "ordinary_mellin_affine_chain_object.json",
    "stokes": ROOT / "mellin_stokes_homology_interchange.json",
    "chains": ROOT / "adelic_cutoff_labelled_chain_functor.json",
    "finite": ROOT / "finite_adelic_mellin_evaluation_naturality.json",
    "completion": ROOT / "reciprocal_orbit_weighted_completion.json",
}
CONTRACT = Path("research/voevodsky/mellin-affine-filler-descent-theorem-v1.json")


def main() -> None:
    theorem = json.loads(CONTRACT.read_text(encoding="utf-8"))
    evidence = {name: json.loads(path.read_text(encoding="utf-8")) for name, path in FILES.items()}
    assert all(item["passed"] for item in evidence.values())

    ordinary = evidence["ordinary"]
    assert ordinary["admitted_affine_triangles"] == 12
    assert ordinary["ordinary_domain_blocker_removed"] is True
    assert ordinary["h1_dimension"] == 0

    stokes = evidence["stokes"]
    assert stokes["homology_level_interchange_verified"] is True
    assert stokes["chain_level_interchange_verified"] is False

    chains = evidence["chains"]
    assert chains["transition_identity_and_composition"] is True
    assert chains["boundary_naturality"] is True
    assert chains["uniform_completion_verified"] is False

    finite = evidence["finite"]
    assert finite["cutoff_transition_naturality"] is True
    assert finite["reciprocal_naturality"] is True

    completion = evidence["completion"]
    assert completion["uniform_tail_dominated_by_source_tail"] is True
    assert completion["boundary_null_preserved_under_limit"] is True
    assert completion["global_spectral_completion_verified"] is False
    assert completion["unconditional_source_decay"] is False

    result = {
        "schema":"marici.voevodsky.mellin-affine-filler-descent-theorem-check.v1",
        "status":"conditional_descent_theorem_verified",
        "dependency_checks_passed":len(evidence),
        "ordinary_affine_filler_complete":True,
        "stokes_relative_class_descent":True,
        "stokes_selected_chain_descent":False,
        "finite_cutoff_descent":True,
        "weighted_orbitwise_completed_descent":True,
        "boundary_null_preserved":True,
        "global_unconditional_descent":False,
        "disposition":theorem["disposition"],
        "passed":True
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
