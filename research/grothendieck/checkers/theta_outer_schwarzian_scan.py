"""Direct completed-source scan of the outer rank-two Schwarzian gate."""

import json
import math
from pathlib import Path


def phi(radius, max_label=10):
    exp2 = math.exp(2 * radius)
    terms = []
    for label in range(1, max_label + 1):
        coefficient = math.pi * label * label
        decay = math.exp(-coefficient * exp2)
        terms.append(
            (4 * coefficient * coefficient * math.exp(4.5 * radius)
             - 6 * coefficient * math.exp(2.5 * radius))
            * decay
        )
    return math.fsum(terms)


def cosh_w_jets(w, u, max_order=7):
    """Return d^n/dw^n cosh(sqrt(w)u), n=0..max_order."""
    jets = [0.0] * (max_order + 1)
    term = 1.0
    for k in range(180):
        if k > 0:
            term *= w * u * u / ((2 * k - 1) * (2 * k))
        falling = 1.0
        for order in range(max_order + 1):
            if order <= k:
                if order > 0:
                    falling *= k - order + 1
                jets[order] += term * falling / (w**order if order else 1.0)
        if k > max_order + 12 and abs(term) < 1e-17 * max(abs(jets[0]), 1.0):
            break
    return jets


def completed_jets(w, steps, cutoff=4.0, max_order=7):
    width = cutoff / steps
    accumulators = [[] for _ in range(max_order + 1)]
    for index in range(steps + 1):
        u = index * width
        source = phi(u)
        coefficient = 1 if index in (0, steps) else (4 if index % 2 else 2)
        jets = cosh_w_jets(w, u, max_order=max_order)
        for order, jet in enumerate(jets):
            accumulators[order].append(coefficient * source * jet)
    return [math.fsum(values) * width / 3 for values in accumulators]


def logarithmic_jets(values):
    c0 = values[0]
    normalized = [value / c0 for value in values]
    logarithmic = [0.0]
    for order in range(1, len(values)):
        correction = math.fsum(
            math.comb(order - 1, index - 1)
            * logarithmic[index]
            * normalized[order - index]
            for index in range(1, order)
        )
        logarithmic.append(normalized[order] - correction)
    return logarithmic[1:]


def determinant(matrix):
    work = [list(row) for row in matrix]
    value = 1.0
    for column in range(len(work)):
        pivot = max(range(column, len(work)), key=lambda row: abs(work[row][column]))
        if work[pivot][column] == 0.0:
            return 0.0
        if pivot != column:
            work[column], work[pivot] = work[pivot], work[column]
            value = -value
        pivot_value = work[column][column]
        value *= pivot_value
        for row in range(column + 1, len(work)):
            ratio = work[row][column] / pivot_value
            for index in range(column + 1, len(work)):
                work[row][index] -= ratio * work[column][index]
    return value


def hankel_determinants(moments, shifted=False):
    offset = 1 if shifted else 0
    maximum_size = (len(moments) - offset + 1) // 2
    return [
        determinant(
            [
                [moments[row + column + offset] for column in range(size)]
                for row in range(size)
            ]
        )
        for size in range(1, maximum_size + 1)
    ]


def normalized_hankel_determinants(moments, shifted=False):
    offset = 1 if shifted else 0
    maximum_size = (len(moments) - offset + 1) // 2
    results = []
    for size in range(1, maximum_size + 1):
        matrix = []
        for row in range(size):
            matrix.append(
                [
                    moments[row + column + offset]
                    / math.sqrt(
                        moments[2 * row + offset]
                        * moments[2 * column + offset]
                    )
                    for column in range(size)
                ]
            )
        results.append(determinant(matrix))
    return results


