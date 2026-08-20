"""Audit whether the down-specific WP10 separator descends through sector exchange.

The original 18 support orbits quotient by S3^3 *and* Yu<->Yd because the
earlier a2-purity question was sector-symmetric. Physical flavor feasibility
is not: up and down spectra are different. This checker separates invariance
under the legitimate labelled S3^3 action from invariance under the extra
sector exchange.
"""
import itertools
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CENSUS = json.loads((ROOT / "results" / "orbit_census.json").read_text())
EXCLUDED = {1, 3, 8, 12}
SLOTS = [(i, j) for i in range(3) for j in range(3)]
INDEX = {slot: k for k, slot in enumerate(SLOTS)}
PERMS = list(itertools.permutations(range(3)))


def permute(mu, md, pq, pu, pd):
    out_u = out_d = 0
    for k, (i, j) in enumerate(SLOTS):
        if mu >> k & 1:
            out_u |= 1 << INDEX[(pq[i], pu[j])]
        if md >> k & 1:
            out_d |= 1 << INDEX[(pq[i], pd[j])]
    return out_u, out_d


def has_perfect_matching(mask):
    support = {(i, j) for k, (i, j) in enumerate(SLOTS) if mask >> k & 1}
    return any(all((i, p[i]) in support for i in range(3)) for p in PERMS)


def connected(mu, md):
    parent = list(range(9))
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    def union(x, y):
        parent[find(x)] = find(y)
    for k, (i, j) in enumerate(SLOTS):
        if mu >> k & 1:
            union(i, 3+j)
        if md >> k & 1:
            union(i, 6+j)
    return len({find(i) for i in range(9)}) == 1


def canonical_s3(mu, md):
    return min(permute(mu, md, pq, pu, pd)
               for pq in PERMS for pu in PERMS for pd in PERMS)


def down_features(mask):
    support = {(i, j) for k, (i, j) in enumerate(SLOTS) if mask >> k & 1}
    col_degrees = [sum(j == col for i, j in support) for col in range(3)]
    row_columns = [{j for i, j in support if i == row} for row in range(3)]
    forced_zeros = sum(
        not (row_columns[i] & row_columns[j])
        for i in range(3) for j in range(i + 1, 3)
    )
    return min(col_degrees), forced_zeros


def separator(mu, md):
    min_col, forced_zeros = down_features(md)
    return min_col >= 2 or forced_zeros >= 2


rows = []
s3_failures = []
exchange_failures = []
for record in CENSUS["orbits"]:
    orbit = record["orbit_index"]
    mu, md = record["mask_u"], record["mask_d"]
    expected = orbit in EXCLUDED
    s3_values = set()
    exchanged_values = set()
    for pq in PERMS:
        for pu in PERMS:
            for pd in PERMS:
                a, b = permute(mu, md, pq, pu, pd)
                s3_values.add(separator(a, b))
                exchanged_values.add(separator(b, a))
    s3_ok = s3_values == {expected}
    exchange_ok = exchanged_values == {expected}
    if not s3_ok:
        s3_failures.append(orbit)
    if not exchange_ok:
        exchange_failures.append(orbit)
    rows.append({
        "orbit": orbit,
        "expected_excluded": expected,
        "s3_values": sorted(s3_values),
        "sector_exchanged_values": sorted(exchanged_values),
        "s3_invariant_and_correct": s3_ok,
        "sector_exchange_preserves_classification": exchange_ok,
    })

out = {
    "schema": "marici.flavor.wp10_sector_exchange_typing_audit.v1",
    "orbit_count": len(rows),
    "s3_failure_orbits": s3_failures,
    "sector_exchange_failure_orbits": exchange_failures,
    "separator_descends_to_s3_cubed": not s3_failures,
    "separator_descends_through_sector_exchange": not exchange_failures,
    "rows": rows,
    "conclusion": (
        "The down-specific separator is well typed on labelled S3^3 orbits "
        "but must not be assumed to descend through Yu/Yd exchange."
    ),
}

# Re-enumerate the physically oriented support set without Yu/Yd exchange.
masks = [m for m in range(512) if has_perfect_matching(m)]
oriented = set()
for mu in masks:
    for md in masks:
        if mu.bit_count()+md.bit_count() == 9 and connected(mu, md):
            oriented.add(canonical_s3(mu, md))
self_exchange = [pair for pair in oriented
                 if canonical_s3(pair[1], pair[0]) == pair]
out["oriented_s3_orbit_count"] = len(oriented)
out["sector_exchange_fixed_orbit_count"] = len(self_exchange)
out["expected_unoriented_count"] = (
    len(self_exchange)+(len(oriented)-len(self_exchange))//2)
out["oriented_count_recovers_18_after_exchange"] = (
    out["expected_unoriented_count"] == len(rows))
(ROOT / "results" / "wp10_sector_exchange_typing_audit.json").write_text(
    json.dumps(out, indent=2) + "\n", encoding="utf-8")
print(json.dumps({k: v for k, v in out.items() if k != "rows"}, indent=2))
