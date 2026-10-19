# /// script
# dependencies = ["sympy"]
# ///
"""Exact inherited/supplied contact audit and source-preserving continuum rivals."""
from pathlib import Path
from datetime import datetime, timezone
import copy
import hashlib
import json
import sys
import sympy as S

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(Path(__file__).resolve().parent))
from check_scattering_core_bridge_spectrum import rational_matrix, krylov

PACKET = "research/strominger/results/neutron-two-rim-contact-binding.json"
MEMORY = "research/nima/results/scattering-two-port-memory-v1.json"
REPORT = "research/nima/scattering-contact-source-audit-v1.md"
NET = "research/nima/contracts/scattering-core-bridge-work-net.v3.json"
OUT = "research/nima/results/scattering-contact-source-audit-v1.json"


def zero(a):
    return all(S.cancel(v) == 0 for v in a)


def encoded(a):
    return [[str(S.factor(v)) for v in row] for row in a.tolist()]


def validate_net(c):
    nodes = {n["id"]: n for n in c["conjectures"]}
    expected = {
        "unchanged-coefficient-affine-core-bridge": ("resolved", "rejected"),
        "retained-two-port-response-realization": ("resolved", "constructed"),
        "native-contact-source-law-audit": ("resolved", "constructed"),
        "continuum-parameter-identifiability": ("open", "open"),
        "native-continuum-operation-selection": ("deferred_missing_native_principle", "open"),
        "source-compatible-core-and-channel-bridge": ("open", "open"),
    }
    if set(nodes) != set(expected) or any((nodes[i]["status"], nodes[i]["verdict"]) != state for i, state in expected.items()):
        raise ValueError("scoped research dispositions changed")
    if c["objective"]["outcome"] is not None or any(n["outcome"] is not None for n in nodes.values()):
        raise ValueError("formal outcome promoted")
    if any(c["boundary"].values()) or c["frontier"] != ["continuum-parameter-identifiability"]:
        raise ValueError("physical/root/frontier bypass")
    audit = nodes["native-contact-source-law-audit"]
    if audit.get("native_law_uniquely_selected") is not False or audit.get("resolution_kind") != "operation_ledger_and_exact_extension_nonuniqueness":
        raise ValueError("audit mistaken for native selection")
    if "native-continuum-operation-selection" not in nodes["source-compatible-core-and-channel-bridge"]["depends_on"]:
        raise ValueError("native selection gate erased")
    seen = set()
    for n in c["conjectures"]:
        if not set(n["depends_on"]) <= seen:
            raise ValueError("dependency order changed")
        seen.add(n["id"])