def evaluate(w, steps):
    l1, l2, l3, l4, l5, l6, l7 = logarithmic_jets(completed_jets(w, steps))
    displacement = w - 0.25
    h0 = displacement * l1
    h1 = l1 + displacement * l2
    h2 = 2 * l2 + displacement * l3
    h3 = 3 * l3 + displacement * l4
    h4 = 4 * l4 + displacement * l5
    h5 = 5 * l5 + displacement * l6
    h6 = 6 * l6 + displacement * l7
    numerator = 2 * h1 * h3 - 3 * h2 * h2
    numerator_prime = 2 * h1 * h4 - 4 * h2 * h3
    numerator_second = 2 * h1 * h5 - 2 * h2 * h4 - 4 * h3 * h3
    numerator_third = 2 * h1 * h6 - 10 * h3 * h4
    schwarzian = numerator / (2 * h1 * h1)
    reciprocal_length_second = -numerator / (4 * h1**2.5)
    return {
        "w": w,
        "H": h0,
        "H_prime": h1,
        "H_second": h2,
        "H_third": h3,
        "H_fourth": h4,
        "H_fifth": h5,
        "H_sixth": h6,
        "schwarzian_numerator": numerator,
        "schwarzian_numerator_prime": numerator_prime,
        "schwarzian_numerator_second": numerator_second,
        "schwarzian_numerator_third": numerator_third,
        "schwarzian": schwarzian,
        "reciprocal_length_second": reciprocal_length_second,
    }


