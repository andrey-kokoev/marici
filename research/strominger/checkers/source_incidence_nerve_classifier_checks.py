"""Deterministic classifier for the current source-incidence fixtures."""
import json
from pathlib import Path


fixtures = [
    {
        "id": "magnetic_chart_comparison",
        "signature": "parallel_source_target",
        "dimension": 1,
        "expected_nerve": "globular",
        "expected_faces": 2,
    },
    {
        "id": "magnetic_reflection_bar",
        "signature": "ordered_chain_with_omissions",
        "dimension": 3,
        "expected_nerve": "simplicial",
        "expected_faces": 4,
    },
    {
        "id": "rh_source_composition_reciprocity",
        "signature": "independent_binary_axes",
        "dimension": 3,
        "expected_nerve": "cubical",
        "expected_faces": 6,
    },
    {
        "id": "cutoff_completion_descent",
        "signature": "ordered_chain_with_omissions",
        "dimension": 3,
        "expected_nerve": "simplicial",
        "expected_faces": 4,
    },
]


def classify(signature, dimension):
    if signature == "parallel_source_target":
        return "globular", 2
    if signature == "ordered_chain_with_omissions":
        return "simplicial", dimension + 1
    if signature == "independent_binary_axes":
        return "cubical", 2 * dimension
    raise ValueError(signature)


classified = []
for fixture in fixtures:
    nerve, faces = classify(fixture["signature"], fixture["dimension"])
    classified.append({**fixture, "actual_nerve": nerve, "actual_faces": faces})

tests = {
    "all_fixtures_classified": all(
        row["actual_nerve"] == row["expected_nerve"]
        and row["actual_faces"] == row["expected_faces"]
        for row in classified
    ),
    "same_dimension_can_have_different_horns": len(
        {
            (row["actual_nerve"], row["actual_faces"])
            for row in classified
            if row["dimension"] == 3
        }
    )
    > 1,
    "rh_cube_retains_six_faces": next(
        row for row in classified if row["id"] == "rh_source_composition_reciprocity"
    )["actual_faces"]
    == 6,
    "reflection_and_completion_are_simplicial": all(
        row["actual_nerve"] == "simplicial"
        for row in classified
        if row["id"] in {"magnetic_reflection_bar", "cutoff_completion_descent"}
    ),
}

result = {
    "schema": "marici.checker_results.v1",
    "checker": "source_incidence_nerve_classifier_checks.py",
    "passed": all(tests.values()),
    "tests": tests,
    "fixtures": classified,
    "verdict": "source incidence, not tower count, selects the next coherence nerve",
}

out = Path(__file__).resolve().parents[1] / "results" / "source_incidence_nerve_classifier_checks.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)
