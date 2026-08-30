import itertools
import json
from fractions import Fraction
from pathlib import Path


M = [
    [Fraction(2), Fraction(-6), Fraction(-5)],
    [Fraction(-2), Fraction(-2), Fraction(-5)],
    [Fraction(0), Fraction(0), Fraction(-2)],
]
M_INV = [
    [Fraction(1, 8), Fraction(-3, 8), Fraction(5, 8)],
    [Fraction(-1, 8), Fraction(-1, 8), Fraction(5, 8)],
    [Fraction(0), Fraction(0), Fraction(-1, 2)],
]
V_INV = [
    [Fraction(3), Fraction(-3), Fraction(1)],
    [Fraction(-5, 2), Fraction(4), Fraction(-3, 2)],
    [Fraction(1, 2), Fraction(-1), Fraction(1, 2)],
]


def multiply(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]


def rank(matrix):
    a = [row[:] for row in matrix]
    row = 0
    for column in range(len(a[0])):
        pivot = next((i for i in range(row, len(a)) if a[i][column]), None)
        if pivot is None:
            continue
        a[row], a[pivot] = a[pivot], a[row]
        scale = a[row][column]
        a[row] = [entry / scale for entry in a[row]]
        for i in range(len(a)):
            if i != row and a[i][column]:
                scale = a[i][column]
                a[i] = [a[i][j] - scale * a[row][j] for j in range(len(a[0]))]
        row += 1
    return row


def main():
    sample_points = [Fraction(1), Fraction(2), Fraction(3)]
    vandermonde = [[1, r, r * r] for r in sample_points]
    observed_scheme_map = multiply(vandermonde, M)
    calibration_decoder = multiply(M_INV, V_INV)
    identity = [[Fraction(i == j) for j in range(3)] for i in range(3)]
    pair_ranks = {
        "-".join(map(str, pair)): rank([vandermonde[i] for i in pair])
        for pair in itertools.combinations(range(3), 2)
    }
    checks = {
        "counterterm_map_invertible": rank(M) == 3,
        "declared_inverse_exact": multiply(M_INV, M) == identity,
        "three_distinct_calibrations_faithful": rank(vandermonde) == 3,
        "vandermonde_inverse_exact": multiply(V_INV, vandermonde) == identity,
        "combined_scheme_readout_faithful": rank(observed_scheme_map) == 3,
        "calibration_decoder_exact": multiply(calibration_decoder, observed_scheme_map) == identity,
        "every_two_calibrations_leave_one_blind_direction": all(value == 2 for value in pair_ranks.values()),
    }
    failed = [name for name, passed in checks.items() if not passed]
    packet = {
        "schema": "marici.three_calibration_renormalized_readout.v1",
        "response_basis": ["1", "r", "r^2"],
        "r_definition": "p^2 eta^2",
        "sample_points": [str(value) for value in sample_points],
        "vandermonde": [[str(value) for value in row] for row in vandermonde],
        "counterterm_map_inverse": [[str(value) for value in row] for row in M_INV],
        "vandermonde_inverse": [[str(value) for value in row] for row in V_INV],
        "calibration_decoder": [[str(value) for value in row] for row in calibration_decoder],
        "pair_ranks": pair_ranks,
        "checks": checks,
        "passed": len(checks) - len(failed),
        "total": len(checks),
        "authority_boundary": "The interface determines how three independently normalized measurements select a scheme point; it does not supply their values."
    }
    output = Path(__file__).resolve().parents[1] / "results" / "three-calibration-renormalized-readout.json"
    output.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(packet, indent=2))
    if failed:
        raise SystemExit("failed: " + ", ".join(failed))


if __name__ == "__main__":
    main()
