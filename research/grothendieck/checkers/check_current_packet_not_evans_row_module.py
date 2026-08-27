from collections import deque


def reachable(edges, source, target):
    graph = {}
    for left, right in edges:
        graph.setdefault(left, set()).add(right)
    queue = deque([source])
    seen = {source}
    while queue:
        node = queue.popleft()
        if node == target:
            return True
        for neighbor in graph.get(node, ()):
            if neighbor not in seen:
                seen.add(neighbor)
                queue.append(neighbor)
    return False


def main():
    executable = {
        ("labels", "forcing"),
        ("forcing", "tail"),
        ("tail", "endpoint_scalar"),
        ("labels", "primitive_boundary"),
        ("labels", "square_boundary"),
        ("source_cut", "seam_state"),
        ("test_boundary", "archimedean_jets"),
        ("doubled_domain", "green_current"),
    }
    correspondences = {
        ("direct_sector", "dual_sector"),
        ("dual_sector", "direct_sector"),
    }

    observation_targets = {
        "endpoint_scalar",
        "primitive_boundary",
        "square_boundary",
        "seam_state",
        "archimedean_jets",
        "green_current",
    }

    checks = {
        "tail_reaches_endpoint": reachable(executable, "tail", "endpoint_scalar"),
        "labels_reach_primitive": reachable(executable, "labels", "primitive_boundary"),
        "labels_reach_square": reachable(executable, "labels", "square_boundary"),
        "no_observation_reaches_sum_carrier": all(
            not reachable(executable, target, "sum_carrier")
            for target in observation_targets
        ),
        "no_common_declared_domain_reaches_all_rows": not any(
            all(reachable(executable, source, target) for target in observation_targets)
            for source in {left for left, _ in executable}
        ),
        "comparison_not_executable": all(edge not in executable for edge in correspondences),
    }

    illegally_promoted = executable | correspondences | {
        ("endpoint_scalar", "sum_carrier")
    }
    checks["illegal_recovery_would_hide_obstruction"] = reachable(
        illegally_promoted, "tail", "sum_carrier"
    )

    for name, passed in checks.items():
        print(f"{name}: {'PASS' if passed else 'FAIL'}")
    print(f"summary: {sum(checks.values())}/{len(checks)} checks passed")
    raise SystemExit(0 if all(checks.values()) else 1)


if __name__ == "__main__":
    main()
