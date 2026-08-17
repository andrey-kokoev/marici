"""Test whether the exceptional V admits a projection to separated sheets."""

from itertools import product


SOURCE = ("h", "rD", "r1")
SOURCE_RELATIONS = (("h", "rD"), ("h", "r1"))


def order_preserving(mapping, target_relations):
    comparable = set(target_relations) | {(value, value) for value in mapping.values()}
    return all((mapping[a], mapping[b]) in comparable for a, b in SOURCE_RELATIONS)


def main():
    # The normalization sheets form a two-point antichain after normalization.
    sheets = ("e-", "e+")
    sheet_maps = []
    for values in product(sheets, repeat=len(SOURCE)):
        mapping = dict(zip(SOURCE, values))
        if order_preserving(mapping, ()):
            sheet_maps.append(mapping)
    assert len(sheet_maps) == 2
    assert all(mapping["rD"] == mapping["r1"] for mapping in sheet_maps)

    required_endpoints = {"rD": "e-", "r1": "e+"}
    assert not any(
        all(mapping[key] == value for key, value in required_endpoints.items())
        for mapping in sheet_maps
    )

    # Adjoin the conductor point c below both sheets.  The required extension
    # then exists uniquely: the central exceptional point must map to c.
    conductor_target = ("c", "e-", "e+")
    target_relations = (("c", "e-"), ("c", "e+"))
    augmented_maps = []
    for values in product(conductor_target, repeat=len(SOURCE)):
        mapping = dict(zip(SOURCE, values))
        if order_preserving(mapping, target_relations) and all(
            mapping[key] == value for key, value in required_endpoints.items()
        ):
            augmented_maps.append(mapping)
    assert augmented_maps == [{"h": "c", "rD": "e-", "r1": "e+"}]

    # Reflection exchanges the rays and sheets while fixing the conductor.
    selected = augmented_maps[0]
    reflected = {"h": selected["h"], "rD": selected["r1"], "r1": selected["rD"]}
    sheet_reflection = {"c": "c", "e-": "e+", "e+": "e-"}
    assert all(sheet_reflection[selected[x]] == reflected[x] for x in SOURCE)

    print("exceptional_source: CONNECTED_V_POSET")
    print("normalized_sheet_target: TWO_POINT_ANTICHAIN")
    print("order_preserving_maps_to_sheets: 2 CONSTANT_MAPS")
    print("required_distinct_endpoint_projection: IMPOSSIBLE")
    print("ordinary_global_span: NO")
    print("minimal_target_augmentation: CONDUCTOR_POINT_BELOW_BOTH_SHEETS")
    print("augmented_projection: UNIQUE")
    print("reflection_equivariance: PASS")
    print("required_geometry: CONDUCTOR_COSPAN_OR_MIXED_VARIANCE_KERNEL")
    print("global_conductor_cospan_realization: NEXT_GATE")


if __name__ == "__main__":
    main()
