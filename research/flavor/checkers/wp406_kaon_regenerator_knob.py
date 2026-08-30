"""Exact neutral-kaon regenerator construction for WP406."""

import json
from pathlib import Path

import sympy as sp


n, tau = sp.symbols("n tau", real=True)
a, b, qre, qim = sp.symbols("a b qre qim", real=True)
lam_l, lam_s = sp.symbols("lambda_L lambda_S")

# A single material density controls both parts of the forward-scattering
# difference.  qre and qim type the first unadmitted nonlinear source terms.
rho = n * (a + sp.I * b) + n**2 * (qre + sp.I * qim)
mu = (lam_l + lam_s) / 2
delta = (lam_l - lam_s) / 2
Omega = sp.sqrt(delta**2 + rho**2)
amplitude = -sp.I * sp.exp(-sp.I * mu * tau) * rho * sp.sin(Omega * tau) / Omega

affine_rho = rho.subs({qre: 0, qim: 0})
source_shift = sp.Matrix([sp.re(affine_rho), sp.im(affine_rho)])
same_knob_tangent = source_shift.jacobian([n])
calibration_jacobian = source_shift.jacobian([a, b])

# Vacuum plus n=1,2 determines each quadratic response coefficient.  A frozen
# affine law has zero quadratic coefficients and makes n=3 genuinely withheld.
design = sp.Matrix([[0, 0, 1], [1, 1, 1], [2, 4, 1]])

benchmark = {
    a: sp.Rational(1, 2),
    b: sp.Rational(1, 4),
    qre: 0,
    qim: 0,
    lam_l: 1 - sp.I * sp.Rational(1, 10),
    lam_s: 3 - sp.I * sp.Rational(1, 2),
    tau: sp.Rational(1, 3),
}
withheld = sp.simplify(amplitude.subs(benchmark | {n: 3}))
deletion = sp.simplify(amplitude.subs({a: 0, b: 0, qre: 0, qim: 0}))

# A second material species is an explicit extra source direction, not an
# after-the-fact correction to the one-material law.
n2, a2, b2 = sp.symbols("n2 a2 b2", real=True)
two_material_shift = sp.Matrix([n * a + n2 * a2, n * b + n2 * b2])
two_material_jacobian = two_material_shift.jacobian([n, n2])
two_material_det = sp.factor(two_material_jacobian.det())

checks = {
    "same_density_knob_moves_dispersive_part": same_knob_tangent.subs({a: 1, b: 1})[0] != 0,
    "same_density_knob_moves_absorptive_part": same_knob_tangent.subs({a: 1, b: 1})[1] != 0,
    "phase_attenuation_calibration_rank_two": calibration_jacobian.subs(n, 1).rank() == 2,
    "quadratic_completion_identifiable_at_zero_one_two": design.det() != 0,
    "finite_widths_present_in_transfer_law": sp.diff(amplitude, lam_l) != 0 and sp.diff(amplitude, lam_s) != 0,
    "zero_forward_difference_deletes_regeneration": deletion == 0,
    "finite_thickness_law_is_nonlinear": sp.diff(amplitude.subs({qre: 0, qim: 0}), n, 3) != 0,
    "extra_material_is_separable_when_noncollinear": two_material_det == a * b2 - a2 * b,
    "withheld_amplitude_is_fixed": not withheld.has(a, b, qre, qim, lam_l, lam_s, tau, n),
}

result = {
    "work_package": "WP406",
    "title": "Executable neutral-kaon regenerator knob",
    "real_flavor_carrier": "the physical K0--anti-K0 doublet",
    "executable_knob": "regenerator material column density n*tau at frozen momentum and composition",
    "source_shifts": {
        "dispersive": "n*a",
        "absorptive": "n*b",
        "common_source": "the complex forward-scattering difference a+i*b",
    },
    "exact_transfer_amplitude": str(amplitude),
    "calibration_jacobian_at_unit_density": [
        [str(x) for x in row] for row in calibration_jacobian.subs(n, 1).tolist()
    ],
    "quadratic_design_determinant": str(design.det()),
    "extra_material_rank_determinant": str(two_material_det),
    "withheld_context": "n=3, tau=1/3 in the frozen benchmark",
    "withheld_displacement_amplitude": str(withheld),
    "classification": "real relational flavor intervention and rigidified transfer prediction; not a physical16 selector",
    "remaining_gate": "bind published phase and attenuation records to one composition/momentum calibration and execute the reserved density without refitting",
    "checks": checks,
    "passed": all(checks.values()),
}

if not result["passed"]:
    raise SystemExit("WP406 exact checks failed")

out = Path(__file__).parents[1] / "results" / "wp406_kaon_regenerator_knob.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
