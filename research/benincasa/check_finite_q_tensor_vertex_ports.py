#!/usr/bin/env python3
"""Exact TT/helicity audit of the primary-source scalar-scalar-graviton vertex."""

import json
from pathlib import Path

import sympy as sp


bx, by, bz, qz, eta = sp.symbols("bx by bz qz eta", nonzero=True)
i = sp.I

beta = sp.Matrix([bx, by, bz])
q = sp.Matrix([0, 0, qz])
pi = sp.diag(1, 1, 0)

raw = beta * beta.T
transverse_beta = pi * beta
tt_vertex_numerator = sp.simplify(
    transverse_beta * transverse_beta.T
    - sp.trace(transverse_beta * transverse_beta.T) * pi / 2
)

assert sp.simplify(q.T * tt_vertex_numerator) == sp.zeros(1, 3)
assert sp.simplify(sp.trace(tt_vertex_numerator)) == 0

e_plus = sp.Matrix([1, i, 0]) / sp.sqrt(2)
e_minus = sp.Matrix([1, -i, 0]) / sp.sqrt(2)
eps_plus = e_plus * e_plus.T
eps_minus = e_minus * e_minus.T

V_plus = sp.factor((e_plus.dot(beta)) ** 2 / (2 * eta**2))
V_minus = sp.factor((e_minus.dot(beta)) ** 2 / (2 * eta**2))

A = bx**2 - by**2
B = 2 * bx * by
assert sp.simplify(V_plus - (A + i * B) / (4 * eta**2)) == 0
assert sp.simplify(V_minus - (A - i * B) / (4 * eta**2)) == 0

helicity_transfer = sp.Matrix([[1, i], [1, -i]])
helicity_det = sp.simplify(helicity_transfer.det())
assert helicity_det == -2 * i

quadrupole_jacobian = sp.Matrix([A, B]).jacobian(sp.Matrix([bx, by]))
quadrupole_det = sp.factor(quadrupole_jacobian.det())
assert sp.simplify(quadrupole_det - 4 * (bx**2 + by**2)) == 0

k2x, k2y, k2z, k4x, k4y, k4z = sp.symbols(
    "k2x k2y k2z k4x k4y k4z"
)
k2 = sp.Matrix([k2x, k2y, k2z])
k4 = sp.Matrix([k4x, k4y, k4z])
ward_identity = sp.expand((k2 + k4).dot(k2 - k4))
ward_difference = sp.expand(k2.dot(k2) - k4.dot(k4))
assert sp.simplify(ward_identity - ward_difference) == 0

packet = {
    "schema": "marici.benincasa.finite-q-tensor-vertex-ports.v1",
    "status": "passed",
    "primary_source": {
        "paper": "Baumann, Duaso Pueyo, Joyce, Lee, Pimentel, arXiv:2005.04234v3",
        "vertex": "page 58, equation (6.22)",
        "vertex_formula": "V_gamma_phi_phi^{ij}=beta_u^i beta_u^j/(2 eta^2)",
        "scalar_action": "page 32, equation following (4.34): conformally coupled scalar bulk action",
        "stress_tensor_Ward_identity": "page 32, equations (4.30)-(4.35)",
        "TT_projector": "page 106, equation (E.5)",
        "transversality": "page 107, equation (E.10)",
    },
    "source_typing": {
        "beta_u": "difference of the two scalar momenta at the vertex",
        "transfer_momentum": "finite and nonzero",
        "scope": "transverse-traceless local vertex; full loop insertion still to be constructed",
    },
    "tt_projection": {
        "projected_matrix": [[str(value) for value in row] for row in tt_vertex_numerator.tolist()],
        "transverse": True,
        "traceless": True,
    },
    "helicity_ports": {
        "V_plus": str(V_plus),
        "V_minus": str(V_minus),
        "real_quadrupole_coordinates": [str(A), str(B)],
        "transfer_matrix": [[str(value) for value in row] for row in helicity_transfer.tolist()],
        "transfer_determinant": str(helicity_det),
        "port_rank": 2,
    },
    "rank_loss": {
        "quadrupole_map_jacobian_determinant": str(quadrupole_det),
        "support": "bx^2+by^2=0; on the real physical locus beta is parallel to q",
        "classification": "existing Gram/collinear support",
    },
    "ward_packet": {
        "q_dot_beta": str(ward_identity),
        "difference_of_scalar_inverse_kinematics": str(ward_difference),
        "interpretation": "the unprojected longitudinal contraction is an endpoint difference; the physical TT projector annihilates it",
    },
    "new_carrier_support": False,
    "scope_warning": (
        "This resolves the local finite-q tensor-vertex and two-helicity provenance gate. "
        "It does not prove that multiplying the scalar rank-60 master system by this numerator "
        "produces the complete gravitational one-loop marked-relative connection. The eta^-2 "
        "weight and Ward contact completion must be transported explicitly."
    ),
}

output = Path(__file__).with_name("finite-q-tensor-vertex-ports.json")
output.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps(packet, indent=2, sort_keys=True))
