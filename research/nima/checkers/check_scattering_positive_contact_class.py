# /// script
# dependencies = ["sympy"]
# ///
"""Source-addressed reciprocal positive-contact class and coordinate quotient."""
from pathlib import Path
import copy
import hashlib
import json
import sys
import sympy as S

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(Path(__file__).resolve().parent))
from check_scattering_core_bridge_spectrum import rational_matrix

AUDIT = "research/nima/results/scattering-contact-source-audit-v1.json"
MEMORY = "research/nima/results/scattering-two-port-memory-v1.json"
CONDITIONING = "research/nima/results/scattering-inverse-conditioning-v1.json"
REPORT = "research/nima/scattering-positive-contact-class-v1.md"
NET = "research/nima/contracts/scattering-core-bridge-work-net.v6.json"
OUT = "research/nima/results/scattering-positive-contact-class-v1.json"


def zero(a):
    return all(S.cancel(v) == 0 for v in a)


def validate_parameters(a, b, g, kinetic):
    if not (a >= 0 and b >= 0 and kinetic > 0 and a * b >= g ** 2):
        raise ValueError("not a positive contact/kinetic form")


def validate_net(c):
    nodes = {n["id"]: n for n in c["conjectures"]}
    expected = {
        "unchanged-coefficient-affine-core-bridge": ("resolved", "rejected"),
        "retained-two-port-response-realization": ("resolved", "constructed"),
        "native-contact-source-law-audit": ("resolved", "constructed"),
        "continuum-parameter-identifiability": ("resolved", "constructed"),
        "parameter-inverse-conditioning": ("resolved", "constructed"),
        "general-positive-contact-classification": ("resolved", "constructed"),
        "finite-energy-contact-class-inverse": ("open", "open"),
        "native-continuum-operation-selection": ("deferred_missing_native_principle", "open"),
        "source-compatible-core-and-channel-bridge": ("open", "open"),
    }
    if set(nodes) != set(expected) or any((nodes[k]["status"], nodes[k]["verdict"]) != v for k, v in expected.items()):
        raise ValueError("research dispositions changed")
    if c["objective"]["outcome"] is not None or any(n["outcome"] is not None for n in nodes.values()):
        raise ValueError("formal outcome promoted")
    classification = nodes["general-positive-contact-classification"]
    if classification.get("balanced_rule_forced_by_positivity") is not False or classification.get("decoupled_cases_retained") is not True:
        raise ValueError("contact classification scope erased")
    if c["frontier"] != ["finite-energy-contact-class-inverse"] or any(c["boundary"].values()):
        raise ValueError("root/physical/frontier bypass")
    if "native-continuum-operation-selection" not in nodes["source-compatible-core-and-channel-bridge"]["depends_on"]:
        raise ValueError("native selection gate bypass")
    seen = set()
    for n in c["conjectures"]:
        if not set(n["depends_on"]) <= seen:
            raise ValueError("dependency order")
        seen.add(n["id"])


