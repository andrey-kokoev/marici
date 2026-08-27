"""Exact scalar one-loop closure of the WP712 bosonic portal extension."""
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
n = sp.symbols("n1:4", real=True)
m = sp.symbols("m1:4", real=True)
chi = sp.symbols("chi", real=True)
ln, lm, lx, lc, lchi, gn, gm = sp.symbols(
    "lambda_n lambda_m lambda_x lambda_c lambda_chi g_n g_m", real=True
)
a = sum(v**2 for v in n)
b = sum(v**2 for v in m)
c = sum(n[i]*m[i] for i in range(3))
V4 = ln*a**2+lm*b**2+lx*a*b+lc*c**2+lchi*chi**4+gn*a*chi**2+gm*b*chi**2
fields = n+m+(chi,)
counterterm = sp.expand(sp.trace(sp.hessian(V4, fields)**2))
basis = [a**2, b**2, a*b, c**2, chi**4, a*chi**2, b*chi**2]
B = sp.symbols("B0:7")
remainder = sp.Poly(sp.expand(counterterm-sum(B[i]*basis[i] for i in range(7))), *fields)
solution = sp.solve(remainder.coeffs(), B, dict=True)[0]
derived = [sp.factor(solution[item]) for item in B]
expected = [
    4*gn**2+4*lc**2+8*lc*lx+176*ln**2+12*lx**2,
    4*gm**2+4*lc**2+8*lc*lx+176*lm**2+12*lx**2,
    8*gm*gn+8*lc**2+16*lc*(ln+lm)+80*lx*(ln+lm)+32*lx**2,
    lc*(40*lc+32*ln+32*lm+64*lx),
    12*gm**2+12*gn**2+144*lchi**2,
    8*gm*lc+24*gm*lx+32*gn**2+80*gn*ln+48*gn*lchi,
    32*gm**2+80*gm*lm+48*gm*lchi+8*gn*lc+24*gn*lx,
]

contrast = sp.factor((derived[0]-expected[0].subs(gn, 0))+(derived[1]-expected[1].subs(gm, 0))-(derived[2]-expected[2].subs({gn: 0, gm: 0})))

checks = {
    "seven_operator_basis_is_closed": all(sp.simplify(derived[i]-expected[i]) == 0 for i in range(7)),
    "no_counterterm_remainder": sp.expand(counterterm-sum(derived[i]*basis[i] for i in range(7))) == 0,
    "wp662_recovered_when_boson_decouples": all(sp.simplify(derived[i].subs({gn: 0, gm: 0, lchi: 0})-expected[i].subs({gn: 0, gm: 0, lchi: 0})) == 0 for i in range(4)),
    "bosonic_wp709_contrast_is_fixed": contrast == 4*(gm-gn)**2,
    "correlation_beta_gets_no_direct_boson_term": sp.diff(derived[3], gn) == 0 and sp.diff(derived[3], gm) == 0,
    "portal_beta_mixings_are_present": sp.diff(derived[5], gm) != 0 and sp.diff(derived[6], gn) != 0,
    "boson_self_beta_is_positive_sum": sp.simplify(derived[4]-12*(gm**2+gn**2+12*lchi**2)) == 0,
}
checks = {name: bool(value) for name, value in checks.items()}
if not all(checks.values()):
    raise SystemExit(checks)

result = {
    "work_package": "WP713",
    "status": "PASS",
    "checks": checks,
    "admitted_state_domain": "WP662 two-triplet scalar theory extended by one real Z2 portal boson and the complete seven-operator quartic basis",
    "faithful_coordinate": "all seven running scalar quartic and portal couplings",
    "source_authorized_operation": "the exact scalar one-loop Hessian-supertrace counterterm map in the WP662 normalization",
    "contextual_partition": "the full beta field retains all seven source coordinates; the radial contrast alone still collapses portal signs and allocations",
    "classification": "RG-closed scalar source extension and transport field; not yet a selector, rigidifier, or physical instrument",
    "smallest_exact_falsifier": "a generated scalar counterterm outside the seven-operator basis or any mismatch in the seven beta polynomials",
    "remaining_gate": "classify full projective rays and transverse basin, then add fermion/gauge running, thresholds, and a calibrated incidence-preserving readout",
}
(ROOT / "results" / "wp713_bosonic_portal_scalar_rg_closure.json").write_text(
    json.dumps(result, indent=2) + "\n", encoding="utf-8"
)
print(json.dumps(result, indent=2))
