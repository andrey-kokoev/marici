"""Exact composable edit transport through finite partial-injection changes.

Content changes are affine: surviving IDs keep values; new IDs get supplied
values. Edits follow the linear part, giving zero to newly introduced IDs.
This is a pure semantic checker, not authorization to rebase a Store request.
"""
from dataclasses import dataclass
from fractions import Fraction as F
from itertools import combinations, permutations, product


@dataclass
class Change:
    source: frozenset
    target: frozenset
    survivors: dict  # partial injection source -> target
    inserted: dict  # target complement -> initial values

    def __post_init__(self):
        assert set(self.survivors) <= self.source
        image=set(self.survivors.values())
        assert len(image)==len(self.survivors)
        assert image <= self.target
        assert set(self.inserted)==self.target-image

    def edit(self, delta):
        assert set(delta)==self.source
        out={j:F(0) for j in self.target}
        for i,j in self.survivors.items(): out[j]=delta[i]
        return out

    def state(self, x):
        out=self.edit(x)
        out.update(self.inserted)
        return out

    def then(self, next_change):
        assert self.target==next_change.source
        survivors={i:next_change.survivors[j] for i,j in self.survivors.items()
                   if j in next_change.survivors}
        # Earlier insertions that survive remain inserted relative to the start.
        inserted={next_change.survivors[j]:v for j,v in self.inserted.items()
                  if j in next_change.survivors}
        inserted.update(next_change.inserted)
        return Change(self.source,next_change.target,survivors,inserted)


def identity(ids): return Change(ids,ids,{i:i for i in ids},{})
def add(x,y): return {i:x[i]+y[i] for i in x}
def cost(x): return sum((v*v for v in x.values()),F(0))


def changes(ids):
    result=[]
    for size in range(len(ids)+1):
        for domain in combinations(sorted(ids),size):
            for image in permutations(sorted(ids),size):
                mapping=dict(zip(domain,image))
                inserted={j:F(j+1) for j in ids-set(image)}
                result.append(Change(ids,ids,mapping,inserted))
    return result


ids=frozenset({0,1})
steps=changes(ids)
vectors=[dict(zip(sorted(ids),v)) for v in product(map(F,(-1,0,1)),repeat=2)]
cases=0
for a,b,c in product(steps,repeat=3):
    left=a.then(b).then(c); right=a.then(b.then(c))
    assert left==right
    for delta in vectors:
        assert left.edit(delta)==c.edit(b.edit(a.edit(delta)))
        assert left.state(delta)==c.state(b.state(a.state(delta)))
        cases+=1
for a in steps:
    assert identity(ids).then(a)==a==a.then(identity(ids))
    for x,delta in product(vectors,repeat=2):
        assert a.state(add(x,delta))==add(a.state(x),a.edit(delta))
        assert cost(a.edit(delta))<=cost(delta)
        assert cost(delta)-cost(a.edit(delta))==sum(delta[i]**2 for i in ids-set(a.survivors))

# Genuine cardinality changes, followed by endpoint/label reindexing.
one=frozenset({0}); two=frozenset({0,1}); renamed=frozenset({7,8})
insert=Change(one,two,{0:0},{1:F(9)})
rename=Change(two,renamed,{0:7,1:8},{})
delete=Change(renamed,frozenset({7}),{7:7},{})
delta={0:F(2)}
assert insert.edit(delta)=={0:F(2),1:F(0)}
assert insert.then(rename).then(delete).edit(delta)=={7:F(2)}
# Mean-only return on the enlarged family cannot represent this scoped vector.
transported=insert.edit(delta)
assert len(set(transported.values()))==2

# Deletion followed by restoration is not an identity transport of live edits.
empty=frozenset()
drop=Change(one,empty,{},{}); restore=Change(empty,one,{}, {0:F(5)})
roundtrip=drop.then(restore)
assert roundtrip.state({0:F(5)})=={0:F(5)}
assert roundtrip.edit(delta)=={0:F(0)} != identity(one).edit(delta)
# Incompatible boundaries and noninjective provenance must be rejected.
for invalid in (
    lambda: insert.then(drop),
    lambda: Change(two,one,{0:0,1:0},{}),
):
    try: invalid()
    except AssertionError: pass
    else: raise AssertionError('invalid transport accepted')
print(f'{cases} exact triple-composition cases passed across 7 partial-injection changes.')
print('Identity, associativity, affine state/edit naturality, and exact deleted-cost law passed.')
print('Insertion -> renaming -> deletion preserves scoped edits on surviving members.')
print('Insertion creates a nonuniform edit; a single current-family mean shift is insufficient.')
print('Delete/restore can restore content without restoring edit scope; provenance, not final IDs alone, determines transport.')
