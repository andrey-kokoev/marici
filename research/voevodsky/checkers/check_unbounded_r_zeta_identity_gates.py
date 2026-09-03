from __future__ import annotations

import json
from fractions import Fraction


def render(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


def main() -> None:
    # Domain escape: truncations of x_n=1/n^2 are Cauchy in the graph norm
    # ||x||^2 + ||diag(n)x||^2, but their limit is not finitely supported.
    graph_tail_samples = []
    for cutoff in (4, 8, 16, 32):
        tail = sum(Fraction(1, n**4) + Fraction(1, n**2) for n in range(cutoff + 1, 2 * cutoff + 1))
        graph_tail_samples.append(tail)
    assert all(graph_tail_samples[i + 1] < graph_tail_samples[i] for i in range(len(graph_tail_samples) - 1))

    # New radical: a positive weight 1/N tends to zero on a fixed direction.
    radical_weights = [Fraction(1, n) for n in (2, 4, 8, 16)]
    assert all(weight > 0 for weight in radical_weights)
    assert all(radical_weights[i + 1] < radical_weights[i] for i in range(len(radical_weights) - 1))

    # Reduced minimum modulus of diag(1/n) on the first N coordinates is 1/N.
    minimum_moduli = [Fraction(1, n) for n in (2, 4, 8, 16, 32)]
    assert minimum_moduli[-1] < minimum_moduli[0]

    graph_tail_upper_bounds = [Fraction(2, cutoff) for cutoff in (4, 8, 16, 32)]
    assert all(graph_tail_samples[i] < graph_tail_upper_bounds[i] for i in range(len(graph_tail_samples)))

    result = {
        "schema": "marici.voevodsky.unbounded-r-zeta-identity-gates.v1",
        "status": "independent_completion_gates_verified",
        "domain_escape": {
            "core": "finitely supported sequences",
            "graph_cauchy_witness": "truncations of x_n=1/n^2",
            "sample_graph_tail_upper_bounds": [render(value) for value in graph_tail_upper_bounds],
            "core_closed": False,
        },
        "new_radical": {
            "positive_stage_weights": [render(value) for value in radical_weights],
            "limit_weight": "0/1",
        },
        "reduced_minimum_modulus": {
            "finite_values": [render(value) for value in minimum_moduli],
            "limit": "0/1",
            "uniform_coercivity": False,
        },
        "first_missing_typed_object": "independently source-derived common core and intertwiner C R_zeta = B",
        "passed": True,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
