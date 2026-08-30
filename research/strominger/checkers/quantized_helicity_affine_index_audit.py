import json
from pathlib import Path


F = ((2, 7), (3, 7))
det_f = F[0][0] * F[1][1] - F[0][1] * F[1][0]
formal_index = abs(det_f)

# Two labelled soft-charge tests independently observe the two normalized
# helicity coordinates q_k=2h_k.  The rational readout matrix is the identity.
helicity_readout = ((1, 0), (0, 1))


def mat_vec(matrix, vector):
    return tuple(sum(row[j] * vector[j] for j in range(len(vector))) for row in matrix)


affine_columns = tuple((F[0][j], F[1][j]) for j in range(2))
column_readouts = [mat_vec(helicity_readout, column) for column in affine_columns]
columns_physically_null = [value == (0, 0) for value in column_readouts]

candidates = {
    "particle_helicity": {
        "independently_quantized": True,
        "spin_memory_coupled": True,
        "comparison_map_established": False,
    },
    "orbital_angular_momentum": {
        "independently_quantized": False,
        "spin_memory_coupled": True,
        "comparison_map_established": False,
    },
    "classical_bms_charge": {
        "independently_quantized": False,
        "spin_memory_coupled": True,
        "comparison_map_established": False,
    },
    "ring_mode_number": {
        "independently_quantized": True,
        "spin_memory_coupled": False,
        "comparison_map_established": False,
    },
    "nut_dual_charge": {
        "independently_quantized": "conditional",
        "spin_memory_coupled": False,
        "comparison_map_established": False,
    },
}

gates = [
    formal_index == 7,
    candidates["particle_helicity"]["independently_quantized"] is True,
    candidates["particle_helicity"]["spin_memory_coupled"] is True,
    not any(columns_physically_null),
    not candidates["particle_helicity"]["comparison_map_established"],
]

result = {
    "schema": "marici.strominger.quantized_helicity_affine_index_audit.v1",
    "normalized_helicity_lattice": "q_k=2h_k in Z",
    "source_coupling": "PSZ T_uz intrinsic-spin derivative term",
    "affine_frame": [list(row) for row in F],
    "formal_smith_index": formal_index,
    "affine_columns": [list(column) for column in affine_columns],
    "labelled_helicity_readouts": [list(value) for value in column_readouts],
    "affine_columns_physically_null": columns_physically_null,
    "physical_index_seven_established": False,
    "failure_code": "variance_mismatch_observation_rows_are_not_charge_relations",
    "candidate_audit": candidates,
    "gates_passed": sum(gates),
    "gates_total": len(gates),
    "all_passed": all(gates),
}

output = (
    Path(__file__).parents[1]
    / "results"
    / "quantized_helicity_affine_index_audit.json"
)
output.write_text(json.dumps(result, indent=2) + "\n", encoding="ascii")
print(json.dumps(result, indent=2))
raise SystemExit(0 if all(gates) else 1)
