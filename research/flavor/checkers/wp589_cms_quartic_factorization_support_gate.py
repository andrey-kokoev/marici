"""Exact WP589 factorization-versus-support audit for the CMS HHH quartic row."""

import json
from pathlib import Path

import sympy as sp

z, lambda_s, lambda_h = sp.symbols(
    "z lambda_s lambda_H", nonnegative=True, real=True
)

kappa_t_sq = 1 - z
q = lambda_s * z**2 / lambda_h
kappa_4 = 1 + q
source_map = sp.Matrix([kappa_t_sq, kappa_4])
source_jacobian = source_map.jacobian([z, lambda_s])

projection = sp.Matrix([[1, 0, 0], [0, 1, 0]])
lift_kernel = sp.Matrix([0, 0, 1])
cms_quartic_row = sp.Matrix([[0, 1, 0]])

cms_slice = {z: 0}
restricted_jacobian = sp.simplify(source_jacobian.subs(cms_slice))
restricted_quartic_lambda_response = sp.diff(kappa_4, lambda_s).subs(cms_slice)

checks = {
    "cms_quartic_row_annihilates_lift_kernel": cms_quartic_row * lift_kernel
    == sp.zeros(1, 1),
    "cms_quartic_row_factors_through_known_projection": cms_quartic_row
    == sp.Matrix([[0, 1]]) * projection,
    "cms_kappa_t_one_slice_forces_z_zero": sp.solve(
        sp.Eq(kappa_t_sq, 1), z
    )
    == [0],
    "quartic_lambda_response_vanishes_on_cms_slice": restricted_quartic_lambda_response
    == 0,
    "combined_source_rank_on_cms_slice_is_one": restricted_jacobian.rank() == 1,
    "source_sensitive_domain_has_empty_cms_overlap": sp.reduce_inequalities(
        [sp.StrictGreaterThan(z, 0), sp.Eq(z, 0)], z
    )
    is sp.false,
}

if not all(checks.values()):
    raise SystemExit(f"WP589 check failed: {checks}")

checks = {key: bool(value) for key, value in checks.items()}
result = {
    "work_package": "WP589",
    "status": "PASS",
    "checks": checks,
    "detector_factorization_gate": "passes algebraically for a pure kappa_4 row",
    "source_support_gate": "fails because the released kappa_t=1 slice pulls back to z=0",
    "restricted_source_jacobian": [
        [sp.sstr(value) for value in restricted_jacobian.row(i)]
        for i in range(restricted_jacobian.rows)
    ],
    "restricted_rank": 1,
    "contextual_partition": "on the admitted CMS-source intersection, lambda_s remains invisible and q is fixed to zero",
    "classification": "physical quartic readout on an incompatible slice; neither selector nor rigidifier",
    "smallest_exact_falsifier": "kappa_t=1 implies z=0 and partial kappa_4/partial lambda_s=z^2/lambda_H=0",
    "remaining_gate": "publish the factorized calibrated quartic response on a nonzero-mixing domain, or publish the complete omitted-coordinate tangent and detector transport there",
}

out = Path(__file__).resolve().parents[1] / "results" / "wp589_cms_quartic_factorization_support_gate.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
