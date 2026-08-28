import json


sizes = [2, 3, 5, 8]
records = []

for size in sizes:
    diagonal = [0] * size
    diagonal[0] = 1
    diagonal[-1] = -1

    assert sum(diagonal) == 0
    assert diagonal[0] == 1
    assert diagonal[-1] == -1
    if size > 2:
        assert diagonal[1] == 0

    records.append(
        {
            "size": size,
            "commutator_diagonal": diagonal,
            "full_trace": sum(diagonal),
            "leading_boundary_trace": diagonal[0],
            "receding_boundary_trace": diagonal[-1],
        }
    )

# Every fixed leading window stabilizes once the receding boundary lies beyond
# it, although the full finite trace remains zero.
fixed_window = 2
leading_windows = [record["commutator_diagonal"][:fixed_window] for record in records[1:]]
assert all(window == [1, 0] for window in leading_windows)

result = {
    "schema": "marici.nima.escaping-counterboundary.v1",
    "records": records,
    "every_finite_full_trace_zero": True,
    "leading_local_limit_trace": 1,
    "receding_counterboundary_charge": -1,
    "fixed_leading_window_stabilizes": True,
    "ordinary_finite_trace_determines_completed_orientation": False,
    "required_anomaly_type": "source_oriented_relative_boundary_trace",
}
print(json.dumps(result, indent=2, sort_keys=True))

