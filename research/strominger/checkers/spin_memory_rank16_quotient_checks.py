"""Exact GF(199) certificate for the rank-16 boundary quotient."""

import hashlib
import itertools
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
ARTIFACT = ROOT / "research/strominger/spin-memory-rank16-quotient-theorem.md"
P = 991
INV3 = pow(3, -1, P)
LATITUDES = (-2 * INV3 % P, -INV3 % P, 0, INV3, 2 * INV3 % P)
OMEGA = pow(6, (P - 1) // 9, P)
COLS = [(degree, m) for degree in (2, 3, 4) for m in range(-degree, degree + 1)]


def sqrt_mod(value):
    return next(root for root in range(P) if root * root % P == value % P)


def assoc_legendre(degree, order, z, radial):
    lower = 1
    for index in range(1, order + 1):
        lower = lower * (-(2 * index - 1)) * radial % P
    if degree == order:
        return lower
    upper = (2 * order + 1) * z * lower % P
    if degree == order + 1:
        return upper
    for current in range(order + 2, degree + 1):
        lower, upper = upper, (
            ((2 * current - 1) * z * upper - (current + order - 1) * lower)
            * pow(current - order, -1, P)
        ) % P
    return upper


def rref(rows, width):
    matrix = [list(row) for row in rows if any(row)]
    lead = 0
    pivots = []
    for column in range(width):
        pivot = next((row for row in range(lead, len(matrix)) if matrix[row][column]), None)
        if pivot is None:
            continue
        matrix[lead], matrix[pivot] = matrix[pivot], matrix[lead]
        inverse = pow(matrix[lead][column], -1, P)
        matrix[lead] = [(entry * inverse) % P for entry in matrix[lead]]
        for row in range(len(matrix)):
            if row != lead and matrix[row][column]:
                factor = matrix[row][column]
                matrix[row] = [
                    (entry - factor * pivot_entry) % P
                    for entry, pivot_entry in zip(matrix[row], matrix[lead])
                ]
        pivots.append(column)
        lead += 1
        if lead == len(matrix):
            break
    return tuple(tuple(row) for row in matrix[:lead]), tuple(pivots)


def null_basis(rows, width):
    reduced, pivots = rref(rows, width)
    free = [column for column in range(width) if column not in pivots]
    basis = []
    for free_column in free:
        vector = [0] * width
        vector[free_column] = 1
        for row, pivot in enumerate(pivots):
            vector[pivot] = -reduced[row][free_column] % P
        basis.append(tuple(vector))
    return tuple(basis)


def dot(left, right):
    return sum(a * b for a, b in zip(left, right)) % P


radials = tuple(sqrt_mod(1 - latitude * latitude) for latitude in LATITUDES)
matrix = tuple(
    tuple(
        assoc_legendre(degree, abs(m), latitude, radial) * pow(OMEGA, longitude * m, P) % P
        for degree, m in COLS
    )
    for latitude, radial in zip(LATITUDES, radials)
    for longitude in range(9)
)

# Extract the three cost-labelled presentations for the first two rings.
first_two = tuple(range(18))
full_space, _ = rref((matrix[index] for index in first_two), 21)
presentation_counts = {}
presentation_spaces = set()
for cost in range(3):
    count = 0
    for omitted in itertools.combinations(first_two, cost):
        kept = [matrix[index] for index in first_two if index not in omitted]
        space, _ = rref(kept, 21)
        if len(space) == 16:
            count += 1
            presentation_spaces.add(space)
    presentation_counts[cost] = count


def max_rows_in_proper_generated_subspace(rows):
    maximum = 0
    witness = None
    for dimension in range(1, 5):
        for indices in itertools.combinations(range(len(rows)), dimension):
            basis, _ = rref((rows[index] for index in indices), 5)
            if len(basis) != dimension:
                continue
            contained = 0
            for row in rows:
                enlarged, _ = rref(basis + (row,), 5)
                contained += len(enlarged) == dimension
            if contained > maximum:
                maximum = contained
                witness = indices
    return maximum, witness


quotients = {}
for dark_pair in itertools.combinations(range(5), 2):
    dark = tuple(9 * ring + longitude for ring in dark_pair for longitude in range(9))
    live = tuple(index for index in range(45) if index not in dark)
    kernel = null_basis((matrix[index] for index in dark), 21)
    quotient_rows = tuple(tuple(dot(matrix[index], vector) for vector in kernel) for index in live)
    maximum_zeros, witness = max_rows_in_proper_generated_subspace(quotient_rows)
    witness_basis = tuple(quotient_rows[index] for index in witness)
    extremal_word = null_basis(witness_basis, 5)[0]
    zero_distribution = {}
    zero_longitudes = {}
    for live_ring_position, ring in enumerate(index for index in range(5) if index not in dark_pair):
        ring_rows = quotient_rows[9 * live_ring_position:9 * (live_ring_position + 1)]
        indices = [longitude for longitude, row in enumerate(ring_rows) if dot(row, extremal_word) == 0]
        zero_distribution[str(ring)] = len(indices)
        zero_longitudes[str(ring)] = indices
    quotients[str(dark_pair)] = {
        "dark_rank": len(rref((matrix[index] for index in dark), 21)[0]),
        "quotient_dimension": len(kernel),
        "maximum_zero_rows": maximum_zeros,
        "minimum_support": len(live) - maximum_zeros,
        "witness_generators": list(witness),
        "extremal_zero_distribution": zero_distribution,
        "extremal_zero_longitudes": zero_longitudes,
    }

checks = {
    "prime_supports_ninth_roots": (P - 1) % 9 == 0 and pow(OMEGA, 9, P) == 1 and OMEGA != 1,
    "latitude_radicals_exist": all(radial * radial % P == (1 - z * z) % P for z, radial in zip(LATITUDES, radials)),
    "full_contour_rank_is_21": len(rref(matrix, 21)[0]) == 21,
    "rank16_boundary_extracted": len(full_space) == 16,
    "three_cost_labels_are_0_1_2": set(presentation_counts) == {0, 1, 2},
    "presentation_counts_exact": presentation_counts == {0: 1, 1: 18, 2: 144},
    "all_presentations_define_one_row_space": len(presentation_spaces) == 1,
    "boundary_space_fixed_by_rotation": rref(tuple(matrix[(index // 9) * 9 + (index + 1) % 9] for index in first_two), 21)[0] == full_space,
    "boundary_space_fixed_by_reflection": rref(tuple(matrix[(index // 9) * 9 + (-index) % 9] for index in first_two), 21)[0] == full_space,
    "every_dark_pair_has_rank16": all(item["dark_rank"] == 16 for item in quotients.values()),
    "every_quotient_is_five_dimensional": all(item["quotient_dimension"] == 5 for item in quotients.values()),
    "every_continuation_spends_at_least_16": all(item["minimum_support"] >= 16 for item in quotients.values()),
    "support16_is_attained_in_quotient_family": any(item["minimum_support"] == 16 for item in quotients.values()),
    "distance16_iff_pair_extends_to_dark_triple": all(
        (quotients[str(pair)]["minimum_support"] == 16) == (
            set(pair).issubset({0, 2, 4}) or set(pair).issubset({1, 2, 3})
        )
        for pair in itertools.combinations(range(5), 2)
    ),
}
failed = [name for name, passed in checks.items() if not passed]
payload = {
    "schema": "marici.strominger.spin-memory-rank16-quotient-result.v1",
    "artifact_sha256": hashlib.sha256(ARTIFACT.read_bytes()).hexdigest().upper(),
    "passed": sum(checks.values()),
    "total": len(checks),
    "checks": checks,
    "observed": {
        "field": f"GF({P})",
        "presentation_counts": presentation_counts,
        "invariant_rank16_row_space_count": len(presentation_spaces),
        "quotients": quotients,
    },
    "verdict": (
        "The three cost-labelled rank-16 states are one rotation/reflection-invariant row space. "
        "Every two-dark-ring boundary has a five-dimensional quotient, and every continuation "
        "either restores rank 21 or uses at least 16 support positions."
    ),
}
print(json.dumps(payload, indent=2, sort_keys=True))
if failed:
    raise SystemExit("failed checks: " + ", ".join(failed))
