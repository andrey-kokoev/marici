#!/usr/bin/env python3
"""Typed reachability audit for the theta/Tate repair compiler."""

from collections import defaultdict, deque


def reachable(edges, source, target):
    graph = defaultdict(list)
    for left, right, _name in edges:
        graph[left].append(right)
    queue = deque([source])
    seen = {source}
    while queue:
        node = queue.popleft()
        if node == target:
            return True
        for neighbor in graph[node]:
            if neighbor not in seen:
                seen.add(neighbor)
                queue.append(neighbor)
    return False


def main():
    executable = [
        ("labels", "F_plus", "label_forcing"),
        ("F_plus", "Y_plus", "tail_actuation"),
        ("Y_minus", "F_minus", "dual_tail_actuation"),
        ("F_plus", "observer", "clark_source_observation"),
        ("Y_plus", "observer", "clark_endpoint_observation"),
        ("labels", "primitive_boundary", "primitive_incidence"),
        ("labels", "square_boundary", "square_incidence"),
        ("primitive_boundary", "completed_boundary", "archimedean_completion"),
        ("square_boundary", "completed_boundary", "archimedean_completion"),
        ("Y_plus", "retained_seam", "seam_retention"),
    ]
    comparison_only = [
        ("Y_plus", "Y_minus", "fourier_tate_tail_comparison"),
        ("F_minus", "F_plus", "fourier_tate_source_comparison"),
    ]

    assert not reachable(executable, "Y_plus", "F_plus")
    assert reachable(executable + comparison_only, "Y_plus", "F_plus")

    print("executable_reverse_path=absent")
    print("comparison_promoted_path=present")
    print("promotion_status=unauthorized_cross_sector_write")
    print("missing_capability=Y_plus_to_F_plus")


if __name__ == "__main__":
    main()

