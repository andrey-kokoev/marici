"""Exact Salam-Sezgin chirality, scale, and family-index audit."""
import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
wp790 = json.loads(
    (ROOT / "results" / "wp790_curvature_flux_radion_magnitude_selector.json")
    .read_text(encoding="utf-8")
)

g, phi0, rho = sp.symbols("g phi0 rho", positive=True, real=True)
charge = sp.symbols("charge", integer=True)

# With F=(1/(2g))*Omega_2 and integral Omega_2=4*pi, the Chern number
# seen by the minimally charged fermions is one.
flux_integral = sp.Rational(1, 2) / g * 4 * sp.pi
chern_number = sp.simplify(g * flux_integral / (2 * sp.pi))
mirror_chern_number = -chern_number

sigma3 = sp.diag(1, -1)
eta_plus = sp.Matrix([1, 0])
plus_bps_residual = (sigma3 - sp.eye(2)) * eta_plus
minus_bps_residual = (sigma3 + sp.eye(2)) * eta_plus

# Physical four-dimensional KK scale identified by the consistent reduction.
M_K = g * sp.exp(phi0 / 2)
scale_response = sp.diff(M_K, phi0)
scaling_redundancy = sp.simplify(
    M_K.subs(
        {g: rho * g, phi0: phi0 - 2 * sp.log(rho)}, simultaneous=True
    )
    - M_K
)

# The retained four-dimensional scalar is massless at the supersymmetric
# vacuum, so its constant mode has no classical selector.
V_phi = sp.Integer(0)
phi_force = sp.diff(V_phi, phi0)
phi_hessian = sp.diff(V_phi, phi0, 2)

index = sp.expand(charge * chern_number)
index_one = index.subs(charge, 1)
index_three = index.subs(charge, 3)

checks = {
    "wp790_dependency_passed": wp790["status"] == "PASS"
    and all(wp790["checks"].values()),
    "minimal_monopole_has_unit_chern_number": chern_number == 1,
    "orientation_reversal_has_minus_unit_chern_number":
        mirror_chern_number == -1,
    "positive_internal_chirality_solves_bps_projector":
        plus_bps_residual == sp.zeros(2, 1),
    "same_admitted_spinor_rejects_mirror_projector":
        minus_bps_residual != sp.zeros(2, 1),
    "kk_scale_depends_on_dilaton_zero_mode": scale_response == M_K / 2,
    "coupling_dilaton_reparameterization_preserves_physical_scale":
        scaling_redundancy == 0,
    "retained_scalar_has_zero_classical_force": phi_force == 0,
    "retained_scalar_has_zero_classical_hessian": phi_hessian == 0,
    "unit_monopole_index_equals_integer_matter_charge": index == charge,
    "one_and_three_family_indices_are_both_allowed": (index_one, index_three)
    == (1, 3),
}
checks = {name: bool(value) for name, value in checks.items()}
if not all(checks.values()):
    raise SystemExit(checks)

result = {
    "work_package": "WP791",
    "status": "PASS",
    "checks": checks,
    "dependency": "WP790",
    "admitted_state_domain": (
        "the supersymmetric Salam-Sezgin Minkowski_4 x S^2 unit-monopole "
        "reduction, fixed six-dimensional N=(1,0) chirality, the retained "
        "dilaton/breathing zero mode phi0, gauge coupling g, and integer matter "
        "charges"
    ),
    "faithful_coordinate": (
        "oriented Chern number, internal spinor chirality, physical KK scale "
        "g*exp(phi0/2), and charged Dirac index"
    ),
    "source_authorized_probe_family": (
        "Dirac quantization, the supersymmetry projector, the exact consistent "
        "S^2 reduction, and the index pairing between unit flux and integer "
        "matter charge"
    ),
    "contextual_partition": (
        "fixed N=(1,0) chirality excludes the mirror monopole from the same BPS "
        "sector, but all dilaton zero modes and all admitted integer matter "
        "charges remain distinct source states"
    ),
    "selector_result": (
        "Salam-Sezgin is a genuine relative flux-orientation selector, "
        "gauge-gravity parallelizer, and Minkowski reduction; it is not an "
        "absolute-scale or three-family selector"
    ),
    "smallest_exact_falsifier": (
        "at the same unit BPS monopole, matter charges one and three give "
        "indices one and three; at fixed g, two phi0 values give different KK "
        "scales while both remain classical vacua"
    ),
    "sign_result": (
        "the unit monopole sign is fixed relative to the admitted positive "
        "six-dimensional chirality; the fully mirror theory would require the "
        "opposite chiral source, so this is relational rather than absolute"
    ),
    "magnitude_result": (
        "supersymmetry fixes curvature and flux coefficients, but the physical "
        "scale g*exp(phi0/2) varies along the retained massless scalar"
    ),
    "family_result": (
        "unit flux yields three zero modes only after choosing matter charge "
        "three; the source theory has not yet derived that charge"
    ),
    "rg_threshold_result": (
        "consistent reduction supplies exact classical threshold transport, "
        "but the massless scalar prevents a strict basin and the full quantum "
        "RG/KK threshold completion is absent"
    ),
    "instrument_result": (
        "the four-dimensional massless sector contains supergravity, an SU(2) "
        "vector multiplet, and a scalar multiplet, not a calibrated physical16 "
        "flavor instrument"
    ),
    "deutschian_status": (
        "chiral gauged supergravity explains why one relative flux orientation "
        "and Minkowski reduction coexist, but three families and the physical "
        "scale remain easy to vary"
    ),
    "remaining_gate": (
        "derive charge three and lift the dilaton zero mode from the anomaly-"
        "complete chiral matter packet without breaking the BPS orientation or "
        "consistent reduction, then construct its flavor threshold and signed "
        "detector channels"
    ),
    "primary_sources": [
        "https://arxiv.org/abs/hep-th/0307052",
        "https://arxiv.org/abs/hep-th/0306201",
        "https://arxiv.org/abs/1204.1060",
    ],
}
(ROOT / "results" / "wp791_salam_sezgin_chirality_scale_charge_fiber.json").write_text(
    json.dumps(result, indent=2) + "\n", encoding="utf-8"
)
print(json.dumps(result, indent=2))
