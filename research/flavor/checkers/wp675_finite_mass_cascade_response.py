"""Exact finite-mass response rank for the protected cascade polarimeter."""
import json
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
u, v = sp.symbols("u v", positive=True)
MA, MB, mn = sp.symbols("MA MB mn", positive=True)
A = MA**2+MB**2-mn**2
C = 4*MA*MB
Lambda = (MA**2-(MB+mn)**2)*(MA**2-(MB-mn)**2)
L = sp.sqrt(Lambda)
W = A*(u+v)+C*sp.sqrt(u*v)
N = L*(u-v)
J = sp.Matrix([W, N]).jacobian([u, v])
expected_det = -L*(2*A+C*(sp.sqrt(v/u)+sp.sqrt(u/v))/2)

witness = {MA: 5, MB: 3, mn: 1, u: 1, v: 1}
threshold = {MA: 4, MB: 3, mn: 1}
polarization = sp.simplify(N/W)

checks = {
    "finite_mass_jacobian_determinant": sp.simplify(J.det()-expected_det) == 0,
    "positive_threshold_witness": Lambda.subs(witness) == 189,
    "witness_response_is_rank_two": J.det().subs(witness) == -378*sp.sqrt(21),
    "exact_threshold_collapses_signed_port": L.subs(threshold) == 0 and J.det().subs(threshold) == 0,
    "massless_limit_recovers_ideal_polarization": sp.simplify(polarization.subs({MB: 0, mn: 0})-(u-v)/(u+v)) == 0,
    "finite_mass_interference_does_not_force_collapse": J.det().subs(witness) != 0,
}
checks = {name: bool(value) for name, value in checks.items()}
if not all(checks.values()):
    raise SystemExit(checks)

result = {
    "work_package": "WP675", "status": "PASS", "checks": checks,
    "domain": "real positive reciprocal vertices, unpolarized parent, narrow-width cascade, massless exit quark with purely chiral exit",
    "rate_kernel": "W=A(u+v)+4M_A M_B sqrt(uv), A=M_A^2+M_B^2-m_n^2",
    "signed_kernel": "N=sqrt(Kallen)(u-v)",
    "jacobian_determinant": "-sqrt(Kallen)[2A+2M_A M_B(sqrt(v/u)+sqrt(u/v))]",
    "witness": "(M_A,M_B,m_n,u,v)=(5,3,1,1,1), det=-378sqrt(21)",
    "classification": "finite masses preserve local rank two everywhere inside this positive real slice; exact parent threshold collapses the angular port",
    "smallest_exact_falsifier": "Kallen=0 at M_A=M_B+m_n",
    "remaining_gate": "complex relative phase, finite widths, off-shell transport, X reconstruction, and detector calibration",
}
(ROOT / "results" / "wp675_finite_mass_cascade_response.json").write_text(
    json.dumps(result, indent=2)+"\n", encoding="utf-8")
print(json.dumps(result, indent=2))