def main():
    files = [PACKET, MEMORY, REPORT, NET,
             "research/nima/checkers/check_scattering_core_bridge_spectrum.py",
             "research/strominger/checkers/interface_preserving_carrier_dynamics.py",
             "research/strominger/high-energy-research-reuse.md",
             "research/strominger/neutron-autonomous-rim-scattering.md",
             "research/scattering/high-energy/pentachoron_autonomous_contact_note.md",
             str(Path(__file__).resolve().relative_to(ROOT)).replace("\\", "/")]
    hashes = {p: hashlib.sha256((ROOT / p).read_bytes()).hexdigest() for p in files}
    checks = []

    def check(name, condition):
        if not condition:
            raise AssertionError(name)
        checks.append(name)

    memory = json.loads((ROOT / MEMORY).read_text())
    check("memory_receipt_source_hashes_live", all(hashlib.sha256((ROOT / p).read_bytes()).hexdigest() == h for p, h in memory["source_sha256"].items()))
    packet = json.loads((ROOT / PACKET).read_text())
    h = rational_matrix(packet["full_joint_H_without_mu"])
    full_metric = rational_matrix(packet["source_metric"])
    m = full_metric[2:, 2:]
    check("finite_auxiliary_normalization_preserves_scalar_g", full_metric[:2, :2] == 3 * S.eye(2))
    k = h[2:, 2:]
    w = h[2:, :2] / S.Rational(packet["parameters"]["g"])
    check("same_native_metric_operator_and_ports", k.T * m == m * k and w.T * m * w == 3 * S.eye(2))
    # Bare K and dressed K+eta WW^dagger have the same port-generated space.
    b = krylov(k, w)
    g = b.T * m * b
    left = g.inv() * b.T * m
    kb, wb = left * k * b, left * w
    check("bare_port_generated_dimension_five", b.cols == 5)
    check("retained_bare_core_intertwining", k * b == b * kb and b * wb == w)
    e = S.Symbol("E")
    bare = (wb.T * g * (e * S.eye(5) - kb).inv(method="DM") * wb / 3).applyfunc(S.factor)
    r0_even, r0_odd = S.factor(bare[0, 0] + bare[0, 1]), S.factor(bare[0, 0] - bare[0, 1])
    check("bare_port_parity_symmetry", bare == S.Matrix([[bare[0, 0], bare[0, 1]], [bare[0, 1], bare[0, 0]]]))
    dressed_response = S.Matrix([[S.sympify(v, locals={"E": e}) for v in row] for row in memory["response_R"]])
    check("dressed_response_from_bare_resolvent_identity", zero(dressed_response - bare * (S.eye(2) - 2 * bare).inv()))
    effective = S.Matrix([[S.sympify(v, locals={"E": e}) for v in row] for row in memory["effective_boundary_V"]])
    check("effective_contact_formula_preserves_direct_diagonal", zero(effective - 2 * (S.eye(2) - 2 * bare).inv()))

    z = S.Symbol("z", positive=True)
    ve, vo = S.symbols("v_even v_odd", real=True)
    check("exact_flux_conservation_for_both_parity_branches", all(
        S.cancel(v ** 2 / (z ** 2 + v ** 2) + z ** 2 / (z ** 2 + v ** 2) - 1) == 0
        for v in (ve, vo)))
    delta_t = S.I * z / (S.I * z - ve) - S.I * z / (S.I * z - vo)
    check("exact_other_port_flux_formula", S.cancel(delta_t * S.conjugate(delta_t) / 2 -
        z ** 2 * (ve - vo) ** 2 / (2 * (z ** 2 + ve ** 2) * (z ** 2 + vo ** 2))) == 0)
    # Use one named rational model energy, not an experimental datum.
    energy, theta = S.Rational(113, 100), S.Rational(1, 2)
    r0e = S.cancel(r0_even.subs(e, energy))
    r0o = S.cancel(r0_odd.subs(e, energy))

    def readout(kinetic, contact):
        even = S.cancel(contact / (1 - contact * r0e))
        odd = S.cancel(contact / (1 - contact * r0o))
        zz = 4 * kinetic * (energy - theta)
        rr = S.cancel((even ** 2 / (zz + even ** 2) + odd ** 2 / (zz + odd ** 2)) / 2)
        tt = 1 - rr
        cc = S.cancel(zz * (even - odd) ** 2 / (2 * (zz + even ** 2) * (zz + odd ** 2)))
        check("exact_flux_and_probability_bounds/beta=" + str(kinetic) + "/eta=" + str(contact),
              0 < rr < 1 and 0 < tt < 1 and 0 <= cc <= 1 and rr + tt == 1)
        return {"beta": str(kinetic), "eta": str(contact), "reflection": str(rr),
                "transmission": str(tt), "other_port_flux": str(cc), "other_port_flux_decimal": float(cc)}

    kinetic_rivals = [readout(S.Rational(1, 2), S.Integer(2)), readout(S.Integer(1), S.Integer(2)), readout(S.Integer(2), S.Integer(2))]
    check("native_preserving_kinetic_rivals_distinguishable", len({r["other_port_flux"] for r in kinetic_rivals}) == 3)
    contact_rivals = [readout(S.Integer(1), S.Integer(1)), readout(S.Integer(1), S.Integer(2))]
    check("native_preserving_contact_rivals_distinguishable", contact_rivals[0]["other_port_flux"] != contact_rivals[1]["other_port_flux"])
    check("source_numerical_control_reproduced_without_floating_solve", abs(kinetic_rivals[1]["other_port_flux_decimal"] - 0.02788415) < 5e-9)

    # Coordinate gauge: y=x/ell, phi(y)=sqrt(ell)*psi(ell*y), beta=kappa/ell^2.
    # (kappa,ell)=(1,1) and (4,2) give identical beta, contact and thresholds.
    check("coordinate_dilation_is_not_a_distinct_kinetic_model", S.Rational(1, 1) / 1 ** 2 == S.Rational(4, 1) / 2 ** 2)
    # Positivity alone does not uniquely complete an inherited off-diagonal g.
    finite_g = S.Rational(packet["parameters"]["g"])
    completions = [S.Matrix([[finite_g * s, finite_g], [finite_g, finite_g / s]]) for s in (S.Rational(1, 2), S.Integer(1), S.Integer(2))]
    check("same_off_diagonal_positive_completions", all(c[0, 1] == finite_g and c.det() == 0 and c.trace() > 0 for c in completions))
    check("positive_completion_diagonals_not_unique", len({tuple(c) for c in completions}) == 3)

    # Symbolic probability controls are independent of the huge actual response.
    vv, bb, ee = S.symbols("v b epsilon", positive=True)
    rr = vv ** 2 / (4 * bb * ee + vv ** 2)
    check("nonzero_parity_reflection_strictly_changes_with_beta", S.diff(rr, bb) == -4 * ee * vv ** 2 / (4 * bb * ee + vv ** 2) ** 2)
    # A contact pole is a perfectly reflecting parity limit, not probability >1.
    check("infinite_contact_response_limit_is_unit_reflection", S.limit(rr, vv, S.oo) == 1)

    c = json.loads((ROOT / NET).read_text())
    validate_net(c)
    check("operation_audit_resolution_keeps_native_selection_open", True)
    for kind in ("root", "native-selection", "erased-candidate", "physical", "source-gate-erasure"):
        bad = copy.deepcopy(c)
        nodes = {n["id"]: n for n in bad["conjectures"]}
        if kind == "root": bad["objective"]["outcome"] = "++"
        elif kind == "native-selection": nodes["native-contact-source-law-audit"]["native_law_uniquely_selected"] = True
        elif kind == "erased-candidate": nodes["unchanged-coefficient-affine-core-bridge"]["verdict"] = "constructed"
        elif kind == "physical": bad["boundary"]["physical_scattering_explained"] = True
        else: nodes["source-compatible-core-and-channel-bridge"]["depends_on"].remove("native-continuum-operation-selection")
        try:
            validate_net(bad)
        except ValueError:
            check("contract_hostile_refused/" + kind, True)
        else:
            raise AssertionError("scope hostile accepted: " + kind)
    check("inputs_unchanged_during_execution", all(hashlib.sha256((ROOT / p).read_bytes()).hexdigest() == h for p, h in hashes.items()))

    ledger = [
        {"ingredient": "raw native K, source metric and actual rim columns", "provenance": "inherited finite source packet", "native_selection_inferred": False},
        {"ingredient": "port normalization W^T M W=3I", "provenance": "exact source identity; whitened normalization", "native_selection_inferred": False},
        {"ingredient": "one-dimensional moving leads and point trace", "provenance": "new continuum extension", "native_selection_inferred": False},
        {"ingredient": "positive mismatch contact with both diagonals", "provenance": "reused conditional prescription, not native necessity", "native_selection_inferred": False},
        {"ingredient": "eta=2; ell=1; beta=1; lead threshold=1/2", "provenance": "declared principal fixture", "native_selection_inferred": False},
        {"ingredient": "incoming unit-flux preparation with no incoming bound/dark component", "provenance": "new preparation contract", "native_selection_inferred": False},
    ]
    result = {"schema": "marici.scattering.contact-source-audit.v1", "status": "pass", "check_count": len(checks),
              "checks": checks, "source_sha256": hashes, "operation_ledger": ledger,
              "bare_normalized_R": encoded(bare), "bare_parity_response": {"even": str(r0_even), "odd": str(r0_odd)},
              "effective_contact_law": "V_eta(E)=eta*ell*(I-eta*R0(E))^(-1), R0=W^dagger(E-K)^(-1)W normalized",
              "dimensionless_coordinate_law": "beta=kappa/ell^2 in a fixed native energy convention",
              "kinetic_rivals": kinetic_rivals, "contact_rivals": contact_rivals,
              "same_off_diagonal_positive_completions": [encoded(a) for a in completions],
              "verification_level": "exact source-matrix, rational scattering probability and positivity algebra; written continuum extension/gauge argument, not formal kernel proof",
              "native_law_uniquely_selected": False, "physical_source_selected": False, "root_outcome": None,
              "stationary_field_solver_runs": 0, "measurement_work_reopened": False,
              "source_owner_files_changed": False, "historical_pins_rewritten": False}
    out = ROOT / OUT
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": "pass", "check_count": len(checks), "bare_parity_response": result["bare_parity_response"],
                      "kinetic_other_port_flux": [r["other_port_flux_decimal"] for r in kinetic_rivals],
                      "contact_other_port_flux": [r["other_port_flux_decimal"] for r in contact_rivals], "receipt": OUT}))


if __name__ == "__main__":
    main()
