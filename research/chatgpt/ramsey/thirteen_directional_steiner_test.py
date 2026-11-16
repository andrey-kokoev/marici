"""Exact test of rotation/reflection generation of S(2,4,13).

Retains four-set occurrences instead of identifying translated/reflected histories.
Pure standard-library Python; run: python thirteen_directional_steiner_test.py
"""
from itertools import combinations
from collections import Counter
from pathlib import Path
import json

N = 13
V = range(N)
r = lambda v: (v + 1) % N
s = lambda v: (-v) % N
f = lambda v: (5 * v) % N


def shift(B, j):
    return frozenset((x + j) % N for x in B)


def negate(B):
    return frozenset(s(x) for x in B)


def multiply(B, m):
    return frozenset((m*x) % N for x in B)


def diffset(B):
    return Counter((a - b) % N for a in B for b in B if a != b) == Counter(range(1, N))


def orbit(B):
    return {shift(B, i) for i in V}


def pair_multiplicities(blocks):
    counts = Counter()
    for B in blocks:
        for pair in combinations(sorted(B), 2):
            counts[pair] += 1
    return counts


def line_through(blocks, a, b):
    ls = [B for B in blocks if {a,b} <= B]
    assert len(ls) == 1
    return ls[0]


def readable(B):
    return sorted(B)


# All four-subsets passing the exact two-point unique-completion test.
all_diffsets = {frozenset(B) for B in combinations(V,4) if diffset(B)}
assert len(all_diffsets) == 52
all_cyclic_orbits = []
remaining = set(all_diffsets)
while remaining:
    B = min(remaining, key=lambda t: tuple(sorted(t)))
    O = orbit(B)
    assert len(O) == 13 and O <= remaining
    all_cyclic_orbits.append(O)
    remaining -= O
assert len(all_cyclic_orbits) == 4

D = frozenset([0,1,3,9])
assert diffset(D)
plus = orbit(D)
minus = orbit(negate(D))
assert plus.isdisjoint(minus)
assert all(pair_multiplicities(plus)[p] == 1 for p in combinations(V,2))
assert all(pair_multiplicities(minus)[p] == 1 for p in combinations(V,2))
assert all(pair_multiplicities(plus | minus)[p] == 2 for p in combinations(V,2))
assert all(pair_multiplicities(all_diffsets)[p] == 4 for p in combinations(V,2))

# The reflection-stable closures come in two genuinely different 26-block families.
D13_orbits = []
remaining = set(all_diffsets)
while remaining:
    B = min(remaining, key=lambda t: tuple(sorted(t)))
    O = orbit(B) | orbit(negate(B))
    assert len(O) == 26 and O <= remaining
    D13_orbits.append(O)
    remaining -= O
assert len(D13_orbits) == 2
assert plus | minus in D13_orbits

# The Ramsey-critical 13-vertex graph C13(1,5).
red_edges = {frozenset((i, (i+d)%N)) for i in V for d in (1,5)}
assert len(red_edges) == 26
assert {frozenset(f(x) for x in e) for e in red_edges} == red_edges
assert {frozenset(r(x) for x in e) for e in red_edges} == red_edges
assert {frozenset(s(x) for x in e) for e in red_edges} == red_edges

independent_fours = {frozenset(B) for B in combinations(V,4)
                     if all(not e <= frozenset(B) for e in red_edges)}
assert len(independent_fours) == 39
assert not independent_fours & all_diffsets
assert Counter(sum(e <= B for e in red_edges) for B in all_diffsets) == {2:52}

# Multiplication by 5 swaps the two full D13-orbits. Thus the UNLABELED Ramsey graph
# cannot canonically choose one family without breaking one of its automorphisms.
assert {multiply(B,5) for B in D13_orbits[0]} == D13_orbits[1]
assert {multiply(B,5) for B in D13_orbits[1]} == D13_orbits[0]

# The two oriented lines through any unordered pair meet in precisely that pair.
for a,b in combinations(V,2):
    line_plus = line_through(plus,a,b)
    line_minus = line_through(minus,a,b)
    assert line_plus & line_minus == {a,b}
    # Reflect through the midpoint of the pair, swapping endpoints.
    axis_reflection = lambda B: frozenset((a+b-x)%N for x in B)
    assert axis_reflection(line_plus) == line_minus

P = (0,1)
line_plus = line_through(plus,*P)
line_minus = line_through(minus,*P)
hexads = []
for O in D13_orbits:
    candidates = [B for B in O if set(P) <= B]
    assert len(candidates) == 2
    assert candidates[0] & candidates[1] == set(P)
    hexads.append(sorted(candidates[0] | candidates[1]))
assert hexads[0] != hexads[1]

out = {
    "positions": N,
    "group": "D13 = <r,s | r^13=e, s^2=e, srs=r^-1>",
    "all_four_subsets": 715,
    "difference_sets": len(all_diffsets),
    "cyclic_orbit_sizes": [len(O) for O in all_cyclic_orbits],
    "full_rotation_reflection_orbit_sizes": [len(O) for O in D13_orbits],
    "distinct_projective_planes": len(all_cyclic_orbits),
    "seed": readable(D),
    "plane_plus_lines": sorted([readable(B) for B in plus]),
    "plane_minus_lines": sorted([readable(B) for B in minus]),
    "pair_occurrences": {
        "one_plane": sorted(set(pair_multiplicities(plus).values())),
        "one_rotation_reflection_closure": sorted(set(pair_multiplicities(plus|minus).values())),
        "all_perfect_difference_sets": sorted(set(pair_multiplicities(all_diffsets).values()))
    },
    "example_pair": list(P),
    "example_line_plus": readable(line_plus),
    "example_line_minus": readable(line_minus),
    "two_distinct_6_point_carriers_for_example_pair": sorted(hexads),
    "ramsey_graph": {
        "edges": len(red_edges),
        "independent_four_sets": len(independent_fours),
        "four_sets_both_independent_and_projective_lines": len(independent_fours & all_diffsets),
        "red_edges_in_each_projective_line": 2,
        "times5_is_automorphism": True,
        "times5_exchanges_two_reflection_stable_block_families": True,
    },
    "interpretation": "2 endpoints determine 1 line only after choosing one of four cyclic block orbits. Rotation+reflection of one orbit produces two lines; no witnessed higher filler is generated by permutation closure alone."
}
path = Path('/mnt/data/thirteen_directional_steiner_results.json')
path.write_text(json.dumps(out,indent=2) + '\n')
print(json.dumps({k:v for k,v in out.items() if k not in ('plane_plus_lines','plane_minus_lines')}, indent=2))
print('Verified results:', path)
