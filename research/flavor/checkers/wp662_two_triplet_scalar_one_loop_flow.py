"""Exact scalar one-loop flow for the closed two-triplet potential."""
import json
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
x = sp.symbols("x0:6", real=True)
rn, rm, ln, lm, lx, lc = sp.symbols("rn rm ln lm lx lc", real=True)
n, m = sp.Matrix(x[:3]), sp.Matrix(x[3:])
a, b, c = n.dot(n), m.dot(m), n.dot(m)
V = -rn*a-rm*b+ln*a**2+lm*b**2+lx*a*b+lc*c**2
divergence = sp.expand(sp.trace(sp.hessian(V, x)**2))

beta_ln = 4*lc**2+8*lc*lx+176*ln**2+12*lx**2
beta_lm = 4*lc**2+8*lc*lx+176*lm**2+12*lx**2
beta_lx = 8*lc**2+16*lc*(lm+ln)+80*lx*(lm+ln)+32*lx**2
beta_lc = lc*(40*lc+32*lm+32*ln+64*lx)
beta_rn = 80*ln*rn+(8*lc+24*lx)*rm
beta_rm = 80*lm*rm+(8*lc+24*lx)*rn
expected = (12*rn**2+12*rm**2-beta_rn*a-beta_rm*b
            +beta_ln*a**2+beta_lm*b**2+beta_lx*a*b+beta_lc*c**2)

benchmark = {rn: 2, rm: 2, ln: 1, lm: 1, lx: 1, lc: 1}
quartic_flow = [sp.expand(z.subs(benchmark)) for z in
                [beta_ln, beta_lm, beta_lx, beta_lc]]
mass_flow = [sp.expand(z.subs(benchmark)) for z in [beta_rn, beta_rm]]
det_radial = 4*ln*lm-lx**2
beta_det = sp.diff(det_radial, ln)*beta_ln+sp.diff(det_radial, lm)*beta_lm+sp.diff(det_radial, lx)*beta_lx
symmetric_norm = rn/(2*ln+lx)
beta_norm = sum(sp.diff(symmetric_norm, z)*bz for z, bz in
                [(rn, beta_rn), (ln, beta_ln), (lx, beta_lx)])

checks = {
    "complete_scalar_support_identity": sp.simplify(divergence-expected) == 0,
    "quartic_flow_at_benchmark": quartic_flow == [200, 200, 232, 168],
    "mass_flow_at_benchmark": mass_flow == [224, 224],
    "orthogonality_coupling_positive_forward": sp.factor(beta_lc/lc).subs(benchmark) == 168,
    "radial_determinant_positive_and_increasing": det_radial.subs(benchmark) == 3 and beta_det.subs(benchmark) == 1136,
    "vacuum_norm_flow_is_finite": beta_norm.subs(benchmark) == -sp.Rational(592, 9),
}
checks = {name: bool(value) for name, value in checks.items()}
if not all(checks.values()):
    raise SystemExit(checks)

result = {
    "work_package": "WP662", "status": "PASS", "checks": checks,
    "normalization": "common positive one-loop factor omitted; beta coefficients are those of Tr(Hess V)^2",
    "parameter_order": ["rn", "rm", "ln", "lm", "lx", "lc"],
    "benchmark_flow": {"masses": ["224", "224"], "quartics": ["200", "200", "232", "168"]},
    "benchmark_radial_determinant": "3",
    "benchmark_radial_determinant_flow": "1136",
    "benchmark_vacuum_norm_flow": "-592/9",
    "classification": "the repaired faithful frame is locally stable under the complete scalar one-loop flow, not yet under messenger-complete RG flow",
    "smallest_exact_falsifier": "a generated scalar operator outside the two masses and four quartics, or nonpositive radial determinant under an infinitesimal forward step",
    "remaining_gate": "add messenger, gauge, and Yukawa contributions and test the completed flow on a finite scale interval",
}
(ROOT / "results" / "wp662_two_triplet_scalar_one_loop_flow.json").write_text(
    json.dumps(result, indent=2)+"\n", encoding="utf-8")
print(json.dumps(result, indent=2))
