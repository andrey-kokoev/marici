"""Can the routed Boolean/Tor decorations select literal short facets?"""

from collections import Counter
from itertools import product
import json


ADJACENT = {
    0: (3, 5),
    1: (0, 4),
    2: (1, 5),
    3: (0, 2),
    4: (1, 3),
    5: (2, 4),
}
DOMAIN = tuple(product(range(6), (0, 1), (0, 1)))


def rot_d(x):
    sector, boolean_extra, tor = x
    return (sector + 2) % 6, boolean_extra, tor


def ref_d(x):
    sector, boolean_extra, tor = x
    return (1 - sector) % 6, 1 - boolean_extra, 1 - tor


def rot_t(facet):
    return (facet + 2) % 6


def ref_t(facet):
    return (-facet) % 6


def orbit(seed):
    pending = [seed]
    seen = {seed}
    while pending:
        item = pending.pop()
        for nxt in (rot_d(item), ref_d(item)):
            if nxt not in seen:
                seen.add(nxt)
                pending.append(nxt)
    return tuple(sorted(seen))


def extend(seed, facet):
    assignment = {seed: facet}
    pending = [seed]
    while pending:
        item = pending.pop()
        value = assignment[item]
        for nxt, target in ((rot_d(item), rot_t(value)), (ref_d(item), ref_t(value))):
            if nxt in assignment:
                if assignment[nxt] != target:
                    return None
            else:
                assignment[nxt] = target
                pending.append(nxt)
    if any(value not in ADJACENT[item[0]] for item, value in assignment.items()):
        return None
    return assignment


def main():
    unseen = set(DOMAIN)
    orbits = []
    while unseen:
        current = orbit(min(unseen))
        orbits.append(current)
        unseen.difference_update(current)
    assert sorted(map(len, orbits)) == [6, 6, 6, 6]

    choices = []
    for current in orbits:
        seed = current[0]
        extensions = [
            result
            for facet in ADJACENT[seed[0]]
            if (result := extend(seed, facet)) is not None
        ]
        choices.append(extensions)

    # If reflection is forgotten, rotation gives eight free three-orbits;
    # either adjacent facet may be chosen on every orbit.
    cyclic_orbits = []
    cyclic_unseen = set(DOMAIN)
    while cyclic_unseen:
        seed = min(cyclic_unseen)
        current = (seed, rot_d(seed), rot_d(rot_d(seed)))
        cyclic_orbits.append(current)
        cyclic_unseen.difference_update(current)
    assert len(cyclic_orbits) == 8
    cyclic_selections = 2 ** len(cyclic_orbits)

    complete = []
    for selected in product(*choices):
        merged = {}
        for assignment in selected:
            merged.update(assignment)
        assert len(merged) == 24
        complete.append(merged)

    fibre_censuses = {
        tuple(sorted(Counter(assignment.values()).items()))
        for assignment in complete
    }
    print(json.dumps({
        "status": "falsified_scoped_reflection_compatible_short_facet_selection",
        "domain_rows": len(DOMAIN),
        "free_D3_orbits": len(orbits),
        "orbit_sizes": [len(value) for value in orbits],
        "choices_per_orbit": [len(value) for value in choices],
        "equivariant_adjacent_selections": len(complete),
        "rotation_only_orbits": len(cyclic_orbits),
        "rotation_only_adjacent_selections": cyclic_selections,
        "fibre_censuses": [list(map(list, census)) for census in sorted(fibre_censuses)],
        "canonical_selection": len(complete) == 1,
        "conclusion": (
            "Boolean/Tor decorations permit 256 rotation-equivariant "
            "adjacent selections, but none is compatible with the frozen "
            "reflection action.  The cyclic routing is not a D3 map into "
            "literal short-facet support."
        ),
    }, indent=2))


if __name__ == "__main__":
    main()
