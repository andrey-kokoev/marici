from __future__ import annotations

import json
from pathlib import Path


MANIFEST = Path("research/voevodsky/coherence-pyramid-integrated-representation.json")
RESULTS = [
    Path("research/voevodsky/results/coherence_pyramid_computad_signature.json"),
    Path("research/voevodsky/results/coherence_pyramid_completion_interface.json"),
    Path("research/voevodsky/results/coherence_pyramid_partial_composition.json"),
    Path("research/voevodsky/results/coherence_pyramid_cells_and_laws.json"),
    Path("research/voevodsky/results/coherence_pyramid_countermodel_suite.json"),
]


def main() -> None:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    modules = {
        name: json.loads(Path(path).read_text(encoding="utf-8"))
        for name, path in manifest["modules"].items()
    }
    results = [json.loads(path.read_text(encoding="utf-8")) for path in RESULTS]
    assert all(result["passed"] is True for result in results)

    signature = modules["signature"]
    composition = modules["composition"]
    coherence = modules["coherence"]
    countermodels = modules["countermodels"]

    assert set(manifest["representation"]["objects"]) == set(signature["object_sorts"])
    assert set(manifest["representation"]["arrow_variances"]) == {
        generator["variance"] for generator in signature["one_generators"].values()
    }
    assert set(manifest["representation"]["partial_reindexing"]) == set(composition["reindexing_constructors"])
    assert set(manifest["representation"]["cell_classes"]) == set(coherence["cells"])
    assert set(manifest["representation"]["law_classes"]) == set(coherence["coherence_obligations"])
    assert len(countermodels["countermodels"]) == 10

    strength = manifest["strength"]
    assert strength["typed_computad"] is True
    assert strength["partial_composition_presentation"] is True
    assert strength["coherence_obligation_presentation"] is True
    assert strength["selected_countermodel_coverage"] is True
    assert strength["partial_double_category_proved"] is False
    assert strength["equipment_proved"] is False
    assert strength["completion_pseudofunctor_proved"] is False

    result = {
        "schema": "marici.voevodsky.coherence-pyramid-integrated-representation-check.v1",
        "status": "candidate_partial_equipment_presentation_integrated",
        "module_count": len(modules),
        "component_result_count": len(results),
        "object_sort_count": len(manifest["representation"]["objects"]),
        "variance_count": len(manifest["representation"]["arrow_variances"]),
        "reindexing_constructor_count": len(manifest["representation"]["partial_reindexing"]),
        "cell_class_count": len(manifest["representation"]["cell_classes"]),
        "law_class_count": len(manifest["representation"]["law_classes"]),
        "countermodel_count": len(countermodels["countermodels"]),
        "full_generator_and_obligation_representation": True,
        "full_categorical_realization": False,
        "first_missing_theorem": manifest["first_missing_theorem"],
        "next_branch": manifest["next_programme_branch"],
        "passed": True,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
