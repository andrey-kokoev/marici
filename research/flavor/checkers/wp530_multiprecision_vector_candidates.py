"""Multiprecision stability test for the eight WP529 sub-cutoff candidates."""

import json
from pathlib import Path

import mpmath as mp


root = Path(__file__).resolve().parents[1]


def load(name):
    return json.loads((root / "results" / name).read_text(encoding="utf-8"))


wp517 = load("wp517_unequal_vector_partial_widths.json")
wp529 = load("wp529_lightweight_vector_census.json")
candidates = wp529["precutoff_census"]["subcutoff_candidate_channels"]
candidate_triples = [
    (item["parent"], item["daughter_1"], item["daughter_2"])
    for item in candidates
]


def mat(rows):
    return mp.matrix(rows)


def trace(matrix):
    return sum(matrix[index, index] for index in range(matrix.rows))


def levi_civita(left, middle, right):
    if len({left, middle, right}) < 3:
        return mp.mpf("0")
    permutation = [left, middle, right]
    inversions = sum(
        permutation[i] > permutation[j]
        for i in range(3)
        for j in range(i + 1, 3)
    )
    return mp.mpf("-1") if inversions % 2 else mp.mpf("1")


def reconstruct(dps):
    mp.mp.dps = dps
    zero = mp.mpf("0")
    one = mp.mpf("1")
    imag = mp.j
    sqrt = mp.sqrt
    lambdas = [
        mat([[0, 1, 0], [1, 0, 0], [0, 0, 0]]),
        mat([[0, -imag, 0], [imag, 0, 0], [0, 0, 0]]),
        mat([[1, 0, 0], [0, -1, 0], [0, 0, 0]]),
        mat([[0, 0, 1], [0, 0, 0], [1, 0, 0]]),
        mat([[0, 0, -imag], [0, 0, 0], [imag, 0, 0]]),
        mat([[0, 0, 0], [0, 0, 1], [0, 1, 0]]),
        mat([[0, 0, 0], [0, 0, -imag], [0, imag, 0]]),
        mat([[1 / sqrt(3), 0, 0], [0, 1 / sqrt(3), 0], [0, 0, -2 / sqrt(3)]]),
    ]
    spin_one = [
        mat([[0, 1 / sqrt(2), 0], [1 / sqrt(2), 0, 1 / sqrt(2)], [0, 1 / sqrt(2), 0]]),
        mat([[0, -imag / sqrt(2), 0], [imag / sqrt(2), 0, -imag / sqrt(2)], [0, imag / sqrt(2), 0]]),
        mat([[1, 0, 0], [0, 0, 0], [0, 0, -1]]),
    ]
    row_generators = [
        mat([[0, 0, 0], [0, 0, -1], [0, 1, 0]]),
        mat([[0, 0, 1], [0, 0, 0], [-1, 0, 0]]),
        mat([[0, -1, 0], [1, 0, 0], [0, 0, 0]]),
    ]
    g_f = sqrt(2)
    g_p = mp.mpf(1) / 10
    g_e = mp.mpf(1) / 50
    mu = one
    s = mp.mpf(16)
    b_squared = mp.mpf(30258) / 160001
    a_squared = 160000 * b_squared
    a = sqrt(a_squared)
    b = sqrt(b_squared)
    identity_3 = mp.eye(3)
    S0 = s * identity_3
    U0 = mp.zeros(3, 2)
    D0 = mp.zeros(3, 2)
    U0[2, 1] = a
    D0[0, 1] = b
    zero_s = mp.zeros(3, 3)
    zero_x = [mp.zeros(3, 3) for _ in range(3)]
    zero_u = mp.zeros(3, 2)
    zero_d = mp.zeros(3, 2)

    def adjoint_coordinates(matrix):
        return [mp.re(trace(matrix * basis)) / 2 for basis in lambdas]

    def complex_coordinates(matrix):
        return [
            mp.re(matrix[row, column])
            for row in range(matrix.rows)
            for column in range(matrix.cols)
        ] + [
            mp.im(matrix[row, column])
            for row in range(matrix.rows)
            for column in range(matrix.cols)
        ]

    def field_vector(delta_s, delta_x, delta_u, delta_d):
        values = [
            mp.re(delta_s[row, column])
            for row in range(3)
            for column in range(3)
        ]
        for matrix in delta_x:
            values.extend(adjoint_coordinates(matrix))
        values.extend(complex_coordinates(delta_u))
        values.extend(complex_coordinates(delta_d))
        return values

    tangent_columns = []
    for generator in lambdas:
        delta_x = [
            imag * g_f * mu * (generator * matrix - matrix * generator)
            for matrix in spin_one
        ]
        tangent_columns.append(field_vector(zero_s, delta_x, zero_u, zero_d))
    for generator in row_generators:
        delta_x = []
        for left in range(3):
            value = mp.zeros(3, 3)
            for right in range(3):
                value += generator[left, right] * spin_one[right]
            delta_x.append(g_p * mu * value)
        tangent_columns.append(
            field_vector(-g_p * S0 * generator, delta_x, zero_u, zero_d)
        )
    for generator in row_generators:
        tangent_columns.append(
            field_vector(
                g_e * generator * S0,
                zero_x,
                g_e * generator * U0,
                g_e * generator * D0,
            )
        )

    tangent = mp.matrix(57, 14)
    for column, values in enumerate(tangent_columns):
        normalization = mp.mpf("0.5") if column < 8 else one
        for row, value in enumerate(values):
            tangent[row, column] = normalization * value
    weights = [one] * 9 + [mp.mpf(2)] * 24 + [mp.mpf(2)] * 24
    mass_matrix = mp.matrix(14, 14)
    for left in range(14):
        for right in range(14):
            mass_matrix[left, right] = sum(
                weights[row] * tangent[row, left] * tangent[row, right]
                for row in range(57)
            )
    eigenvalues, rotation = mp.eigsy(mass_matrix)
    masses = [sqrt(max(eigenvalues[index], zero)) for index in range(14)]

    gauge_nonzero = []
    for left in range(8):
        for middle in range(8):
            commutator = lambdas[left] * lambdas[middle] - lambdas[middle] * lambdas[left]
            for right in range(8):
                value = g_f * mp.re(trace(commutator * lambdas[right]) / (4 * imag))
                if value:
                    gauge_nonzero.append((left, middle, right, value))
    for offset, coupling in ((8, g_p), (11, g_e)):
        for left in range(3):
            for middle in range(3):
                for right in range(3):
                    value = coupling * levi_civita(left, middle, right)
                    if value:
                        gauge_nonzero.append(
                            (offset + left, offset + middle, offset + right, value)
                        )

    def coupling(parent, daughter_1, daughter_2):
        return sum(
            value
            * rotation[left, parent]
            * rotation[middle, daughter_1]
            * rotation[right, daughter_2]
            for left, middle, right, value in gauge_nonzero
        )

    def partial_width(parent, daughter_1, daughter_2, value):
        M = masses[parent]
        m1 = masses[daughter_1]
        m2 = masses[daughter_2]
        kallen = (
            M**4
            + m1**4
            + m2**4
            - 2 * M**2 * m1**2
            - 2 * M**2 * m2**2
            - 2 * m1**2 * m2**2
        )
        polynomial = (
            M**4
            + m1**4
            + m2**4
            + 10 * M**2 * m1**2
            + 10 * M**2 * m2**2
            + 10 * m1**2 * m2**2
        )
        polarization_sum = kallen * polynomial / (12 * M**2 * m1**2 * m2**2)
        momentum = sqrt(kallen) / (2 * M)
        return momentum * abs(value) ** 2 * polarization_sum / (8 * mp.pi * M**2)

    packets = []
    for parent, daughter_1, daughter_2 in candidate_triples:
        value = coupling(parent, daughter_1, daughter_2)
        packets.append(
            {
                "triple": [parent, daughter_1, daughter_2],
                "absolute_coupling": mp.nstr(abs(value), dps - 5),
                "partial_width_GeV": mp.nstr(
                    partial_width(parent, daughter_1, daughter_2, value), dps - 5
                ),
            }
        )
    residual = max(
        abs(
            sum(mass_matrix[row, column] * rotation[column, state] for column in range(14))
            - eigenvalues[state] * rotation[row, state]
        )
        for row in range(14)
        for state in range(14)
    )
    minimum_gap = min(
        abs(eigenvalues[index + 1] - eigenvalues[index]) for index in range(13)
    )
    return {
        "dps": dps,
        "eigenpair_residual": mp.nstr(residual, dps - 5),
        "minimum_mass_squared_gap": mp.nstr(minimum_gap, dps - 5),
        "candidates": packets,
        "candidate_width_sum_GeV": mp.nstr(
            sum(mp.mpf(packet["partial_width_GeV"]) for packet in packets), dps - 5
        ),
    }


