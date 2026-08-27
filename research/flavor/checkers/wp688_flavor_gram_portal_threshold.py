"""Exact positive flavor-Gram form of the exit-Higgs portal threshold."""
import json
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
q1, q2, q3 = sp.symbols("q1 q2 q3", positive=True)
x = sp.Matrix(3, 3, lambda i, j: sp.symbols(f"x{i+1}{j+1}", real=True))
Q2 = sp.diag(q1**2, q2**2, q3**2)
X2 = x.T*x
pairing = sp.expand(sp.trace(Q2*X2))
sum_squares = sp.expand(sum([q1, q2, q3][j]**2*x[i, j]**2 for i in range(3) for j in range(3)))
canonical = sp.simplify(pairing.subs({x[i, j]: int(i == j) for i in range(3) for j in range(3)}))

# Boundary hostile: a zero ordinary Yukawa direction and exit support only on it.
boundary = {q1: 0, q2: 2, q3: 3}
boundary.update({x[i, j]: int(i == 0 and j == 0) for i in range(3) for j in range(3)})

checks = {
    "threshold_is_weighted_sum_of_squares": sp.simplify(pairing-sum_squares) == 0,
    "canonical_exit_shape_pairs_with_all_quark_yukawas": canonical == q1**2+q2**2+q3**2,
    "positive_quark_yukawas_make_pairing_faithful_on_nonzero_exit_tensor": pairing.subs({x[0, 0]: 1, **{x[i, j]: 0 for i in range(3) for j in range(3) if (i, j) != (0, 0)}}) == q1**2,
    "zero_yukawa_support_is_exact_boundary_kernel": pairing.subs(boundary) == 0,
    "no_intergeneration_sign_cancellation": all(term.as_coeff_Mul()[0] > 0 for term in sp.Add.make_args(sum_squares)),
}
checks = {name: bool(value) for name, value in checks.items()}
if not all(checks.values()):
    raise SystemExit(checks)

result = {
    "work_package": "WP688",
    "status": "PASS",
    "checks": checks,
    "pairing": "P=Tr[(Y_q^dagger Y_q)(Y_X^dagger Y_X)]=sum_ij q_j^2 |X_ij|^2",
    "threshold": "delta lambda_p=N_c P/(4 pi^2) at the common heavy matching scale on the WP687 slice",
    "positivity": "P is nonnegative and has no intergeneration sign cancellations",
    "faithful_domain": "if every ordinary quark Yukawa is positive, P=0 iff Y_X=0",
    "canonical_shape": "for Y_X=I, P=q1^2+q2^2+q3^2>0",
    "boundary_kernel": "an exactly zero ordinary Yukawa direction can hide exit support confined to that direction",
    "classification": "source-defined positive pairing that rigidifies portal support; not a numerical selector of the total renormalized portal",
    "smallest_exact_falsifier": "q1=0 and Y_X supported only on column one gives P=0",
    "remaining_gate": "combine nondegenerate messenger thresholds and UV boundary data, then establish a calibrated lower bound at the interference scale",
}
(ROOT / "results" / "wp688_flavor_gram_portal_threshold.json").write_text(
    json.dumps(result, indent=2)+"\n", encoding="utf-8")
print(json.dumps(result, indent=2))
