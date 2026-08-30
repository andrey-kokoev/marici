"""Coefficient closures at the physical X1-soft/triangle intersection."""

import json

import check_rank26_tangent_support_closure as support


def main():
    point = (0, 3, 3)
    cases = {
        "physical_soft_triangle_tangent": ((0, 1, 1),),
        "ambient_soft_plane_tangents": ((0, 1, 0), (0, 0, 1)),
    }
    records = {
        name: support.tangent_closure(point, tangents)
        for name, tangents in cases.items()
    }
    print(json.dumps({
        "schema": "marici.benincasa.rank26-physical-soft-triangle-closure.v1",
        "field": support.cyclic.base.PRIME,
        "point": list(point),
        "records": records,
        "warning": (
            "ordinary tangent closures at the soft-triangle intersection; "
            "the weighted kappa normal and nearby/Rees extension are not included"
        ),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
