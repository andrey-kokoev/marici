import json
from pathlib import Path


def determinant_2(matrix):
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]


# Fiber hostile: same real capability, different integral Smith target.
p1 = ((1,),)
p7 = ((7,),)
same_real_rank = True
same_real_kernel = True
smith_p1 = 1
smith_p7 = 7
fiber_gate_passes_after_forgetting_units = smith_p1 == smith_p7

# Arity hostile: endpoint objects are held fixed while the attachment changes.
F = ((2, 7), (3, 7))
attachment_primitive = ((1, 0), (0, 1))
attachment_nonprimitive = ((1, 0), (0, 7))


def multiply(a, b):
    return tuple(
        tuple(sum(a[i][k] * b[k][j] for k in range(2)) for j in range(2))
        for i in range(2)
    )


paired_primitive = multiply(attachment_primitive, F)
paired_nonprimitive = multiply(attachment_nonprimitive, F)
index_primitive = abs(determinant_2(paired_primitive))
index_nonprimitive = abs(determinant_2(paired_nonprimitive))
endpoint_only_determines_index = index_primitive == index_nonprimitive

required_fields = {
    "charge_lattice": True,
    "charge_primitive_unit": True,
    "observation_lattice": True,
    "observation_primitive_unit": False,
    "grade_scope": False,
    "common_integral_carrier": False,
    "charge_attachment": False,
    "observation_attachment": False,
    "comparison_variance": False,
    "smith_target": True,
    "source_authority": False,
}

complete_germ = all(required_fields.values())
authority_gate_passes = required_fields["source_authority"]

gates = [
    same_real_rank,
    same_real_kernel,
    not fiber_gate_passes_after_forgetting_units,
    index_primitive == 7,
    index_nonprimitive == 49,
    not endpoint_only_determines_index,
    not complete_germ,
    not authority_gate_passes,
]

result = {
    "schema": "marici.strominger.aspect_germ_physical_charge_affine_seven.v1",
    "fiber_gate": {
        "same_real_capability": same_real_rank and same_real_kernel,
        "smith_targets": [smith_p1, smith_p7],
        "passes_after_forgetting_primitive_units": fiber_gate_passes_after_forgetting_units,
        "verdict": "fail",
    },
    "arity_gate": {
        "native_target": "charge_lattice_observation_lattice_primitive_comparison_span",
        "primitive_attachment_index": index_primitive,
        "nonprimitive_attachment_index": index_nonprimitive,
        "endpoint_objects_alone_determine_index": endpoint_only_determines_index,
        "verdict": "fail_without_attachment_cell",
    },
    "authority_gate": {
        "required_fields": required_fields,
        "complete_marked_germ": complete_germ,
        "source_authorized": authority_gate_passes,
        "verdict": "fail",
    },
    "grade_gate": {
        "affine_scope": "cross_grade",
        "physical_scope": "fixed_grade_three",
        "authorized_grade_changing_constructor": False,
        "verdict": "fail",
    },
    "smallest_adequate_germ": "PrimitiveIntegralComparisonGerm",
    "physical_smith_index_defined": False,
    "gates_passed": sum(gates),
    "gates_total": len(gates),
    "all_passed": all(gates),
}

output = (
    Path(__file__).parents[1]
    / "results"
    / "aspect_germ_physical_charge_affine_seven_checks.json"
)
output.write_text(json.dumps(result, indent=2) + "\n", encoding="ascii")
print(json.dumps(result, indent=2))
raise SystemExit(0 if all(gates) else 1)
