"""Exact first-order lifting of the symmetric cubic branch zero."""
import json
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
h, x = sp.symbols("h x", real=True)
lam, p, v = sp.symbols("lambda p v", positive=True)
delta = sp.symbols("delta", real=True)
rt2 = sp.sqrt(2)
fields = (h, x)

def potential(portal):
    muh2 = (lam + delta + portal) * v**2
    mux2 = (lam - delta + portal) * v**2
    return (
        -muh2*h**2/2 - mux2*x**2/2
        +(lam+delta)*h**4/4 +(lam-delta)*x**4/4
        +portal*h**2*x**2/2
    )

def cubic(V, a, b, c):
    return sp.expand(sum(
        a[i]*b[j]*c[k]*sp.diff(V, fields[i], fields[j], fields[k]).subs({h: v, x: v})
        for i in range(2) for j in range(2) for k in range(2)
    ))

Hp0 = sp.Matrix([1, 1])/rt2
Lp0 = sp.Matrix([1, -1])/rt2
Hm0 = sp.Matrix([1, -1])/rt2
Lm0 = sp.Matrix([1, 1])/rt2

# Nondegenerate eigenvector perturbation through first order in delta.
Hp = Hp0 + delta*Lp0/(2*p)
Lp = Lp0 - delta*Hp0/(2*p)
Hm = Hm0 + delta*Lm0/(2*p)
Lm = Lm0 - delta*Hm0/(2*p)

gp = cubic(potential(p), Hp, Lp, Lp)
gm = cubic(potential(-p), Hm, Lm, Lm)
gp0 = sp.simplify(gp.subs(delta, 0))
gm0 = sp.simplify(gm.subs(delta, 0))
dgp = sp.factor(sp.diff(gp, delta).subs(delta, 0))
dgm = sp.factor(sp.diff(gm, delta).subs(delta, 0))

Mplus = 2*v**2*sp.Matrix([[lam+delta, p], [p, lam-delta]])
Mminus = 2*v**2*sp.Matrix([[lam+delta, -p], [-p, lam-delta]])

checks = {
    "source_hessians_remain_isospectral": sp.simplify(Mplus.charpoly().as_expr()-Mminus.charpoly().as_expr()) == 0,
    "positive_branch_symmetric_value": gp0 == rt2*v*(3*lam-p),
    "negative_branch_symmetric_zero": gm0 == 0,
    "positive_branch_has_no_linear_asymmetry": dgp == 0,
    "negative_branch_is_lifted_linearly": sp.simplify(dgm + rt2*v*(3*lam-p)/(2*p)) == 0,
    "eigenvector_equations_hold_through_first_order_plus": all(sp.expand(value).coeff(delta, n) == 0 for value in (Mplus*Hp-2*v**2*(lam+p)*Hp) for n in (0, 1)),
    "eigenvector_equations_hold_through_first_order_minus": all(sp.expand(value).coeff(delta, n) == 0 for value in (Mminus*Hm-2*v**2*(lam+p)*Hm) for n in (0, 1)),
}
checks = {name: bool(value) for name, value in checks.items()}
if not all(checks.values()):
    raise SystemExit(checks)

result = {
    "work_package": "WP697",
    "status": "PASS",
    "checks": checks,
    "admitted_state_domain": "equal vacuum norms with quartic asymmetry lambda_h=lambda+delta, lambda_x=lambda-delta and portal branches plus or minus p",
    "two_point_result": "the two branches remain exactly isospectral for every delta",
    "positive_branch_expansion": "g_HLL plus=sqrt(2) v(3lambda-p)+O(delta^2)",
    "negative_branch_expansion": "g_HLL minus=-sqrt(2) v(3lambda-p) delta/(2p)+O(delta^2)",
    "classification": "the exact negative-branch zero is a symmetry-slice rigidification, while the branch hierarchy is perturbatively robust; identifier, not selector",
    "smallest_exact_falsifier": "any nonzero quartic asymmetry generically lifts the negative-branch tree-level zero at first order",
    "remaining_gate": "derive a nonasymptotic finite-asymmetry rate margin and include the other full flavor orientation invariants, loops, widths, and calibrated detector response",
}
(ROOT / "results" / "wp697_asymmetric_cubic_lifting.json").write_text(
    json.dumps(result, indent=2) + "\n", encoding="utf-8"
)
print(json.dumps(result, indent=2))
