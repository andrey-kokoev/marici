import json
from pathlib import Path

# Sparse exact polynomials in (u,z), represented by
# {(u_degree,z_degree): integer coefficient}.
P4 = {
    (0, 2): 1, (1, 1): 2, (2, 1): 4, (3, 1): -4,
    (2, 0): 1, (3, 0): -4, (4, 0): 4,
}
D = {(0, 2): -1, (1, 1): -6, (2, 1): 4, (2, 0): -1}
H = {(0, 1): 1, (1, 1): 2, (2, 1): -1, (1, 0): 1, (2, 0): -2, (3, 0): 1}

def initial(poly):
    degree = min(i + j for i, j in poly)
    return {m: c for m, c in poly.items() if sum(m) == degree}

initials = {"4P6": initial(P4), "D": initial(D), "H": initial(H)}
assert initials["4P6"] == {(0, 2): 1, (1, 1): 2, (2, 0): 1}
assert initials["D"] == {(0, 2): -1, (1, 1): -6, (2, 0): -1}
assert initials["H"] == {(0, 1): 1, (1, 0): 1}

packet = {
    "schema": "marici.p6_wall_soft_corner.v1",
    "chart": "X1=1; u=E_T; X2=(u+v)/2-1; X3=(u-v)/2",
    "center": {"u": 0, "v": 2, "support": ["E_T=0", "X2=0"]},
    "local_coordinate": "z=v-2",
    "shifted_equations": {
        "4P6": "z^2+2*u*(1+2*u-2*u^2)*z+u^2*(1-2*u)^2",
        "D": "-z^2+(-6*u+4*u^2)*z-u^2",
        "H": "(1+2*u-u^2)*z+u*(1-u)^2",
    },
    "initial_forms": {
        "4P6": "(z+u)^2",
        "D": "-(z^2+6*u*z+u^2)",
        "H": "z+u",
    },
    "shared_tangent": {"4P6": "(u+z)^2", "H": "u+z"},
    "D_tangent_discriminant": 32,
    "classification": "existing total-energy/site-soft incidence; nontransverse coefficient collision",
}
Path("research/benincasa/results/p6-wall-soft-corner.json").write_text(
    json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8"
)
print(json.dumps(packet, sort_keys=True))
