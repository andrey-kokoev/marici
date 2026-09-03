"""Exact linearized audit of incidence/recovery on the forcing skew product."""
from fractions import Fraction as F
from pathlib import Path
import json


def matmul(a, b):
    return [[sum((a[i][k] * b[k][j] for k in range(len(b))), F(0)) for j in range(len(b[0]))] for i in range(len(a))]


def matvec(a, x):
    return [sum((a[i][k] * x[k] for k in range(len(x))), F(0)) for i in range(len(a))]


# One endpoint coordinate plus source coordinates (y,f); target has two route
# coordinates plus the same source coordinates. I_route(e)=(e,e), R_route=(1/2,1/2).
I = [[F(1)], [F(1)]]
R = [[F(1, 2), F(1, 2)]]
I_tilde = [
    [F(1), 0, 0],
    [F(1), 0, 0],
    [0, F(1), 0],
    [0, 0, F(1)],
]
R_tilde = [
    [F(1, 2), F(1, 2), 0, 0],
    [0, 0, F(1), 0],
    [0, 0, 0, F(1)],
]
identity3 = [[F(i == j) for j in range(3)] for i in range(3)]
jet_source = [F(0), F(2), F(-6)]  # sample tangent (0,y',f')
jet_target = matvec(I_tilde, jet_source)
jet_recovered = matvec(R_tilde, jet_target)
checks = {
    "route_recovery_is_left_inverse": matmul(R, I) == [[F(1)]],
    "augmented_recovery_is_left_inverse": matmul(R_tilde, I_tilde) == identity3,
    "forcing_jet_is_retained": jet_recovered == jet_source and jet_source != [0, 0, 0],
    "forcing_jet_cannot_be_in_recovery_annihilated_auxiliary": jet_recovered != [0, 0, 0],
    "forgetful_recovery_would_not_recover_augmented_source": matvec([[F(1,2),F(1,2),0,0]], jet_target) == [0],
}
result = {
    "status": "pass" if all(checks.values()) else "fail",
    "arithmetic": "fractions.Fraction only",
    "checks": checks,
    "source_tangent": [str(x) for x in jet_source],
    "target_tangent": [str(x) for x in jet_target],
    "recovered_tangent": [str(x) for x in jet_recovered],
    "theorem": "If R_tilde I_tilde=Id, no nonzero retained source tangent can lie in an auxiliary subspace annihilated by R_tilde.",
}
out = Path("research/aspect/results/forcing_skew_product_recovery.json")
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["status"] == "pass" else 1)
