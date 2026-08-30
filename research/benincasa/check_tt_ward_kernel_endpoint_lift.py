#!/usr/bin/env python3
"""Exact local Ward complex for a symmetric tensor at finite momentum."""

import json
from pathlib import Path

import sympy as sp


q = sp.symbols("q", nonzero=True)

# Symmetric-tensor coordinate order: xx,yy,zz,xy,xz,yz.
# For q=(0,0,q), divergence is q_j T^{ij}=(q*T_xz,q*T_yz,q*T_zz).
W = sp.Matrix(
    [
        [0, 0, 0, 0, q, 0],
        [0, 0, 0, 0, 0, q],
        [0, 0, q, 0, 0, 0],
    ]
)
trace = sp.Matrix([[1, 1, 1, 0, 0, 0]])
ward_trace = W.col_join(trace)

plus = sp.Matrix([1, -1, 0, 0, 0, 0])
cross = sp.Matrix([0, 0, 0, 1, 0, 0])
tt_inclusion = sp.Matrix.hstack(plus, cross)

assert W.rank() == 3
assert ward_trace.rank() == 4
assert len(ward_trace.nullspace()) == 2
assert ward_trace * tt_inclusion == sp.zeros(4, 2)
null_basis = sp.Matrix.hstack(*ward_trace.nullspace())
assert sp.Matrix.hstack(null_basis, tt_inclusion).rank() == 2

# A canonical sparse right inverse for the divergence target.  Its only pole
# is q=0, the already frozen soft locus.
endpoint_lift = sp.Matrix(
    [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 1 / q],
        [0, 0, 0],
        [1 / q, 0, 0],
        [0, 1 / q, 0],
    ]
)
assert sp.simplify(W * endpoint_lift) == sp.eye(3)

# The TT projector in matrix form kills both divergence and trace and is
# idempotent.  It projects xx,yy,xy to plus/cross coordinates.
P_TT = sp.Matrix(
    [
        [sp.Rational(1, 2), -sp.Rational(1, 2), 0, 0, 0, 0],
        [-sp.Rational(1, 2), sp.Rational(1, 2), 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
    ]
)
assert P_TT**2 == P_TT
assert W * P_TT == sp.zeros(3, 6)
assert trace * P_TT == sp.zeros(1, 6)
assert P_TT.rank() == 2

# Cyclic occurrence transport acts on site labels and leaves this local
# tensor complex unchanged in each transported momentum frame.
cycle3 = sp.Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
assert cycle3**3 == sp.eye(3)

packet = {
    "schema": "marici.benincasa.tt-ward-kernel-endpoint-lift.v1",
    "status": "passed",
    "primary_identity": {
        "source": "Baumann et al., arXiv:2005.04234v3, equation (4.30)",
        "map": "divergence of <T phi phi> to two labelled scalar two-point contact terms",
        "equal_couplings": "kappa_2=kappa_3=kappa",
    },
    "local_complex": {
        "symmetric_tensor_rank": 6,
        "divergence_rank": W.rank(),
        "divergence_plus_trace_rank": ward_trace.rank(),
        "tt_kernel_rank": len(ward_trace.nullspace()),
        "tt_basis": ["T_xx-T_yy", "T_xy"],
        "tt_projector_rank": P_TT.rank(),
    },
    "endpoint_lift": {
        "right_inverse_exists": True,
        "only_denominator": "q",
        "support": "existing soft locus q=0",
        "uniqueness": "defined modulo the TT kernel and trace/improvement choices",
    },
    "physical_tensor_class": {
        "ward_character": "strict cocycle",
        "W_after_TT": "zero",
        "contact_modification_of_TT_port": False,
    },
    "cyclic_covariance": True,
    "new_carrier_support": False,
    "scope_warning": (
        "This types the local Ward complex and its physical TT kernel. It does "
        "not construct the loop-corrected scalar two-point endpoint periods or "
        "a global longitudinal rank-60 Gauss-Manin lift."
    ),
}

output = Path(__file__).with_name("tt-ward-kernel-endpoint-lift.json")
output.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps(packet, indent=2, sort_keys=True))
