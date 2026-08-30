import json
import math
from pathlib import Path


F = ((2, 7), (3, 7))
det_f = F[0][0] * F[1][1] - F[0][1] * F[1][0]
physical_v3 = (13, 16)

# Port rescaling hostile: the same faithful real one-dimensional observation
# has arbitrarily different integral cokernels if primitive port units are not
# source fixed.
real_rank_before = 1
real_rank_after = 1
smith_before = 1  # [1]
smith_after = 7   # [7], obtained by rescaling the sole port by seven

candidates = [
    {
        "id": "particle_helicity",
        "independently_quantized": True,
        "magnetic_coupling": True,
        "common_integral_carrier": False,
    },
    {
        "id": "orbital_angular_momentum",
        "independently_quantized": False,
        "magnetic_coupling": True,
        "common_integral_carrier": False,
    },
    {
        "id": "classical_bms_charge",
        "independently_quantized": False,
        "magnetic_coupling": True,
        "common_integral_carrier": False,
    },
    {
        "id": "nut_dual_charge",
        "independently_quantized": "conditional_pairing",
        "magnetic_coupling": False,
        "common_integral_carrier": False,
    },
    {
        "id": "ring_mode_number",
        "independently_quantized": True,
        "magnetic_coupling": False,
        "common_integral_carrier": False,
    },
    {
        "id": "low_mode_occupation_labels",
        "independently_quantized": True,
        "magnetic_coupling": "off_diagonal_quadrature",
        "common_integral_carrier": False,
    },
    {
        "id": "symbolic_grade",
        "independently_quantized": False,
        "magnetic_coupling": "only_grade_three_source_derived",
        "common_integral_carrier": False,
    },
]

successful = [
    item for item in candidates
    if item["independently_quantized"] is True
    and item["magnetic_coupling"] is True
    and item["common_integral_carrier"] is True
]

gates = [
    abs(det_f) == 7,
    math.gcd(*physical_v3) == 1,
    real_rank_before == real_rank_after,
    smith_before != smith_after,
    len(successful) == 0,
]

result = {
    "schema": "marici.strominger.physical_charge_affine_seven_completion_audit.v1",
    "cross_grade_affine_discriminant": abs(det_f),
    "physical_grade_three_vector": list(physical_v3),
    "physical_grade_three_content": math.gcd(*physical_v3),
    "source_authorized_grade_changing_charge_constructor": False,
    "source_authorized_integral_contour_port_units": False,
    "port_rescaling_hostile": {
        "real_rank_before": real_rank_before,
        "real_rank_after": real_rank_after,
        "smith_factor_before": smith_before,
        "smith_factor_after": smith_after,
    },
    "candidate_audit": candidates,
    "successful_physical_index_seven_candidates": successful,
    "physical_index_seven_established": False,
    "minimal_reopening_evidence": [
        "source-derived grade-changing magnetic charge constructor with matrix F",
        "fixed-grade primitive integral state-port pairing with Smith factor seven",
    ],
    "gates_passed": sum(gates),
    "gates_total": len(gates),
    "all_passed": all(gates),
}

output = (
    Path(__file__).parents[1]
    / "results"
    / "physical_charge_affine_seven_completion_audit.json"
)
output.write_text(json.dumps(result, indent=2) + "\n", encoding="ascii")
print(json.dumps(result, indent=2))
raise SystemExit(0 if all(gates) else 1)
