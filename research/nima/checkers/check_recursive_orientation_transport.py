"""Recursive orientation transport and invariant readout/metric constraints.

Degree2 product classes transform by independent signs. Optional interchange
of the two operands at each comparison node adds binary-tree automorphisms.
These are stated symmetry choices, not inferred physical gauge groups.
"""
from fractions import Fraction as F
from itertools import permutations, product, combinations_with_replacement
from biclique_complex import rank


def compose(g,h):
    # Action sends input coordinate i to position p[i], multiplied by s[i].
    p,s=g; q,t=h
    return tuple(p[q[i]] for i in range(len(p))),tuple(t[i]*s[q[i]] for i in range(len(p)))


def act(g,x):
    p,s=g; result=[F(0)]*len(x)
    for i,value in enumerate(x): result[p[i]]=s[i]*value
    return tuple(result)


def tree_permutations(n):
    if n==1: return {(0,)}
    half=n//2; small=tree_permutations(half); result=set()
    for p,q in product(small,repeat=2):
        result.add(p+tuple(i+half for i in q))
        result.add(tuple(i+half for i in p)+q)
    return result


def metric_dimension(group,n):
    pairs=list(combinations_with_replacement(range(n),2)); labels={pair:i for i,pair in enumerate(pairs)}
    constraints=[]
    for p,s in group:
        for i,j in pairs:
            before=labels[i,j]; after=labels[tuple(sorted((p[i],p[j])))]
            row={after:F(s[i]*s[j])}
            row[before]=row.get(before,F(0))-1
            constraints.append(row)
    return len(pairs)-rank(constraints)


def monomial_orbits(perms,n,degree):
    # Independent sign changes eliminate all monomials with an odd exponent.
    monomials={exponents for exponents in product(range(degree+1),repeat=n)
               if sum(exponents)==degree and all(k%2==0 for k in exponents)}
    orbits=[]
    while monomials:
        exponents=min(monomials); orbit=set()
        for p in perms:
            image=[0]*n
            for i,k in enumerate(exponents): image[p[i]]=k
            orbit.add(tuple(image))
        monomials-=orbit; orbits.append(orbit)
    return orbits


# Primitive orientation really is a representation of rooted context changes.
rooted=[p for p in permutations(range(4)) if p[0]==0]
def parity(p): return (-1)**sum(p[i]>p[j] for i in range(4) for j in range(i+1,4))
for g,h in product(rooted,repeat=2):
    assert parity(tuple(g[h[i]] for i in range(4)))==parity(g)*parity(h)

for n in (1,2,4):
    perms=tree_permutations(n)
    signs=list(product((-1,1),repeat=n))
    labelled=[(tuple(range(n)),s) for s in signs]
    group=[(p,s) for p,s in product(sorted(perms),signs)]
    group_set=set(group)
    assert len(group)=={1:2,2:8,4:128}[n]
    x=tuple(F(i+1) for i in range(n))
    for g,h in product(group,repeat=2):
        combined=compose(g,h)
        assert combined in group_set
        assert act(combined,x)==act(g,act(h,x))
    assert metric_dimension(labelled,n)==n
    assert metric_dimension(group,n)==1
    # No invariant linear readout: each basis direction has an independent flip.
    linear_constraints=[]
    for p,s in group:
        for i in range(n):
            row={p[i]:F(s[i])}; row[i]=row.get(i,F(0))-1
            linear_constraints.append(row)
    assert n-rank(linear_constraints)==0
    quartics=monomial_orbits(perms,n,4)
    assert len(quartics)=={1:1,2:2,4:3}[n]
    # Every admitted invariant quadratic form is lambda*I under tree swaps.
    # The least-change return of a transported linear covector is equivariant.
    a=tuple(F(i+2) for i in range(n)); delta=F(3,7)
    denominator=sum(v*v for v in a)
    returned=tuple(delta*v/denominator for v in a)
    for g in group:
        ga=act(g,a)
        expected=tuple(delta*v/sum(w*w for w in ga) for v in ga)
        assert act(g,returned)==expected
        assert sum(v*v for v in act(g,x))==sum(v*v for v in x)
    print(f'rank{n}: signed tree-action order={len(group)}; labelled metric parameters={n}; exchange-invariant metric parameters=1; invariant linear readouts=0; quartic parameters={len(quartics)}.')

# Tree-preserving swaps retain a quartic sibling/cross-pair distinction.
perms=tree_permutations(4)
def sibling(x): return x[0]**2*x[1]**2+x[2]**2*x[3]**2
def cross(x): return (x[0]**2+x[1]**2)*(x[2]**2+x[3]**2)
x=(F(1),F(2),F(3),F(4))
for p,s in product(perms,product((-1,1),repeat=4)):
    assert sibling(act((p,s),x))==sibling(x)
    assert cross(act((p,s),x))==cross(x)
swap=(0,2,1,3)
assert swap not in perms
assert sibling(act((swap,(1,1,1,1)),x))!=sibling(x)
assert len(monomial_orbits(set(permutations(range(4))),4,4))==2
# At zero, an equivariant request for positive norm cannot select a direction:
# its output would have to be fixed by every sign flip, forcing zero.
assert all(act((tuple(range(4)),s),(F(0),)*4)==(F(0),)*4 for s in product((-1,1),repeat=4))
# An explicitly additive budget carries one chosen scale through the product.
# This is a composition law in addition to symmetry; symmetry alone permits
# a separate common scale at each rank.
scale=F(5,3)
for half in (1,2):
    left=tuple(F(i+1) for i in range(half))
    right=tuple(F(i+3) for i in range(half))
    budget=lambda values:scale*sum(v*v for v in values)
    assert budget(left+right)==budget(left)+budget(right)
print('Composition and least-change covector-return covariance passed at ranks1,2,4.')
print('Rank4 tree symmetry retains three quartic invariants; arbitrary factor permutations retain two.')
print('A positive-norm return from zero needs directional data: the full fixed vector space is zero.')
