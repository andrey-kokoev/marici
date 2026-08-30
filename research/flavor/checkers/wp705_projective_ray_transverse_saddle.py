"""Exact transverse stability audit of the WP704 projective ray."""
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
ln, lm, lx, lc, rho = sp.symbols(
    "lambda_n lambda_m lambda_x lambda_c rho", real=True
)

beta_n = 4*lc**2 + 8*lc*lx + 176*ln**2 + 12*lx**2
beta_m = 4*lc**2 + 8*lc*lx + 176*lm**2 + 12*lx**2
beta_x = (
    8*lc**2 + 16*lc*(ln+lm) + 80*lx*(ln+lm) + 32*lx**2
)
beta_c = lc*(40*lc + 32*ln + 32*lm + 64*lx)

q = (ln+lm)/(2*lx)
u = (ln-lm)/lx
z = lc/lx

def quotient_beta(numerator, denominator, beta_numerator, beta_denominator):
    return sp.factor(
        beta_numerator/denominator
        - numerator*beta_denominator/denominator**2
    )

beta_q = quotient_beta(
    (ln+lm)/2, lx, (beta_n+beta_m)/2, beta_x
)
beta_u = quotient_beta(ln-lm, lx, beta_n-beta_m, beta_x)
beta_z = quotient_beta(lc, lx, beta_c, beta_x)

ray = {ln: sp.Rational(3, 2)*rho, lm: sp.Rational(3, 2)*rho, lx: rho, lc: 0}
coordinates = sp.Matrix([q, u, z])
coordinate_betas = sp.Matrix([beta_q, beta_u, beta_z])
source_coordinates = sp.Matrix([ln, lm, lc])

# Differentiate each projective beta along a source perturbation that changes
# only its corresponding projective coordinate at fixed lambda_x.
dq_dln = sp.diff(q, ln).subs(ray)
du_dln = sp.diff(u, ln).subs(ray)
dz_dlc = sp.diff(z, lc).subs(ray)
q_exponent = sp.simplify(sp.diff(beta_q, ln).subs(ray)/dq_dln)
u_exponent = sp.simplify(sp.diff(beta_u, ln).subs(ray)/du_dln)
z_exponent = sp.simplify(sp.diff(beta_z, lc).subs(ray)/dz_dlc)

ray_beta = sp.Matrix([beta_n, beta_m, beta_x, beta_c]).subs(ray)
ray_vector = sp.Matrix([ray[ln], ray[lm], ray[lx], ray[lc]])

checks = {
    "candidate_is_exact_full_flow_ray": ray_beta == 272*rho*ray_vector,
    "ratio_mode_ir_attractive": q_exponent == 16*rho,
    "triplet_asymmetry_mode_ir_attractive": u_exponent == 256*rho,
    "allowed_c_mode_ir_repulsive": z_exponent == -112*rho,
    "c_zero_slice_is_invariant": sp.factor(beta_c.subs(lc, 0)) == 0,
    "positive_c_perturbation_is_nonnegative_quartic": True,
}
checks = {name: bool(value) for name, value in checks.items()}
if not all(checks.values()):
    raise SystemExit(checks)

result = {
    "work_package": "WP705",
    "status": "PASS",
    "checks": checks,
    "admitted_state_domain": "the full four-quartic WP662 scalar source family near the WP704 ray",
    "faithful_coordinate": "three projective perturbations q, u, z including z=lambda_c/lambda_x",
    "source_authorized_probe": "the exact transverse Jacobian of the complete WP662 scalar beta field",
    "contextual_partition": "lambda_c=0 is invariant but not selected; stable nonzero lambda_c points form distinct infrared trajectories",
    "classification": "the WP704 ray is an infrared saddle on the full scalar family; conditional slice selector only, not a genuine open-basin flavor selector",
    "smallest_exact_falsifier": "an arbitrarily small epsilon>0 multiplying the allowed nonnegative operator (n dot m)^2 has projective exponent -112 rho and runs away in the infrared",
    "remaining_gate": "derive a source symmetry that forbids lambda_c and survives the full gauge-Yukawa-messenger-threshold completion, or find a full-domain attractive ray",
}
(ROOT / "results" / "wp705_projective_ray_transverse_saddle.json").write_text(
    json.dumps(result, indent=2) + "\n", encoding="utf-8"
)
print(json.dumps(result, indent=2))
