"""Derive polygon OFPT denominator packets from exact cosmological-polytope incidence."""
import itertools
import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research/benincasa/results/four-cycle-ofpt-packet.json"


def rank(rows):
    a = [[Fraction(x) for x in row] for row in rows if any(row)]
    if not a:
        return 0
    m, n, r = len(a), len(a[0]), 0
    for c in range(n):
        pivot = next((i for i in range(r, m) if a[i][c]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        p = a[r][c]
        a[r] = [x / p for x in a[r]]
        for i in range(m):
            if i != r and a[i][c]:
                q = a[i][c]
                a[i] = [x - q * y for x, y in zip(a[i], a[r])]
        r += 1
        if r == m:
            break
    return r


def polygon(n):
    # Coordinates are x_0,...,x_(n-1),y_0,...,y_(n-1), where y_i joins i to i+1.
    vertices = []
    for i in range(n):
        j = (i + 1) % n
        for sx_i, sx_j, sy in ((1, 1, -1), (1, -1, 1), (-1, 1, 1)):
            v = [0] * (2 * n)
            v[i], v[j], v[n + i] = sx_i, sx_j, sy
            vertices.append(v)

    facets = {}
    # Proper cyclic intervals.
    for length in range(1, n):
        for start in range(n):
            sites = {(start + k) % n for k in range(length)}
            q = [0] * (2 * n)
            for i in sites:
                q[i] = 1
            for e in range(n):
                if ((e in sites) != (((e + 1) % n) in sites)):
                    q[n + e] = 1
            label = "g_" + "".join(str(i + 1) for i in sorted(sites))
            facets[label] = q
    # Connected all-site spanning paths obtained by deleting one cycle edge.
    for e in range(n):
        q = [1] * n + [0] * n
        q[n + e] = 2
        facets[f"G_minus_e{e + 1}{(e + 1) % n + 1}"] = q
    facets["G"] = [1] * n + [0] * n

    # Every declared q must be a genuine facet: nonnegative on all source
    # vertices, with a codimension-one zero span in projective dimension 2n-1.
    zero_vertices = {}
    for name, q in facets.items():
        values = [sum(a * b for a, b in zip(q, v)) for v in vertices]
        assert min(values) >= 0 and max(values) > 0
        zeros = [v for v, value in zip(vertices, values) if value == 0]
        base = zeros[0]
        assert rank([[x - y for x, y in zip(v, base)] for v in zeros[1:]]) == 2 * n - 2
        zero_vertices[name] = zeros

    common = ["G"] + [f"g_{i + 1}" for i in range(n)]
    remaining = sorted(set(facets) - set(common))
    needed = n - 1
    compatible = []
    for subset in itertools.combinations(remaining, needed):
        zeros = [
            v for v in vertices
            if all(sum(a * b for a, b in zip(facets[name], v)) == 0 for name in subset)
        ]
        if not zeros:
            continue
        base = zeros[0]
        affine_dim = rank([[x - y for x, y in zip(v, base)] for v in zeros[1:]])
        if affine_dim != (2 * n - 1) - needed:
            continue
        denominator_rows = [facets[name] for name in common + list(subset)]
        if rank(denominator_rows) == 2 * n:
            compatible.append(subset)

    # The packet must be closed under the labelled cyclic occurrence action.
    by_vector = {tuple(q): name for name, q in facets.items()}
    def rotate_name(name):
        q = facets[name]
        rotated = [0] * (2 * n)
        for i in range(n):
            rotated[(i + 1) % n] = q[i]
            rotated[n + (i + 1) % n] = q[n + i]
        return by_vector[tuple(rotated)]

    term_set = {tuple(sorted(term)) for term in compatible}
    assert all(
        tuple(sorted(rotate_name(name) for name in term)) in term_set
        for term in compatible
    )
    unseen = set(term_set)
    orbit_sizes = []
    while unseen:
        seed = unseen.pop()
        orbit = {seed}
        current = seed
        for _ in range(n - 1):
            current = tuple(sorted(rotate_name(name) for name in current))
            orbit.add(current)
            unseen.discard(current)
        orbit_sizes.append(len(orbit))

    return {
        "n": n,
        "projective_dimension": 2 * n - 1,
        "source_vertex_count": len(vertices),
        "facet_count": len(facets),
        "common_prefactor": common,
        "additional_denominators_per_term": needed,
        "term_count": len(compatible),
        "cyclic_orbit_sizes": sorted(orbit_sizes),
        "terms": [list(x) for x in compatible],
    }


triangle = polygon(3)
assert triangle["facet_count"] == 10
assert triangle["term_count"] == 6
assert triangle["cyclic_orbit_sizes"] == [3, 3]
assert {tuple(term) for term in triangle["terms"]} == {
    ("G_minus_e12", "g_13"), ("G_minus_e12", "g_23"),
    ("G_minus_e23", "g_12"), ("G_minus_e23", "g_13"),
    ("G_minus_e31", "g_12"), ("G_minus_e31", "g_23"),
}

square = polygon(4)
assert square["facet_count"] == 17
assert all(len(term) == 3 for term in square["terms"])
assert sum(square["cyclic_orbit_sizes"]) == square["term_count"]

packet = {
    "schema": "marici.benincasa.four_cycle_ofpt_packet.v1",
    "method": "exact source-vertex/facet incidence with G plus all singleton facets fixed",
    "triangle_replication": triangle,
    "four_cycle": square,
}
OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(packet, indent=2) + "\n")
print(json.dumps({"triangle_terms": triangle["term_count"], "four_cycle_terms": square["term_count"]}))
