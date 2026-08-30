import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results"


def load(name):
    return json.loads((RESULTS / name).read_text(encoding="utf-8"))


wp738 = load("wp738_required_link_mediators_fixed_point_exhaustion.json")
wp744 = load("wp744_so5_anomaly_quantization_type_no_go.json")
wp854 = load("wp854_oriented_unitary_cycle_boundary_compression_constructor.json")
wp855 = load("wp855_boundary_current_readout_hierarchy.json")

T, g1, g2, s = sp.symbols("T g1 g2 s", nonnegative=True)
kappa_a = -sp.Rational(6, 103) * (4 * T + 12 * g1 + 53 * g2)
kappa_hostile = sp.expand(kappa_a + s / 103)

tests = {
    "wp735_shared_field_mate_is_nonpositive": sp.ask(
        sp.Q.nonpositive(kappa_a), sp.Q.nonnegative(T) & sp.Q.nonnegative(g1) & sp.Q.nonnegative(g2)
    ) is True,
    "wp738_exhausts_256_compulsory_mediator_branches": wp738["exact_branch_count"] == 256,
    "wp738_has_no_physical_branch": wp738["physical_branch_count"] == 0,
    "wp738_fully_interacting_color_is_negative": sp.Rational(
        wp738["fully_interacting_hostile_witness"]["alpha_3"]
    ) < 0,
    "wp738_fully_interacting_su2b_is_negative": sp.Rational(
        wp738["fully_interacting_hostile_witness"]["alpha_B"]
    ) < 0,
    "wp744_has_wrong_portal_operator_type": wp744["checks"][
        "chern_simons_reduction_has_wrong_operator_signature"
    ],
    "wp854_lacks_microscopic_flavor_map": "derive the flavor cycle and boundary microscopically"
    in wp854["remaining_gates"],
    "wp854_lacks_normalized_portal_map": "map defect current to normalized g_n-g_m"
    in wp854["remaining_gates"],
    "wp855_is_a_detector_instrument_gate": "source-derived pre-projection difference channel"
    in wp855["instrument_gate"],
    "smallest_integer_coefficient_laundering_hostile": kappa_hostile.subs(
        {T: 0, g1: 1, g2: 0, s: 72}
    ) == 0
    and kappa_hostile.subs({T: 0, g1: 1, g2: 0, s: 73}) == sp.Rational(1, 103),
}
tests = {name: bool(value) for name, value in tests.items()}

result = {
    "work_package": "WP876",
    "status": "PASS" if all(tests.values()) else "FAIL",
    "summary": {"passed": sum(tests.values()), "total": len(tests), "all_passed": all(tests.values())},
    "tests": tests,
    "admitted_source_domain": "WP736 product-group parent plus only the WP738 vectorlike mediators compelled by link-generated Standard Model Yukawas",
    "aspect_outer_mate": "shared-field anomalous dimensions must be formed before separate singlet/triplet completion",
    "largest_source_authorized_beta_modifying_family": "WP738 compulsory link-mediator Lagrangian",
    "contextual_partition": {
        "pre_quotient_dynamical_source": ["WP738 compulsory link mediators"],
        "different_operator_type": ["WP744 anomaly/Chern-Simons response"],
        "unmapped_relational_carrier": ["WP854 oriented-cycle return link"],
        "post_source_instrument": ["WP855 complementary difference port"],
    },
    "classification": "no currently adjacent compulsory object repairs the simultaneous fixed-point source; WP736 remains only a matching-scale selector",
    "smallest_exact_falsifier": "at T=0, g1=1, g2=0 an untyped correction s=73 changes kappa_A from -72/103 to 1/103",
    "remaining_source_gate": "derive new Yukawa-active matter, multiplicities, and vertices from one independent source principle before computing the fixed point",
    "remaining_physical_instrument_gate": "after source existence, derive threshold intertwining and a calibrated rank-sufficient physical16 response",
}

out = RESULTS / "wp876_source_compelled_simultaneous_portal_repair_closure.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result["summary"], indent=2))
if not all(tests.values()):
    raise SystemExit(1)
