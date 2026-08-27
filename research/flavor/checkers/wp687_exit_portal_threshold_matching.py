"""Exact heavy-eigenvalue threshold term for the radiative exit-Higgs portal."""
import json
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
H, X = sp.symbols("H X", nonnegative=True)
A, C, M, mu = sp.symbols("A C M mu", positive=True)
Nc = sp.symbols("N_c", positive=True, integer=True)

trace = M**2+A*H+C*X
disc = sp.sqrt(trace**2-4*A*H*M**2)
heavy = (trace+disc)/2
heavy_hx = sp.simplify(sp.diff(heavy, H, X).subs({H: 0, X: 0}))
f_heavy = heavy**2*(sp.log(heavy/mu**2)-sp.Rational(3, 2))
f_hx = sp.factor(sp.diff(f_heavy, H, X).subs({H: 0, X: 0}))
f_hx_canonical = sp.expand_log(f_hx, force=True)

# One Dirac fermion per color: V1=-Nc f/(16 pi^2). The potential convention
# is V contains lambda_p H X/2, so delta lambda_p is twice the HX coefficient.
delta_lambda = sp.factor(-Nc*f_hx_canonical/(8*sp.pi**2))
matched = sp.simplify(delta_lambda.subs(mu, M))

checks = {
    "heavy_eigenvalue_has_mixed_threshold_curvature": heavy_hx == A*C/M**2,
    "msbar_heavy_function_mixed_coefficient": sp.simplify(f_hx_canonical-2*A*C*(2*sp.log(M)-2*sp.log(mu)-1)) == 0,
    "portal_threshold_in_declared_convention": sp.simplify(delta_lambda+Nc*A*C*(2*sp.log(M)-2*sp.log(mu)-1)/(4*sp.pi**2)) == 0,
    "matching_at_heavy_scale_is_positive": matched == Nc*A*C/(4*sp.pi**2),
    "three_color_value": matched.subs(Nc, 3) == 3*A*C/(4*sp.pi**2),
}
checks = {name: bool(value) for name, value in checks.items()}
if not all(checks.values()):
    raise SystemExit(checks)

result = {
    "work_package": "WP687",
    "status": "PASS",
    "checks": checks,
    "domain": "one Dirac exit-messenger block, constant real radial backgrounds, MSbar one-loop Coleman-Weinberg matching, no orientation quartics",
    "mass_matrix_invariant": "Tr=M_B^2+y_q^2 h^2+y_X^2 x^2, det=y_q^2 h^2 M_B^2",
    "heavy_mixed_curvature": "d_H d_X lambda_heavy=y_q^2 y_X^2/M_B^2",
    "threshold_general_scale": "delta lambda_p=-N_c y_q^2 y_X^2[log(M_B^2/mu^2)-1]/(4 pi^2) for V containing lambda_p h^2 x^2/2",
    "threshold_at_matching_scale": "delta lambda_p=N_c y_q^2 y_X^2/(4 pi^2)>0",
    "classification": "source-derived finite threshold contribution in a declared scheme; not a total portal prediction",
    "smallest_exact_falsifier": "y_q=0 or y_X=0 removes the threshold",
    "remaining_gate": "add the independent UV boundary coupling, all messenger generations and orientation invariants, then transport to a calibrated interference scale",
}
(ROOT / "results" / "wp687_exit_portal_threshold_matching.json").write_text(
    json.dumps(result, indent=2)+"\n", encoding="utf-8")
print(json.dumps(result, indent=2))
