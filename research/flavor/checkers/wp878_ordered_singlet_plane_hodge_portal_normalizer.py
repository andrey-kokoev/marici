import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]


def load(path):
    return json.loads(path.read_text(encoding="utf-8"))


wp877 = load(ROOT / "results" / "wp877_sequential_so5_two_vector_projector_repair.json")
strominger = load(ROOT.parent / "strominger" / "results" / "celestial_hodge_bridge_checks.json")
sontag = load(ROOT.parent / "sontag" / "results" / "physical_diversity_disturbance_excitation.json")
aspect = load(ROOT.parent / "aspect" / "results" / "reflection_component_path_tomography.json")

eu = sp.Matrix([1, 0])
ev = sp.Matrix([0, 1])
Pu = eu * eu.T
Pv = ev * ev.T
P2 = sp.eye(2)
J = ev * eu.T - eu * ev.T
H = Pv - Pu

a, b, c, theta = sp.symbols("a b c theta", real=True)
S = a * Pu + b * Pv
Jinv = -J
odd_residual = sp.expand(J * S * Jinv + S)
primitive_residual = sp.expand((c * H) ** 2 - P2)
R = sp.cos(theta) * P2 + sp.sin(theta) * J

response_rank_two = sp.eye(2)
inclusive_response = sp.Matrix([[1, 1]])

tests = {
    "wp877_source_projector_packet_passed": wp877["summary"]["all_passed"],
    "strominger_real_hodge_bridge_passed": strominger["status"] == "passed" and strominger["passed"] == strominger["total"] == 11,
    "sontag_two_excitation_rank_test_passed": sontag["passed"] == sontag["total"] == 8,
    "aspect_path_tomography_passed": aspect["status"] == "pass",
    "real_complex_structure_is_skew": J.T == -J,
    "real_complex_structure_squares_to_minus_identity": J**2 == -P2,
    "complex_structure_exchanges_source_projectors": J * Pu * Jinv == Pv and J * Pv * Jinv == Pu,
    "oddness_forces_opposite_diagonal_coefficients": odd_residual == (a + b) * P2,
    "primitive_ordered_contrast_is_an_involution": H**2 == P2,
    "hodge_and_contrast_anticommute": J * H + H * J == sp.zeros(2),
    "nonunit_scaling_fails_primitive_normalization": primitive_residual.subs(c, 2) == 3 * P2,
    "generic_hodge_rotation_leaves_projector_stabilizer": sp.simplify((R * Pu * R.T - Pu).subs(theta, sp.pi / 4)) != sp.zeros(2),
    "two_independent_source_excitations_have_rank_two": response_rank_two.rank() == 2,
    "inclusive_readout_erases_one_direction": inclusive_response.rank() == 1 and len(inclusive_response.nullspace()) == 1,
}
tests = {name: bool(value) for name, value in tests.items()}

result = {
    "work_package": "WP878",
    "status": "PASS" if all(tests.values()) else "FAIL",
    "summary": {"passed": sum(tests.values()), "total": len(tests), "all_passed": all(tests.values())},
    "source_domain": "WP877 ordered orthogonal singlet projectors with retained two-stage SO(5)->SO(4)->SO(3) provenance",
    "faithful_coordinate": "ordered real Clifford packet (Pu,Pv,J,H) plus common physical coupling and co-moving connection",
    "source_authorized_operation": "H=Pv-Pu, uniquely fixed by projector diagonality, Hodge oddness, primitive unit normalization, and ordered-stage sign",
    "transfers": {
        "strominger": "oriented real two-plane supplies source complex structure without scalar extension",
        "grothendieck": "moving source frame requires a co-moving incidence/connection rather than a frozen normalized row",
        "sontag": "physical diversity requires two independent source excitations and rank-two calibrated response",
        "aspect": "algebraic generator existence does not authorize a path that leaves the prepared-projector stabilizer",
        "kitaev": "flattened scalar output must retain a constructor-history port if labelled reconstruction is claimed",
        "nima": "pairwise source/RG/threshold/readout compatibility does not replace the higher coherence of their complete composite",
        "buzzard": "a selected detector-port zero may be a transmission zero while a complementary labelled output remains bright",
        "benincasa": "shared endpoint terminology does not type an action or comparison map between distinct source objects",
    },
    "classification": "dimensionless sign-and-normalization selector plus conditional threshold rigidifier; not a common-coupling, RG-basin, or physical-instrument selector",
    "contextual_partition": {
        "ordered_clifford_packet": "H and -H are separated by retained source order",
        "unoriented_plane": "H and -H become one reflection-related class",
        "inclusive_detector": "the contrast direction lies in the readout kernel",
    },
    "smallest_exact_falsifier": "gH with g=1 and g=2 obeys the same dimensionless Clifford relations but predicts different physical magnitudes",
    "remaining_source_gate": "complete simple-parent gauge-Yukawa fixed point and global basin fixing the common coupling g",
    "remaining_threshold_gate": "derive the co-moving projector/Hodge connection and finite mass/width matching from the same source action",
    "remaining_instrument_gate": "independently excite both labelled singlet directions and measure a calibrated rank-two physical16 response",
}

out = ROOT / "results" / "wp878_ordered_singlet_plane_hodge_portal_normalizer.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result["summary"], indent=2))
if not all(tests.values()):
    raise SystemExit(1)
