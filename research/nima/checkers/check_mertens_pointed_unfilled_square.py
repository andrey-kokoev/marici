import json


mertens_origin = 0
completed_values = [0, 1, 3]

records = []
for completed in completed_values:
    defect = completed - mertens_origin
    records.append(
        {
            "mertens_origin": mertens_origin,
            "completed_value": completed,
            "square_defect": defect,
            "same_relative_readout_rule": True,
            "same_pointing": True,
        }
    )

assert all(record["mertens_origin"] == 0 for record in records)
assert [record["square_defect"] for record in records] == completed_values
assert len({record["square_defect"] for record in records}) == 3

result = {
    "schema": "marici.nima.mertens-pointed-unfilled-square.v1",
    "records": records,
    "mertens_normalization_supplies_origin": True,
    "relative_anomaly_is_well_typed": True,
    "pointing_forces_square_commutativity": False,
    "missing_structure": "source_derived_comparison_2_cell",
}
print(json.dumps(result, indent=2, sort_keys=True))

