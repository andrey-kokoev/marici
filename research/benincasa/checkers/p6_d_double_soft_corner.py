import json
from math import comb
from pathlib import Path

# Exact polynomials in (u,v).
P4 = {
    (0, 2): 1, (0, 1): -4, (1, 1): 2, (2, 1): 4, (3, 1): -4,
    (0, 0): 4, (1, 0): -4, (2, 0): -7, (3, 0): 4, (4, 0): 4,
}
D = {
    (0, 2): -1, (0, 1): 4, (1, 1): -6, (2, 1): 4,
    (0, 0): -4, (1, 0): 12, (2, 0): -9,
}

def translate(poly, u0, v0):
    out = {}
    for (i, j), c in poly.items():
        for p in range(i + 1):
            for q in range(j + 1):
                key = (p, q)
                out[key] = out.get(key, 0) + c * comb(i, p) * u0**(i-p) * comb(j, q) * v0**(j-q)
    return {k: v for k, v in sorted(out.items()) if v}

p = translate(P4, 1, 1)
d = translate(D, 1, 1)
assert p == {(0, 2): 1, (1, 0): 8, (1, 1): -2, (2, 0): 21,
             (2, 1): -8, (3, 0): 16, (3, 1): -4, (4, 0): 4}
assert d == {(0, 2): -1, (1, 0): -4, (1, 1): 2, (2, 0): -5, (2, 1): 4}

packet = {
    "schema": "marici.p6_d_double_soft_corner.v1",
    "chart": "X1=1; u=E_T; X2=(u+v)/2-1; X3=(u-v)/2",
    "center": {"u": 1, "v": 1, "support": ["X2=0", "X3=0"]},
    "local_coordinates": ["x=u-1", "z=v-1"],
    "translated_equations": {
        "4P6": "z^2+8*x-2*x*z+21*x^2-8*x^2*z+16*x^3-4*x^3*z+4*x^4",
        "D": "-z^2-4*x+2*x*z-5*x^2+4*x^2*z",
    },
    "initial_forms": {"4P6": "8*x", "D": "-4*x"},
    "shared_tangent": "x=0",
    "classification": "existing double-site-soft incidence; tangency of two smooth coefficient branches",
}
Path("research/benincasa/results/p6-d-double-soft-corner.json").write_text(
    json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8"
)
print(json.dumps(packet, sort_keys=True))
