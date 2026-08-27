"""Exact stable mixed-vacuum test for the minimal radial Higgs-exit portal."""
import json
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
h, x = sp.symbols("h x", real=True)
muh2, mux2 = sp.symbols("mu_h2 mu_x2", real=True)
lh, lx, lp = sp.symbols("lambda_h lambda_x lambda_p", real=True)

V = -muh2*h**2/2-mux2*x**2/2+lh*h**4/4+lx*x**4/4+lp*h**2*x**2/2
stationarity = sp.Matrix([sp.diff(V, h)/h, sp.diff(V, x)/x]).applyfunc(sp.simplify)
solution = sp.simplify(sp.Matrix([[lh, lp], [lp, lx]]).inv()*sp.Matrix([muh2, mux2]))
h2sol, x2sol = solution
H = sp.hessian(V, (h, x))
Hvac = sp.simplify(H.subs({muh2: lh*h**2+lp*x**2, mux2: lp*h**2+lx*x**2}))

witness = {lh: 2, lx: 3, lp: 1, muh2: 3, mux2: 4}
zero_portal = sp.simplify(Hvac[0, 1].subs(lp, 0))

checks = {
    "nonzero_stationarity_is_linear_in_squared_vevs": stationarity == sp.Matrix([-muh2+lh*h**2+lp*x**2, -mux2+lp*h**2+lx*x**2]),
    "mixed_vacuum_solution_exact": h2sol == (lx*muh2-lp*mux2)/(lh*lx-lp**2) and x2sol == (lh*mux2-lp*muh2)/(lh*lx-lp**2),
    "radial_hessian_at_vacuum": Hvac == sp.Matrix([[2*lh*h**2, 2*lp*h*x], [2*lp*h*x, 2*lx*x**2]]),
    "radial_hessian_determinant": sp.factor(Hvac.det()) == 4*h**2*x**2*(lh*lx-lp**2),
    "stable_nonzero_mixed_witness": h2sol.subs(witness) == 1 and x2sol.subs(witness) == 1 and (lh*lx-lp**2).subs(witness) == 5,
    "zero_portal_is_allowed_and_unmixed": zero_portal == 0,
}
checks = {name: bool(value) for name, value in checks.items()}
if not all(checks.values()):
    raise SystemExit(checks)

result = {
    "work_package": "WP685",
    "status": "PASS",
    "checks": checks,
    "declared_candidate_domain": "minimal O(N)-radial truncation in h and the exit-flavon norm x; orientation-dependent quartics are intentionally excluded",
    "potential": "-mu_h^2 h^2/2-mu_x^2 x^2/2+lambda_h h^4/4+lambda_x x^4/4+lambda_p h^2 x^2/2",
    "stable_mixed_condition": "h^2>0, x^2>0, lambda_h>0, lambda_x>0, lambda_h lambda_x-lambda_p^2>0",
    "exact_witness": "lambda_h=2, lambda_x=3, lambda_p=1, mu_h^2=3, mu_x^2=4 gives h^2=x^2=1 and positive Hessian determinant 20",
    "mixing_entry": "2 lambda_p h x",
    "selection_result": "a stable nonzero portal exists on an open source domain, but lambda_p=0 is equally legal and leaves the reference absent",
    "classification": "existence constructor, not a selector and not a completion-safe full scalar potential",
    "smallest_exact_falsifier": "lambda_p=0 makes radial Higgs-exit mixing exactly zero while preserving two independent stable vacua",
    "remaining_gate": "derive orientation-dependent invariants and RG/threshold completion, or a source principle that excludes the zero-portal stratum",
}
(ROOT / "results" / "wp685_radial_portal_vacuum.json").write_text(
    json.dumps(result, indent=2)+"\n", encoding="utf-8")
print(json.dumps(result, indent=2))
