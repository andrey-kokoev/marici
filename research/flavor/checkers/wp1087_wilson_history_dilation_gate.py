import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# Conditional Wilson evolution: use the order-three cyclic permutation U.
# Its complex eigenvalues are the three distinct cube roots of unity, so it is
# a simple-spectrum unitary model of a Wilson three-line flag.
perm = [1, 2, 0]  # U e_i = e_perm[i]

def apply_U(v):
    return [v[perm.index(i)] for i in range(3)]

def matmul_perm(p, q):
    return [p[q[i]] for i in range(3)]

identity = [0, 1, 2]
U2 = matmul_perm(perm, perm)
U3 = matmul_perm(perm, U2)
assert U3 == identity

# Three-grade history bundle:
#   V x = (x, Ux, U^2 x)/sqrt(3).
# For unitary U, sum_k U^{-k}U^k = 3I, hence V is an isometry.
x = [Fraction(1), Fraction(2), Fraction(3)]
Ux = apply_U(x)
U2x = apply_U(Ux)
assert U2x != x

norm_sq = lambda v: sum(a*a for a in v)
grade_norm_sum = norm_sq(x) + norm_sq(Ux) + norm_sq(U2x)
assert grade_norm_sum == 3 * norm_sq(x)

# The exact isometry is conditional on source unitary evolution.  It still
# does not choose x or provide physical readout ports/reference rho.
supply = {
    "source_fixed_unitary_wilson_evolution": False,
    "three_grade_isometric_bundle": True,
    "physical_grade_register": False,
    "typed_readout_ports": False,
    "cyclic_ray": False,
    "volume_reference_rho": False,
}
assert list(supply.values()).count(False) == 5

result = {
    "schema": "marici.flavor.wp1087.v1",
    "status": "PASS",
    "question": "Can a unitary Wilson evolution admit a minimal nondestructive three-grade history bundle?",
    "unitary_model": {
        "U": "cyclic permutation e1->e2->e3->e1",
        "U_cubed": "I",
        "eigenvalues": "three distinct cube roots of unity",
    },
    "history_bundle": {
        "V": "(x,Ux,U^2 x)/sqrt(3)",
        "isometry_identity": "sum_k U^(-k) U^k = 3I",
        "witness_x": [str(v) for v in x],
        "grade_norm_sum": str(grade_norm_sum),
        "input_norm_squared": str(norm_sq(x)),
    },
    "conditional_supply": supply,
    "classification": "conditional history constructor: source-fixed unitary Wilson evolution admits an exact three-grade isometric bundle, but no physical grade register, readout ports, cyclic ray, or rho are sourced",
    "remaining_gate": "derive the physical grade register and typed readout ports from the source packet, after deriving the Wilson flag and coherent cyclic ray; rho remains separate",
    "hostile_gate": "do not promote the mathematical isometric bundle to a sourced physical history instrument",
    "claim_boundary": "the bundle exists only after the conditional source-fixed Wilson evolution is supplied",
    "disposition": "productive: separates mathematical history dilation from physical history instrumentation",
}

(ROOT / "results" / "wp1087_wilson_history_dilation_gate.json").write_text(json.dumps(result, indent=2) + "\n")
print("WP1087 PASS:", grade_norm_sum, norm_sq(x), len(perm))
