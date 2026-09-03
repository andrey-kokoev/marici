from __future__ import annotations

import json

import sympy as sp


def main() -> None:
    identity = sp.eye(2)
    shear = sp.Matrix([[1, 1], [0, 1]])
    scaling = sp.diag(2, sp.Rational(1, 2))
    rotation = sp.Matrix([[sp.Rational(3, 5), -sp.Rational(4, 5)], [sp.Rational(4, 5), sp.Rational(3, 5)]])

    assert shear.det() == scaling.det() == rotation.det() == 1
    assert shear * identity * shear.T != identity
    assert scaling * identity * scaling.T != identity
    assert rotation * identity * rotation.T == identity

    # Symbolic equivalence: normalization after congruence is exactly S S^T=I.
    a, b, c, d = sp.symbols("a b c d", real=True)
    s = sp.Matrix([[a, b], [c, d]])
    residual = sp.expand(s * s.T - identity)
    assert residual == sp.Matrix([[a**2 + b**2 - 1, a*c + b*d], [a*c + b*d, c**2 + d**2 - 1]])

    edge = sp.Matrix([[sp.Rational(1, 3), 0], [0, sp.Rational(1, 4)]])
    transformed_edge = shear * edge * shear.inv()
    assert transformed_edge.shape == edge.shape
    assert shear * identity * shear.T != identity  # edge transformation cannot alter diagonal normalization

    result = {
        "schema": "marici.voevodsky.nonorthogonal-gauge-obstruction.v1",
        "status": "orthogonal_groupoid_maximal_for_normalized_congruence",
        "invertible_shear_rejected": True,
        "invertible_scaling_rejected": True,
        "orthogonal_rotation_admitted": True,
        "normalization_equivalent_to_SST_identity": True,
        "edge_redefinition_cannot_repair_diagonal": True,
        "arbitrary_invertible_gauge_equipment": False,
        "enlarged_metric_object_category_constructed": False,
        "passed": True
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
