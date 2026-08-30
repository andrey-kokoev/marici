"""Local singularity census at soft-triangle endpoint intersections."""

from __future__ import annotations

import json

import sympy as sp


def main() -> None:
    w, t, kappa, xi = sp.symbols("w t kappa xi")
    kernel = (
        t**4
        - (10 + 8 * kappa * xi) * t**2
        + 16 * kappa**2 + 40 * kappa * xi + 16 * xi**2 + 9
    )
    hypersurface = w**2 - kernel
    variables = (w, t, kappa, xi)
    gradient = [sp.diff(hypersurface, variable) for variable in variables]
    hessian = sp.hessian(hypersurface, variables)

    records = []
    for epsilon in (-1, 1):
        for delta in (-1, 1):
            root_squared = 9 if epsilon * delta == 1 else 1
            corner_factor = sp.factor(kernel.subs({kappa: epsilon, xi: delta}))
            expected = (t**2 - root_squared) ** 2
            assert sp.expand(corner_factor - expected) == 0
            for tau in (-sp.sqrt(root_squared), sp.sqrt(root_squared)):
                point = {w: 0, t: tau, kappa: epsilon, xi: delta}
                grad = [sp.simplify(component.subs(point)) for component in gradient]
                hess = hessian.subs(point)
                determinant = sp.factor(hess.det())
                rank = hess.rank()
                assert grad == [0, 0, 0, 0]
                assert rank == 4 and determinant != 0
                records.append({
                    "kappa": epsilon,
                    "xi": delta,
                    "t": int(tau),
                    "signed_face": f"t={int(tau)}",
                    "hessian_rank": rank,
                    "hessian_determinant": str(determinant),
                    "singularity_type": "ordinary_double_point_A1",
                    "milnor_rank": 1,
                })

    assert len(records) == 8
    critical_solutions = sp.solve_poly_system(
        [
            kernel,
            sp.diff(kernel, t),
            sp.diff(kernel, kappa),
            sp.diff(kernel, xi),
        ],
        t,
        kappa,
        xi,
    )
    expected_solutions = {
        (record["t"], record["kappa"], record["xi"])
        for record in records
    }
    normalized_solutions = {
        tuple(int(value) for value in solution)
        for solution in critical_solutions
    }
    assert normalized_solutions == expected_solutions
    s, W = sp.symbols("s W")
    compact_kernel = sp.factor(sp.expand(s**4 * kernel.subs(t, 1 / s)))
    compact_hypersurface = W**2 - compact_kernel
    infinity_sections = []
    for sign in (-1, 1):
        point = {s: 0, W: sign}
        normal_derivative = sp.diff(compact_hypersurface, W).subs(point)
        assert normal_derivative == 2 * sign
        infinity_sections.append({
            "W": sign,
            "normal_derivative": int(normal_derivative),
            "smooth": True,
        })
    print(json.dumps({
        "schema": "marici.benincasa.soft-triangle-endpoint-nodes.v1",
        "records": records,
        "labelled_node_count": len(records),
        "total_local_milnor_rank": sum(record["milnor_rank"] for record in records),
        "full_affine_critical_locus": [
            {"t": solution[0], "kappa": solution[1], "xi": solution[2]}
            for solution in sorted(normalized_solutions)
        ],
        "all_affine_singularities_exhausted": True,
        "t_zero_projection_factor_is_total_space_singularity": False,
        "compactified_t_infinity": {
            "equation": str(compact_kernel),
            "sections": infinity_sections,
            "singularities": 0,
        },
        "global_affine_plus_t_infinity_singularities_exhausted": True,
        "support": (
            "intersections of kappa=+-1, xi=+-1 with the frozen signed "
            "face sections t=+-1 or t=+-3"
        ),
        "status": "eight_labelled_A1_nodes_on_existing_support_intersections",
        "scope": (
            "complex local hypersurface Milnor rank; no physical thimble selection, "
            "integral orientation, or global relation among the eight cycles"
        ),
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