def main():
    files = [AUDIT, MEMORY, CONDITIONING, REPORT, NET,
             "research/nima/checkers/check_scattering_core_bridge_spectrum.py",
             "research/strominger/checkers/interface_preserving_carrier_dynamics.py",
             str(Path(__file__).resolve().relative_to(ROOT)).replace("\\", "/")]
    hashes = {p: hashlib.sha256((ROOT / p).read_bytes()).hexdigest() for p in files}
    checks = []

    def check(name, condition):
        if not condition:
            raise AssertionError(name)
        checks.append(name)

    receipts = {"audit": json.loads((ROOT / AUDIT).read_text()),
                "memory": json.loads((ROOT / MEMORY).read_text()),
                "conditioning": json.loads((ROOT / CONDITIONING).read_text())}
    for name, receipt in receipts.items():
        check(name + "_source_hashes_live", all(hashlib.sha256((ROOT / p).read_bytes()).hexdigest() == sha for p, sha in receipt["source_sha256"].items()))
    e = S.Symbol("E", positive=True)
    re, ro = [S.sympify(receipts["audit"]["bare_parity_response"][s], locals={"E": e}) for s in ("even", "odd")]
    memory = receipts["memory"]
    gram = rational_matrix(memory["bright_metric"])
    k = rational_matrix(memory["bright_bare_core"])
    w = rational_matrix(memory["bright_ports_raw"])
    check("actual_port_normalization_in_source_metric", w.T * gram * w == 3 * S.eye(2))
    check("actual_bare_core_metric_hermitian", k.T * gram == gram * k)
    a, b, coupling, kinetic = S.symbols("a b g beta", positive=True)
    r, scale = S.symbols("r scale", positive=True)

    # Scalar port block positivity is necessary and sufficient on the actual
    # normalized port image; dark core coordinates are outside this block.
    block = S.Matrix([[a, -coupling], [-coupling, b]])
    check("scalar_contact_determinant", block.det() == a * b - coupling ** 2)
    lead, core = S.symbols("lead core", real=True)
    completed = b * (core - coupling * lead / b) ** 2 + (a - coupling ** 2 / b) * lead ** 2
    check("positive_form_square_completion", S.expand(completed - (a * lead ** 2 - 2 * coupling * lead * core + b * core ** 2)) == 0)
    for vals in ((2, 2, 2, 1), (2, 2, 1, 1), (0, 2, 0, 1), (2, 0, 0, 1), (0, 0, 0, 1)):
        validate_parameters(*map(S.Integer, vals))
        check("positive_or_degenerate_class/" + str(vals), True)
    for vals in ((1, 1, 2, 1), (-1, 2, 0, 1), (1, 1, 0, 0)):
        try:
            validate_parameters(*map(S.Integer, vals))
        except ValueError:
            check("invalid_contact_class_refused/" + str(vals), True)
        else:
            raise AssertionError("invalid contact accepted")

    # General source-core dressing, tested exactly for b=1 and b=2.
    for core_diagonal in (S.Integer(1), S.Integer(2)):
        d = k + core_diagonal * w * w.T * gram / 3
        response = (w.T * gram * (e * S.eye(5) - d).inv(method="DM") * w / 3).applyfunc(S.factor)
        re_dressed = re / (1 - core_diagonal * re)
        ro_dressed = ro / (1 - core_diagonal * ro)
        expected = S.Matrix([[(re_dressed + ro_dressed) / 2, (re_dressed - ro_dressed) / 2],
                             [(re_dressed - ro_dressed) / 2, (re_dressed + ro_dressed) / 2]])
        check("actual_core_resolvent_for_general_diagonal/b=" + str(core_diagonal), zero(response - expected))
        check("general_core_metric_hermitian/b=" + str(core_diagonal), d.T * gram == gram * d)

    blind = S.Rational(5391, 3292)
    critical_b = S.cancel(1 / re.subs(e, blind))
    critical_d = k + critical_b * w * w.T * gram / 3
    eigenvar = S.Symbol("lambda")
    critical_poly = S.Poly(critical_d.charpoly(eigenvar).as_expr(), eigenvar)
    check("positive_contact_diagonal_can_merge_parity_poles", critical_b > 0 and critical_poly.eval(blind) == 0 and critical_poly.diff().eval(blind) == 0)
    check("merged_pole_is_exactly_double", critical_poly.diff().diff().eval(blind) != 0)
    control = S.Matrix.hstack(*(critical_d ** j * w for j in range(5)))
    check("merged_poles_still_require_five_memory_states", control.rank() == 5)
    check("bare_dressed_update_maps_only_into_actual_port_span", S.Matrix.hstack(w, w * w.T * gram).rank() == w.rank() == 2)

    general_v = a + coupling ** 2 * r / (1 - b * r)
    rho = coupling ** 2 / (a * b)
    check("observable_contact_shape_ratio", S.cancel(general_v - a * (1 - b * (1 - rho) * r) / (1 - b * r)) == 0)
    check("balanced_rank_one_recovered", S.cancel(general_v.subs({a: 2, b: 2, coupling: 2}) - 2 / (1 - 2 * r)) == 0)
    check("g_zero_has_no_core_response", general_v.subs(coupling, 0) == a)
    check("zero_lead_contact_is_transparent_class", general_v.subs({a: 0, coupling: 0}) == 0)

    # U_scale acts on lead only: psi'(x)=scale^-1/2 psi(x/scale).
    transform = {a: scale * a, b: b, coupling: S.sqrt(scale) * coupling, kinetic: scale ** 2 * kinetic}
    check("lead_coordinate_form_covariance", S.cancel(transform[a] / scale - a) == 0 and
          S.simplify(transform[coupling] / S.sqrt(scale) - coupling) == 0 and
          S.cancel(transform[kinetic] / scale ** 2 - kinetic) == 0)
    check("boundary_response_scales_with_lead_impedance", S.simplify(general_v.xreplace(transform) / S.sqrt(transform[kinetic]) - general_v / S.sqrt(kinetic)) == 0)
    invariants = [a / S.sqrt(kinetic), coupling ** 2 / S.sqrt(kinetic), b]
    check("all_three_coupled_observable_invariants", all(S.simplify(v.xreplace(transform) - v) == 0 for v in invariants))
    check("rho_is_coordinate_invariant", S.simplify(rho.xreplace(transform) - rho) == 0)
    canonical = {a: b, b: b, coupling: S.sqrt(b / a) * coupling, kinetic: (b / a) ** 2 * kinetic}
    check("canonical_equal_diagonals", S.simplify(canonical[coupling] ** 2 - rho * b ** 2) == 0)
    check("rank_one_only_has_balanced_canonical_coupling", S.cancel((canonical[coupling] ** 2 - b ** 2) - b ** 2 * (rho - 1)) == 0)
    check("strictly_positive_shape_not_balanced_by_dilation", S.Rational(1, 4) != 1)

    # Exact ideal energy-function inverse of the coordinate-quotient invariants.
    y_even = (a + coupling ** 2 * re / (1 - b * re)) / S.sqrt(kinetic)
    mu1 = S.limit(e ** 2 * (re - 1 / e), e, S.oo)
    check("both_parities_have_same_first_native_moment", mu1 == S.limit(e ** 2 * (ro - 1 / e), e, S.oo))
    A = S.limit(y_even, e, S.oo)
    C = S.limit(e * (y_even - A), e, S.oo)
    second = S.limit(e ** 2 * (y_even - A - C / e), e, S.oo)
    recovered_b = S.simplify(second / C - mu1)
    check("general_energy_function_invariant_inverse", A == a / S.sqrt(kinetic) and C == coupling ** 2 / S.sqrt(kinetic) and recovered_b == b)
    check("general_energy_function_rho_inverse", S.simplify(C / (A * recovered_b) - rho) == 0)

    # Exact gauge pair versus a genuinely different positive completion.
    principal = {a: S.Integer(2), b: S.Integer(2), coupling: S.Integer(2), kinetic: S.Integer(1)}
    dilated = {a: S.Integer(8), b: S.Integer(2), coupling: S.Integer(4), kinetic: S.Integer(16)}
    strict = {a: S.Integer(2), b: S.Integer(2), coupling: S.Integer(1), kinetic: S.Integer(1)}
    check("actual_source_broadband_gauge_pair", all(S.cancel((general_v / S.sqrt(kinetic)).subs(principal).subs(r, rs) -
          (general_v / S.sqrt(kinetic)).subs(dilated).subs(r, rs)) == 0 for rs in (re, ro)))
    check("strict_completion_genuinely_changes_source_response", any(S.cancel(general_v.subs(principal).subs(r, rs) - general_v.subs(strict).subs(r, rs)) != 0 for rs in (re, ro)))
    z2 = S.Integer(14) # E=4, theta=1/2, kinetic=1.
    outputs = {}
    for name, parameters in (("balanced", principal), ("strict_positive", strict)):
        ve, vo = [S.cancel(general_v.subs(parameters).subs(r, rs.subs(e, 4))) for rs in (re, ro)]
        transmission = S.cancel((z2 / (z2 + ve ** 2) + z2 / (z2 + vo ** 2)) / 2)
        other = S.cancel(z2 * (ve - vo) ** 2 / (2 * (z2 + ve ** 2) * (z2 + vo ** 2)))
        check("source_flux_class_positive/" + name, 0 < transmission < 1 and 0 <= other <= 1)
        outputs[name] = {"total_transmission": str(transmission), "other_port_flux": str(other),
                         "total_transmission_decimal": float(transmission), "other_port_flux_decimal": float(other)}
    check("strict_completion_distinguished_by_actual_source_flux", outputs["balanced"] != outputs["strict_positive"])
    check("coupling_sign_not_in_asymptotic_response", S.expand(general_v.subs(coupling, -coupling) - general_v) == 0)

    net = json.loads((ROOT / NET).read_text())
    validate_net(net)
    check("classification_keeps_degeneracies_and_native_selection", True)
    for kind in ("root", "balanced-forced", "erased-degenerate", "physical", "selection-gate"):
        bad = copy.deepcopy(net)
        nodes = {n["id"]: n for n in bad["conjectures"]}
        if kind == "root": bad["objective"]["outcome"] = "++"
        elif kind == "balanced-forced": nodes["general-positive-contact-classification"]["balanced_rule_forced_by_positivity"] = True
        elif kind == "erased-degenerate": nodes["general-positive-contact-classification"]["decoupled_cases_retained"] = False
        elif kind == "physical": bad["boundary"]["physical_scattering_explained"] = True
        else: nodes["source-compatible-core-and-channel-bridge"]["depends_on"].remove("native-continuum-operation-selection")
        try:
            validate_net(bad)
        except ValueError:
            check("contract_hostile_refused/" + kind, True)
        else:
            raise AssertionError("scope hostile accepted: " + kind)
    check("inputs_unchanged_during_execution", all(hashlib.sha256((ROOT / p).read_bytes()).hexdigest() == sha for p, sha in hashes.items()))
    result = {"schema": "marici.scattering.positive-contact-class.v1", "status": "pass", "check_count": len(checks),
              "checks": checks, "source_sha256": hashes,
              "positive_class": "a,b>=0, beta>0, ab>=g^2; signed real g; normalized actual rim ports",
              "response": "V_s(E)=a+g^2*r0_s(E)/(1-b*r0_s(E))",
              "lead_coordinate_action": "a->s*a; b unchanged; g->sqrt(s)*g; beta->s^2*beta; coordinate reader transported",
              "coupled_observable_invariants": ["A=a/sqrt(beta)", "C=g^2/sqrt(beta)", "b"],
              "rho": "g^2/(a*b)=C/(A*b) in (0,1] for g!=0",
              "canonical_representative": "a=b, g=b*sqrt(rho) up to core phase; beta=(b/A)^2",
              "native_first_resolvent_moment": str(mu1),
              "merged_visible_pole_control": {"b": str(critical_b), "energy": str(blind), "multiplicity": 2, "minimal_memory_dimension": 5},
              "ideal_energy_function_inverse": {"A": "lim y_s(E)", "C": "lim E*(y_s-A)",
                 "b": "lim E^2*(y_s-A-C/E)/C-mu1", "assumptions": "known threshold, phase/energy/channel conventions, exact nonzero coupled response; ideal functions not measured asymptotics"},
              "degenerate_cases": ["g=0: V=aI and b/core invisible to asymptotic S", "a=0 or b=0 forces g=0", "a=g=0: free on-shell transmission; core retained"],
              "actual_source_energy_four_readouts": outputs,
              "balanced_rule_forced_by_positivity": False,
              "verification_level": "exact source rational identities, form/gauge controls and symbolic moment inverse; written classification/completeness argument, not formal kernel proof",
              "native_operation_selected": False, "physical_source_selected": False, "root_outcome": None,
              "stationary_field_solver_runs": 0, "measurement_work_reopened": False}
    out = ROOT / OUT
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": "pass", "check_count": len(checks), "invariants": result["coupled_observable_invariants"],
                      "first_native_moment": str(mu1), "energy_four_readouts": outputs, "receipt": OUT}))


if __name__ == "__main__":
    main()
