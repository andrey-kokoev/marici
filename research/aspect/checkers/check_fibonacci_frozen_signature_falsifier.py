import json
from pathlib import Path

import sympy as sp


root = Path(__file__).parents[1]
contract_path = root / "contracts" / "frozen-bivariant-network-signature.v1.json"
contract = json.loads(contract_path.read_text(encoding="utf-8"))

golden = (1 + sp.sqrt(5)) / 2
F = sp.Matrix(
    [
        [1 / golden, 1 / sp.sqrt(golden)],
        [1 / sp.sqrt(golden), -1 / golden],
    ]
)


def matrix_zero(matrix):
    return all(sp.simplify(entry) == 0 for entry in matrix)


nonzero_per_row = [sum(sp.simplify(entry) != 0 for entry in F.row(i)) for i in range(2)]
nonzero_per_col = [sum(sp.simplify(entry) != 0 for entry in F.col(i)) for i in range(2)]
allowed_cells = set(contract["cell_types"])

checks = {
    "signature_is_frozen": contract["cell_creation_during_replay"] is False,
    "fibonacci_associator_is_orthogonal": matrix_zero(F.T * F - sp.eye(2)),
    "fibonacci_associator_is_involutive": matrix_zero(F * F - sp.eye(2)),
    "both_routes_mix_in_each_output": nonzero_per_row == [2, 2],
    "both_inputs_feed_each_route": nonzero_per_col == [2, 2],
    "not_scalar_times_permutation": nonzero_per_row != [1, 1],
    "matrix_associator_type_is_absent": "matrix_route_associator" not in allowed_cells,
    "gram_cell_cannot_be_retyped": contract["laws"]["gram_pairing"] == "does not substitute for a composition associator",
    "hostile_matches_frozen_forbidden_residual": "non-scalar mixing between distinct factorization routes" in contract["forbidden_residuals"],
}

result = {
    "schema": "marici.aspect.fibonacci-frozen-signature-falsifier.v1",
    "status": "frozen_signature_falsified" if all(checks.values()) else "checker_failure",
    "check_count": len(checks),
    "checks": {k: bool(v) for k, v in checks.items()},
    "hostile": "Fibonacci associator on the two tau-tau-tau to tau fusion routes",
    "residual_type": "non-scalar 2x2 route mixing",
    "disposition": "reject under v1; do not add a matrix associator until a separately authorized v2 theory is proposed",
}

out = root / "results" / "fibonacci_frozen_signature_falsifier.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["status"] == "frozen_signature_falsified" else 1)
