import json

import sympy as sp


A, B = sp.symbols("A B")
H = sp.Matrix([[1, -1], [1, 1]])
routes = sp.Matrix([A, B])
ports = H * routes
inverse = H.inv()

H_mod_two = H.applyfunc(lambda x: int(x) % 2)

checks = {
    "forward_readout_is_integral": all(x.is_Integer for x in H),
    "determinant_is_two": H.det() == 2,
    "inverse_requires_half": inverse
    == sp.Matrix([[sp.Rational(1, 2), sp.Rational(1, 2)],
                  [-sp.Rational(1, 2), sp.Rational(1, 2)]]),
    "equal_routes_give_dark_comparison": ports[0].subs(B, A) == 0,
    "equal_routes_preserve_bright_output": ports[1].subs(B, A) == 2 * A,
    "mod_two_rows_coincide": H_mod_two.row(0) == H_mod_two.row(1),
    "mod_two_rank_collapses": H_mod_two.rank(iszerofunc=lambda x: x % 2 == 0)
    == 1,
    "integral_cokernel_has_order_two": abs(int(H.det())) == 2,
}

result = {
    "schema": "marici.aspect.hadamard-integral-deck-extension.v1",
    "status": "pass" if all(checks.values()) else "fail",
    "checks": checks,
    "forward_matrix": str(H),
    "inverse_matrix": str(inverse),
    "ports": {"comparison": str(ports[0]), "physical": str(ports[1])},
    "interpretation": (
        "The coherent readout is invertible after scalar extension but has "
        "an order-two obstruction over the integral source lattice."
    ),
}

print(json.dumps(result, indent=2))
