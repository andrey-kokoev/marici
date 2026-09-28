"""Exact pairwise-settling prototype on three nonreference state values.

Shared fourth state is held fixed outside this vector. Pair comparison sets
both values to their mean. This update rule is a trial, not carrier-derived.
Every comparison attempt costs one unit, including zero-change attempts.
Writes no files. No mass-ratio target enters this calculation.
"""
from fractions import Fraction as F


def update(x,i,j):
    y=list(x)
    y[i]=y[j]=(x[i]+x[j])/2
    return tuple(y)


def disagreement(x):
    mean=sum(x)/3
    return sum((v-mean)**2 for v in x)


start=(F(1),F(0),F(0))
first=update(start,0,1)
second=update(first,1,2)
assert first==(F(1,2),F(1,2),F(0))
assert second==(F(1,2),F(1,4),F(1,4))
assert first[0]==first[1] and second[0]!=second[1]
print(f'Initial={start}; compare01 -> {first}; compare12 -> {second}')
print('Second comparison reopens the first agreement by1/4.')

schedule=((0,1),(1,2),(2,0))
x=start
initial_energy=disagreement(x)
assert initial_energy==F(2,3)
settled_drop=F(0)
hits={F(1,10):None,F(1,100):None,F(1,1000):None}
for step in range(1,61):
    i,j=schedule[(step-1)%3]
    y=update(x,i,j)
    drop=disagreement(x)-disagreement(y)
    assert drop==(x[i]-x[j])**2/2
    assert drop>=0
    settled_drop+=drop
    x=y
    assert sum(x)==1
    assert all(v.denominator & (v.denominator-1)==0 for v in x)
    assert settled_drop+disagreement(x)==initial_energy
    spread=max(x)-min(x)
    for tolerance in hits:
        if hits[tolerance] is None and spread<=tolerance:
            hits[tolerance]=step
assert all(n is not None for n in hits.values())
assert disagreement(x)>0
for tolerance,step in hits.items():
    print(f'Absolute spread <= {tolerance}: {step} comparison attempts at unit cost each.')
print('Finite updates retain dyadic coordinates; exact consensus would require1/3.')
print('Hence this initial state cannot settle exactly after finitely many averaging updates.')
print('Cumulative decrease in squared disagreement tends to2/3 as consensus is approached.')
print('Traversal cost and decrease in disagreement are distinct resource models.')
# Scaling the input preserves schedule but scales quadratic discrepancy drops.
scaled=tuple(2*v for v in start)
assert disagreement(scaled)==4*initial_energy
print('Doubling initial disturbance multiplies squared-disagreement budget by4.')
print('Exact disturbance propagation, positivity, and accounting checks passed.')
