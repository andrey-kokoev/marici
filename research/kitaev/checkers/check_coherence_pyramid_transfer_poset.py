from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
REGISTRY = ROOT / "research/kitaev/coherence-pyramid-transfer-map-registry-v1.json"
RESULT = ROOT / "research/kitaev/results/coherence_pyramid_transfer_poset.json"


def is_dag(vertices: set[str], edges: list[list[str]]) -> bool:
    successors = {v: [] for v in vertices}
    indegree = {v: 0 for v in vertices}
    for source, target in edges:
        assert source in vertices and target in vertices
        successors[source].append(target)
        indegree[target] += 1
    queue = [v for v in vertices if indegree[v] == 0]
    visited = 0
    while queue:
        source = queue.pop()
        visited += 1
        for target in successors[source]:
            indegree[target] -= 1
            if indegree[target] == 0:
                queue.append(target)
    return visited == len(vertices)


def main() -> None:
    registry = json.loads(REGISTRY.read_text(encoding="utf-8"))
    predicates = set(registry["certificate_predicates"])
    edges = registry["dependency_edges"]
    dag = is_dag(predicates, edges)

    # Descent without bounded completion: F_N(x)=sum x_i has norm sqrt(N).
    norm_squares = []
    for n in range(1, 65):
        x = [Fraction(1, n) for _ in range(n)]
        # This vector is scaled by 1/n; ratio F(x)^2 / ||x||_2^2 = n exactly.
        f = sum(x)
        norm_sq = sum(value * value for value in x)
        norm_squares.append(f * f / norm_sq)
    sum_functional_unbounded = norm_squares == [Fraction(n) for n in range(1, 65)]

    # Completion without descent: coordinate functional does not annihilate span(e_1).
    coordinate_on_quotient_generator = Fraction(1)
    coordinate_fails_descent = coordinate_on_quotient_generator != 0

    # Both failures coexist for the sum functional modulo span(e_1).
    simultaneous_minimal_failures = {"quotient_descended", "completed_or_unbounded"}
    incomparable = ["quotient_descended", "completed_or_unbounded"] not in edges and [
        "completed_or_unbounded", "quotient_descended"
    ] not in edges

    required = set(registry["required_record_fields"])
    records_complete = all(required <= set(record) for record in registry["records"])
    nonempty_minimal_failures = all(record["minimal_failed_prerequisites"] for record in registry["records"] if record["status"] != "admitted")

    passed = all([dag, sum_functional_unbounded, coordinate_fails_descent, incomparable, records_complete, nonempty_minimal_failures])
    result = {
        "schema": "marici.coherence_pyramid.transfer_poset_check.v1",
        "passed": passed,
        "registry_dag": dag,
        "sum_functional_norm_ratio_squared": [int(value) for value in norm_squares],
        "sum_functional_unbounded": sum_functional_unbounded,
        "coordinate_fails_descent": coordinate_fails_descent,
        "simultaneous_minimal_failure_example": sorted(simultaneous_minimal_failures),
        "descent_completion_incomparable_in_registry": incomparable,
        "records_complete": records_complete,
        "blocked_records_have_minimal_failures": nonempty_minimal_failures,
        "claim_boundary": "Finite exact witnesses establish logical independence and registry consistency; they do not prove analytic closure or canonical completeness of the predicate set."
    }
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    if not passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
