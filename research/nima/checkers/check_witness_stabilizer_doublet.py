"""Exact witness-fixed carrier split and conditional Gram-weight test.
No observed coupling input, no files written.
"""
from fractions import Fraction as F
from itertools import permutations

u = (1,1,1,1)
v = (3,-1,-1,-1)
h1 = (0,1,-1,0)
h2 = (0,1,0,-1)

def dot(x,y): return sum(a*b for a,b in zip(x,y))
def act(p,x):
    out = [0]*4
    for i in range(4): out[p[i]] = x[i]
    return tuple(out)
def gram(x): return tuple(11*t+sum(x) for t in x)

for tail in permutations((1,2,3)):
    p = (0,)+tail
    assert act(p,u)==u and act(p,v)==v
    for h in (h1,h2):
        moved = act(p,h)
        assert moved[0]==0 and sum(moved)==0
assert all(dot(u,h)==dot(v,h)==0 for h in (h1,h2))
assert gram(u)==tuple(15*t for t in u)
for x in (v,h1,h2): assert gram(x)==tuple(11*t for t in x)

# With an additional equal-per-state identification of the two fixed lines
# as singlet states, average singlet weight=(a+b)/2 and doublet weight=b.
def ratio(a,b): return (a+b)/(2*b)
assert ratio(F(1),F(1))==1
assert ratio(F(15),F(11))==F(13,11)
assert ratio(F(1,15),F(1,11))==F(13,15)
assert ratio(F(7,2),F(1))==F(9,4)
print('Witness stabilizer S3: 4 = 1 + 1 + 2; both lines are trivial S3 reps.')
print('Gram diag=12, offdiag=1: eigenvalues 15 (uniform), 11 (other three).')
print('Conditional mean-singlet/doublet weights: identity=1, Gram=13/11, inverse=13/15.')
print('Required 9/4 would need uniform-mode/contrast-mode weight 7/2.')
print('Exact invariance and weight checks passed; physical matter map unspecified.')
