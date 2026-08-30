import json
from fractions import Fraction
from pathlib import Path


def main():
    # q(x,y)=x and J(x,y)=y: e_2 is the minimal descent witness.
    descent = {"q_e2": 0, "J_e2": 1, "passes": False}

    # T e_n=e_1 and x_N=(1/N)sum e_n.
    graph = []
    for n in (1, 2, 4, 8, 16):
        graph.append({
            "N": n,
            "input_norm_squared": str(Fraction(1, n)),
            "output_norm_squared": "1",
        })

    # Primitive coefficient 2^n.  Squared norm in diagonal pivot w_n is
    # sum 4^n/w_n.  Polynomial weights fail; Laplace weights 16^n converge.
    topology = []
    for n in (1, 2, 4, 8):
        tempered = sum(Fraction(4**k, (k + 1) ** 2) for k in range(1, n + 1))
        laplace = sum(Fraction(1, 4**k) for k in range(1, n + 1))
        topology.append({"N": n, "tempered_constant_squared": str(tempered),
                         "laplace_constant_squared": str(laplace)})
    assert topology[-1]["tempered_constant_squared"] != topology[0]["tempered_constant_squared"]
    assert all(Fraction(x["laplace_constant_squared"]) < Fraction(1, 3)
               for x in topology)

    # Same scalar x, opposite seam y; seam erasure also preserves scalar x.
    v = (3, 5)
    scalar = v[0]
    trace_plus = v
    trace_minus = (v[0], -v[1])
    erased = (v[0], 0)
    assert trace_plus != trace_minus and scalar == trace_minus[0] == erased[0]

    result = {
        "owner": "marici.Kitaev",
        "classification": "closable_only_after_adjoining_typed_boundary_current",
        "additive_l2_restriction": descent,
        "nonclosable_absolute_sum_graph": {
            "samples": graph,
            "limit_input_norm_squared": 0,
            "limit_output_norm_squared": 1,
            "adjoint_domain": "e1_perp",
            "adjoint_domain_dense": False,
        },
        "typed_increment_repair": {
            "map": "R e_n = e_n",
            "closable": True,
            "isometry": True,
        },
        "primitive_topology": {
            "samples": topology,
            "laplace_uniform_upper_bound_squared": "1/3",
            "common_tempered_topology_rejected": True,
        },
        "scalar_nonuniqueness": {
            "input": list(v), "trace_plus": list(trace_plus),
            "trace_minus": list(trace_minus), "seam_erased": list(erased),
            "common_scalar": scalar,
        },
        "theta_closability_status": "unresolved_dense_adjoint_domain_range_problem",
        "unresolved_gate": "density of {y: H* y in Ran G}",
    }
    out = Path(__file__).parents[1] / "results" / "rigged-tate-trace-correspondence.json"
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
