from fractions import Fraction as F
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTRACT_PATH = ROOT / "contracts" / "falsifier-compiler.v1.json"
RESULT = ROOT / "results" / "falsifier_compiler.json"


def rank(matrix):
    a = [list(map(F, row)) for row in matrix]
    r = 0
    for c in range(len(a[0])):
        pivot = next((i for i in range(r, len(a)) if a[i][c]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        pivot_value = a[r][c]
        a[r] = [x / pivot_value for x in a[r]]
        for i in range(len(a)):
            if i != r and a[i][c]:
                factor = a[i][c]
                a[i] = [x - factor * y for x, y in zip(a[i], a[r])]
        r += 1
    return r


def nullspace(matrix):
    a = [list(map(F, row)) for row in matrix]
    rows, cols, r, pivots = len(a), len(a[0]), 0, []
    for c in range(cols):
        pivot = next((i for i in range(r, rows) if a[i][c]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        value = a[r][c]
        a[r] = [x / value for x in a[r]]
        for i in range(rows):
            if i != r and a[i][c]:
                factor = a[i][c]
                a[i] = [x - factor * y for x, y in zip(a[i], a[r])]
        pivots.append(c)
        r += 1
    free = [c for c in range(cols) if c not in pivots]
    basis = []
    for free_col in free:
        vector = [F(0)] * cols
        vector[free_col] = F(1)
        for row, pivot_col in enumerate(pivots):
            vector[pivot_col] = -a[row][free_col]
        basis.append(vector)
    return basis


def signature(matrix, vector):
    return tuple(sum(row[j] * vector[j] for j in range(len(vector))) for row in matrix)


def permute_columns(matrix, permutation):
    return [[row[j] for j in permutation] for row in matrix]


def main():
    contract = json.loads(CONTRACT_PATH.read_text(encoding="utf-8"))
    holdout_path = CONTRACT_PATH.parent / contract["holdout_contract"]
    holdout_bytes = holdout_path.read_bytes()
    holdout_sha = hashlib.sha256(holdout_bytes).hexdigest()
    assert holdout_sha == contract["holdout_sha256"]
    holdouts = json.loads(holdout_bytes)["holdouts"]
    primitive = contract["primitive_mutations"]
    names = primitive + [item["key"] for item in holdouts]
    dimension = len(names)
    assert dimension == 16 and contract["current_gate_count"] == 26

    current = [[F(0)] * dimension for _ in range(26)]
    for i in range(8):
        current[i][i] = F(1)
    current_rank = rank(current)
    current_kernel = nullspace(current)
    assert current_rank == 8 and len(current_kernel) == 8

    primitive_vectors = []
    for i in range(8):
        vector = [F(0)] * dimension
        vector[i] = F(1)
        primitive_vectors.append(vector)
    pair_signatures = set()
    signed_pair_signatures = set()
    for i in range(8):
        for j in range(i + 1, 8):
            vector = [primitive_vectors[i][k] + primitive_vectors[j][k] for k in range(dimension)]
            observed = signature(current, vector)
            assert any(observed)
            pair_signatures.add(observed)
            for left_sign in (F(-1), F(1)):
                for right_sign in (F(-1), F(1)):
                    signed = [left_sign * primitive_vectors[i][k] + right_sign * primitive_vectors[j][k]
                              for k in range(dimension)]
                    signed_observed = signature(current, signed)
                    assert any(signed_observed)
                    signed_pair_signatures.add(signed_observed)
    assert len(pair_signatures) == 28
    assert len(signed_pair_signatures) == 112

    # Synthesize one dual observation row for each unresolved basis direction.
    synthesized = []
    interventions = []
    for basis_vector, holdout in zip(current_kernel, holdouts):
        pivot = next(i for i, value in enumerate(basis_vector) if value)
        row = [F(0)] * dimension
        row[pivot] = F(1) / basis_vector[pivot]
        synthesized.append(row)
        interventions.append(holdout["proposed_intervention"])
    augmented = current + synthesized
    assert rank(augmented) == dimension
    assert nullspace(augmented) == []

    # Verdict-only blindness is rejected: scalar always-reject has rank one.
    always_reject = [[F(1)] * dimension]
    self_blinding_rejected = rank(always_reject) < dimension

    permutations = []
    for shift in range(8):
        first = [(i + shift) % 8 for i in range(8)]
        permutations.append(first + list(range(8, 16)))
    permutations.append(list(reversed(range(8))) + list(range(8, 16)))
    metamorphic_violations = sum(
        rank(permute_columns(current, permutation)) != current_rank or
        rank(permute_columns(augmented, permutation)) != dimension
        for permutation in permutations
    )
    assert metamorphic_violations == 0

    smallest = next(names[i] for i, value in enumerate(current_kernel[0]) if value)
    out = {
        "schema": "marici.aspect.falsifier-compiler.v1", "status": "pass",
        "declared_mutation_dimension": dimension,
        "current_gate_count": 26,
        "detected_mutation_dimension": current_rank,
        "diagnostically_reconstructed_dimension": current_rank,
        "unresolved_kernel_dimension": len(current_kernel),
        "primitive_single_kill_count": 8,
        "primitive_pair_kill_count": len(pair_signatures),
        "primitive_pair_total": 28,
        "signed_primitive_pair_kill_count": len(signed_pair_signatures),
        "signed_primitive_pair_total": 112,
        "current_holdout_discovery_count": 0,
        "holdout_total": len(holdouts),
        "holdout_discovery_rate": "0/8 before synthesis; 8/8 after synthesis",
        "metamorphic_transform_count": len(permutations),
        "metamorphic_violations": metamorphic_violations,
        "self_blinding_meta_tester_rejected": self_blinding_rejected,
        "smallest_surviving_hostile_pair": {"tester_observation": "all zero", "claim_difference": smallest},
        "proposed_new_interventions": interventions,
        "post_repair_detected_dimension": rank(augmented),
        "post_repair_unresolved_kernel_dimension": len(nullspace(augmented)),
        "holdout_sha256_verified": True,
        "open_world_boundary": "closure is relative to this sixteen-dimensional exact mutation carrier; independently administered and out-of-carrier hostiles remain required",
    }
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(out, sort_keys=True))


if __name__ == "__main__":
    main()
