"""Exact composable return paths on the full four-state directed carrier.

No self edges. Unit resource per traversal; uniform choice among three
outgoing edges. Root=0. No particle interpretation or target fitting.
Writes no artifacts.
"""
from itertools import product
from fractions import Fraction as F

states=range(4)
for n in range(2,7):
    paths=[]
    for tail in product(states,repeat=n):
        p=(0,)+tail
        if all(p[i]!=p[i+1] for i in range(n)):
            paths.append(p)
    closed=[p for p in paths if p[-1]==0]
    first=[p for p in closed if 0 not in p[1:-1]]
    assert len(paths)==3**n
    assert len(closed)==(3**n+3*(-1)**n)//4
    assert len(first)==3*2**(n-2)
    prob=F(len(first),len(paths))
    assert prob==F(1,3)*F(2,3)**(n-2)
    assert all(len(p)-1==n for p in first)  # positive path resources
    print(f'length={n}: closed={len(closed)}, first-return={len(first)}, first-return probability={prob}, resource/path={n}')

# After departure, any nonroot state has one edge to root and two to
# another nonroot state. Expected hitting resource h=1+(2/3)h => h=3.
h=F(3)
assert h==1+F(2,3)*h
expected_cycle=1+h
assert expected_cycle==4
print('Root-to-root expected first-return resource=4 traversals.')
print('Uniform full-carrier walk returns with probability one.')
print('Reverse traversal consumes resource: root->i->root costs2.')
print('Previous 1/15552 routing fraction is not implied by this graph.')
print('Exact finite path counts and expected-resource equation passed.')
