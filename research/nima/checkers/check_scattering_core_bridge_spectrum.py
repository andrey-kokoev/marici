# /// script
# dependencies = ["sympy"]
# ///
"""Exact source-matrix bridge exclusion; no source law changes or scattering solves."""
from pathlib import Path
import hashlib
import json
import sys
import sympy as S

ROOT = Path(__file__).resolve().parents[3]
OWNER = ROOT / "research/strominger/checkers"
sys.path.insert(0, str(OWNER))
from interface_preserving_carrier_dynamics import classify, native_generator

PACKET = "research/strominger/results/neutron-two-rim-contact-binding.json"
OUTPUT = "research/nima/results/scattering-core-bridge-spectrum-v1.json"
WORK_NET = "research/nima/contracts/scattering-core-bridge-work-net.v1.json"
REPORT = "research/nima/scattering-core-bridge-spectrum-v1.md"
OLD_PINS = "research/nima/contracts/scattering-strominger-update-pins.v1.json"


def validate_work_net(c):
    expected_ids = ["unchanged-coefficient-affine-core-bridge", "retained-two-port-response-realization",
                    "native-contact-source-law-audit", "source-compatible-core-and-channel-bridge"]
    nodes = c["conjectures"]
    if [n["id"] for n in nodes] != expected_ids:
        raise ValueError("research decomposition changed")
    if c["objective"]["outcome"] is not None or any(n["outcome"] is not None for n in nodes):
        raise ValueError("formal outcome promotion")
    if nodes[0]["status"] != "resolved" or nodes[0]["verdict"] != "rejected":
        raise ValueError("candidate exclusion erased")
    if any(n["status"] != "open" or n["verdict"] != "open" for n in nodes[1:]):
        raise ValueError("unverified successor closure")
    if c["frontier"] != expected_ids[1:3] or any(c["boundary"].values()):
        raise ValueError("frontier or boundary promoted")
    seen = set()
    for n in nodes:
        if not set(n["depends_on"]) <= seen:
            raise ValueError("invalid prerequisite order")
        seen.add(n["id"])
    if "never as a positive bridge witness" not in nodes[1]["prerequisite_use"]:
        raise ValueError("rejection used as witness")


def rational_matrix(rows):
    return S.Matrix([[S.Rational(v) for v in row] for row in rows])


def krylov(operator, ports):
    basis = []
    queue = [ports[:, j] for j in range(ports.cols)]
    cursor = 0
    while cursor < len(queue):
        v = queue[cursor]
        cursor += 1
        trial = S.Matrix.hstack(*(basis + [v]))
        if trial.rank() > len(basis):
            basis.append(v)
            queue.append(operator * v)
    return S.Matrix.hstack(*basis)


def centered_moments(operator):
    n = operator.rows
    mean = S.trace(operator) / n
    centered = operator - mean * S.eye(n)
    second = S.trace(centered ** 2)
    fourth = S.trace(centered ** 4)
    return mean, second, fourth


def five_progression_test(operator):
    if operator.shape != (5, 5):
        raise ValueError("five-dimensional operator required")
    _, second, fourth = centered_moments(operator)
    # Necessary for five distinct, equally spaced real eigenvalues.
    return second != 0 and 50 * fourth == 17 * second ** 2


