"""Exact finite audit of mean-lens laws and changing-domain obstructions.

The algebraic proofs are in dependent-mean-return-laws.md. Exhaustive finite
fixtures are regression checks, not a proof for arbitrary cardinalities.
"""
from fractions import Fraction as F
from itertools import combinations, product
from pathlib import Path
import runpy


def mean(x, members):
    assert members and set(members) <= x.keys()
    return sum((x[i] for i in members), F(0))/len(members)


def shift(x, members, delta):
    return {i: value+(delta if i in members else 0) for i,value in x.items()}


def put(x, members, target):
    return shift(x, members, target-mean(x,members))


ids=range(3)
subsets=[frozenset(c) for n in range(1,4) for c in combinations(ids,n)]
values=tuple(map(F,(-1,0,1)))
law_cases=0
for entries in product(values, repeat=3):
    x=dict(zip(ids,entries))
    for members in subsets:
        assert put(x,members,mean(x,members))==x  # GetPut on CONTENT
        residual={i:x[i]-mean(x,members) for i in members}
        for y,z in product(values,repeat=2):
            returned=put(x,members,y)
            assert mean(returned,members)==y  # PutGet
            assert put(returned,members,z)==put(x,members,z)  # PutPut
            assert {i:returned[i]-y for i in members}==residual
            assert all(returned[i]==x[i] for i in x.keys()-members)
            law_cases+=1
        # Renaming is a genuine complete presentation change.
        rename={0:2,1:0,2:1}
        renamed={rename[i]:v for i,v in x.items()}
        renamed_members=frozenset(rename[i] for i in members)
        left={rename[i]:v for i,v in put(x,members,F(2,3)).items()}
        assert left==put(renamed,renamed_members,F(2,3))

# Insertion: the natural transport of a scoped shift leaves the new ID alone.
# Expanding its scope to the new family generally fails this equation.
insertion_cases=0
for entries in product(values,repeat=2):
    x=dict(enumerate(entries)); members=frozenset(x)
    for v,delta in product(values,repeat=2):
        inserted={**x,2:v}
        edit_then_insert={**shift(x,members,delta),2:v}
        assert edit_then_insert==shift(inserted,members,delta)
        expanded=shift(inserted,frozenset(inserted),delta)
        assert (edit_then_insert==expanded)==(delta==0)
        # Even choosing the unique target mean of the desired result cannot
        # recover it through a full-family minimum-change return.
        desired_mean=mean(edit_then_insert,frozenset(inserted))
        full_return=put(inserted,frozenset(inserted),desired_mean)
        assert (full_return==edit_then_insert)==(delta==0)
        # Alternatively extend the inserted value's action by the same shift.
        assert {**shift(x,members,delta),2:v+delta}==expanded
        insertion_cases+=1

# Absolute mean replacement is not the same action as a scoped increment.
x={0:F(0),1:F(0),2:F(0)}
a=frozenset({0,1}); b=frozenset({1,2})
assert shift(shift(x,a,F(1)),b,F(2))==shift(shift(x,b,F(2)),a,F(1))
assert put(put(x,a,F(1)),b,F(2))!=put(put(x,b,F(2)),a,F(1))

# Audit metadata cannot be silently quotiented away by a content lens law.
module=runpy.run_path(str(Path(__file__).with_name('check_recursive_record_transactions.py')))
store=module['Store']()
store.set_leaf(0,0,1,F(3))
rid=next(iter(store.levels[0]))
before=dict(store.leaves); events=len(store.events)
assert store.commit(store.snapshot(0,rid,F(0)))
assert store.payload(store.leaves[0])==store.payload(before[0])
assert store.leaves[0].version>before[0].version
assert len(store.events)==events+1
print(f'{law_cases} exact content lens-law cases passed, plus renaming, residual, and frame checks.')
print(f'{insertion_cases} insertion cases: old-member scoped transport commutes; expanded-family return fails for every nonzero shift.')
print('Scoped increments commute on overlapping fixed sets; absolute mean replacements need not.')
print('Zero content shift still advances the prototype audit/version state: GetPut is not full-store equality.')