runs = [reconstruct(dps) for dps in (50, 80, 120)]


def decimal(value):
    return mp.mpf(value)


maximum_couplings = [
    max(decimal(packet["absolute_coupling"]) for packet in run["candidates"])
    for run in runs
]
width_sums = [decimal(run["candidate_width_sum_GeV"]) for run in runs]
residuals = [decimal(run["eigenpair_residual"]) for run in runs]
residual_ratios = [
    maximum_couplings[index] / residuals[index] for index in range(3)
]

checks = {
    "wp517_dependency_passed": bool(wp517["passed"]),
    "wp529_dependency_passed": bool(wp529["passed"]),
    "eight_candidates_are_retested": len(candidate_triples) == 8,
    "maximum_candidate_tracks_precision_at_50_digits": maximum_couplings[0]
    < mp.mpf("1e-45"),
    "maximum_candidate_tracks_precision_at_80_digits": maximum_couplings[1]
    < mp.mpf("1e-75"),
    "maximum_candidate_tracks_precision_at_120_digits": maximum_couplings[2]
    < mp.mpf("1e-114"),
    "candidate_width_sum_collapses_below_1e_225": width_sums[2]
    < mp.mpf("1e-225"),
    "candidate_couplings_remain_within_1e5_eigenpair_residuals": all(
        ratio < mp.mpf("1e5") for ratio in residual_ratios
    ),
    "eigenpair_residual_is_below_1e_110": decimal(runs[2]["eigenpair_residual"])
    < mp.mpf("1e-110"),
}
checks = {name: bool(value) for name, value in checks.items()}

