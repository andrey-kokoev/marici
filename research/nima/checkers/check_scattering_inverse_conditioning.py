# /// script
# dependencies = ["sympy"]
# ///
"""Exact finite conditioning bounds and admissible-source failure families."""
from pathlib import Path
import copy
import hashlib
import json
import sys
import sympy as S

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(Path(__file__).resolve().parent))
from check_scattering_parameter_inverse import recover_point
from check_scattering_core_bridge_spectrum import rational_matrix

INVERSE = "research/nima/results/scattering-parameter-inverse-v1.json"
AUDIT = "research/nima/results/scattering-contact-source-audit-v1.json"
MEMORY = "research/nima/results/scattering-two-port-memory-v1.json"
REPORT = "research/nima/scattering-inverse-conditioning-v1.md"
NET = "research/nima/contracts/scattering-core-bridge-work-net.v5.json"
OUT = "research/nima/results/scattering-inverse-conditioning-v1.json"


def finite_bounds(h, d, c, z_lower, z_upper, b_over_z_bound, q, energy_gap):
    """Rational sufficient bounds on the algebraic inverse; no noise model."""
    if not (0 <= h < d and c > 0 and z_upper >= z_lower > 0 and b_over_z_bound >= 0 and q > 0 and energy_gap > 0):
        raise ValueError("outside declared bound domain")
    u = h / (d * (d - h))
    dz = 2 * u / c
    if dz >= z_lower:
        raise ValueError("impedance margin exhausted")
    dq = (u + b_over_z_bound * dz) / (z_lower - dz)
    if dq >= q:
        raise ValueError("contact reciprocal margin exhausted")
    return {"b_error": S.cancel(u), "z_error": S.cancel(dz), "q_error": S.cancel(dq),
            "eta_error": S.cancel(dq / (q * (q - dq))),
            "beta_error": S.cancel((2 * z_upper * dz + dz ** 2) / (4 * energy_gap))}


def validate_net(c):
    nodes = {n["id"]: n for n in c["conjectures"]}
    expected = {
        "unchanged-coefficient-affine-core-bridge": ("resolved", "rejected"),
        "retained-two-port-response-realization": ("resolved", "constructed"),
        "native-contact-source-law-audit": ("resolved", "constructed"),
        "continuum-parameter-identifiability": ("resolved", "constructed"),
        "parameter-inverse-conditioning": ("resolved", "constructed"),
        "general-positive-contact-classification": ("open", "open"),
        "native-continuum-operation-selection": ("deferred_missing_native_principle", "open"),
        "source-compatible-core-and-channel-bridge": ("open", "open"),
    }
    if set(nodes) != set(expected) or any((nodes[k]["status"], nodes[k]["verdict"]) != v for k, v in expected.items()):
        raise ValueError("research disposition changed")
    if c["objective"]["outcome"] is not None or any(n["outcome"] is not None for n in nodes.values()):
        raise ValueError("formal outcome promotion")
    if nodes["parameter-inverse-conditioning"].get("uniform_global_stability") is not False:
        raise ValueError("failure domains erased")
    if nodes["parameter-inverse-conditioning"].get("empirical_noise_model_admitted") is not False:
        raise ValueError("algebraic perturbations made empirical")
    if c["frontier"] != ["general-positive-contact-classification"] or any(c["boundary"].values()):
        raise ValueError("boundary/frontier bypass")
    if "native-continuum-operation-selection" not in nodes["source-compatible-core-and-channel-bridge"]["depends_on"]:
        raise ValueError("selection gate bypass")
    seen = set()
    for n in c["conjectures"]:
        if not set(n["depends_on"]) <= seen:
            raise ValueError("dependency order")
        seen.add(n["id"])


