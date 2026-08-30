import json
from pathlib import Path
import sympy as sp


def main():
    delta = sp.symbols("delta", positive=True)

    # Gaussian translate plus its first two label derivatives: each fixed
    # analytic feature difference has zero adjacent-spacing limit.
    feature_residuals = []
    for order in range(3):
        # Exact control with scalar analytic feature exp(-q)*(q+1)^order.
        q = sp.symbols("q", real=True)
        f = sp.exp(-q) * (q + 1) ** order
        difference = sp.simplify(f.subs(q, delta) - f.subs(q, 0))
        limit = sp.limit(difference, delta, 0, dir="+")
        assert limit == 0
        feature_residuals.append({"order": order, "difference": str(difference),
                                  "zero_spacing_limit": str(limit)})

    # Pro-Gram norm is the Euclidean norm of the aggregate observation by
    # construction, so the sharp isometry constant is exactly one.
    observation = sp.Matrix([[1, 2], [0, 3], [4, 0]])
    gram = observation.T * observation
    x = sp.Matrix(sp.symbols("x0:2"))
    identity_residual = sp.expand((observation * x).dot(observation * x) -
                                  (x.T * gram * x)[0])
    assert identity_residual == 0

    result = {
        "owner": "marici.Kitaev",
        "claim_strength": "abstract_completion_theorem_and_fixed_finite_continuous_family_no_go",
        "fixed_continuous_feature_samples": feature_residuals,
        "aggregate_observation_gram": [[str(v) for v in row] for row in gram.tolist()],
        "pro_gram_isometry_residual": str(identity_residual),
        "pro_gram_sharp_lower_bound": "1_by_definition",
        "independent_green_energy_lower_bound": "unproved",
        "raw_l2_uniform_observability_for_fixed_continuous_family": False,
        "typed_escape_routes": ["change_source_topology", "authorized_discrete_port",
                                "source_dynamical_restriction"],
        "infinite_joint_faithfulness_implies_finite_coercive_energy": False,
    }
    out = Path(__file__).parents[1] / "results" / "theta-pro-gram-coercivity-gap.json"
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
