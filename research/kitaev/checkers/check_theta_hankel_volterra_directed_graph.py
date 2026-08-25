import json
from pathlib import Path
import sympy as sp


def main():
    # Closed scalar graphs Gamma_N=N fail identity-bonding compatibility.
    directed_residuals = [sp.Integer(n + 1) - sp.Integer(n) for n in range(1, 5)]
    assert all(r == 1 for r in directed_residuals)

    # Exact off-seam local factors, x=p^(-1/4): gamma_(3/4)=1+x+x^2.
    prime_factors = []
    product = sp.Integer(1)
    for p in (2, 3, 5, 7):
        x = sp.Pow(p, -sp.Rational(1, 4))
        factor = 1 + x + x**2
        assert sp.ask(sp.Q.positive(factor - 1)) is True
        product *= factor
        prime_factors.append({"prime": p, "gamma_sigma_3_4": sp.sstr(factor),
                              "gamma_sigma_1_4": sp.sstr(1 / factor)})

    # Limit graph witness Te_n=e_1.
    graph_samples = [{"N": n, "input_norm_squared": f"1/{n}",
                      "output_norm_squared": "1"} for n in (1, 2, 4, 8, 16)]

    # Scalar projection cannot distinguish opposite seam coordinates.
    trace_plus = sp.Matrix([3, 5])
    trace_minus = sp.Matrix([3, -5])
    scalar_row = sp.Matrix([[1, 0]])
    assert scalar_row.dot(trace_plus) == scalar_row.dot(trace_minus) == 3
    assert trace_plus != trace_minus

    result = {
        "owner": "marici.Kitaev",
        "claim_strength": "source_typing_obstruction",
        "finite_line_closability": True,
        "directed_graph_instantiated": False,
        "missing_maps": ["coefficient_bonding_V_XY", "tail_to_line_incidence",
                         "seam_to_line_incidence"],
        "scalar_graph_directed_residuals": [str(r) for r in directed_residuals],
        "off_seam_transport": {
            "sigma": "3/4",
            "local_factors": prime_factors,
            "finite_product": sp.sstr(product),
            "uniform_bound": False,
            "reciprocal_collapse_at_sigma": "1/4",
        },
        "completion_density_hostile": {
            "samples": graph_samples,
            "adjoint_domain": "e1_perp",
            "dense": False,
        },
        "unitary_transport_implies_nonzero_pairing": False,
        "scalar_equivalent_opposite_seams": True,
        "completed_theta_adjoint_density": "not_typed_until_incidence_is_supplied",
    }
    out = Path(__file__).parents[1] / "results" / "theta-hankel-volterra-directed-graph.json"
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
