import json


SOURCE = (-1, 1)


def cp_equivariant(portal):
    return all(portal[-s] == -portal[s] for s in SOURCE)


def faithful(portal):
    return len({portal[s] for s in SOURCE}) == 2


def noncollapsed(portal):
    return all(portal[s] != 0 for s in SOURCE)


def main():
    portals = {
        "sign_preserving": {-1: -1, 1: 1},
        "sign_reversing": {-1: 1, 1: -1},
        "collapsed": {-1: 0, 1: 0},
    }

    results = {}
    for name, portal in portals.items():
        results[name] = {
            "cp_equivariant": cp_equivariant(portal),
            "faithful": faithful(portal),
            "noncollapsed": noncollapsed(portal),
        }

    assert results["sign_preserving"] == {
        "cp_equivariant": True,
        "faithful": True,
        "noncollapsed": True,
    }
    assert results["sign_reversing"] == results["sign_preserving"]
    assert results["collapsed"] == {
        "cp_equivariant": True,
        "faithful": False,
        "noncollapsed": False,
    }

    print(
        json.dumps(
            {
                "schema": "marici.flavor_orientation_portal_torsor.v1",
                "results": results,
                "faithful_equivariant_portal_count": 2,
                "verdict": (
                    "CP equivariance permits collapse and leaves two faithful "
                    "orientation sheets. A source-derived comparison is required."
                ),
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
