import json
from pathlib import Path

import mpmath as mp
import sympy as sp


mp.mp.dps = 70
z = sp.symbols("z")
H_symbolic = sum(
    sp.sinh(z * sp.log(p)) / (sp.sqrt(p) * z)
    for p in (2, 3)
)


def local(p, w):
    if abs(w) < mp.mpf("1e-60"):
        return mp.log(p) / mp.sqrt(p)
    return mp.sinh(w * mp.log(p)) / (mp.sqrt(p) * w)


def aggregate(w):
    return local(2, w) + local(3, w)


root = mp.findroot(
    aggregate,
    (mp.mpc("0.68", "7.43"), mp.mpc("0.70", "7.45")),
    tol=mp.mpf("1e-60"),
    maxsteps=100,
)
residual = abs(aggregate(root))
partners = [root, -root, mp.conj(root), -mp.conj(root)]
partner_residual = max(abs(aggregate(w)) for w in partners)

checks = {
    "aggregate_is_symbolically_even": sp.simplify(H_symbolic.subs(z, -z) - H_symbolic) == 0,
    "removable_origin_is_positive": sum(mp.log(p) / mp.sqrt(p) for p in (2, 3)) > 0,
    "root_is_off_seam": abs(mp.re(root)) > mp.mpf("0.1"),
    "root_is_nonreal": abs(mp.im(root)) > mp.mpf("1"),
    "off_seam_residual_below_1e_50": residual < mp.mpf("1e-50"),
    "reflection_conjugation_orbit_is_zero": partner_residual < mp.mpf("1e-50"),
    "neither_local_cell_vanishes_at_aggregate_root": all(
        abs(local(p, root)) > mp.mpf("0.05") for p in (2, 3)
    ),
}

result = {
    "status": "pass" if all(checks.values()) else "fail",
    "checks": checks,
    "primes": [2, 3],
    "weights": ["2^(-1/2)", "3^(-1/2)"],
    "off_seam_root": {"real": mp.nstr(mp.re(root), 30), "imag": mp.nstr(mp.im(root), 30)},
    "residual": mp.nstr(residual, 8),
    "maximum_orbit_residual": mp.nstr(partner_residual, 8),
    "local_values_at_root": {str(p): mp.nstr(local(p, root), 25) for p in (2, 3)},
}
out = Path(__file__).resolve().parents[1] / "results" / "two_prime_evenized_off_seam_zero.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