def hierarchy_evaluate(w, steps, numerator_order=6):
    log_jets = logarithmic_jets(
        completed_jets(w, steps, max_order=numerator_order + 4)
    )
    displacement = w - 0.25
    # h[index] is H^(index), with the unused zeroth slot set to zero.
    h = [0.0]
    for order in range(1, numerator_order + 4):
        h.append(
            order * log_jets[order - 1]
            + displacement * log_jets[order]
        )
    numerator_derivatives = []
    for order in range(numerator_order + 1):
        first_product = math.fsum(
            math.comb(order, index) * h[index + 1] * h[order - index + 3]
            for index in range(order + 1)
        )
        second_product = math.fsum(
            math.comb(order, index) * h[index + 2] * h[order - index + 2]
            for index in range(order + 1)
        )
        numerator_derivatives.append(2.0 * first_product - 3.0 * second_product)
    moments = [
        (-1.0) ** order * value
        for order, value in enumerate(numerator_derivatives)
    ]
    hankel_2 = moments[0] * moments[2] - moments[1] ** 2
    hankel_shifted_2 = moments[1] * moments[3] - moments[2] ** 2
    hankel_3 = (
        moments[0] * (moments[2] * moments[4] - moments[3] ** 2)
        - moments[1] * (moments[1] * moments[4] - moments[2] * moments[3])
        + moments[2] * (moments[1] * moments[3] - moments[2] ** 2)
    )
    h_prime_moments = [
        (-1.0) ** order * h[order + 1]
        for order in range(numerator_order + 3)
    ]
    order_two_stieltjes_moments = [
        value / math.factorial(order + 1)
        for order, value in enumerate(h_prime_moments)
    ]
    rh_support_localizing_moments = [
        order_two_stieltjes_moments[order] / w
        - order_two_stieltjes_moments[order + 1]
        for order in range(len(order_two_stieltjes_moments) - 1)
    ]
    h_prime_hankel_2 = (
        h_prime_moments[0] * h_prime_moments[2]
        - h_prime_moments[1] ** 2
    )
    h_prime_shifted_hankel_2 = (
        h_prime_moments[1] * h_prime_moments[3]
        - h_prime_moments[2] ** 2
    )
    h_prime_hankel_3 = (
        h_prime_moments[0]
        * (h_prime_moments[2] * h_prime_moments[4] - h_prime_moments[3] ** 2)
        - h_prime_moments[1]
        * (h_prime_moments[1] * h_prime_moments[4] - h_prime_moments[2] * h_prime_moments[3])
        + h_prime_moments[2]
        * (h_prime_moments[1] * h_prime_moments[3] - h_prime_moments[2] ** 2)
    )
    return {
        "w": w,
        "numerator_derivatives": numerator_derivatives,
        "signed_moment_candidates": moments,
        "all_derivative_signs_through_order_6_pass": all(
            value >= 0.0 for value in moments
        ),
        "hankel_2_determinant": hankel_2,
        "shifted_hankel_2_determinant": hankel_shifted_2,
        "hankel_3_determinant": hankel_3,
        "first_stieltjes_hankel_tests_pass": (
            hankel_2 >= 0.0 and hankel_shifted_2 >= 0.0 and hankel_3 >= 0.0
        ),
        "H_prime_signed_moment_candidates": h_prime_moments,
        "H_prime_all_derivative_signs_pass": all(
            value >= 0.0 for value in h_prime_moments
        ),
        "H_prime_hankel_2_determinant": h_prime_hankel_2,
        "H_prime_shifted_hankel_2_determinant": h_prime_shifted_hankel_2,
        "H_prime_hankel_3_determinant": h_prime_hankel_3,
        "H_prime_first_stieltjes_hankel_tests_pass": (
            h_prime_hankel_2 >= 0.0
            and h_prime_shifted_hankel_2 >= 0.0
            and h_prime_hankel_3 >= 0.0
        ),
        "all_ordinary_hankel_determinants": hankel_determinants(moments),
        "all_shifted_hankel_determinants": hankel_determinants(
            moments, shifted=True
        ),
        "H_prime_all_ordinary_hankel_determinants": hankel_determinants(
            h_prime_moments
        ),
        "H_prime_all_shifted_hankel_determinants": hankel_determinants(
            h_prime_moments, shifted=True
        ),
        "H_prime_order_two_Stieltjes_moment_candidates": (
            order_two_stieltjes_moments
        ),
        "H_prime_order_two_ordinary_hankel_determinants": hankel_determinants(
            order_two_stieltjes_moments
        ),
        "H_prime_order_two_shifted_hankel_determinants": hankel_determinants(
            order_two_stieltjes_moments, shifted=True
        ),
        "H_prime_order_two_normalized_ordinary_hankel_determinants": (
            normalized_hankel_determinants(order_two_stieltjes_moments)
        ),
        "H_prime_order_two_normalized_shifted_hankel_determinants": (
            normalized_hankel_determinants(
                order_two_stieltjes_moments, shifted=True
            )
        ),
        "H_prime_order_two_nonnegative_rate_support_bounds_pass": all(
            order_two_stieltjes_moments[order + 1]
            <= order_two_stieltjes_moments[order] / (w - 0.25)
            for order in range(len(order_two_stieltjes_moments) - 1)
        ),
        "H_prime_order_two_RH_rate_support_bounds_pass": all(
            order_two_stieltjes_moments[order + 1]
            <= order_two_stieltjes_moments[order] / w
            for order in range(len(order_two_stieltjes_moments) - 1)
        ),
        "H_prime_order_two_RH_rate_support_margins": [
            order_two_stieltjes_moments[order] / w
            - order_two_stieltjes_moments[order + 1]
            for order in range(len(order_two_stieltjes_moments) - 1)
        ],
        "H_prime_order_two_RH_support_localizing_moments": (
            rh_support_localizing_moments
        ),
        "H_prime_order_two_RH_support_localizing_hankel_determinants": (
            hankel_determinants(rh_support_localizing_moments)
        ),
        "H_prime_order_two_RH_support_normalized_localizing_hankel_determinants": (
            normalized_hankel_determinants(rh_support_localizing_moments)
        ),
    }


w_values = [0.251, 0.26, 0.3, 0.5, 1.0, 2.0, 5.0, 10.0, 30.0, 100.0, 300.0, 400.0]
resolutions = [4000, 8000]
rows = []
for w in w_values:
    low = evaluate(w, resolutions[0])
    high = evaluate(w, resolutions[1])
    high["resolution_discrepancy_schwarzian_numerator"] = abs(
        high["schwarzian_numerator"] - low["schwarzian_numerator"]
    )
    high["passes"] = high["H_prime"] > 0 and high["schwarzian_numerator"] >= 0
    rows.append(high)

compact_bridge_x_values = [
    0.25 * math.exp(index * math.log(400.0 / 0.25) / 64)
    for index in range(65)
]
compact_bridge_rows = []
for w in compact_bridge_x_values:
    compact_low = evaluate(w, 2000)
    compact_high = evaluate(w, 4000)
    compact_high["resolution_discrepancy_numerator"] = abs(
        compact_high["schwarzian_numerator"]
        - compact_low["schwarzian_numerator"]
    )
    compact_high["resolution_discrepancy_numerator_prime"] = abs(
        compact_high["schwarzian_numerator_prime"]
        - compact_low["schwarzian_numerator_prime"]
    )
    compact_bridge_rows.append(compact_high)
