"""Exact SU(4) cubic-orientation and portal-fiber audit."""
import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
wp786 = json.loads(
    (ROOT / "results" / "wp786_mirror_completion_sign_selection_no_go.json")
    .read_text(encoding="utf-8")
)

kappa, lam, a, eta, rho = sp.symbols(
    "kappa lambda a eta rho", nonzero=True, real=True
)
T = sp.diag(1, 1, 1, -3)

tr2 = sp.trace(T**2)
tr3 = sp.trace(T**3)
tr4 = sp.trace(T**4)

# Scale-invariant ray potential at vanishing relevant mass.
V = sp.expand(kappa * sp.trace((a * T) ** 3) / 3 + lam * sp.trace((a * T) ** 2) ** 2 / 4)
dV = sp.factor(sp.diff(V, a))
a_star = sp.simplify(kappa / (6 * lam))
V_star = sp.simplify(V.subs(a, a_star))
ray_hessian = sp.simplify(sp.diff(V, a, 2).subs(a, a_star))

def tr(matrix):
    return sp.simplify(sp.trace(matrix))

def hessian_on(X):
    """Second variation at Phi=a_star*T for Tr(X^2)=1."""
    Phi = a_star * T
    S0 = tr(Phi**2)
    return sp.simplify(
        2 * kappa * tr(Phi * X**2)
        + lam * (S0 * tr(X**2) + 2 * tr(Phi * X) ** 2)
    )

sqrt2 = sp.sqrt(2)
basis_unbroken = []
basis_broken = []
for i in range(4):
    for j in range(i + 1, 4):
        S = sp.zeros(4)
        S[i, j] = S[j, i] = 1 / sqrt2
        A = sp.zeros(4)
        A[i, j] = -sp.I / sqrt2
        A[j, i] = sp.I / sqrt2
        (basis_unbroken if j < 3 else basis_broken).extend([S, A])

basis_unbroken.extend(
    [
        sp.diag(1, -1, 0, 0) / sqrt2,
        sp.diag(1, 1, -2, 0) / sp.sqrt(6),
    ]
)
radial = T / sp.sqrt(12)

unbroken_hessians = [hessian_on(X) for X in basis_unbroken]
broken_hessians = [hessian_on(X) for X in basis_broken]
radial_hessian = hessian_on(radial)

# A linear adjoint spurion on a fundamental 3+1 carrier.
g_n = sp.expand(eta * a_star)
g_m = sp.expand(-3 * eta * a_star)
contrast = sp.simplify(g_n - g_m)
eta_sign_hostile = sp.simplify(contrast.subs(eta, -eta) + contrast)
scale_fiber = sp.simplify(
    contrast.subs({kappa: rho * kappa, eta: eta / rho}, simultaneous=True)
    - contrast
)

checks = {
    "wp786_dependency_passed": wp786["status"] == "PASS"
    and all(wp786["checks"].values()),
    "su4_generator_is_traceless": tr(T) == 0,
    "fundamental_has_three_plus_one_weights": tuple(T.diagonal())
    == (1, 1, 1, -3),
    "cubic_orientation_invariant_is_nonzero": (tr2, tr3, tr4)
    == (12, -24, 84),
    "ray_stationary_equation_is_exact": dV
    == 24 * a**2 * (6 * a * lam - kappa),
    "nonzero_stationary_point_is_kappa_over_six_lambda": sp.simplify(
        dV.subs(a, a_star)
    )
    == 0,
    "selected_ray_vacuum_has_negative_energy": V_star
    == -kappa**4 / (108 * lam**3),
    "ray_hessian_is_positive_for_positive_lambda": ray_hessian
    == 4 * kappa**2 / lam,
    "eight_unbroken_modes_are_strictly_positive": len(unbroken_hessians) == 8
    and set(unbroken_hessians) == {2 * kappa**2 / (3 * lam)},
    "six_broken_modes_are_goldstone_zeroes": len(broken_hessians) == 6
    and set(broken_hessians) == {0},
    "radial_normalized_mode_is_positive": radial_hessian
    == kappa**2 / (3 * lam),
    "linear_spurion_portal_contrast": contrast
    == 2 * eta * kappa / (3 * lam),
    "free_spurion_sign_reverses_portal": eta_sign_hostile == 0,
    "continuous_kappa_eta_scale_fiber_preserves_portal": scale_fiber == 0,
}
checks = {name: bool(value) for name, value in checks.items()}
if not all(checks.values()):
    raise SystemExit(checks)

result = {
    "work_package": "WP787",
    "status": "PASS",
    "checks": checks,
    "dependency": "WP786",
    "admitted_state_domain": (
        "the SU(4) adjoint ray Phi=a*diag(1,1,1,-3), its minimal cubic-plus-"
        "quartic invariant potential at zero relevant mass, all fifteen "
        "normalized adjoint fluctuations, and a candidate linear adjoint "
        "portal spurion eta"
    ),
    "faithful_coordinate": (
        "the signed adjoint amplitude a, cubic invariant Tr(Phi^3), complete "
        "adjoint Hessian spectrum, and signed portal contrast g_n-g_m"
    ),
    "source_authorized_probe_family": (
        "SU(4)-invariant quadratic, cubic, and quartic traces and the exact "
        "tree-level Hessian; eta is explicitly a candidate coupling, not "
        "source-authorized"
    ),
    "contextual_partition": (
        "a fixed nonzero kappa selects one of the two adjoint orientations and "
        "stabilizes eight physical unbroken-sector modes, with six Goldstones; "
        "the portal still varies with eta*kappa/lambda"
    ),
    "selector_result": (
        "the cubic parent is an orientation selector and stable 3+1 carrier "
        "rigidifier conditional on the sign of kappa, but it is not a portal "
        "sign or magnitude selector because eta is independent"
    ),
    "smallest_exact_falsifier": (
        "eta and -eta give the same selected SU(4) vacuum and opposite portal "
        "contrasts; simultaneous kappa->rho*kappa and eta->eta/rho leaves the "
        "portal unchanged while changing source scales"
    ),
    "rg_threshold_instrument_result": (
        "the exact tree Hessian proves a local vacuum basin only; no beta "
        "function, finite matching map, or calibrated physical16 instrument "
        "is supplied"
    ),
    "deutschian_status": (
        "SU(4) cubic geometry explains a 3+1 orientation only after kappa is "
        "given; attaching eta afterward makes the desired portal easy to vary"
    ),
    "remaining_gate": (
        "derive kappa and the portal vertex from one quantized chiral source "
        "operation, eliminate the eta and scale fibers, then compute its full "
        "RG basin, thresholds, and labelled detector response"
    ),
}
(ROOT / "results" / "wp787_su4_cubic_orientation_portal_fiber.json").write_text(
    json.dumps(result, indent=2) + "\n", encoding="utf-8"
)
print(json.dumps(result, indent=2))
