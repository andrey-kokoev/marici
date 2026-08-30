"""Direct-fiber rank of the literal interacting source at total energy zero.

This deliberately computes ordinary restriction of the finite quotient
presentation.  It is not a logarithmic nearby-cycle calculation.
"""

import json

import check_rank26_unsplit_source_cyclicity as cyclic


POINTS = ((2, 3, -5), (3, 5, -8), (5, 8, -13))
NEARBY_POINT = (2, 3, -4)


def record(point):
    cyclic.charts.SOURCE_POINT = point
    presentation, span, source, closure = cyclic.source_closure(14)
    return {
        "point": list(point),
        "total_energy": sum(point),
        "source_support": len(source),
        "first_covariant_jet_rank": closure["first_covariant_jet_rank"],
        "horizontal_cyclic_rank": len(span),
        "relation_rank": len(presentation["pivots"]),
    }


def main():
    records = [record(point) for point in POINTS]
    nearby = record(NEARBY_POINT)
    assert all(item["total_energy"] == 0 for item in records)
    assert all(item["source_support"] == 3 for item in records)
    assert all(item["first_covariant_jet_rank"] == 3 for item in records)
    assert all(item["horizontal_cyclic_rank"] == 7 for item in records)
    assert len({item["relation_rank"] for item in records}) == 1
    assert nearby["total_energy"] == 1
    assert nearby["horizontal_cyclic_rank"] == 26
    print(json.dumps({
        "schema": "marici.benincasa.rank26-total-energy-direct-specialization.v1",
        "field": cyclic.base.PRIME,
        "support": "E_T=X1+X2+X3=0",
        "functor": "ordinary direct fiber restriction",
        "records": records,
        "nearby_control": nearby,
        "generic_rank": 26,
        "restricted_source_closure_rank": 7,
        "rank_loss": 19,
        "nearby_cycle_warning": (
            "ordinary restriction is not the logarithmic nearby-cycle functor; "
            "the known rank-12 nilpotent system must be compared by a typed "
            "specialization map"
        ),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
