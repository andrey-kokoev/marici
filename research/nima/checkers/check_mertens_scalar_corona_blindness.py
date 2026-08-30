import json


cutoffs = [2, 4, 8, 16]
records = []

for cutoff in cutoffs:
    zero = [0] * cutoff
    alternating = [1 if index % 2 == 0 else -1 for index in range(cutoff)]

    zero_average = sum(zero) / cutoff
    alternating_average = sum(alternating) / cutoff
    zero_tail_norm = max(abs(value) for value in zero)
    alternating_tail_norm = max(abs(value) for value in alternating)

    assert zero_average == 0
    assert alternating_average == 0
    assert zero_tail_norm == 0
    assert alternating_tail_norm == 1

    records.append(
        {
            "cutoff": cutoff,
            "zero_scalar_average": zero_average,
            "alternating_scalar_average": alternating_average,
            "zero_tail_norm": zero_tail_norm,
            "alternating_tail_norm": alternating_tail_norm,
        }
    )

result = {
    "schema": "marici.nima.mertens-scalar-corona-blindness.v1",
    "records": records,
    "scalar_records_identical": True,
    "corona_classes_distinct": True,
    "alternating_corona_norm": 1,
    "three_grade_scalar_controls_corona": False,
    "required_successor": "source_derived_state_valued_boundary_residual",
}
print(json.dumps(result, indent=2, sort_keys=True))

