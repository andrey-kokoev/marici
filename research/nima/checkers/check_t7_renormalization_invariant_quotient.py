import json
from fractions import Fraction
from pathlib import Path


OUT = Path(__file__).resolve().parents[1] / "results" / "t7_renormalization_invariant_quotient.json"


def rank(rows):
    matrix = [[Fraction(x) for x in row] for row in rows]
    if not matrix:
        return 0
    r = 0
    for col in range(len(matrix[0])):
        pivot = next((i for i in range(r, len(matrix)) if matrix[i][col]), None)
        if pivot is None:
            continue
        matrix[r], matrix[pivot] = matrix[pivot], matrix[r]
        q = matrix[r][col]
        matrix[r] = [x / q for x in matrix[r]]
        for i in range(len(matrix)):
            if i != r and matrix[i][col]:
                q = matrix[i][col]
                matrix[i] = [matrix[i][j] - q * matrix[r][j] for j in range(len(matrix[0]))]
        r += 1
    return r


# Residual basis: r_odd is detected by e1-dual; r_supported is detected by
# e2-dual-e4-dual+180*v_alg-dual.  The leading UV counterterm has nonzero e1
# component and generically a v_alg component, so its image is a mixed line.
residual_basis = [(1, 0), (0, 1)]
counterterm_image = [(1, 180)]
residual_rank = rank(residual_basis)
counterterm_rank = rank(counterterm_image)
renormalization_invariant_rank = residual_rank - counterterm_rank

result = {
    "checker": "t7_renormalization_invariant_quotient",
    "residual_basis": ["r_odd=e1", "r_supported"],
    "residual_rank": residual_rank,
    "counterterm_image_basis": ["one mixed residual line with nonzero r_odd component"],
    "counterterm_image_rank": counterterm_rank,
    "renormalization_invariant_quotient_rank": renormalization_invariant_rank,
    "scheme_independent_rank_two_completion_possible": renormalization_invariant_rank >= 2,
    "surviving_target": "the quotient transverse to the mixed leading counterterm line, modulo lower UV grades",
}

assert residual_rank == 2
assert counterterm_rank == 1
assert renormalization_invariant_rank == 1
assert not result["scheme_independent_rank_two_completion_possible"]
OUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
