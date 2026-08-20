"""Audit forced infinity coincidences and concurrencies in the 28-term C4 OFPT packet."""
import itertools
import json
from collections import Counter, defaultdict
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
SOURCE = ROOT / "research/benincasa/results/four-cycle-ofpt-packet.json"
OUT = ROOT / "research/benincasa/results/four-cycle-residue-incidence.json"


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
    return r


def normal(label):
    # Edge order: 12,23,34,41.
    if label.startswith("G_minus_e"):
        edge = label.removeprefix("G_minus_e")
        edges = ("12", "23", "34", "41")
        v = [0] * 4
        v[edges.index(edge)] = 2
        return tuple(v)
    assert label.startswith("g_")
    sites = {int(x) - 1 for x in label.removeprefix("g_")}
    v = []
    for i in range(4):
        v.append(int((i in sites) != (((i + 1) % 4) in sites)))
    return tuple(v)


packet = json.loads(SOURCE.read_text())
terms = packet["four_cycle"]["terms"]
common = ["g_1", "g_2", "g_3", "g_4"]

term_profiles = Counter()
pivot_profiles = Counter()
forced_pairs = Counter()
forced_triples = Counter()
examples = defaultdict(list)

for term_id, extra in enumerate(terms):
    labels = common + extra
    groups = defaultdict(list)
    for label in labels:
        groups[normal(label)].append(label)
    profile = tuple(sorted(len(x) for x in groups.values()))
    term_profiles[str(profile)] += 1
    if len(examples[f"term_{profile}"]) < 2:
        examples[f"term_{profile}"].append({"term": term_id, "groups": list(groups.values())})

    for pivot in labels:
        p = normal(pivot)
        partners = sorted(set(groups[p]) - {pivot})
        active_groups = {n: xs for n, xs in groups.items() if n != p}
        active_normals = list(active_groups)

        coincident_line_pairs = []
        for a, b in itertools.combinations(active_normals, 2):
            if rank([p, a, b]) <= 2:
                coincident_line_pairs.append((active_groups[a], active_groups[b]))

        concurrent_triples = []
        for a, b, c in itertools.combinations(active_normals, 3):
            if rank([p, a, b, c]) <= 3:
                concurrent_triples.append((active_groups[a], active_groups[b], active_groups[c]))

        key = (
            len(partners),
            len(active_normals),
            len(coincident_line_pairs),
            len(concurrent_triples),
        )
        pivot_profiles[str(key)] += 1
        forced_pairs[len(coincident_line_pairs)] += 1
        forced_triples[len(concurrent_triples)] += 1
        if len(examples[f"pivot_{key}"]) < 2:
            examples[f"pivot_{key}"].append({
                "term": term_id,
                "pivot": pivot,
                "parallel_partner": partners,
                "active_line_groups": list(active_groups.values()),
                "coincident_line_pairs": coincident_line_pairs,
                "concurrent_line_triples": concurrent_triples,
            })

assert sum(term_profiles.values()) == 28
assert sum(pivot_profiles.values()) == 28 * 7
assert any("2" in profile for profile in term_profiles)

result = {
    "schema": "marici.benincasa.four_cycle_residue_incidence.v1",
    "term_count": 28,
    "residue_pivot_count": 196,
    "term_normal_multiplicity_profiles": dict(term_profiles),
    "pivot_profile_key": [
        "parallel_partner_count",
        "active_distinct_line_count",
        "coincident_active_line_pair_count",
        "concurrent_active_line_triple_count",
    ],
    "pivot_profiles": dict(pivot_profiles),
    "forced_active_pair_census": {str(k): v for k, v in sorted(forced_pairs.items())},
    "forced_active_triple_census": {str(k): v for k, v in sorted(forced_triples.items())},
    "examples": dict(examples),
    "classification": "source-forced infinity incidence on the existing marked-hyperplane carrier",
}
OUT.write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps({
    "term_profiles": result["term_normal_multiplicity_profiles"],
    "pivot_profiles": result["pivot_profiles"],
}))
