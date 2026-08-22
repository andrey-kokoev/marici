"""WP13 probe: structural features separating identically_zero from
first_harmonic cases (marici.Figueiredo).

For each orbit representative and each cycle edge as phase placement,
print the derived Q-Q shared-neighbor pair counts (u-side and d-side),
the phase slot, cycle length, and the exact class.
"""
import sys
sys.path.insert(0, "checkers")
from wp13_all_topology_census import (
    slots_of, has_perfect_matching, unique_cycle_edges, canonical_form,
    analyze_case, decode_cycle_edge,
)

masks = range(512)
pm = {m: (bin(m).count("1") in (3, 4, 5, 6)) and has_perfect_matching(m)
      for m in masks}
supports = []
for mu in masks:
    if not pm.get(mu):
        continue
    ku = bin(mu).count("1")
    for md in masks:
        if bin(md).count("1") != 9 - ku or not pm.get(md):
            continue
        cyc = unique_cycle_edges(mu, md)
        if cyc is None:
            continue
        supports.append((mu, md, cyc))

orbits = {}
for mu, md, cyc in supports:
    orbits.setdefault(canonical_form(mu, md), []).append((mu, md, cyc))


def pair_counts(mask):
    """For Q-Q pair (i,j): number of shared column neighbors."""
    cols = [[j for (i, j) in slots_of(mask) if i == r] for r in range(3)]
    out = {}
    for i in range(3):
        for j in range(i + 1, 3):
            out[(i, j)] = len(set(cols[i]) & set(cols[j]))
    return out


for canon, members in sorted(orbits.items()):
    mu, md, cyc = members[0]
    U = pair_counts(mu)
    D = pair_counts(md)
    print(f"== orbit member=({mu},{md}) cycle_len={len(cyc)} "
          f"U={U} D={D}")
    for e in sorted(cyc, key=lambda f: tuple(sorted(f))):
        sector, slot = decode_cycle_edge(e)
        r = analyze_case(mu, md, sector, slot)
        # derived pair containing the phase edge's Q endpoint
        q = slot[0]
        print(f"   phase {sector}{slot} -> {r['class']}"
              f"  (Q endpoint q{q})")
