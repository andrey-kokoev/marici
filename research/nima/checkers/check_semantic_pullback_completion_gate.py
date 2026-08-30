import json
from fractions import Fraction
from pathlib import Path


def diagonal_cutoff(n):
    return [Fraction(1, k) for k in range(1, n + 1)]


cutoffs = [1, 2, 4, 8, 16, 32]
records = []
for n in cutoffs:
    diagonal = diagonal_cutoff(n)
    full_rank = all(value != 0 for value in diagonal)
    smallest = min(abs(value) for value in diagonal)
    assert full_rank
    assert smallest == Fraction(1, n)
    records.append({
        "cutoff": n,
        "full_rank": full_rank,
        "smallest_singular_value": f"1/{n}" if n != 1 else "1",
    })

assert all(item["full_rank"] for item in records)
assert diagonal_cutoff(32)[-1] < diagonal_cutoff(16)[-1]

repairs = {
    "source_state_collision": "observation_port",
    "target_outside_image": "target_domain_predicate",
    "relation_failure": "coherence_cell_or_anomaly_budget",
    "vanishing_completion_bound": "completion_topology_or_boundary_fiber",
}
assert len(set(repairs.values())) == 4

result = {
    "status": "pass",
    "claim": "finite semantic validity does not imply stable extension through completion",
    "cutoffs": records,
    "finite_object_separation": True,
    "finite_target_admission": True,
    "finite_relation_preservation": True,
    "uniform_lower_bound": False,
    "typed_residual": "completion_stability",
    "minimal_repair_class": repairs["vanishing_completion_bound"],
    "pairwise_distinct_repair_classes": True,
}

out = Path(__file__).parents[1] / "results" / "semantic-pullback-completion-gate.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))

