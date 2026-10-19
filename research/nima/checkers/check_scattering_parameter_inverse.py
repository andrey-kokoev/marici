# /// script
# dependencies = ["sympy"]
# ///
"""Exact observation-relative continuum inverse and source-specific blind energy."""
from pathlib import Path
import copy
import hashlib
import json
import sympy as S

ROOT = Path(__file__).resolve().parents[3]
AUDIT = "research/nima/results/scattering-contact-source-audit-v1.json"
REPORT = "research/nima/scattering-parameter-inverse-v1.md"
NET = "research/nima/contracts/scattering-core-bridge-work-net.v4.json"
OUT = "research/nima/results/scattering-parameter-inverse-v1.json"


def validate_net(c):
    nodes = {n["id"]: n for n in c["conjectures"]}
    expected = {
        "unchanged-coefficient-affine-core-bridge": ("resolved", "rejected"),
        "retained-two-port-response-realization": ("resolved", "constructed"),
        "native-contact-source-law-audit": ("resolved", "constructed"),
        "continuum-parameter-identifiability": ("resolved", "constructed"),
        "parameter-inverse-conditioning": ("open", "open"),
        "native-continuum-operation-selection": ("deferred_missing_native_principle", "open"),
        "source-compatible-core-and-channel-bridge": ("open", "open"),
    }
    if set(nodes) != set(expected) or any((nodes[k]["status"], nodes[k]["verdict"]) != v for k, v in expected.items()):
        raise ValueError("research dispositions changed")
    if c["objective"]["outcome"] is not None or any(n["outcome"] is not None for n in nodes.values()):
        raise ValueError("formal outcome promotion")
    inverse = nodes["continuum-parameter-identifiability"]
    if inverse.get("native_law_selected") is not False or inverse.get("all_observation_vocabularies_identifying") is not False:
        raise ValueError("inverse scope promoted")
    if c["frontier"] != ["parameter-inverse-conditioning"] or any(c["boundary"].values()):
        raise ValueError("root/physical/frontier bypass")
    if "native-continuum-operation-selection" not in nodes["source-compatible-core-and-channel-bridge"]["depends_on"]:
        raise ValueError("selection gate bypass")
    seen = set()
    for n in c["conjectures"]:
        if not set(n["depends_on"]) <= seen:
            raise ValueError("dependency order")
        seen.add(n["id"])


def recover_point(energy, phases, re, ro, symbol, threshold=None):
    """Exact point inverse, refusing data outside the declared regular domain."""
    source = [S.cancel(r.subs(symbol, energy)) for r in (re, ro)]
    if any(r.is_finite is not True for r in source) or source[0] == source[1]:
        raise ValueError("source pole or zero parity contrast")
    if any(S.simplify(t) == 0 for t in phases):
        raise ValueError("zero transmission")
    a = [S.simplify(S.expand_complex(-S.I * (1 / t - 1))) for t in phases]
    if any(v.is_real is not True or v.is_finite is not True or v == 0 for v in a):
        raise ValueError("not finite nonzero real impedance ratios")
    z = S.simplify((1 / a[0] - 1 / a[1]) / (source[1] - source[0]))
    q = S.simplify(source[0] + 1 / (z * a[0]))
    if z.is_positive is not True or q.is_positive is not True:
        raise ValueError("nonpositive lead impedance or contact strength")
    result = {"z": z, "eta": 1 / q}
    if threshold is not None:
        if S.simplify(energy - threshold).is_positive is not True:
            raise ValueError("not above declared threshold")
        result["beta"] = S.simplify(z ** 2 / (4 * (energy - threshold)))
    return result