for row in compact_bridge_rows:
    row["local_sign_length_scale"] = (
        row["schwarzian_numerator"]
        / abs(row["schwarzian_numerator_prime"])
    )
compact_bridge_boxes = []
for left, right in zip(compact_bridge_rows[:-1], compact_bridge_rows[1:]):
    derivative_budget = 2.0 * max(
        abs(left["schwarzian_numerator_prime"]),
        abs(right["schwarzian_numerator_prime"]),
    )
    lower_budget = min(
        left["schwarzian_numerator"], right["schwarzian_numerator"]
    ) - (right["w"] - left["w"]) * derivative_budget
    compact_bridge_boxes.append(
        {
            "interval": [left["w"], right["w"]],
            "inflated_derivative_budget": derivative_budget,
            "budgeted_lower_bound": lower_budget,
            "passes_budget": lower_budget > 0.0,
        }
    )
hierarchy_rows = []
for w in [0.251, 1.0, 10.0, 100.0, 400.0]:
    hierarchy_low = hierarchy_evaluate(w, 2000)
    hierarchy_high = hierarchy_evaluate(w, 4000)
    hierarchy_high["maximum_relative_signed_moment_resolution_discrepancy"] = max(
        abs(high - low) / max(abs(high), 1.0e-300)
        for high, low in zip(
            hierarchy_high["signed_moment_candidates"],
            hierarchy_low["signed_moment_candidates"],
        )
    )
    hierarchy_rows.append(hierarchy_high)
extended_hierarchy_rows = []
for w in [0.251, 10.0, 400.0]:
    extended_low = hierarchy_evaluate(w, 2000, numerator_order=10)
    extended_high = hierarchy_evaluate(w, 4000, numerator_order=10)
    extended_high["maximum_relative_numerator_moment_resolution_discrepancy"] = max(
        abs(high - low) / max(abs(high), 1.0e-300)
        for high, low in zip(
            extended_high["signed_moment_candidates"],
            extended_low["signed_moment_candidates"],
        )
    )
    extended_high["maximum_relative_H_prime_moment_resolution_discrepancy"] = max(
        abs(high - low) / max(abs(high), 1.0e-300)
        for high, low in zip(
            extended_high["H_prime_signed_moment_candidates"],
            extended_low["H_prime_signed_moment_candidates"],
        )
    )
    for name in [
        "H_prime_order_two_normalized_ordinary_hankel_determinants",
        "H_prime_order_two_normalized_shifted_hankel_determinants",
    ]:
        extended_high[f"{name}_resolution_comparison"] = [
            {
                "size": size,
                "low": low,
                "high": high,
                "relative_discrepancy": abs(high - low)
                / max(abs(high), abs(low), 1.0e-300),
                "numerically_resolved_same_positive_sign": (
                    high > 0.0
                    and low > 0.0
                    and abs(high - low) < 0.1 * min(abs(high), abs(low))
                ),
            }
            for size, (low, high) in enumerate(
                zip(extended_low[name], extended_high[name]), start=1
            )
        ]
    extended_hierarchy_rows.append(extended_high)
extended_order_12_rows = []
for w in [0.251, 10.0, 400.0]:
    order_12_low = hierarchy_evaluate(w, 2000, numerator_order=12)
    order_12_high = hierarchy_evaluate(w, 4000, numerator_order=12)
    order_12_high["maximum_relative_H_prime_moment_resolution_discrepancy"] = max(
        abs(high - low) / max(abs(high), 1.0e-300)
        for high, low in zip(
            order_12_high["H_prime_signed_moment_candidates"],
            order_12_low["H_prime_signed_moment_candidates"],
        )
    )
    extended_order_12_rows.append(order_12_high)