def main():
    files = [INVERSE, AUDIT, MEMORY, REPORT, NET,
             "research/nima/checkers/check_scattering_parameter_inverse.py",
             "research/nima/checkers/check_scattering_core_bridge_spectrum.py",
             "research/strominger/checkers/interface_preserving_carrier_dynamics.py",
             str(Path(__file__).resolve().relative_to(ROOT)).replace("\\", "/")]
    hashes = {p: hashlib.sha256((ROOT / p).read_bytes()).hexdigest() for p in files}
    checks = []

    def check(name, condition):
        if not condition:
            raise AssertionError(name)
        checks.append(name)

    inverse = json.loads((ROOT / INVERSE).read_text())
    audit = json.loads((ROOT / AUDIT).read_text())
    memory = json.loads((ROOT / MEMORY).read_text())
    for label, receipt in (("inverse", inverse), ("audit", audit), ("memory", memory)):
        check(label + "_source_hashes_live", all(hashlib.sha256((ROOT / p).read_bytes()).hexdigest() == h for p, h in receipt["source_sha256"].items()))
    e = S.Symbol("E", positive=True)
    re, ro = [S.sympify(audit["bare_parity_response"][s], locals={"E": e}) for s in ("even", "odd")]
    contrast = S.factor(ro - re)
    blind = S.Rational(5391, 3292)
    contrast_constant = S.Rational(2504107, 10837264)
    check("source_contrast_order_four", S.limit(e ** 4 * contrast, e, S.oo) == contrast_constant)
    slope = S.cancel(S.diff(contrast, e).subs(e, blind))
    check("blind_zero_simple", slope != 0 and contrast.subs(e, blind) == 0)
    gram = rational_matrix(memory["bright_metric"])
    bare_core = rational_matrix(memory["bright_bare_core"])
    check("all_visible_bare_poles_below_four", all((gram * (4 * S.eye(5) - bare_core))[:j, :j].det() > 0 for j in range(1, 6)))
    check("source_response_at_four_below_principal_reciprocal", all(0 < r.subs(e, 4) < S.Rational(1, 2) for r in (re, ro)))
    # Positive spectral residues imply these inequalities persist for E>=4.

    # Jacobian in reciprocal-impedance observation coordinates b_s=i*t/(1-t).
    be, bo, delta = S.symbols("b_even b_odd Delta", real=True)
    se = S.Symbol("r0_even", real=True)
    z_expr = (be - bo) / delta
    q_expr = se + be / z_expr
    check("inverse_impedance_jacobian", S.diff(z_expr, be) == 1 / delta and S.diff(z_expr, bo) == -1 / delta)
    check("inverse_contact_jacobian", S.simplify(S.diff(q_expr, be) + bo / (z_expr ** 2 * delta)) == 0 and
          S.simplify(S.diff(q_expr, bo) - be / (z_expr ** 2 * delta)) == 0)
    t, dt = S.symbols("t dt")
    b_map = lambda v: S.I * v / (1 - v)
    check("reciprocal_impedance_finite_difference", S.cancel(b_map(t + dt) - b_map(t) - S.I * dt / ((1 - t - dt) * (1 - t))) == 0)
    check("reciprocal_impedance_derivative", S.simplify(S.diff(b_map(t), t) - S.I / (1 - t) ** 2) == 0)

    # Principal eta=2,beta=1,theta=1/2. Squared gains avoid irrational comparisons.
    q, theta = S.Rational(1, 2), S.Rational(1, 2)
    z2 = 4 * (e - theta)
    be2 = z2 * (q - re) ** 2
    z_gain_squared = S.factor((1 + be2) ** 2 / contrast ** 2)
    eta_gain_squared = S.factor(16 * (q - ro) ** 2 * (1 + be2) ** 2 / (z2 * contrast ** 2))
    beta_gain_squared = S.factor(z2 * (1 + be2) ** 2 / (4 * (e - theta) ** 2 * contrast ** 2))
    check("high_energy_impedance_amplitude_gain_order_five", S.limit(z_gain_squared / e ** 10, e, S.oo) == 1 / contrast_constant ** 2)
    check("high_energy_eta_amplitude_gain_order_nine_halves", S.limit(eta_gain_squared / e ** 9, e, S.oo) == 1 / contrast_constant ** 2)
    check("high_energy_beta_amplitude_gain_order_nine_halves", S.limit(beta_gain_squared / e ** 9, e, S.oo) == 1 / contrast_constant ** 2)
    blind_gain = S.limit((e - blind) ** 2 * z_gain_squared, e, blind)
    check("blind_impedance_gain_simple_pole", blind_gain > 0 and blind_gain == S.cancel((1 + be2.subs(e, blind)) ** 2 / slope ** 2))

    # Actual admissible rival family: eta'=1 and beta'(E) chosen to keep the
    # even transmission EXACT, not a coordinate change with K co-scaled.
    qp = S.Integer(1)
    beta_rival = S.factor(((q - re) / (qp - re)) ** 2)
    da_odd_squared = S.factor((q - qp) ** 2 * contrast ** 2 /
                             (z2 * (q - re) ** 2 * (qp - ro) ** 2 * (q - ro) ** 2))
    a_odd_squared = 1 / (z2 * (q - ro) ** 2)
    rival_a_odd_squared = (qp - re) ** 2 / (z2 * (q - re) ** 2 * (qp - ro) ** 2)
    odd_phase_gap_squared = S.factor(da_odd_squared / ((1 + a_odd_squared) * (1 + rival_a_odd_squared)))
    lam = S.Symbol("lambda")
    direction_block = S.ones(2)
    check("full_on_shell_S_operator_gap_is_twice_odd_transmission_gap",
          S.expand((direction_block.T * direction_block).charpoly(lam).as_expr() - lam * (lam - 4)) == 0)
    check("rival_kinetic_parameter_stays_separated_at_infinity", S.limit(beta_rival, e, S.oo) == S.Rational(1, 4))
    check("admissible_phase_rivals_coalesce_order_nine_halves", S.limit(e ** 9 * odd_phase_gap_squared, e, S.oo) == contrast_constant ** 2)
    rows = []
    for energy in map(S.Integer, (4, 8, 16, 32)):
        re_v, ro_v = re.subs(e, energy), ro.subs(e, energy)
        zz = S.sqrt(z2.subs(e, energy))
        zp = S.simplify(zz * (q - re_v) / (qp - re_v))
        a_even, ap_even = 1 / (zz * (q - re_v)), 1 / (zp * (qp - re_v))
        check("rival_admissible_and_even_phase_exact/E=" + str(energy), zp > 0 and S.simplify(a_even - ap_even) == 0)
        gap = S.cancel(odd_phase_gap_squared.subs(e, energy))
        check("rival_odd_phase_gap_positive/E=" + str(energy), gap > 0)
        rows.append({"energy": str(energy), "eta_original": "2", "eta_rival": "1",
                     "beta_original": "1", "beta_rival": str(beta_rival.subs(e, energy)),
                     "odd_transmission_gap_squared": str(gap), "gap_decimal": float(S.sqrt(gap))})
    check("rival_gap_decreases_on_named_exact_controls", all(S.Rational(rows[i + 1]["odd_transmission_gap_squared"]) < S.Rational(rows[i]["odd_transmission_gap_squared"]) for i in range(3)))

    # Concrete rational finite perturbation on the real, model-admissible b chart.
    energy = S.Integer(2)
    r_even, r_odd = re.subs(e, energy), ro.subs(e, energy)
    c = abs(r_odd - r_even)
    z = S.sqrt(6)
    eps = S.Rational(1, 10 ** 6)
    h = 3 * eps
    b0e, b0o = z * (q - r_even), z * (q - r_odd)
    b1e = b0e + z * eps
    nominal_phases = [S.simplify(b / (b + S.I)) for b in (b0e, b0o)]
    perturbed_phases = [S.simplify(b / (b + S.I)) for b in (b1e, b0o)]
    check("declared_transmission_and_one_minus_transmission_margins", all(
        1 / (1 + b ** 2) >= S.Rational(1, 4) and b ** 2 / (1 + b ** 2) >= S.Rational(1, 4) for b in (b0e, b0o)))
    actual_dt_squared = S.cancel(6 * eps ** 2 / ((1 + b0e ** 2) * (1 + b1e ** 2)))
    check("finite_phase_perturbation_within_declared_h", actual_dt_squared <= h ** 2)
    check("nominal_impedance_and_contact_ratio_bounds", 2 < z < 3 and abs(q - r_even) < 1)
    bounds = finite_bounds(h, S.Rational(1, 2), c, S.Integer(2), S.Integer(3), S.Integer(1), q, S.Rational(3, 2))
    zratio = 1 + eps / (r_odd - r_even)
    qhat = S.cancel(r_even + (q - r_even + eps) / zratio)
    etahat, betahat = 1 / qhat, zratio ** 2
    check("finite_perturbation_stays_in_positive_model_class", qhat > 0 and zratio > 0 and betahat > 0)
    recovered = recover_point(energy, perturbed_phases, re, ro, e, theta)
    check("guarded_inverse_recovers_finite_perturbation", S.cancel(recovered["eta"] - etahat) == 0 and S.cancel(recovered["beta"] - betahat) == 0)
    check("finite_eta_error_within_rational_bound", abs(etahat - 2) <= bounds["eta_error"])
    check("finite_beta_error_within_rational_bound", abs(betahat - 1) <= bounds["beta_error"])
    check("zero_perturbation_bound_exact", all(v == 0 for v in finite_bounds(S.Integer(0), S.Rational(1, 2), c, S.Integer(2), S.Integer(3), S.Integer(1), q, S.Rational(3, 2)).values()))
    for name, args in (
        ("transmission-singularity", (S.Rational(1, 2), S.Rational(1, 2), c, 2, 3, 1, q, S.Rational(3, 2))),
        ("zero-contrast", (h, S.Rational(1, 2), 0, 2, 3, 1, q, S.Rational(3, 2))),
        ("impedance-margin", (S.Rational(1, 100), S.Rational(1, 2), S.Rational(1, 1000), 2, 3, 1, q, S.Rational(3, 2))),
        ("contact-margin", (S.Rational(1, 100), S.Rational(1, 2), S.Integer(1), S.Rational(1, 10), 3, 1, q, S.Rational(3, 2))),
        ("negative-ratio-bound", (h, S.Rational(1, 2), c, 2, 3, -1, q, S.Rational(3, 2))),
    ):
        try:
            finite_bounds(*args)
        except ValueError:
            check("bound_domain_refusal/" + name, True)
        else:
            raise AssertionError("invalid bound domain accepted: " + name)

    net = json.loads((ROOT / NET).read_text())
    validate_net(net)
    check("conditional_stability_preserves_failure_and_native_selection", True)
    for kind in ("root", "uniform-global", "empirical-noise", "physical", "selection-gate"):
        bad = copy.deepcopy(net)
        nodes = {n["id"]: n for n in bad["conjectures"]}
        if kind == "root": bad["objective"]["outcome"] = "++"
        elif kind == "uniform-global": nodes["parameter-inverse-conditioning"]["uniform_global_stability"] = True
        elif kind == "empirical-noise": nodes["parameter-inverse-conditioning"]["empirical_noise_model_admitted"] = True
        elif kind == "physical": bad["boundary"]["physical_scattering_explained"] = True
        else: nodes["source-compatible-core-and-channel-bridge"]["depends_on"].remove("native-continuum-operation-selection")
        try:
            validate_net(bad)
        except ValueError:
            check("contract_hostile_refused/" + kind, True)
        else:
            raise AssertionError("scope hostile accepted: " + kind)
    check("inputs_unchanged_during_execution", all(hashlib.sha256((ROOT / p).read_bytes()).hexdigest() == sha for p, sha in hashes.items()))
    result = {"schema": "marici.scattering.inverse-conditioning.v1", "status": "pass", "check_count": len(checks),
              "checks": checks, "source_sha256": hashes, "contrast_high_energy_coefficient": str(contrast_constant),
              "contrast_decay": "E^-4", "blind_contrast_slope": str(slope),
              "principal_amplitude_gain_orders": {"z": "E^5", "eta": "E^(9/2)", "beta": "E^(9/2)"},
              "high_energy_coalescing_rivals": rows,
              "finite_bound_example": {"energy": "2", "amplitude_radius_h": str(h), "contrast_lower_bound": str(c),
                    "bounds": {k: str(v) for k, v in bounds.items()}, "eta_error": str(abs(etahat - 2)), "beta_error": str(abs(betahat - 1))},
              "uniform_global_stability": False, "empirical_noise_model_admitted": False,
              "verification_level": "exact symbolic limits, rational margins and admissible model perturbations; written finite-bound inference, not formal kernel proof",
              "native_operation_selected": False, "physical_source_selected": False, "root_outcome": None,
              "stationary_field_solver_runs": 0, "measurement_work_reopened": False}
    out = ROOT / OUT
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": "pass", "check_count": len(checks), "contrast_decay": "E^-4",
                      "principal_gain_orders": result["principal_amplitude_gain_orders"],
                      "rival_phase_gap_decimals": [r["gap_decimal"] for r in rows], "receipt": OUT}))


if __name__ == "__main__":
    main()
