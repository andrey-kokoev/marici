#!/usr/bin/env python3
"""Compile the three finite-q helicity vertices from labelled CM geometry."""

import json
from pathlib import Path

import sympy as sp


c, a, b = sp.symbols("c a b")  # y12,y23,y31
P1, P2, P3 = sp.symbols("P1 P2 P3", nonzero=True)

CM = sp.Matrix(
    [
        [0, 1, 1, 1, 1],
        [1, 0, c**2, a**2, b**2],
        [1, c**2, 0, P2**2, P1**2],
        [1, a**2, P2**2, 0, P3**2],
        [1, b**2, P1**2, P3**2, 0],
    ]
)
K = sp.factor(-CM.det() / 2)


def vertex_packet(label, p, r, s, d0, d1, d2):
    """Use base vertices O,V1,V2 and apex distances d0,d1,d2."""

    lam = sp.factor((p - r - s) * (p - r + s) * (p + r - s) * (p + r + s))
    hx = (p**2 + r**2 - s**2) / (2 * p)
    hy2 = sp.factor(-lam / (4 * p**2))
    x = (d0**2 + p**2 - d1**2) / (2 * p)
    dot_l_v2 = (d0**2 + r**2 - d2**2) / 2
    y2 = sp.factor((dot_l_v2 - x * hx) ** 2 / hy2)

    gram = sp.Matrix(
        [
            [p**2, (p**2 + r**2 - s**2) / 2, (p**2 + d0**2 - d1**2) / 2],
            [(p**2 + r**2 - s**2) / 2, r**2, (r**2 + d0**2 - d2**2) / 2],
            [(p**2 + d0**2 - d1**2) / 2, (r**2 + d0**2 - d2**2) / 2, d0**2],
        ]
    )
    det_gram = sp.factor(gram.det())
    z2 = sp.factor(det_gram / (p**2 * hy2))
    rho2 = sp.factor(d0**2 - x**2)
    face_heron = sp.factor(
        (p - d0 - d1) * (p - d0 + d1) * (p + d0 - d1) * (p + d0 + d1)
    )

    assert sp.factor(y2 + z2 - rho2) == 0
    assert sp.factor(rho2 + face_heron / (4 * p**2)) == 0

    return {
        "label": label,
        "external_edge": str(p),
        "adjacent_occurrences": [str(d0), str(d1)],
        "opposite_occurrence": str(d2),
        "external_gram": str(lam),
        "in_plane_square": str(y2),
        "normal_square": str(z2),
        "transverse_radius_square": str(rho2),
        "quadrupole_jacobian": str(sp.factor(4 * rho2)),
        "rank_loss_support": str(face_heron),
    }


# The source CM ordering says the base edge between y12 and y31 is P1,
# between y23 and y12 is P2, and between y31 and y23 is P3.
vertices = [
    vertex_packet("site1", P1, P2, P3, c, b, a),
    vertex_packet("site2", P2, P3, P1, a, c, b),
    vertex_packet("site3", P3, P1, P2, b, a, c),
]

# For site 1, the tetrahedral Gram determinant is exactly -K/4.  Therefore
# z^2=K/Lambda in the source normalization D_CM=-2K.
gram_site1 = sp.Matrix(
    [
        [P1**2, (P1**2 + P2**2 - P3**2) / 2, (P1**2 + c**2 - b**2) / 2],
        [(P1**2 + P2**2 - P3**2) / 2, P2**2, (P2**2 + c**2 - a**2) / 2],
        [(P1**2 + c**2 - b**2) / 2, (P2**2 + c**2 - a**2) / 2, c**2],
    ]
)
assert sp.factor(gram_site1.det() + K / 4) == 0
lambda_external = sp.factor(
    (P1 - P2 - P3) * (P1 - P2 + P3) * (P1 + P2 - P3) * (P1 + P2 + P3)
)
site1_hy2 = -lambda_external / (4 * P1**2)
site1_z2 = sp.factor(gram_site1.det() / (P1**2 * site1_hy2))
assert sp.factor(site1_z2 - K / lambda_external) == 0

# Cyclic relabelling preserves K exactly.
cyclic = {c: a, a: b, b: c, P1: P2, P2: P3, P3: P1}
assert sp.factor(K.xreplace(cyclic) - K) == 0

# Each local real quadrupole pair maps isomorphically to the two helicities.
i = sp.I
helicity_transfer = sp.Matrix([[1, i], [1, -i]])
block_transfer = sp.diag(helicity_transfer, helicity_transfer, helicity_transfer)
assert helicity_transfer.det() == -2 * i
assert sp.factor(block_transfer.det() - (-2 * i) ** 3) == 0
assert block_transfer.rank() == 6

packet = {
    "schema": "marici.benincasa.cyclic-tensor-vertex-cm-sheet.v1",
    "status": "passed",
    "source_coordinates": {
        "fiber_occurrences": ["c=y12", "a=y23", "b=y31"],
        "base_edges": ["P1 between y12,y31", "P2 between y23,y12", "P3 between y31,y23"],
        "cm_normalization": "D_CM=-2*K",
    },
    "vertices": vertices,
    "normal_sheet_identity": "z_i^2=K/Lambda(P1,P2,P3) in each cyclic chart",
    "helicity_formula": "H_i^±=(Y_i±i Z_i)^2",
    "deck_action": "Z_i -> -Z_i exchanges H_i^+ and H_i^-",
    "helicity_transfer": [[str(value) for value in row] for row in helicity_transfer.tolist()],
    "cyclic_block_rank": block_transfer.rank(),
    "cyclic_block_determinant": str(block_transfer.det()),
    "rank_loss_classification": "each local loss is an existing triangular face Gram/collinear divisor",
    "coefficient_classification": "external Gram orientation plus the existing Cayley-Menger Kummer sheet",
    "new_carrier_support": False,
    "scope_warning": (
        "This compiles the occurrence-labelled local tensor numerators from the "
        "frozen distance geometry. It does not yet reduce their multiplication "
        "on the rank-60 twisted cohomology or add the Ward-correlated contact channels."
    ),
}

output = Path(__file__).with_name("cyclic-tensor-vertex-cm-sheet.json")
output.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps(packet, indent=2, sort_keys=True))
