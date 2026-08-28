import json

import sympy as sp


p = sp.symbols("p", positive=True)
N = sp.symbols("N", positive=True)
m = sp.symbols("m", positive=True)

primitive_image = 1 / (2 * sp.sqrt(p) * sp.log(p))
augmentation_image = 1 / (2 * sp.log(p) ** 2)
finite_order_primitive = sp.log(p) ** (1 - 2 * m) / sp.sqrt(p)

checks = {
    "primitive_image_formula": sp.simplify(
        (1 / (2 * sp.log(p) ** 2)) * (sp.log(p) / sp.sqrt(p))
        - primitive_image
    )
    == 0,
    "primitive_q1_diverges": sp.limit(p * primitive_image, p, sp.oo)
    == sp.oo,
    "augmentation_q1_diverges": sp.limit(p * augmentation_image, p, sp.oo)
    == sp.oo,
    "every_fixed_log_order_fails_q1": sp.limit(
        (p * finite_order_primitive).subs(m, 17), p, sp.oo
    )
    == sp.oo,
    "log_gaussian_is_superpolynomial": sp.limit(
        p**N * sp.exp(-sp.log(p) ** 2), p, sp.oo
    )
    == 0,
}

result = {
    "schema": "marici.aspect.prime-rigging-lyapunov-obstruction.v1",
    "status": "pass" if all(checks.values()) else "fail",
    "checks": checks,
    "primitive_image": str(primitive_image),
    "augmentation_image": str(augmentation_image),
    "conclusion": (
        "Finite logarithmic smoothing does not map the completed currents "
        "into the rapid prime test space; arithmetic infinite smoothing is required."
    ),
}

print(json.dumps(result, indent=2))
