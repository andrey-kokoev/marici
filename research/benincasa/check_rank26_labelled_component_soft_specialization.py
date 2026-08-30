"""Occurrence-labelled direct specialization of the rank-26 source at Xi=0."""

import json
from concurrent.futures import ProcessPoolExecutor

import check_rank26_unsplit_source_cyclicity as cyclic


POINTS = {
    "X1": ((0, 3, 5), (0, 5, 7), (0, 7, 11)),
    "X2": ((3, 0, 5), (5, 0, 7), (7, 0, 11)),
    "X3": ((3, 5, 0), (5, 7, 0), (7, 11, 0)),
}
EXPECTED = {"X1": 20, "X2": 20, "X3": 24}
CONTROL = (1, 3, 5)


def sample(point):
    cyclic.charts.SOURCE_POINT = point
    presentation, span, source, closure = cyclic.source_closure(14)
    return {
        "point": list(point),
        "source_support": len(source),
        "first_covariant_jet_rank": closure["first_covariant_jet_rank"],
        "horizontal_cyclic_rank": len(span),
        "relation_rank": len(presentation["pivots"]),
    }


def main():
    labelled_points = [(label, point) for label, points in POINTS.items()
                       for point in points]
    all_points = [point for _, point in labelled_points] + [CONTROL]
    with ProcessPoolExecutor(max_workers=4) as pool:
        computed = list(pool.map(sample, all_points))
    sectors = {label: [] for label in POINTS}
    for (label, _), result in zip(labelled_points, computed[:-1]):
        sectors[label].append(result)
    control = computed[-1]
    for label, records in sectors.items():
        assert all(record["horizontal_cyclic_rank"] == EXPECTED[label]
                   for record in records)
        assert len({record["relation_rank"] for record in records}) == 1
        assert all(record["source_support"] == 3 for record in records)
        assert all(record["first_covariant_jet_rank"] == 3 for record in records)
    assert control["horizontal_cyclic_rank"] == 26
    print(json.dumps({
        "schema": "marici.benincasa.rank26-labelled-component-soft-specialization.v1",
        "field": cyclic.base.PRIME,
        "functor": "ordinary direct fiber restriction",
        "sectors": sectors,
        "control": control,
        "generic_rank": 26,
        "soft_ranks": EXPECTED,
        "interpretation": (
            "the literal occurrence-labelled source distinguishes the X3-soft "
            "chart from the X1/X2-soft charts; no cyclic identification is imposed"
        ),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
