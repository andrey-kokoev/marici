from fractions import Fraction
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULT = ROOT / "results" / "endpoint_grade_chain_scalar_holonomy_checks.json"


def spin_one_tensor_degrees(l):
    if l == 0:
        return [1]
    return [l + 1, l, l - 1]


def weight_squared(l):
    return Fraction(2 * (2 * l + 1), l + 1)


def main():
    max_degree = 50
    gates = {}

    gates["target_multiplicity_one"] = all(
        spin_one_tensor_degrees(l).count(l + 1) == 1
        for l in range(max_degree + 1)
    )

    weights = [weight_squared(l) for l in range(max_degree + 1)]
    gates["all_transfer_weights_nonzero"] = all(w != 0 for w in weights)

    vertex_scales = [Fraction(1)]
    for w in weights:
        vertex_scales.append(w * vertex_scales[-1])
    normalized = [
        weights[l] * vertex_scales[l] / vertex_scales[l + 1]
        for l in range(len(weights))
    ]
    gates["chain_weights_trivialize"] = all(x == 1 for x in normalized)

    zero_fixture = [Fraction(2), Fraction(0), Fraction(3)]
    nonzero_vertex_gauge = [Fraction(5), Fraction(7), Fraction(11), Fraction(13)]
    transformed_zero = (
        zero_fixture[1]
        * nonzero_vertex_gauge[1]
        / nonzero_vertex_gauge[2]
    )
    gates["zero_edge_is_gauge_invariant"] = transformed_zero == 0

    cycle_edges = [Fraction(2), Fraction(3), Fraction(5, 7)]
    cycle_holonomy = cycle_edges[0] * cycle_edges[1] * cycle_edges[2]
    gauges = [Fraction(11), Fraction(13), Fraction(17)]
    transformed_cycle = [
        cycle_edges[0] * gauges[0] / gauges[1],
        cycle_edges[1] * gauges[1] / gauges[2],
        cycle_edges[2] * gauges[2] / gauges[0],
    ]
    transformed_holonomy = (
        transformed_cycle[0] * transformed_cycle[1] * transformed_cycle[2]
    )
    gates["cycle_holonomy_is_gauge_invariant"] = (
        transformed_holonomy == cycle_holonomy
    )
    gates["hostile_cycle_is_not_trivializable"] = cycle_holonomy != 1

    gates["dimension_formula_matches_decomposition"] = all(
        3 * (2 * l + 1)
        == sum(2 * j + 1 for j in spin_one_tensor_degrees(l))
        for l in range(max_degree + 1)
    )

    status = "pass" if all(gates.values()) else "fail"
    payload = {
        "schema": "marici.strominger.endpoint-grade-chain-scalar-holonomy.v1",
        "status": status,
        "max_degree": max_degree,
        "gates": gates,
        "summary": {
            "passed": sum(gates.values()),
            "total": len(gates),
            "cycle_holonomy": str(cycle_holonomy),
            "classification": (
                "nonzero scalar edge data on the acyclic grade chain is "
                "presentation gauge; zero edges and cycle products survive"
            ),
        },
    }
    encoded = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(encoded, encoding="ascii")
    digest = hashlib.sha256(encoded.encode("ascii")).hexdigest()
    print(json.dumps({"status": status, "sha256": digest, **payload["summary"]}))
    raise SystemExit(0 if status == "pass" else 1)


if __name__ == "__main__":
    main()

