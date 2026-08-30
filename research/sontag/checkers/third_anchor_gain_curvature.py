import json
from fractions import Fraction as F
from pathlib import Path


def rref(matrix):
    work = [[F(value) for value in row] for row in matrix]
    pivot_row = 0
    pivot_columns = []
    for column in range(len(work[0])):
        pivot = next(
            (row for row in range(pivot_row, len(work)) if work[row][column]),
            None,
        )
        if pivot is None:
            continue
        work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
        pivot_value = work[pivot_row][column]
        work[pivot_row] = [value / pivot_value for value in work[pivot_row]]
        for row in range(len(work)):
            if row == pivot_row:
                continue
            factor = work[row][column]
            if factor:
                work[row] = [
                    value - factor * pivot_entry
                    for value, pivot_entry in zip(work[row], work[pivot_row])
                ]
        pivot_columns.append(column)
        pivot_row += 1
        if pivot_row == len(work):
            break
    return work, pivot_columns


def design_row(time, setting):
    return [
        1,
        time,
        time * time,
        1 if setting == "YY" else 0,
        1 if setting == "XY" else 0,
        1 if setting == "YX" else 0,
    ]


def records(schedule, coefficients, offsets):
    intercept, slope, curvature = coefficients
    return [
        intercept
        + slope * F(time)
        + curvature * F(time * time)
        + offsets.get(setting, F(0))
        for time, setting in schedule
    ]


endpoint_schedule = [(0, "XX"), (1, "YY"), (2, "XY"), (3, "YX"), (4, "XX")]
three_reference_schedule = [
    (0, "XX"),
    (1, "YY"),
    (2, "XX"),
    (3, "XY"),
    (4, "XX"),
    (5, "YX"),
]

endpoint_design = [design_row(time, setting) for time, setting in endpoint_schedule]
three_reference_design = [
    design_row(time, setting) for time, setting in three_reference_schedule
]
endpoint_rank = len(rref(endpoint_design)[1])
three_reference_rank = len(rref(three_reference_design)[1])

quadratic = (F(0), F(-4), F(1))
endpoint_quadratic_records = records(endpoint_schedule, quadratic, {})
endpoint_offset_alias = records(
    endpoint_schedule,
    (F(0), F(0), F(0)),
    {"YY": F(-3), "XY": F(-4), "YX": F(-3)},
)
three_reference_records = records(three_reference_schedule, quadratic, {})
curvature_contrast = (
    three_reference_records[0]
    - 2 * three_reference_records[2]
    + three_reference_records[4]
)

augmented = [
    row + [value]
    for row, value in zip(three_reference_design, three_reference_records)
]
solved, pivots = rref(augmented)
recovered = tuple(solved[index][-1] for index in range(6))

checks = {
    "endpoint_quadratic_design_has_rank_five": endpoint_rank == 5,
    "quadratic_model_has_six_coordinates": len(endpoint_design[0]) == 6,
    "endpoint_schedule_aliases_curvature_and_offsets": endpoint_quadratic_records
    == endpoint_offset_alias,
    "three_reference_design_has_full_rank_six": three_reference_rank == 6,
    "reference_curvature_contrast_is_eight": curvature_contrast == 8,
    "contrast_recovers_unit_quadratic_coefficient": curvature_contrast / 8 == 1,
    "full_schedule_recovers_quadratic_drift": recovered[:3] == quadratic,
    "full_schedule_recovers_zero_setting_offsets": recovered[3:]
    == (F(0), F(0), F(0)),
    "augmented_system_has_six_parameter_pivots": pivots[:6]
    == [0, 1, 2, 3, 4, 5],
}

result = {
    "status": "PASS" if all(checks.values()) else "FAIL",
    "checks": checks,
    "endpoint_rank": endpoint_rank,
    "three_reference_rank": three_reference_rank,
    "endpoint_alias_records": [str(value) for value in endpoint_quadratic_records],
    "three_reference_records": [str(value) for value in three_reference_records],
    "curvature_contrast": str(curvature_contrast),
    "recovered_parameters": [str(value) for value in recovered],
    "classification": {
        "new_rank": "one third reference anchor exposes one quadratic drift coordinate",
        "minimum": "six scalar records for quadratic drift plus three relative setting offsets",
        "boundary": "no finite anchor schedule identifies unrestricted drift",
    },
}

output = Path(__file__).parents[1] / "results" / "third_anchor_gain_curvature.json"
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))