def main():
    files = [AUDIT, REPORT, NET,
             "research/nima/checkers/check_scattering_contact_source_audit.py",
             "research/strominger/results/neutron-two-rim-contact-binding.json",
             str(Path(__file__).resolve().relative_to(ROOT)).replace("\\", "/")]
    hashes = {p: hashlib.sha256((ROOT / p).read_bytes()).hexdigest() for p in files}
    checks = []

    def check(name, value):
        if not value:
            raise AssertionError(name)
        checks.append(name)

    audit = json.loads((ROOT / AUDIT).read_text())
    check("source_audit_hashes_live", all(hashlib.sha256((ROOT / p).read_bytes()).hexdigest() == h for p, h in audit["source_sha256"].items()))
    e = S.Symbol("E")
    re, ro = [S.sympify(audit["bare_parity_response"][s], locals={"E": e}) for s in ("even", "odd")]
    contrast = S.factor(ro - re)
    numerator, denominator = S.fraction(contrast)
    contrast_roots = S.solve(numerator, e)
    blind = S.Rational(5391, 3292)
    check("actual_source_single_finite_contrast_zero", contrast_roots == [blind])
    check("blind_energy_propagates_in_principal_lead", blind > S.Rational(1, 2))
    check("blind_energy_not_bare_pole", denominator.subs(e, blind) != 0)
    check("source_parities_equal_at_blind_energy", S.cancel((re - ro).subs(e, blind)) == 0)

    # General point inverse in the named native energy/channel convention.
    z, q = S.symbols("z q", positive=True)
    se, so = S.symbols("r0_even r0_odd", real=True)
    ae, ao = 1 / (z * (q - se)), 1 / (z * (q - so))
    inverse_z = S.cancel((1 / ae - 1 / ao) / (so - se))
    inverse_q = S.cancel(se + 1 / (inverse_z * ae))
    check("general_two_parity_signed_inverse", inverse_z == z and inverse_q == q)
    a = S.Symbol("a", real=True)
    t = 1 / (1 + S.I * a)
    check("signed_phase_extraction", S.simplify(-S.I * (1 / t - 1)) == a)
    check("probability_loses_sign", S.simplify(t * S.conjugate(t)) == 1 / (1 + a ** 2))

    def forward(energy, eta, beta, theta):
        zz = S.sqrt(4 * beta * (energy - theta))
        r_even, r_odd = [S.cancel(r.subs(e, energy)) for r in (re, ro)]
        check("forward_energy_admissible/" + str(energy), energy > theta and r_even != r_odd)
        pair = [S.simplify(1 / (zz * (1 / eta - r))) for r in (r_even, r_odd)]
        phases = [S.simplify(1 / (1 + S.I * v)) for v in pair]
        extracted = [S.simplify(-S.I * (1 / v - 1)) for v in phases]
        check("phase_extraction_roundtrip/" + str(energy), all(S.simplify(u - v) == 0 for u, v in zip(extracted, pair)))
        recovered_z = S.simplify((1 / extracted[0] - 1 / extracted[1]) / (r_odd - r_even))
        recovered_q = S.simplify(r_even + 1 / (recovered_z * extracted[0]))
        check("actual_source_eta_and_impedance_roundtrip/" + str(energy),
              S.simplify(recovered_z - zz) == 0 and recovered_q == 1 / eta)
        checked = recover_point(energy, phases, re, ro, e, theta)
        check("guarded_point_inverse_roundtrip/" + str(energy), checked["eta"] == eta and checked["beta"] == beta)
        return pair, phases, recovered_z, recovered_q

    eta0, beta0, theta0 = S.Integer(2), S.Integer(1), S.Rational(1, 2)
    e1, e2 = S.Rational(113, 100), S.Integer(2)
    point1 = forward(e1, eta0, beta0, theta0)
    point2 = forward(e2, eta0, beta0, theta0)
    beta_recovered = S.simplify((point2[2] ** 2 - point1[2] ** 2) / (4 * (e2 - e1)))
    theta_recovered = S.simplify(e1 - point1[2] ** 2 / (4 * beta_recovered))
    check("two_energy_unknown_threshold_inverse", beta_recovered == beta0 and theta_recovered == theta0)
    check("one_energy_known_threshold_beta_inverse", S.simplify(point1[2] ** 2 / (4 * (e1 - theta0))) == beta0)
    # Unknown threshold: same eta and same beta*(E-theta), different parameters.
    theta_alt = e1 - beta0 * (e1 - theta0) / 2
    alternative = forward(e1, eta0, S.Integer(2), theta_alt)
    check("unknown_threshold_one_energy_alias", theta_alt != theta0 and all(S.simplify(u - v) == 0 for u, v in zip(point1[1], alternative[1])))

    # Exact parity probability alias at E=2 with known theta=1/2.
    r_even, r_odd = [S.cancel(r.subs(e, e2)) for r in (re, ro)]
    scale = S.cancel((2 / eta0 - r_even - r_odd) / (r_odd - r_even))
    q_alt = S.cancel(r_even + (1 / eta0 - r_even) / scale)
    eta_alt, beta_alt = 1 / q_alt, beta0 * scale ** 2
    check("probability_alias_positive_distinct_parameters", scale > 0 and q_alt > 0 and eta_alt != eta0 and beta_alt != beta0)
    alias = forward(e2, eta_alt, beta_alt, theta0)
    original_a, alias_a = point2[0], alias[0]
    probabilities = lambda pair: [S.simplify(1 / (1 + v ** 2)) for v in pair]
    check("parity_probabilities_identical_for_alias", probabilities(original_a) == probabilities(alias_a))
    check("alias_changes_one_signed_phase", S.simplify(alias_a[0] - original_a[0]) == 0 and S.simplify(alias_a[1] + original_a[1]) == 0)
    conversion = lambda pair: S.simplify((pair[0] - pair[1]) ** 2 / (2 * (1 + pair[0] ** 2) * (1 + pair[1] ** 2)))
    c_original, c_alias = conversion(original_a), conversion(alias_a)
    check("other_port_flux_distinguishes_parity_probability_alias", c_original != c_alias)
    te, to = probabilities(original_a)
    product = S.simplify(((1 / te - 1) + (1 / to - 1) - 2 * c_original / (te * to)) / 2)
    check("augmented_probabilities_reconstruct_relative_sign", S.simplify(product - original_a[0] * original_a[1]) == 0)
    # The remaining common sign flip sends recovered z to -z, excluded by z>0.
    check("positive_lead_impedance_resolves_common_sign", S.simplify((-1 / original_a[0] + 1 / original_a[1]) / (r_odd - r_even) + point2[2]) == 0)

    # At the source-specific contrast zero, even full complex S at one energy
    # admits positive eta/beta rivals. This is not a broadband equivalence.
    r_blind = S.cancel(re.subs(e, blind))
    v_base, v_alt = 1 / (1 / eta0 - r_blind), 1 / (1 - r_blind)
    beta_blind_alt = S.cancel(beta0 * (v_alt / v_base) ** 2)
    check("blind_alias_positive_same_response_sign", beta_blind_alt > 0 and v_alt / v_base > 0)
    a_blind = S.simplify(v_base / S.sqrt(4 * beta0 * (blind - theta0)))
    a_blind_alt = S.simplify(v_alt / S.sqrt(4 * beta_blind_alt * (blind - theta0)))
    check("blind_energy_complete_two_parity_phase_alias", S.simplify(a_blind - a_blind_alt) == 0 and beta_blind_alt != beta0)
    away = forward(e2, S.Integer(1), beta_blind_alt, theta0)
    check("blind_alias_not_broadband_equivalence", any(S.simplify(u - v) != 0 for u, v in zip(away[0], point2[0])))

    blind_phase = 1 / (1 + S.I * a_blind)
    refusals = [
        ("nonconservative-amplitude", e1, [S.Integer(2), point1[1][1]], theta0),
        ("negative-impedance", e1, [S.conjugate(v) for v in point1[1]], theta0),
        ("closed-threshold", e1, point1[1], e1),
        ("blind-source-energy", blind, [blind_phase, blind_phase], theta0),
        ("zero-transmission", e1, [S.Integer(0), point1[1][1]], theta0),
    ]
    for name, energy, phases, theta in refusals:
        try:
            recover_point(energy, phases, re, ro, e, theta)
        except ValueError:
            check("inverse_domain_refusal/" + name, True)
        else:
            raise AssertionError("invalid inverse data accepted: " + name)

    # Common energy-unit change co-transports native K and the energy argument.
    unit = S.Integer(3)
    r_scaled = re.subs(e, e / unit) / unit
    check("native_energy_unit_covariance", S.cancel(r_scaled.subs(e, unit * e1) - re.subs(e, e1) / unit) == 0)
    vv = 1 / (1 / eta0 - re.subs(e, e1))
    vv_scaled = 1 / (1 / (unit * eta0) - r_scaled.subs(e, unit * e1))
    check("stationary_amplitude_energy_unit_gauge", S.simplify(vv_scaled / (unit * point1[2]) - vv / point1[2]) == 0)

    net = json.loads((ROOT / NET).read_text())
    validate_net(net)
    check("observation_scoped_inverse_keeps_native_selection_open", True)
    for kind in ("root", "universal-observation", "native-selection", "physical", "selection-gate"):
        bad = copy.deepcopy(net)
        nodes = {n["id"]: n for n in bad["conjectures"]}
        if kind == "root": bad["objective"]["outcome"] = "++"
        elif kind == "universal-observation": nodes["continuum-parameter-identifiability"]["all_observation_vocabularies_identifying"] = True
        elif kind == "native-selection": nodes["continuum-parameter-identifiability"]["native_law_selected"] = True
        elif kind == "physical": bad["boundary"]["physical_scattering_explained"] = True
        else: nodes["source-compatible-core-and-channel-bridge"]["depends_on"].remove("native-continuum-operation-selection")
        try:
            validate_net(bad)
        except ValueError:
            check("contract_hostile_refused/" + kind, True)
        else:
            raise AssertionError("scope hostile accepted: " + kind)
    check("inputs_unchanged_during_execution", all(hashlib.sha256((ROOT / p).read_bytes()).hexdigest() == h for p, h in hashes.items()))
    result = {"schema": "marici.scattering.parameter-inverse.v1", "status": "pass", "check_count": len(checks),
              "checks": checks, "source_sha256": hashes, "source_contrast": str(contrast), "blind_energy": str(blind),
              "phase_inverse": {"a_s": "-i*(1/t_s-1)", "z": "(1/a_even-1/a_odd)/(r0_odd-r0_even)",
                                "eta": "1/(r0_even+1/(z*a_even))", "known_threshold_beta": "z^2/[4(E-theta)]",
                                "two_energy_beta": "(z2^2-z1^2)/[4(E2-E1)]", "two_energy_theta": "E1-z1^2/(4*beta)"},
              "known_threshold_probability_alias": {"energy": str(e2), "eta_original": str(eta0), "beta_original": str(beta0),
                 "eta_alternative": str(eta_alt), "beta_alternative": str(beta_alt),
                 "parity_transmission_probabilities": [str(v) for v in probabilities(original_a)],
                 "other_port_flux_original": str(c_original), "other_port_flux_alternative": str(c_alias)},
              "blind_energy_phase_alias": {"eta_original": str(eta0), "beta_original": str(beta0), "eta_alternative": "1", "beta_alternative": str(beta_blind_alt)},
              "observation_scope": "Declared channel/contact phase convention, known native K,M,W and anchored model energy labels. Phase-complete point inverse generic; parity-probability-only aliases retained; augmented probability triple generically sufficient.",
              "remaining_gauges": ["encounter-coordinate dilation with transported reader", "common energy unit with K co-scaled", "hbar/physical-time calibration absent from stationary S"],
              "verification_level": "exact symbolic source-response inverse and counterexamples; written uniqueness/observation argument, not formal kernel proof",
              "native_law_selected": False, "physical_source_selected": False, "root_outcome": None,
              "stationary_field_solver_runs": 0, "measurement_work_reopened": False}
    out = ROOT / OUT
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": "pass", "check_count": len(checks), "blind_energy": str(blind),
                      "probability_alias_eta": str(eta_alt), "probability_alias_beta": str(beta_alt), "receipt": OUT}))


if __name__ == "__main__":
    main()