result = {
    "target": "2 H' H''' - 3 H''^2 >= 0 for w > 1/4",
    "w_values": w_values,
    "simpson_resolutions": resolutions,
    "folded_radius_cutoff": 4.0,
    "max_theta_label": 10,
    "rows": rows,
    "all_samples_pass": all(row["passes"] for row in rows),
    "smallest_schwarzian_numerator": min(rows, key=lambda row: row["schwarzian_numerator"]),
    "all_sampled_numerator_derivatives_negative": all(
        row["schwarzian_numerator_prime"] < 0 for row in rows
    ),
    "compact_bridge_reconnaissance": {
        "sample_count": len(compact_bridge_rows),
        "all_numerators_positive": all(
            row["schwarzian_numerator"] > 0 for row in compact_bridge_rows
        ),
        "all_numerator_derivatives_negative": all(
            row["schwarzian_numerator_prime"] < 0
            for row in compact_bridge_rows
        ),
        "all_numerator_second_derivatives_positive": all(
            row["schwarzian_numerator_second"] > 0
            for row in compact_bridge_rows
        ),
        "smallest_numerator_second_derivative_row": min(
            compact_bridge_rows,
            key=lambda row: row["schwarzian_numerator_second"],
        ),
        "all_numerator_third_derivatives_negative": all(
            row["schwarzian_numerator_third"] < 0
            for row in compact_bridge_rows
        ),
        "largest_numerator_third_derivative_row": max(
            compact_bridge_rows,
            key=lambda row: row["schwarzian_numerator_third"],
        ),
        "minimum_local_sign_length_scale_row": min(
            compact_bridge_rows, key=lambda row: row["local_sign_length_scale"]
        ),
        "largest_relative_numerator_resolution_discrepancy": max(
            row["resolution_discrepancy_numerator"]
            / abs(row["schwarzian_numerator"])
            for row in compact_bridge_rows
        ),
        "largest_relative_numerator_prime_resolution_discrepancy": max(
            row["resolution_discrepancy_numerator_prime"]
            / abs(row["schwarzian_numerator_prime"])
            for row in compact_bridge_rows
        ),
        "maximum_local_sign_length_scale_row": max(
            compact_bridge_rows, key=lambda row: row["local_sign_length_scale"]
        ),
        "rows": compact_bridge_rows,
        "inflated_derivative_box_budget": {
            "inflation_factor": 2.0,
            "box_count": len(compact_bridge_boxes),
            "all_boxes_pass": all(
                box["passes_budget"] for box in compact_bridge_boxes
            ),
            "weakest_box": min(
                compact_bridge_boxes,
                key=lambda box: box["budgeted_lower_bound"],
            ),
            "smallest_relative_box_margin": min(
                box["budgeted_lower_bound"]
                / min(
                    compact_bridge_rows[index]["schwarzian_numerator"],
                    compact_bridge_rows[index + 1]["schwarzian_numerator"],
                )
                for index, box in enumerate(compact_bridge_boxes)
            ),
            "boxes": compact_bridge_boxes,
        },
    },
    "complete_monotonicity_hankel_reconnaissance": {
        "rows": hierarchy_rows,
        "all_derivative_signs_pass": all(
            row["all_derivative_signs_through_order_6_pass"]
            for row in hierarchy_rows
        ),
        "all_first_stieltjes_hankel_tests_pass": all(
            row["first_stieltjes_hankel_tests_pass"] for row in hierarchy_rows
        ),
        "H_prime_all_derivative_signs_pass": all(
            row["H_prime_all_derivative_signs_pass"] for row in hierarchy_rows
        ),
        "H_prime_all_first_stieltjes_hankel_tests_pass": all(
            row["H_prime_first_stieltjes_hankel_tests_pass"]
            for row in hierarchy_rows
        ),
        "extended_order_10_rows": extended_hierarchy_rows,
        "extended_order_12_rows": extended_order_12_rows,
    },
    "interval_certified": False,
    "rh_proved_or_disproved": False,
}


if __name__ == "__main__":
    output = Path(__file__).parents[1] / "results" / "theta-outer-schwarzian-scan.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    for row in rows:
        print(row)
    print(f"all_samples_pass={result['all_samples_pass']}")
