import itertools
import json
import ast
import math
from fractions import Fraction
from pathlib import Path


def subsets(n):
    return list(itertools.product((0, 1), repeat=n))


def count_vector(route, classes):
    return tuple(sum(route[i] for i in cls) for cls in classes)


def specialization_matrix(class_sizes):
    n = sum(class_sizes)
    classes = []
    start = 0
    for size in class_sizes:
        classes.append(tuple(range(start, start + size)))
        start += size
    routes = subsets(n)
    counts = list(itertools.product(*(range(size + 1) for size in class_sizes)))
    rows = []
    for count in counts:
        rows.append([1 if count_vector(route, classes) == count else 0 for route in routes])
    return routes, counts, rows


def rank(matrix):
    a = [[Fraction(x) for x in row] for row in matrix]
    r = 0
    cols = len(a[0]) if a else 0
    for c in range(cols):
        pivot = next((i for i in range(r, len(a)) if a[i][c]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        p = a[r][c]
        a[r] = [x / p for x in a[r]]
        for i in range(len(a)):
            if i != r and a[i][c]:
                q = a[i][c]
                a[i] = [x - q * y for x, y in zip(a[i], a[r])]
        r += 1
    return r


def apply(matrix, vector):
    return [sum(a * b for a, b in zip(row, vector)) for row in matrix]


def main():
    census = {}
    for sizes in ((1, 1, 1), (2, 1), (3,)):
        routes, counts, matrix = specialization_matrix(sizes)
        matrix_rank = rank(matrix)
        census[str(sizes)] = {
            "labelled_dimension": len(routes),
            "physical_rank": matrix_rank,
            "kernel_dimension": len(routes) - matrix_rank,
            "count_vectors": [list(x) for x in counts],
        }

    # With all three labels tied, the singleton routes 100 and 010 are in the
    # same orbit. Their difference is invisible to every tied score moment.
    routes, _, tied = specialization_matrix((3,))
    i100 = routes.index((1, 0, 0))
    i010 = routes.index((0, 1, 0))
    invisible = [0] * len(routes)
    invisible[i100] = 1
    invisible[i010] = -1

    # On the source-invariant subspace, one coefficient c_k is repeated on
    # every route in the orbit. The tied readout returns |O_k| c_k, which is
    # invertible in characteristic zero but need not be in characteristic p.
    invariant_coefficients = [2, 1, 5, 7]
    orbit_sizes = [math.comb(3, k) for k in range(4)]
    orbit_sums = [size * value for size, value in zip(orbit_sizes, invariant_coefficients)]
    reconstructed = [Fraction(total, size) for total, size in zip(orbit_sums, orbit_sizes)]
    characteristic_three_collision = orbit_sums[1] % 3 == 0 and invariant_coefficients[1] % 3 != 0

    gates = {
        "distinct_triangle_scores_are_faithful": census["(1, 1, 1)"]["kernel_dimension"] == 0,
        "two_plus_one_partition_has_rank_six": census["(2, 1)"]["physical_rank"] == 6,
        "fully_tied_triangle_has_rank_four": census["(3,)"]["physical_rank"] == 4,
        "fully_tied_triangle_has_four_hidden_directions": census["(3,)"]["kernel_dimension"] == 4,
        "within_orbit_difference_is_invisible": apply(tied, invisible) == [0] * len(tied),
        "rank_matches_product_formula": all(
            data["physical_rank"] == math.prod(size + 1 for size in ast.literal_eval(key))
            for key, data in census.items()
        ),
        "source_invariant_subspace_is_reconstructed_in_characteristic_zero": reconstructed == invariant_coefficients,
        "modular_characteristic_can_destroy_restricted_faithfulness": characteristic_three_collision,
    }
    assert all(gates.values()), gates

    result = {
        "schema": "marici.physical-score-tower-orbit-quotient.v1",
        "gates": gates,
        "triangle_census": census,
        "source_symmetry_restriction": {
            "orbit_sizes": orbit_sizes,
            "invariant_coefficients": invariant_coefficients,
            "orbit_sums": orbit_sums,
            "reconstructed_characteristic_zero": [int(x) for x in reconstructed],
            "characteristic_three_singleton_orbit_collapses": characteristic_three_collision,
        },
        "conclusion": "tied physical scores reconstruct orbit sums, not labelled routes",
    }
    out = Path(__file__).parents[1] / "results" / "physical-score-tower-orbit-quotient.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
