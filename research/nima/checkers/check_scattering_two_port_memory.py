# /// script
# dependencies = ["sympy"]
# ///
"""Exact source-addressed port response and retained conservative core memory."""
from pathlib import Path
import copy
import hashlib
import json
import sys
from itertools import combinations
import sympy as S

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(Path(__file__).resolve().parent))
from check_scattering_core_bridge_spectrum import rational_matrix, krylov

PACKET = "research/strominger/results/neutron-two-rim-contact-binding.json"
PREVIOUS = "research/nima/results/scattering-core-bridge-spectrum-v1.json"
OUT = "research/nima/results/scattering-two-port-memory-v1.json"
REPORT = "research/nima/scattering-two-port-memory-v1.md"
CONTRACT = "research/nima/contracts/scattering-core-bridge-work-net.v2.json"


def zero(matrix):
    return all(S.cancel(v) == 0 for v in matrix)


def encoded(matrix):
    return [[str(S.factor(v)) for v in row] for row in matrix.tolist()]


def validate_contract(c):
    nodes = c["conjectures"]
    if c["objective"]["outcome"] is not None or any(n["outcome"] is not None for n in nodes):
        raise ValueError("formal outcomes promoted")
    if (nodes[0]["status"], nodes[0]["verdict"]) != ("resolved", "rejected"):
        raise ValueError("excluded coefficient candidate erased")
    if (nodes[1]["status"], nodes[1]["verdict"]) != ("resolved", "constructed"):
        raise ValueError("response disposition mismatched")
    if nodes[1].get("resolution_kind") != "exact_source_addressed_port_memory_realization":
        raise ValueError("unscoped response")
    if any(n["status"] != "open" for n in nodes[2:]):
        raise ValueError("source selection/root bypass")
    if c["frontier"] != ["native-contact-source-law-audit"] or any(c["boundary"].values()):
        raise ValueError("frontier/boundary bypass")
    if nodes[1].get("physical_source_selected") is not False:
        raise ValueError("conditional response made physical")


