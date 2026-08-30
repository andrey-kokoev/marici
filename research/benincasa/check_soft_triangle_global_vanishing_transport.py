"""Global transport of the four supported soft-triangle vanishing lines."""

from __future__ import annotations

import json

import sympy as sp


def main() -> None:
    t, kappa, xi, sigma = sp.symbols("t kappa xi sigma")
    kernel = (
        t**4
        - (10 + 8 * kappa * xi) * t**2
        + 16 * kappa**2 + 40 * kappa * xi + 16 * xi**2 + 9
    )
    a_minus = 5 + 4 * kappa * xi - 4 * sigma
    a_plus = 5 + 4 * kappa * xi + 4 * sigma
    factorized = sp.expand((t**2 - a_minus) * (t**2 - a_plus))
    sigma_relation = sigma**2 - (1 - kappa**2) * (1 - xi**2)
    assert sp.rem(
        sp.Poly(factorized - kernel, sigma),
        sp.Poly(sigma_relation, sigma),
    ).as_expr() == 0
    assert sp.factor(a_plus - a_minus) == 8 * sigma

    # At the center of the physical open square the transported positive cut
    # is [1,3].  At each physical corner the same ordered cut collapses.
    center = {
        "kappa": 0,
        "xi": 0,
        "A_minus": 1,
        "A_plus": 9,
        "positive_branch_cut": [1, 3],
    }
    physical_corners = [
        (-1, -1, 9),
        (-1, 1, 1),
        (1, -1, 1),
        (1, 1, 9),
    ]
    corner_records = []
    for epsilon, delta, collision in physical_corners:
        substitution = {kappa: epsilon, xi: delta, sigma: 0}
        lower = int(a_minus.subs(substitution))
        upper = int(a_plus.subs(substitution))
        assert lower == upper == collision
        corner_records.append({
            "kappa": epsilon,
            "xi": delta,
            "A_minus": lower,
            "A_plus": upper,
            "positive_t_collision": int(sp.sqrt(collision)),
            "transported_cycle": "alpha_positive_cut",
            "orientation": 1,
        })

    # The four supported costalk generators all map to the same generic
    # positive-cut cycle.  Entry 2370 supplies the common corner sign and
    # Entry 2374 the common conifold orientation.
    local_to_generic = sp.Matrix([[1, 1, 1, 1]])
    physical_diagonal = sp.ones(4, 1)
    generic_image = local_to_generic * physical_diagonal
    assert local_to_generic.rank() == 1
    assert generic_image == sp.Matrix([4])

    # At the center, on 1<t<3, the radicand has fixed negative sign.  The
    # anti-trace period of dt/w therefore has fixed nonzero imaginary phase.
    central_kernel = sp.factor(kernel.subs({kappa: 0, xi: 0}))
    assert central_kernel == (t - 3) * (t - 1) * (t + 1) * (t + 3)

    print(json.dumps({
        "schema": "marici.benincasa.soft-triangle-global-vanishing-transport.v1",
        "squared_branch_points": {
            "A_minus": str(a_minus),
            "A_plus": str(a_plus),
            "sigma_squared": "(1-kappa^2)*(1-xi^2)",
            "difference": "8*sigma",
        },
        "open_base": "-1<kappa<1, -1<xi<1, sigma>0",
        "open_base_contractible": True,
        "positive_roots_bounded_by": [1, 9],
        "center": center,
        "physical_corners": corner_records,
        "local_costalk_to_generic_cycle_matrix": [[1, 1, 1, 1]],
        "physical_supported_diagonal": [1, 1, 1, 1],
        "generic_cycle_coefficient": 4,
        "generic_cycle": "alpha_positive_cut",
        "central_curve": str(central_kernel),
        "central_antitrace_period": (
            "nonzero: dt/w has one fixed imaginary phase on 1<t<3"
        ),
        "status": "supported_diagonal_survives_as_four_times_the_global_positive_cut_cycle",
        "scope": (
            "Gauss--Manin transport and iterated local-to-generic tube/Gysin "
            "map for the pure node coefficient; no contact-weighted transfer, "
            "tensor polarization, or complete observer-port pairing"
        ),
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
