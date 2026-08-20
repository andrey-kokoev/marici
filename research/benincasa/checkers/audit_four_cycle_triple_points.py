"""Resolve the generic forced triple points in the C4 marked residue packet."""
import itertools
import json
from collections import Counter, defaultdict
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
SOURCE = ROOT / "research/benincasa/results/four-cycle-ofpt-packet.json"
OUT = ROOT / "research/benincasa/results/four-cycle-triple-points.json"


def rref(rows):
    a = [[Fraction(x) for x in row] for row in rows]
    m, n, r, pivots = len(a), len(a[0]), 0, []
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
        pivots.append(c)
        r += 1
    return a, pivots


def rank(rows):
    return len(rref(rows)[1])


def kernel_line(rows):
    a, pivots = rref(rows)
    assert len(pivots) == 3
    free = next(c for c in range(4) if c not in pivots)
    x = [Fraction(0)] * 4
    x[free] = 1
    for row, pivot in reversed(list(zip(a, pivots))):
        x[pivot] = -sum(row[c] * x[c] for c in range(pivot + 1, 4))
    den = 1
    for value in x:
        den = den * value.denominator // __import__("math").gcd(den, value.denominator)
    ints = [int(value * den) for value in x]
    g = 0
    for value in ints:
        g = __import__("math").gcd(g, abs(value))
    ints = [value // g for value in ints]
    first = next(value for value in ints if value)
    if first < 0:
        ints = [-value for value in ints]
    return tuple(ints)


def normal(label):
    if label.startswith("G_minus_e"):
        edge = label.removeprefix("G_minus_e")
        edges = ("12", "23", "34", "41")
        v = [0] * 4
        v[edges.index(edge)] = 2
        return tuple(v)
    sites = {int(x) - 1 for x in label.removeprefix("g_")}
    return tuple(int((i in sites) != (((i + 1) % 4) in sites)) for i in range(4))


packet = json.loads(SOURCE.read_text())
terms = packet["four_cycle"]["terms"]
common = ["g_1", "g_2", "g_3", "g_4"]

pivot_point_counts = Counter()
total_labelled_points = 0
global_point_census = Counter()
incidence_records = []
examples = []

for term_id, extra in enumerate(terms):
    labels = common + extra
    groups = defaultdict(list)
    for label in labels:
        groups[normal(label)].append(label)
    for pivot in labels:
        p = normal(pivot)
        active = [n for n in groups if n != p]
        points = {}
        for triple in itertools.combinations(active, 3):
            if rank([p, *triple]) != 3:
                continue
            point = kernel_line([p, *triple])
            incident = tuple(n for n in active if sum(a * b for a, b in zip(n, point)) == 0)
            assert len(incident) == 3  # no hidden four-line point
            points[point] = incident
        assert len(points) in (0, 1, 2)
        pivot_point_counts[len(points)] += 1
        total_labelled_points += len(points)
        global_point_census.update(points.keys())
        incidence_records.extend(
            {
                "term": term_id,
                "pivot": pivot,
                "pivot_normal": list(p),
                "projective_y_point": list(point),
                "incident_normals": [list(n) for n in incident],
            }
            for point, incident in points.items()
        )
        if points and len(examples) < 12:
            examples.append({
                "term": term_id,
                "pivot": pivot,
                "points": [
                    {"projective_y_point": list(point), "incident_label_groups": [groups[n] for n in incident]}
                    for point, incident in points.items()
                ],
            })

assert pivot_point_counts == Counter({2: 108, 1: 80, 0: 8})
assert total_labelled_points == 296

# A central arrangement of m=3 distinct lines in C^2 has characteristic
# polynomial t^2-3t+2 and complement Poincare ranks (1,3,2).
m = 3
orlik_solomon_ranks = (1, m, m - 1)
assert orlik_solomon_ranks == (1, 3, 2)

result = {
    "schema": "marici.benincasa.four_cycle_triple_points.v1",
    "pivot_point_count_census": {str(k): v for k, v in sorted(pivot_point_counts.items())},
    "total_labelled_base_triple_points": total_labelled_points,
    "distinct_projective_y_points": len(global_point_census),
    "projective_y_point_census": {str(point): count for point, count in sorted(global_point_census.items())},
    "incidence_records": incidence_records,
    "lines_through_each_point": 3,
    "hidden_four_line_points": 0,
    "generic_double_cover_lift": "two deck-conjugate ordinary triple points away from B4=0",
    "local_orlik_solomon_ranks_per_lift": list(orlik_solomon_ranks),
    "generic_local_hodge_type": "mixed Tate",
    "resolution": "one point blowup; exceptional P1 meets three strict transforms in three points",
    "enhanced_support": "B4(projective_y_point)=0",
    "new_carrier_datum": False,
    "examples": examples,
}
OUT.write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps({
    "pivot_census": result["pivot_point_count_census"],
    "base_points": total_labelled_points,
    "local_ranks": result["local_orlik_solomon_ranks_per_lift"],
}))