result = {
    "work_package": "WP530",
    "domain": "The eight WP529 sub-cutoff candidate triples at the frozen WP516 source witness.",
    "multiprecision_runs": runs,
    "stability": {
        "maximum_candidate_coupling_by_precision": [
            mp.nstr(value, 20) for value in maximum_couplings
        ],
        "candidate_width_sum_by_precision": [
            mp.nstr(value, 20) for value in width_sums
        ],
        "maximum_coupling_over_eigenpair_residual": [
            mp.nstr(value, 20) for value in residual_ratios
        ],
    },
    "classification": "Independent arbitrary-precision collapse certificate. Every WP529 candidate decreases with working precision and remains within 10^5 times the eigenpair residual; the apparent widths collapse below 10^-225 GeV. They are numerical basis artifacts consistent with structural zeros, not stable sub-cutoff channels.",
    "selector": False,
    "rigidifier": False,
    "instrument": "The numerical channel census returns to the 34 WP517 channels. Exact total-width authority still requires an algebraic block-support or interval proof that the collapsing class is identically zero.",
    "smallest_exact_falsifier": "One candidate stabilizes at a precision-independent nonzero value or a cluster-summed spectral-projector calculation is nonzero.",
    "remaining_gate": "Derive exact block-support spectral-projector zeros for the collapsing class, then promote the 34-channel WP517 sum on the WP527 source witness and transport it through WP525.",
    "checks": checks,
    "passed": all(checks.values()),
}

out = root / "results" / "wp530_multiprecision_vector_candidates.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)
