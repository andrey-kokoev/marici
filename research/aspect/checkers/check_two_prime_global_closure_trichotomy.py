import json
from pathlib import Path

import mpmath as mp
import sympy as sp


mp.mp.dps = 70
z = sp.symbols("z")


def local(p, w):
    if abs(w) < mp.mpf("1e-60"):
        return mp.log(p) / mp.sqrt(p)
    return mp.sinh(w * mp.log(p)) / (mp.sqrt(p) * w)


def codiagonal(w):
    return local(2, w) + local(3, w)


root = mp.findroot(
    codiagonal,
    (mp.mpc("0.68", "7.43"), mp.mpc("0.70", "7.45")),
    tol=mp.mpf("1e-60"),
)
h2 = local(2, root)
h3 = local(3, root)
determinant = h2 * h3
dagger_norm = abs(h2) ** 2 + abs(h3) ** 2

H2 = sp.sinh(z * sp.log(2)) / (sp.sqrt(2) * z)
H3 = sp.sinh(z * sp.log(3)) / (sp.sqrt(3) * z)

# A bounded arithmetic witness supplements the exact unique-factorization
# argument recorded in the accompanying note.
common_lattice_collision = any(
    2**m == 3**n for m in range(1, 65) for n in range(1, 65)
)

checks = {
    "both_local_cells_are_even": all(
        sp.simplify(H.subs(z, -z) - H) == 0 for H in (H2, H3)
    ),
    "codiagonal_has_off_seam_zero": abs(codiagonal(root)) < mp.mpf("1e-50") and abs(mp.re(root)) > mp.mpf("0.1"),
    "local_ports_are_nonzero_at_codiagonal_null": min(abs(h2), abs(h3)) > mp.mpf("0.05"),
    "local_ports_cancel": abs(h2 + h3) < mp.mpf("1e-50"),
    "determinant_port_is_nonzero_at_codiagonal_null": abs(determinant) > mp.mpf("1e-3"),
    "dagger_packet_monitor_is_bright": dagger_norm > mp.mpf("1e-2"),
    "no_bounded_common_prime_zero_lattice": not common_lattice_collision,
}

result = {
    "status": "pass" if all(checks.values()) else "fail",
    "checks": checks,
    "off_seam_codiagonal_root": {"real": mp.nstr(mp.re(root), 30), "imag": mp.nstr(mp.im(root), 30)},
    "local_2": mp.nstr(h2, 25),
    "local_3": mp.nstr(h3, 25),
    "determinant_at_codiagonal_root": mp.nstr(determinant, 25),
    "dagger_norm_at_codiagonal_root": mp.nstr(dagger_norm, 25),
    "common_zero_lattice_search": {"max_index": 64, "collision": common_lattice_collision},
}
out = Path(__file__).resolve().parents[1] / "results" / "two_prime_global_closure_trichotomy.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