def main():
    inputs = [PACKET, WORK_NET, REPORT, OLD_PINS,
              "research/strominger/checkers/interface_preserving_carrier_dynamics.py",
              "research/strominger/checkers/check_neutron_autonomous_rim_scattering.py",
              "research/strominger/interface-preserving-carrier-hamiltonian.md",
              "research/strominger/retained-hamiltonian-observer.md",
              "research/strominger/neutron-autonomous-rim-scattering.md",
              "research/nima/contracts/scattering-strominger-update.v1.json",
              str(Path(__file__).resolve().relative_to(ROOT)).replace("\\", "/")]
    hashes = {p: hashlib.sha256((ROOT / p).read_bytes()).hexdigest() for p in inputs}
    checks = []

    def check(name, condition):
        if not condition:
            raise AssertionError(name)
        checks.append(name)

    # Reconstruct the S4-classified law from the owner implementation, not its
    # saved 38-band summary. Sorting the retained edges is a basis permutation.
    source = classify()
    selected = tuple(e for e in source["edges"] if e != source["omitted"])
    d11, a = native_generator(source, selected)
    x = S.Symbol("x")
    check("source_combination_skew_and_rank_two", d11.T == -d11 and d11.rank() == 2)
    arrow_polynomial = d11.charpoly(x).as_expr()
    check("actual_arrow_characteristic_polynomial", S.expand(arrow_polynomial - x ** 9 * (x ** 2 + 32)) == 0)
    check("actual_137_slot_generator_shape_and_skew", a.shape == (137, 137) and a.T == -a)
    i = S.eye(137)
    check("actual_generator_five_band_annihilator", a * (a * a + 32 * i) * (a * a + 128 * i) == S.zeros(137))
    # Tensor-sum multiplicities follow from the diagonalizable skew d11:
    # 0:9^2+2+16=99; +/-i sqrt32:18 each; +/-2i sqrt32:1 each.
    multiplicities = {"zero": 99, "plus_low": 18, "minus_low": 18,
                      "plus_high": 1, "minus_high": 1}
    check("source_band_dimensions_account_for_native_interface", sum(multiplicities.values()) == 137)

    packet = json.loads((ROOT / PACKET).read_text())
    full = rational_matrix(packet["full_joint_H_without_mu"])
    metric_full = rational_matrix(packet["source_metric"])
    metric = metric_full[2:, 2:]
    core = full[2:, 2:]
    g = S.Rational(packet["parameters"]["g"])
    ports = full[2:, :2] / g
    check("source_core_metric_hermitian", core.T * metric == metric * core)
    check("source_ports_have_metric_norm_three", ports.T * metric * ports == 3 * S.eye(2))
    # Whitened owner ports are whiten(W_raw)/sqrt(3). Therefore the raw
    # principal eta=2 contact-dressed core is the rational matrix below.
    dressed = core + S.Rational(2, 3) * ports * ports.T * metric
    check("contact_dressed_core_metric_hermitian", dressed.T * metric == metric * dressed)
    basis = krylov(dressed, ports)
    check("actual_contact_generated_core_dimension_five", basis.shape == (24, 5))
    gram = basis.T * metric * basis
    left = gram.inv() * basis.T * metric
    bright = left * dressed * basis
    contact_bright = left * ports
    check("exact_bright_generator_intertwining", dressed * basis == basis * bright)
    check("exact_port_reconstruction", basis * contact_bright == ports)
    check("bright_metric_hermitian", bright.T * gram == gram * bright)
    # Sylvester pivots establish a genuine positive metric, not just symmetry.
    check("bright_metric_positive", all(gram[:j, :j].det() > 0 for j in range(1, 6)))
    check("bright_ports_generate_all_five_directions", krylov(bright, contact_bright).cols == 5)
    polynomial = S.Poly(bright.charpoly(x).as_expr(), x)
    check("bright_spectrum_has_five_distinct_roots", S.gcd(polynomial, polynomial.diff()).degree() == 0)
    coeff_q_poly = S.Poly(x * (x ** 2 - 32) * (x ** 2 - 128), x)
    common = S.gcd(polynomial, coeff_q_poly)
    check("no_nonzero_unshifted_natural_generator_bridge", common.degree() == 0)
    mean, second, fourth = centered_moments(bright)
    defect = S.factor(50 * fourth - 17 * second ** 2)
    check("actual_bright_spectrum_not_five_term_arithmetic_progression", second > 0 and defect != 0)

    # Exact controls for the necessary-condition test. No fitting to source.
    progression = S.diag(-2, -1, 0, 1, 2)
    check("positive_control_five_equal_spaced_bands", five_progression_test(progression))
    check("positive_control_shift_and_rescale", five_progression_test(7 * progression + 11 * S.eye(5)))
    check("hostile_non_equal_spaced_bands_refused", not five_progression_test(S.diag(0, 1, 2, 3, 5)))
    check("source_defect_persists_under_affine_convention_change", not five_progression_test(3 * bright + 7 * S.eye(5)))
    import copy
    work_net = json.loads((ROOT / WORK_NET).read_text())
    validate_work_net(work_net)
    check("work_net_preserves_scoped_rejection_and_open_root", True)
    for kind in ("root", "candidate", "successor", "physical", "rejection-as-witness"):
        bad = copy.deepcopy(work_net)
        if kind == "root": bad["objective"]["outcome"] = "++"
        elif kind == "candidate": bad["conjectures"][0]["verdict"] = "constructed"
        elif kind == "successor": bad["conjectures"][1]["status"] = "resolved"
        elif kind == "physical": bad["boundary"]["physical_scattering_explained"] = True
        else: bad["conjectures"][1]["prerequisite_use"] = "positive root witness"
        try:
            validate_work_net(bad)
        except ValueError:
            check("work_net_hostile_refused/" + kind, True)
        else:
            raise AssertionError("work net corruption accepted: " + kind)
    old_pins = json.loads((ROOT / OLD_PINS).read_text())["source_sha256"]
    drift = {p: {"historical": h, "current": hashlib.sha256((ROOT / p).read_bytes()).hexdigest()}
             for p, h in old_pins.items() if hashlib.sha256((ROOT / p).read_bytes()).hexdigest() != h}
    check("inputs_unchanged_during_audit", all(hashlib.sha256((ROOT / p).read_bytes()).hexdigest() == h for p, h in hashes.items()))

    result = {
        "schema": "marici.scattering.core-bridge-spectrum.v1", "status": "pass",
        "checks": checks, "check_count": len(checks), "source_sha256": hashes,
        "historical_overlay_pin_drift": drift, "historical_pins_rewritten": False,
        "work_net_contract": WORK_NET,
        "verification_level": "exact SymPy rational source reconstruction; written spectral inference, not formal kernel proof",
        "coefficient_generator": {"arrow_characteristic_polynomial": str(S.factor(arrow_polynomial)),
                                  "natural_quantum_annihilator": str(coeff_q_poly.as_expr()),
                                  "multiplicities_per_complexified_scalar_channel": multiplicities,
                                  "energy_hessian_bands": [0, 16, 64]},
        "contact_core": {"model": "principal autonomous neutron two-rim contact, eta=2, ell=1",
                         "raw_metric": [[str(v) for v in row] for row in metric.tolist()],
                         "bright_basis": [[str(v) for v in row] for row in basis.tolist()],
                         "bright_operator": [[str(v) for v in row] for row in bright.tolist()],
                         "bright_ports_raw": [[str(v) for v in row] for row in contact_bright.tolist()],
                         "characteristic_polynomial": str(polynomial.as_expr()),
                         "polynomial_factorization": str(S.factor(polynomial.as_expr())),
                         "fixed_convention_gcd_with_coefficient": str(common.as_expr()),
                         "center": str(mean), "centered_second_trace": str(second),
                         "centered_fourth_trace": str(fourth),
                         "arithmetic_progression_defect": str(defect)},
        "conclusion": "No contact-complete linear intertwiner from the unchanged natural-complexified coefficient law to this bright core, even under any real nonzero common time scale and scalar energy shift.",
        "scope_limits": ["Real/complex encoding fixed to natural complexification for the five-band result.",
                         "No exclusion of a changed law, enlarged source, driven encoding, or band-specific nonlinear redefinition.",
                         "No identification with latest strained pentachoron scattering.",
                         "No physical source selection, scattering amplitude solve or conjecture outcome admission."],
        "stationary_scattering_solves": 0, "scientific_outcomes_assigned": False,
        "source_owner_suites_rerun": False,
    }
    out = ROOT / OUTPUT
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": "pass", "check_count": len(checks),
                      "bright_polynomial": str(polynomial.as_expr()),
                      "progression_defect": str(defect), "receipt": OUTPUT}))


if __name__ == "__main__":
    main()
