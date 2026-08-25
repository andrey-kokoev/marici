import json
from pathlib import Path


def first_separating_stage(left, right, stages):
    for index, probes in enumerate(stages):
        if any(probe(left) != probe(right) for probe in probes):
            return index
    return None


def separation_profile(left, right, named_probes):
    return sorted(name for name, probe in named_probes.items() if probe(left) != probe(right))


def pareto_minimal(values):
    return sorted(v for v in values if not any(
        w != v and w[0] <= v[0] and w[1] <= v[1] for w in values
    ))


def main():
    a, b = 0, 1
    u = lambda x: x
    same_probe_family_short = [[], [u]]
    same_probe_family_delayed = [[], [], [u]]

    named = {
        "direct": u,
        "duplicate": lambda x: x,
        "constant": lambda _: 0,
    }
    profile = separation_profile(a, b, named)

    # Two incomparable source resources: depth/support = (1,3) and (2,1).
    # Neither is the unique first rung.
    costs = [(1, 3), (2, 1), (3, 4)]
    frontier = pareto_minimal(costs)

    gates = {
        "literal_rung_changes_under_empty_stage_insertion": (
            first_separating_stage(a, b, same_probe_family_short) == 1
            and first_separating_stage(a, b, same_probe_family_delayed) == 2
        ),
        "separation_profile_ignores_stage_index": profile == ["direct", "duplicate"],
        "duplicate_probe_does_not_change_operativity": bool(profile),
        "resource_depth_can_be_pareto_not_scalar": frontier == [(1, 3), (2, 1)],
    }
    assert all(gates.values()), gates

    result = {
        "schema": "marici.future-rung-reindexing-falsifier.v1",
        "gates": gates,
        "literal_rungs": {"short": 1, "delayed": 2},
        "same_total_probe_family": True,
        "separating_profile": profile,
        "minimal_resource_frontier": frontier,
        "conclusion": "probe profile is intrinsic; rung requires a source-canonical resource grading",
    }
    out = Path(__file__).parents[1] / "results" / "future-rung-reindexing-falsifier.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
