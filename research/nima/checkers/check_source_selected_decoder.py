"""Exact decoder-selection audit on the 3x3 periodic toric chain complex."""

import importlib.util
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location(
    "toric", HERE / "check_toric_code_chain_carrier.py"
)
toric = importlib.util.module_from_spec(spec)
spec.loader.exec_module(toric)


def weighted_cost(chain, weights, n_edges):
    return sum(weights[i] for i in range(n_edges) if (chain >> i) & 1)


def minimizers(candidates, weights, n_edges):
    costs = [(weighted_cost(chain, weights, n_edges), chain) for chain in candidates]
    best = min(cost for cost, _ in costs)
    return best, sorted(chain for cost, chain in costs if cost == best)


def main():
    L = 3
    d1, d2 = toric.lattice(L)
    n_edges = 2 * L * L
    repairs = toric.column_space(d2)
    syndrome = (1 << 0) | (1 << 4)  # vertices (0,0) and (1,1)
    candidates = [
        chain for chain in range(1 << n_edges)
        if toric.apply_columns(d1, chain) == syndrome
    ]

    uniform_cost, uniform = minimizers(candidates, [1] * n_edges, n_edges)
    assert uniform_cost == 2 and len(uniform) == 2
    assert (uniform[0] ^ uniform[1]) in repairs

    # The two shortest paths are h(0,0)+v(1,0) and v(0,0)+h(0,1).
    weights_a = [10] * n_edges
    for edge in (0, 12):
        weights_a[edge] = 1
    weights_b = [10] * n_edges
    for edge in (9, 1):
        weights_b[edge] = 1
    cost_a, selected_a = minimizers(candidates, weights_a, n_edges)
    cost_b, selected_b = minimizers(candidates, weights_b, n_edges)
    assert cost_a == cost_b == 2
    assert len(selected_a) == len(selected_b) == 1
    assert selected_a[0] != selected_b[0]
    assert (selected_a[0] ^ selected_b[0]) in repairs

    # A cost assignment that makes a noncontractible detour cheap can select a
    # different logical recovery class despite the identical syndrome.
    horizontal_loop = sum(1 << (x * L) for x in range(L))
    detour = selected_a[0] ^ horizontal_loop
    assert toric.apply_columns(d1, detour) == syndrome
    assert (detour ^ selected_a[0]) not in repairs
    weights_detour = [10] * n_edges
    for i in range(n_edges):
        if (detour >> i) & 1:
            weights_detour[i] = 0
    detour_cost, detour_selected = minimizers(candidates, weights_detour, n_edges)
    assert detour_cost == 0 and detour in detour_selected
    assert all((chain ^ selected_a[0]) not in repairs for chain in detour_selected)

    print(
        json.dumps(
            {
                "schema": "marici.source-selected-decoder.v1",
                "L": L,
                "syndrome": syndrome,
                "uniform": {
                    "minimum_cost": uniform_cost,
                    "minimizer_count": len(uniform),
                    "same_repair_class": True,
                },
                "biased_local_models": {
                    "unique_each": True,
                    "different_representatives": True,
                    "same_repair_class": True,
                },
                "hostile_nonlocal_model": {
                    "minimum_cost": detour_cost,
                    "selects_different_logical_class": True,
                },
                "gates": {
                    "complex_does_not_select_decoder": True,
                    "cost_model_selects_representative": True,
                    "syndrome_plus_cost_need_not_preserve_logical_class": True,
                },
            },
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
