from __future__ import annotations

import json

import sympy as sp


def main() -> None:
    x2, y2, x3, y3, x4, y4 = sp.symbols("x2 y2 x3 y3 x4 y4", real=True)
    z2, z3, z4 = x2 + sp.I * y2, x3 + sp.I * y3, x4 + sp.I * y4
    numerator = (1 + sp.conjugate(z2) * z3) * (1 + sp.conjugate(z3) * z4)
    denominator = (1 + z2 * sp.conjugate(z2)) * (1 + z3 * sp.conjugate(z3)) * (1 + z4 * sp.conjugate(z4))
    bargmann = sp.simplify(sp.expand_complex(numerator / denominator))
    observables = sp.Matrix([sp.re(bargmann), sp.im(bargmann)])
    variables = (x2, y2, x3, y3, x4, y4)
    jacobian = observables.jacobian(variables)

    fixture = {x2: 1, y2: 0, x3: 1, y3: 1, x4: 0, y4: 1}
    exact_jacobian = sp.simplify(jacobian.subs(fixture))
    assert exact_jacobian.rank() == 2

    affine_dimension = 6
    stabilizer_dimension = 1
    quotient_dimension = affine_dimension - stabilizer_dimension
    prequotient_fiber_dimension = affine_dimension - exact_jacobian.rank()
    quotient_fiber_dimension = quotient_dimension - exact_jacobian.rank()
    assert quotient_dimension == 5
    assert prequotient_fiber_dimension == 4
    assert quotient_fiber_dimension == 3

    # Common phase is an infinitesimal stabilizer direction for the observable.
    phase_direction = sp.Matrix([-y2, x2, -y3, x3, -y4, x4]).subs(fixture)
    assert exact_jacobian * phase_direction == sp.zeros(2, 1)

    result = {
        "schema": "marici.voevodsky.bargmann-generic-fiber-dimension.v1",
        "status": "generic_local_nonidentifiability_verified",
        "labelled_four_ray_dimension": 8,
        "generic_PU2_orbit_dimension": 3,
        "generic_quotient_dimension": quotient_dimension,
        "observable_real_dimension": 2,
        "exact_fixture_jacobian_rank": exact_jacobian.rank(),
        "prequotient_local_fiber_dimension": prequotient_fiber_dimension,
        "quotient_local_fiber_dimension": quotient_fiber_dimension,
        "common_phase_stabilizer_in_kernel": True,
        "frozen_D_S3_fiber_dimension_computed": False,
        "passed": True,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
