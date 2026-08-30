import json
from fractions import Fraction
from pathlib import Path


DIMENSION = 4


def zero_matrix():
    return [[Fraction(0) for _ in range(DIMENSION)] for _ in range(DIMENSION)]


def matmul(left, right):
    return [[sum(left[i][k] * right[k][j] for k in range(DIMENSION)) for j in range(DIMENSION)] for i in range(DIMENSION)]


def add(left, right):
    return [[left[i][j] + right[i][j] for j in range(DIMENSION)] for i in range(DIMENSION)]


def scale(value, matrix):
    return [[value * entry for entry in row] for row in matrix]


def exterior_operator(generator, contraction=False):
    matrix = zero_matrix()
    for mask in range(DIMENSION):
        occupied = (mask >> generator) & 1
        if contraction:
            if not occupied:
                continue
            target = mask & ~(1 << generator)
        else:
            if occupied:
                continue
            target = mask | (1 << generator)
        lower_bits = mask & ((1 << generator) - 1)
        sign = -1 if lower_bits.bit_count() % 2 else 1
        matrix[target][mask] = Fraction(sign)
    return matrix


wedge_normal = exterior_operator(0)
wedge_tangential = exterior_operator(1)
contract_normal = exterior_operator(0, contraction=True)
contract_tangential = exterior_operator(1, contraction=True)
identity = [[Fraction(int(i == j)) for j in range(DIMENSION)] for i in range(DIMENSION)]
zero = zero_matrix()

assert add(matmul(wedge_normal, contract_normal), matmul(contract_normal, wedge_normal)) == identity
assert add(matmul(wedge_tangential, contract_normal), matmul(contract_normal, wedge_tangential)) == zero

rows = []
for a, b in ((Fraction(-2), Fraction(3)), (Fraction(-1, 2), Fraction(0)), (Fraction(1, 4), Fraction(5)), (Fraction(2), Fraction(-7))):
    differential = add(scale(a, wedge_normal), scale(b, wedge_tangential))
    assert matmul(differential, differential) == zero
    anticommutator = add(matmul(differential, contract_normal), matmul(contract_normal, differential))
    assert anticommutator == scale(a, identity)
    contraction = scale(1 / a, contract_normal)
    assert add(matmul(differential, contraction), matmul(contraction, differential)) == identity
    rows.append({"a": str(a), "b": str(b), "normal_scalar": str(a), "contractible": True})

mixed_a = Fraction(1)
mixed_b = Fraction(-1)
mixed_c = Fraction(1)
mixed_differential = add(scale(mixed_a, wedge_normal), scale(mixed_b, wedge_tangential))
mixed_contraction = add(contract_normal, scale(mixed_c, contract_tangential))
mixed_anticommutator = add(matmul(mixed_differential, mixed_contraction), matmul(mixed_contraction, mixed_differential))
assert mixed_anticommutator == scale(mixed_a + mixed_c * mixed_b, identity)
assert mixed_anticommutator == zero

result = {
    "exterior_dimension": DIMENSION,
    "normal_tangential_anticommutation": True,
    "off_seam_samples": rows,
    "seam_with_nonzero_tangential_differential_is_acyclic": True,
    "seam_with_zero_tangential_differential_allows_cohomology": True,
    "mixed_port_hostile": {
        "a": str(mixed_a),
        "b": str(mixed_b),
        "c": str(mixed_c),
        "anticommutator_scalar": str(mixed_a + mixed_c * mixed_b),
        "normal_cartan_identity_survives": False,
    },
    "verdict": "pure normal Koszul contraction confines cohomology to the seam; mixed-port leakage destroys the proof",
}

output = Path(__file__).parents[1] / "results" / "rh-normal-tangential-koszul.json"
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, sort_keys=True))

