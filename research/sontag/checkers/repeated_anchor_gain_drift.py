import json
from fractions import Fraction as F
from pathlib import Path


def matrix_rank(rows):
    matrix = [[F(value) for value in row] for row in rows]
    rank = 0
    column = 0
    while rank < len(matrix) and column < len(matrix[0]):
        pivot = next(
            (index for index in range(rank, len(matrix)) if matrix[index][column]),
            None,
        )
        if pivot is None:
            column += 1
            continue
        matrix[rank], matrix[pivot] = matrix[pivot], matrix[rank]
        pivot_value = matrix[rank][column]
        matrix[rank] = [value / pivot_value for value in matrix[rank]]
        for index in range(len(matrix)):
            if index == rank:
                continue
            factor = matrix[index][column]
            if factor:
                matrix[index] = [
                    value - factor * pivot_entry
                    for value, pivot_entry in zip(matrix[index], matrix[rank])
                ]
        rank += 1
        column += 1
    return rank


def design_row(time, setting):
    return [
        1,
        time,
        1 if setting == "YY" else 0,
        1 if setting == "XY" else 0,
        1 if setting == "YX" else 0,
    ]


one_pass = [(0, "XX"), (1, "YY"), (2, "XY"), (3, "YX")]
anchored = one_pass + [(4, "XX")]
one_pass_design = [design_row(time, setting) for time, setting in one_pass]
anchored_design = [design_row(time, setting) for time, setting in anchored]


def records(schedule, intercept, slope, offsets):
    return [
        intercept + slope * F(time) + offsets.get(setting, F(0))
        for time, setting in schedule
    ]


static_offsets = {"YY": F(1), "XY": F(2), "YX": F(3)}
one_pass_setting_hostile = records(one_pass, F(0), F(0), static_offsets)
one_pass_drift_alias = records(one_pass, F(0), F(1), {})
anchored_setting_hostile = records(anchored, F(0), F(0), static_offsets)
anchored_drift_alias = records(anchored, F(0), F(1), {})

# Endpoint reference anchors recover affine drift; interior residuals recover
# relative setting offsets.
anchor_intercept = anchored_setting_hostile[0]
anchor_slope = (anchored_setting_hostile[-1] - anchor_intercept) / F(4)
recovered_offsets = {
    setting: anchored_setting_hostile[index]
    - (anchor_intercept + anchor_slope * F(time))
    for index, (time, setting) in enumerate(anchored[1:4], start=1)
}

checks = {
    "one_pass_design_has_rank_four": matrix_rank(one_pass_design) == 4,
    "one_pass_has_five_unknown_coordinates": len(one_pass_design[0]) == 5,
    "one_pass_setting_offsets_equal_affine_drift": one_pass_setting_hostile
    == one_pass_drift_alias
    == [F(0), F(1), F(2), F(3)],
    "anchored_design_has_full_rank_five": matrix_rank(anchored_design) == 5,
    "fifth_anchor_breaks_the_affine_alias": anchored_setting_hostile
    != anchored_drift_alias,
    "hostile_reference_anchors_force_zero_slope": anchor_intercept == 0
    and anchor_slope == 0,
    "anchored_schedule_recovers_all_setting_offsets": recovered_offsets
    == static_offsets,
    "nominal_affine_drift_has_zero_recovered_offsets": {
        setting: value
        for setting, value in zip(
            ("YY", "XY", "YX"),
            [
                records(anchored, F(2), F(1, 2), {})[index]
                - (
                    records(anchored, F(2), F(1, 2), {})[0]
                    + F(1, 2) * F(anchored[index][0])
                )
                for index in range(1, 4)
            ],
        )
    }
    == {"YY": F(0), "XY": F(0), "YX": F(0)},
}

result = {
    "status": "PASS" if all(checks.values()) else "FAIL",
    "checks": checks,
    "one_pass_rank": matrix_rank(one_pass_design),
    "anchored_rank": matrix_rank(anchored_design),
    "one_pass_alias_records": [str(value) for value in one_pass_drift_alias],
    "anchored_hostile_records": [str(value) for value in anchored_setting_hostile],
    "recovered_offsets": {
        setting: str(value) for setting, value in recovered_offsets.items()
    },
    "classification": {
        "defect": "one visit per setting aliases persistent setting offsets with temporal drift",
        "repair": "repeat one reference setting around the three other settings",
        "minimum": "five scalar records for affine drift plus three relative setting offsets",
    },
}

output = Path(__file__).parents[1] / "results" / "repeated_anchor_gain_drift.json"
output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))

