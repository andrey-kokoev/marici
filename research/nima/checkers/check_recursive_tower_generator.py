"""Repeat the same incoming-family promotion through two tower cycles.

Compare endpoint footprints with an explicit coarser endpoint policy. Both
retain full member references. Count families/support; no gauge identification.
"""
from dataclasses import dataclass
from itertools import product
from collections import defaultdict
from fractions import Fraction as F


@dataclass(frozen=True)
class Record:
    rid: tuple
    source: object
    target: object
    members: tuple
    leaves: frozenset


def index(records, field):
    groups=defaultdict(list)
    for row in records.values(): groups[getattr(row,field)].append(row.rid)
    return dict(groups)


def promote(records, depth, policy):
    result={}
    for serial,(key,members) in enumerate(index(records,'target').items()):
        members=tuple(members)
        source=('source-footprint',frozenset(records[m].source for m in members))
        target=('target-footprint',frozenset(records[m].target for m in members))
        if policy=='coarse':
            # Explicit alternative endpoint: one common target, all detail
            # remains recoverable from child records and membership links.
            target=('common-target',)
        rid=(depth,serial)
        leaves=frozenset().union(*(records[m].leaves for m in members))
        result[rid]=Record(rid,source,target,members,leaves)
    return result


def verify_views(records):
    for field in ('source','target'):
        groups=index(records,field)
        restored={rid:records[rid] for members in groups.values() for rid in members}
        assert restored==records


def leaf_mean(row, values):
    return sum((values[i] for i in row.leaves),F(0))/len(row.leaves)


V=range(4)
edges=[e for e in product(V,repeat=2) if e[0]!=e[1] and e!=(0,1)]
slots=[('arrow',a,b) for a,b in product(edges,repeat=2)]
slots += [('state',a,b) for a,b in product(V,repeat=2)]
base={}
for i,(kind,a,b) in enumerate(slots):
    source=(kind,a[0],b[0]) if kind=='arrow' else (kind,a,b)
    target=(kind,a[1],b[1]) if kind=='arrow' else (kind,a,b)
    rid=(0,i)
    base[rid]=Record(rid,source,target,(),frozenset({rid}))
values={rid:F(i,7) for i,rid in enumerate(base)}

profiles={}
for policy in ('footprint','coarse'):
    levels=[base]
    for depth in range(1,4):
        old=levels[-1]; new=promote(old,depth,policy)
        verify_views(old); verify_views(new)
        assert set().union(*(r.leaves for r in new.values()))==set(base)
        assert sum(len(r.leaves) for r in new.values())==len(base)
        for row in new.values():
            assert frozenset().union(*(old[m].leaves for m in row.members))==row.leaves
            weighted=sum((len(old[m].leaves)*leaf_mean(old[m],values) for m in row.members),F(0))/len(row.leaves)
            assert weighted==leaf_mean(row,values)
            # Mean-return composition under this partition policy: same delta
            # on each child updates precisely the direct parent's leaf support.
            staged={i:F(0) for i in base}
            for child in row.members:
                for i in old[child].leaves: staged[i]+=F(2,3)
            direct={i:F(2,3) if i in row.leaves else F(0) for i in base}
            assert staged==direct
        levels.append(new)
    profiles[policy]=[len(level) for level in levels]
    if policy=='footprint':
        assert all(len(row.members)==1 for level in levels[2:] for row in level.values())
        supports=[{r.leaves for r in level.values()} for level in levels[1:]]
        assert supports[0]==supports[1]==supports[2]
    else:
        assert len(levels[2])==1 and len(next(iter(levels[2].values())).members)==32

assert profiles['footprint']==[137,32,32,32]
assert profiles['coarse']==[137,32,1,1]
print('Same incoming-family rule repeated:')
for policy,counts in profiles.items(): print(f'  {policy}: record counts {counts}')
print('Both policies reconstruct all 137 leaves and preserve weighted means and direct/staged returns.')
print('Footprint targets separate first-level families: every later promotion is singleton wrapping.')
print('Coarse targets merge all 32 families at the next cycle. Coherence alone admits both policies.')
print('Neither construction derives a 1,2,4 structural progression.')
