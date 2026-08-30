import json
from pathlib import Path

import mpmath as mp
import sympy as sp


a, b = sp.symbols("a b", real=True)
ell = sp.Matrix([[a, b]])
gram = ell.T * ell
kernel_vector = sp.Matrix([b, -a])

mp.mp.dps = 60


def local(p, w):
    return mp.sinh(w * mp.log(p)) / (mp.sqrt(p) * w)


def codiagonal(w):
    return local(2, w) + local(3, w)


root = mp.findroot(
    codiagonal,
    (mp.mpc("0.68", "7.43"), mp.mpc("0.70", "7.45")),
    tol=mp.mpf("1e-50"),
)
packet = [local(2, root), local(3, root)]
scalar_power = abs(sum(packet)) ** 2
dagger_power = sum(abs(value) ** 2 for value in packet)

checks = {
    "scalar_pullback_gram_has_zero_determinant": sp.simplify(gram.det()) == 0,
    "explicit_nonzero_kernel_direction": sp.simplify((ell * kernel_vector)[0]) == 0,
    "kernel_direction_has_positive_generic_dagger_norm": sp.simplify(
        (kernel_vector.T * kernel_vector)[0] - (a**2 + b**2)
    ) == 0,
    "one_by_two_scalar_map_has_rank_at_most_one": ell.rank() == 1,
    "hostile_scalar_port_is_dark": scalar_power < mp.mpf("1e-45"),
    "hostile_dagger_packet_is_bright": dagger_power > mp.mpf("1e-2"),
    "current_to_line_character_is_zero_free_on_sample_grid": all(
        abs(mp.exp(k * y)) > 0
        for k in (mp.mpc(1, 0), mp.mpc(0, 1), mp.mpc(1, 1))
        for y in (mp.mpc(-3, 2), mp.mpc(0, 0), mp.mpc(4, -5))
    ),
}

result = {
    "status": "pass" if all(checks.values()) else "fail",
    "checks": checks,
    "scalar_pullback_gram": str(gram),
    "kernel_vector": [str(value) for value in kernel_vector],
    "hostile_root": {"real": mp.nstr(mp.re(root), 25), "imag": mp.nstr(mp.im(root), 25)},
    "scalar_power": mp.nstr(scalar_power, 8),
    "dagger_power": mp.nstr(dagger_power, 25),
    "minimum_faithful_complex_output_dimension": 2,
}
out = Path(__file__).resolve().parents[1] / "results" / "scalar_dagger_faithfulness_no_go.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
