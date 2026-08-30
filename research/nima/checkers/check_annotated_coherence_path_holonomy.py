"""Finite annotation-holonomy checker for a filled constructor diamond."""


edges = {
    ("T", "L"): {"support": {"a"}, "resource": 1, "epoch": {1, 2}, "fault": "BFT1"},
    ("L", "N"): {"support": {"c"}, "resource": 2, "epoch": {2, 3}, "fault": "BFT1"},
    ("T", "R"): {"support": {"b"}, "resource": 1, "epoch": {1, 2}, "fault": "BFT1"},
    ("R", "N"): {"support": {"c"}, "resource": 2, "epoch": {2, 3}, "fault": "BFT1"},
}


def accumulate(path):
    support = set()
    resource = 0
    epoch = None
    fault = None
    for edge in zip(path, path[1:]):
        label = edges[edge]
        support |= label["support"]
        resource += label["resource"]
        epoch = set(label["epoch"]) if epoch is None else epoch & label["epoch"]
        if fault is None:
            fault = label["fault"]
        elif fault != label["fault"]:
            return {"code": "fault_model_crossing_missing", "edge": edge}
    return {"support": support, "resource": resource, "epoch": epoch, "fault": fault}


left_path = ["T", "L", "N"]
right_path = ["T", "R", "N"]
left = accumulate(left_path)
right = accumulate(right_path)

assert left_path[-1] == right_path[-1] == "N"
assert left["resource"] == right["resource"] == 3
assert left["epoch"] == right["epoch"] == {2}
assert left["fault"] == right["fault"] == "BFT1"
delta = left["support"] ^ right["support"]
assert delta == {"a", "b"}

failure = {
    "code": "constructor_path_annotation_mismatch",
    "normal_form": "N",
    "component": "support",
    "left": sorted(left["support"]),
    "right": sorted(right["support"]),
    "symmetric_difference": sorted(delta),
}

print("shared constructor normal form:", "N")
print("left annotations:", left)
print("right annotations:", right)
print("holonomy witness:", failure)
print("PASS: a filled shape diamond can still launder authority annotations")
