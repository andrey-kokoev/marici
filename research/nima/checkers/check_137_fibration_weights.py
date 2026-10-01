"""Exact 137-slot audit under grouping and fresh family labels.

Four-state complete directed graph minus reference edge (0,1) on each side.
Slots are comparisons, not automatically composable traversals. Source/target
families retain members. All weighting choices are explicitly distinguished.
"""
from fractions import Fraction as F
from itertools import product
from collections import defaultdict, Counter

vertices = range(4)
edges = [(a,b) for a,b in product(vertices,repeat=2) if a != b and (a,b) != (0,1)]
slots = [('arrow',e,f) for e,f in product(edges,repeat=2)]
slots += [('state',a,b) for a,b in product(vertices,repeat=2)]
assert len(slots) == len(set(slots)) == 137

for endpoint in (0,1):
    groups = defaultdict(list)
    for slot in slots:
        kind, a, b = slot
        key = (kind,a[endpoint],b[endpoint]) if kind == 'arrow' else slot
        groups[key].append(slot)
    promoted = {i: (key,tuple(members)) for i,(key,members) in enumerate(sorted(groups.items()))}
    assert len(promoted) == 32
    assert {s for _,members in promoted.values() for s in members} == set(slots)
    sizes = Counter(len(members) for _,members in promoted.values())
    assert sizes == Counter({1:16,4:1,6:6,9:9})
    # Every slot's original uniform weight survives grouping iff the group
    # gets its full mass |fiber|/137 before its conditional uniform average.
    restored = {}
    equal_groups = {}
    for _,members in promoted.values():
        group_mass = F(len(members),137)
        for slot in members:
            restored[slot] = group_mass/len(members)
            equal_groups[slot] = F(1,len(promoted)*len(members))
    assert set(restored.values()) == {F(1,137)}
    assert sum(restored.values()) == sum(equal_groups.values()) == 1
    assert restored != equal_groups
    arrow_mass = sum(w for slot,w in equal_groups.items() if slot[0] == 'arrow')
    assert arrow_mass == F(1,2)

# Endpoint matching is a different domain rule, not a regrouping.
composable = [(e,f) for e,f in product(edges,repeat=2) if e[1] == f[0]]
assert len(composable) == 30

# Linear scalar response at unit leg values: delta(x_i*y_j)=dx_i+dy_j.
# Arrow block has22 leg parameters, state block8; the row map rank is28.
rows = []
for i,j in product(range(11),repeat=2):
    row = [F(0)]*30; row[i]=row[11+j]=1; rows.append(row)
for i,j in product(range(4),repeat=2):
    row = [F(0)]*30; row[22+i]=row[26+j]=1; rows.append(row)
rank = 0
for col in range(30):
    pivot = next((i for i in range(rank,len(rows)) if rows[i][col]),None)
    if pivot is None: continue
    rows[rank],rows[pivot] = rows[pivot],rows[rank]
    scale = rows[rank][col]
    rows[rank] = [v/scale for v in rows[rank]]
    for i in range(rank+1,len(rows)):
        scale = rows[i][col]
        if scale: rows[i] = [a-scale*b for a,b in zip(rows[i],rows[rank])]
    rank += 1
assert rank == 28
print('137 comparison slots survive source/target grouping and labelled promotion.')
print('32 groups: 16 of size1, one of size4, six of size6, nine of size9.')
print('Inherited group mass=size/137 preserves every slot weight1/137.')
print('Equal group weighting gives arrow/state block masses1/2 each, instead of121/137 and16/137.')
print('Equal-group per-slot weights: state1/32; arrow1/128,1/192,1/288.')
print('Endpoint-composable arrow pairs:30 (distinct domain from121 comparison pairs).')
print('Independent infinitesimal scalar responses at unit legs:28, despite137 labelled slots.')
