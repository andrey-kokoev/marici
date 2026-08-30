"""Exact WP654 finite-width two-template overlap."""
import json
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
z, D, g = sp.symbols("z D g", positive=True, real=True)
f = g**2/sp.pi**2/((z**2+g**2)*((z-D)**2+g**2))
cross = sp.simplify(2*sp.pi*sp.I*(sp.residue(f, z, sp.I*g) + sp.residue(f, z, D+sp.I*g)))
self_overlap = sp.simplify(cross.subs(D, 0))
rho = sp.simplify(cross/self_overlap)
G = sp.Matrix([[1, rho], [rho, 1]])
sigma_min = sp.simplify(1-rho)
checks = {
    "cross_overlap_residue_formula": sp.simplify(cross-2*g/(sp.pi*(D**2+4*g**2))) == 0,
    "self_overlap_formula": self_overlap == 1/(2*sp.pi*g),
    "normalized_overlap_formula": sp.simplify(rho-4*g**2/(D**2+4*g**2)) == 0,
    "template_gram_determinant": sp.simplify(G.det()-(1-rho**2)) == 0,
    "smallest_eigenvalue_formula": sp.simplify(sigma_min-D**2/(D**2+4*g**2)) == 0,
    "nonzero_separation_has_rank_two": G.subs({D: 3, g: 1}).rank() == 2,
    "exact_degeneracy_has_rank_one": sp.simplify(G.subs(D, 0)).rank() == 1,
}
checks = {name: bool(value) for name, value in checks.items()}
if not all(checks.values()):
    raise SystemExit(checks)
result = {
    "work_package": "WP654", "status": "PASS", "checks": checks,
    "line_shape": "equal-width normalized Lorentzian templates",
    "normalized_overlap": "rho=4 gamma^2/(Delta^2+4 gamma^2)",
    "matched_filter_gram_determinant": "1-rho^2",
    "smallest_eigenvalue": "Delta^2/(Delta^2+4 gamma^2)",
    "conditioning_gate": "lambda_min >= epsilon requires Delta^2 >= 4 epsilon gamma^2/(1-epsilon)",
    "classification": "finite widths preserve two-port faithfulness away from exact degeneracy but can make it arbitrarily ill-conditioned",
    "smallest_exact_falsifier": "Delta=0, where the two normalized line-shape templates coincide",
    "remaining_experimental_gate": "detector resolution convolution, unequal widths, backgrounds, efficiencies, and calibrated uncertainty bounds",
}
(ROOT / "results" / "wp654_finite_width_template_overlap.json").write_text(json.dumps(result, indent=2)+"\n", encoding="utf-8")
print(json.dumps(result, indent=2))
