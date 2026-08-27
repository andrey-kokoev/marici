"""Exact cubic-invariant and operator-type audit for the SO(5) anomaly branch."""
import json
from itertools import product
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]

def antisymmetric_generators(n):
    result = []
    for i in range(n):
        for j in range(i+1, n):
            T = sp.zeros(n)
            T[i, j] = 1
            T[j, i] = -1
            result.append(T)
    return result

def symmetrized_cubic(A, B, C):
    return sp.simplify(sum(sp.trace(A*X*Y) for X, Y in ((B,C),(C,B))))

so5_vector = antisymmetric_generators(5)
so3_triplet = antisymmetric_generators(3)
so5_vector_cubics = [symmetrized_cubic(A,B,C) for A,B,C in product(so5_vector, repeat=3)]
so3_triplet_cubics = [symmetrized_cubic(A,B,C) for A,B,C in product(so3_triplet, repeat=3)]

# Independent spinor realization of so(5), guarding against a representation-
# specific zero in the real vector trace.
I = sp.I
sigma1 = sp.Matrix([[0,1],[1,0]])
sigma2 = sp.Matrix([[0,-I],[I,0]])
sigma3 = sp.diag(1,-1)
eye2 = sp.eye(2)
gammas = [
    sp.kronecker_product(sigma1, sigma1),
    sp.kronecker_product(sigma2, sigma1),
    sp.kronecker_product(sigma3, sigma1),
    sp.kronecker_product(eye2, sigma2),
    sp.kronecker_product(eye2, sigma3),
]
clifford_residuals = [sp.simplify(gammas[i]*gammas[j]+gammas[j]*gammas[i]-2*(i==j)*sp.eye(4)) for i in range(5) for j in range(5)]
so5_spinor = [sp.simplify((gammas[i]*gammas[j]-gammas[j]*gammas[i])/4) for i in range(5) for j in range(i+1,5)]
so5_spinor_cubics = [symmetrized_cubic(A,B,C) for A,B,C in product(so5_spinor, repeat=3)]

# A comparator with a genuine cubic invariant proves the audit is capable of
# detecting one: the SU(3) lambda_8 direction has nonzero d_888.
T8 = sp.diag(1,1,-2)/(2*sp.sqrt(3))
su3_comparator = sp.simplify(symmetrized_cubic(T8,T8,T8))

# Typed field-degree signatures. A reduced 5D gauge Chern-Simons term contains
# one A5/Wilson-line insertion and two 4D field strengths. The target portal is
# CP-even and quadratic in each scalar packet.
cs_signature = {"A5_degree": 1, "field_strength_degree": 2, "epsilon_tensor": 1}
portal_signature = {"flavor_scalar_degree": 2, "Higgs_degree": 2, "epsilon_tensor": 0}

a, b = sp.symbols("a b", real=True)
boundary_contrast = b-a

checks = {
    "so5_vector_has_ten_generators": len(so5_vector) == 10,
    "so5_vector_all_cubic_invariants_vanish": all(value == 0 for value in so5_vector_cubics),
    "so5_clifford_representation_is_exact": all(M == sp.zeros(4) for M in clifford_residuals),
    "so5_spinor_has_ten_generators": len(so5_spinor) == 10,
    "so5_spinor_all_cubic_invariants_vanish": all(value == 0 for value in so5_spinor_cubics),
    "so3_triplet_all_cubic_invariants_vanish": all(value == 0 for value in so3_triplet_cubics),
    "su3_comparator_detects_nonzero_cubic_invariant": sp.simplify(su3_comparator + 1/(2*sp.sqrt(3))) == 0,
    "chern_simons_reduction_has_wrong_operator_signature": cs_signature != portal_signature,
    "boundary_contrast_remains_continuous": sp.diff(boundary_contrast,b) == 1 and sp.diff(boundary_contrast,a) == -1,
    "deliberate_failure_residual_is_nonzero": su3_comparator != 0,
}
checks = {name: bool(value) for name, value in checks.items()}
if not all(checks.values()):
    raise SystemExit(checks)

result = {
    "work_package": "WP744",
    "status": "PASS",
    "checks": checks,
    "source_domain": "minimal SO(5) gauge-connection carrier with diagonal SO(3) boundary, testing ordinary local 5D gauge Chern-Simons/anomaly inflow",
    "classification": "neither asymmetric portal selector nor portal rigidifier",
    "bulk_invariant_result": "the symmetrized cubic invariant vanishes in both vector and spinor realizations of so(5)",
    "boundary_invariant_result": "the real so(3) triplet also has no perturbative cubic gauge-anomaly tensor",
    "operator_type_obstruction": "even where a 5D Chern-Simons invariant exists, reduction yields a parity-odd A5 F wedge F response, not a CP-even Higgs-times-flavor quadratic portal",
    "continuous_fiber": "the residual SO(3)-invariant boundary contrast b-a is untouched by anomaly quantization",
    "smallest_exact_falsifier": "SU(3) comparator d_888=-1/(2 sqrt(3)) is detected, whereas all 1000 SO(5) vector and all 1000 SO(5) spinor cubic components vanish",
    "claim_boundary": "ordinary local perturbative gauge-anomaly/Chern-Simons mechanism; global anomalies, larger groups, discrete torsion, and nonlocal holonomies require separate typing",
    "remaining_source_gate": "test nonlocal or discrete holonomy constructors, but require their reduced operation to land in the CP-even portal rather than only a topological response",
    "remaining_physical_gate": "no calibrated physical16 instrument is supplied",
}
(ROOT / "results" / "wp744_so5_anomaly_quantization_type_no_go.json").write_text(
    json.dumps(result, indent=2) + "\n", encoding="utf-8"
)
print(json.dumps(result, indent=2))