def main():
    files = [PACKET, PREVIOUS, REPORT, CONTRACT,
             "research/nima/checkers/check_scattering_core_bridge_spectrum.py",
             "research/strominger/checkers/interface_preserving_carrier_dynamics.py",
             "research/strominger/checkers/check_neutron_autonomous_rim_scattering.py",
             "research/strominger/neutron-autonomous-rim-scattering.md",
             str(Path(__file__).resolve().relative_to(ROOT)).replace("\\", "/")]
    hashes = {p: hashlib.sha256((ROOT / p).read_bytes()).hexdigest() for p in files}
    checks = []

    def check(name, condition):
        if not condition:
            raise AssertionError(name)
        checks.append(name)

    previous = json.loads((ROOT / PREVIOUS).read_text())
    check("prior_spectral_receipt_hashes_live", all(
        hashlib.sha256((ROOT / p).read_bytes()).hexdigest() == h
        for p, h in previous["source_sha256"].items()))
    packet = json.loads((ROOT / PACKET).read_text())
    full = rational_matrix(packet["full_joint_H_without_mu"])
    metric = rational_matrix(packet["source_metric"])[2:, 2:]
    core = full[2:, 2:]
    ports = full[2:, :2] / S.Rational(packet["parameters"]["g"])
    eta, ell = S.Integer(2), S.Integer(1)
    check("full_source_metric_positive", metric.T == metric and all(
        metric[:j, :j].det() > 0 for j in range(1, 25)))
    check("full_bare_core_metric_hermitian", core.T * metric == metric * core)
    check("raw_port_metric_norm_three", ports.T * metric * ports == 3 * S.eye(2))
    dressed = core + eta * ports * ports.T * metric / 3
    basis = krylov(dressed, ports)
    gram = basis.T * metric * basis
    left = gram.inv() * basis.T * metric
    d = left * dressed * basis
    k = left * core * basis
    w = left * ports
    n = S.eye(24) - basis * left
    check("fresh_bright_basis_matches_prior_source_reconstruction",
          basis == rational_matrix(previous["contact_core"]["bright_basis"]) and
          d == rational_matrix(previous["contact_core"]["bright_operator"]))
    check("bright_dimension_five", basis.shape == (24, 5))
    check("bright_metric_positive", all(gram[:j, :j].det() > 0 for j in range(1, 6)))
    check("bare_and_dressed_core_metric_hermitian", k.T * gram == gram * k and d.T * gram == gram * d)
    bare_form = gram * k
    check("bright_bare_core_positive_semidefinite", all(
        bare_form.extract(indices, indices).det() >= 0
        for size in range(1, 6) for indices in combinations(range(5), size)))
    check("bright_dressed_core_positive", all((gram * d)[:j, :j].det() > 0 for j in range(1, 6)))
    check("contact_diagonal_retained", d == k + eta * w * w.T * gram / 3)
    check("dark_projector_retains_nineteen_dimensions", n * n == n and n.rank() == 19)
    check("dark_metric_orthogonal_and_dynamically_reducing", n.T * metric == metric * n and n * dressed == dressed * n)
    check("ports_do_not_drive_or_read_dark_records", n * ports == S.zeros(24, 2) and ports.T * metric * n == S.zeros(2, 24))
    check("full_state_reconstruction_includes_dark_records", basis * left + n == S.eye(24))
    check("bare_core_energy_splits_without_erasing_dark_state", core * basis == basis * k and basis.T * metric * core * n == S.zeros(5, 24))

    e = S.Symbol("E")
    inverse = (e * S.eye(5) - d).inv(method="DM")
    x = (inverse * w).applyfunc(S.cancel)
    response = (w.T * gram * x / 3).applyfunc(S.factor)
    # The symbolic full-core identity proves equality for all resolvent energies
    # without computing a slow 24x24 symbolic inverse or sampling energies.
    check("full24_resolvent_solution_exact", zero((e * S.eye(24) - dressed) * basis * x - ports))
    check("full24_port_response_equals_bright_response", zero(ports.T * metric * basis * x / 3 - response))
    check("response_symmetric", zero(response - response.T))
    check("actual_rim_exchange_symmetry", zero(response - S.Matrix([[response[0, 0], response[0, 1]], [response[0, 1], response[0, 0]]])))
    even = S.factor(response[0, 0] + response[0, 1])
    odd = S.factor(response[0, 0] - response[0, 1])
    parity = S.Matrix([[1, 1], [1, -1]])
    check("exact_even_odd_port_diagonalization", zero(parity.T * response * parity / 2 - S.diag(even, odd)))
    branch_data = {}
    denominator_product = S.Integer(1)
    for name, function in (("even", even), ("odd", odd)):
        numerator, denominator = S.fraction(S.cancel(function))
        num_poly, den_poly = S.Poly(numerator, e), S.Poly(denominator, e)
        check(name + "_no_pole_cancellation", S.gcd(num_poly, den_poly).degree() == 0)
        check(name + "_strictly_proper", num_poly.degree() < den_poly.degree())
        branch_data[name] = {"response": str(function), "numerator": str(numerator),
                             "denominator": str(denominator), "pole_count": den_poly.degree()}
        denominator_product *= den_poly.monic().as_expr()
    characteristic = d.charpoly(e).as_expr()
    check("all_five_bright_poles_are_visible", S.expand(denominator_product - characteristic) == 0)
    check("five_poles_simple", S.gcd(S.Poly(characteristic, e), S.Poly(characteristic, e).diff()).degree() == 0)
    check("high_energy_normalization_is_identity", w.T * gram * w / 3 == S.eye(2))
    effective = eta * ell * S.eye(2) + eta ** 2 * ell * response
    check("contact_direct_term_not_discarded", zero(effective - 2 * S.eye(2) - 4 * response))
    check("resolvent_derivative_identity", zero(response.diff(e) + w.T * gram * inverse * inverse * w / 3))

    # Positive metric plus Hermitian d implies observability from controllability.
    # Direct exact Hankel rank gives a bound even for general finite linear I/O realizations.
    moments = [(w.T * gram * d ** j * w / 3) for j in range(9)]
    hankel = S.BlockMatrix([[moments[i + j] for j in range(5)] for i in range(5)]).as_explicit()
    check("port_memory_hankel_rank_five", hankel.rank() == 5)
    observable = S.Matrix.vstack(*(w.T * gram * d ** j for j in range(5)))
    check("port_memory_observability_rank_five", observable.rank() == 5)

    # Basis covariance without a second expensive inverse: X'=T^-1 X.
    t = S.eye(5)
    t[0, 1], t[2, 4] = 2, -3
    tp = t.inv()
    transformed_d, transformed_w, transformed_g = tp * d * t, tp * w, t.T * gram * t
    transformed_x = tp * x
    check("core_coordinate_covariance", zero((e * S.eye(5) - transformed_d) * transformed_x - transformed_w) and
          zero(transformed_w.T * transformed_g * transformed_x / 3 - response))
    u = S.Matrix([[S.Rational(3, 5), -S.Rational(4, 5)], [S.Rational(4, 5), S.Rational(3, 5)]])
    check("port_frame_covariance", u.T * u == S.eye(2) and zero((w * u).T * gram * (x * u) / 3 - u.T * response * u))
    check("normalization_hostile_detected", w.T * gram * w != S.eye(2))
    check("contact_diagonal_hostile_detected", d != k)
    check("memoryless_hostile_detected", any(S.cancel(v) != 0 for v in response.diff(e)))

    contract = json.loads((ROOT / CONTRACT).read_text())
    validate_contract(contract)
    check("new_contract_constructed_response_keeps_source_selection_and_root_open", True)
    for kind in ("root", "erased-rejection", "source-selection", "physical", "unscoped-response"):
        bad = copy.deepcopy(contract)
        if kind == "root": bad["objective"]["outcome"] = "++"
        elif kind == "erased-rejection": bad["conjectures"][0]["verdict"] = "constructed"
        elif kind == "source-selection": bad["conjectures"][2]["status"] = "resolved"
        elif kind == "physical": bad["conjectures"][1]["physical_source_selected"] = True
        else: bad["conjectures"][1]["resolution_kind"] = "physical_scattering_explanation"
        try:
            validate_contract(bad)
        except ValueError:
            check("contract_hostile_refused/" + kind, True)
        else:
            raise AssertionError("contract hostile accepted: " + kind)
    check("inputs_unchanged_during_execution", all(hashlib.sha256((ROOT / p).read_bytes()).hexdigest() == h for p, h in hashes.items()))
    result = {
        "schema": "marici.scattering.two-port-memory.v1", "status": "pass", "check_count": len(checks),
        "checks": checks, "source_sha256": hashes, "verification_level": "exact rational source-matrix and transfer-function identities; written minimality/passivity argument, not formal kernel proof",
        "model": "principal autonomous neutron two-rim contact; eta=2, ell=1; no strained pentachoron identification",
        "response_R": encoded(response), "effective_boundary_V": encoded(effective),
        "parity_branches": branch_data, "visible_pole_polynomial": str(S.factor(characteristic)),
        "bright_basis": encoded(basis), "bright_metric": encoded(gram), "bright_bare_core": encoded(k),
        "bright_dressed_core": encoded(d), "bright_ports_raw": encoded(w), "dark_projector": encoded(n),
        "moment_matrices_zero_through_eight": [encoded(m) for m in moments],
        "minimal_finite_linear_memory_dimension": 5, "retained_dark_dimension": 19,
        "bare_bright_kernel_dimension": 5 - k.rank(),
        "bare_core_positive_semidefinite": True, "dressed_bright_core_positive_definite": True,
        "conservative_memory_law": "i*hbar*q'=D_bright*q-(eta*sqrt(ell)/sqrt(3))*W_raw_bright*psi(0); full dark state retained independently",
        "boundary_observation": "sqrt(ell)*psi(0)-W_raw_bright^T*G_bright*q/sqrt(3)",
        "root_outcome": None, "physical_source_selected": False, "stationary_scattering_solves": 0,
        "historical_pins_rewritten": False, "source_owner_files_changed": False,
    }
    out = ROOT / OUT
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": "pass", "check_count": len(checks), "parity_branches": branch_data,
                      "minimal_memory_dimension": 5, "receipt": OUT}))


if __name__ == "__main__":
    main()
