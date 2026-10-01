"""Independent comparison routes, quartic descent, and additive readout law.

Extend ordered Cartesian comparison to unequal operand arities to test all
binary bracketings. Keep factor IDs fixed when transporting representations.
Construction histories remain separate from reconstructed member content.
"""
from fractions import Fraction as F
from itertools import permutations, product


def trees(labels):
    if len(labels)==1: return [labels[0]]
    return [(left,right) for split in range(1,len(labels))
            for left in trees(labels[:split]) for right in trees(labels[split:])]


def encode(tree,values):
    if isinstance(tree,int): return (tree,values[tree])
    return (encode(tree[0],values),encode(tree[1],values))


def decode(tree,record):
    if isinstance(tree,int):
        assert record[0]==tree
        return {tree:record[1]}
    left=decode(tree[0],record[0]); right=decode(tree[1],record[1])
    assert left.keys().isdisjoint(right)
    return left|right


def history(tree):
    if isinstance(tree,int): return (),frozenset({tree})
    lh,ls=history(tree[0]); rh,rs=history(tree[1])
    return lh+rh+((ls,rs),),ls|rs


ordered=trees((0,1,2,3))
assert len(ordered)==5
all_routes=[tree for labels in permutations(range(4)) for tree in trees(labels)]
assert len(all_routes)==120
primitive=[edge for edge in product(range(4),repeat=2) if edge[0]!=edge[1]]
# Exhaust all arrow quadruples through every order-preserving bracketing.
coverage=0
for entries in product(primitive,repeat=4):
    values=dict(enumerate(entries))
    for tree in ordered:
        assert decode(tree,encode(tree,values))==values
        coverage+=1
# Rebracketing plus factor exchange still preserves the explicitly named IDs.
values=dict(enumerate(primitive[:4]))
for tree in all_routes:
    assert decode(tree,encode(tree,values))==values
assert len({history(tree)[0] for tree in ordered})==5

alpha=F(3,2); beta=F(5,3)


def merge(left,right):
    q,f=left; r,g=right
    return q+r,f+g+beta*q*r


def evaluate(tree,x):
    if isinstance(tree,int): return x[tree]**2,alpha*x[tree]**4
    return merge(evaluate(tree[0],x),evaluate(tree[1],x))


def gradient(tree,x):
    if isinstance(tree,int):
        return ({tree:2*x[tree]},{tree:4*alpha*x[tree]**3})
    left,right=tree
    q,_=evaluate(left,x); r,_=evaluate(right,x)
    dq,df=gradient(left,x); dr,dg=gradient(right,x)
    return dq|dr,({i:df[i]+beta*dq[i]*r for i in dq}|
                  {i:dg[i]+beta*q*dr[i] for i in dr})


def depth_weighted(tree,x,depth=0):
    if isinstance(tree,int): return x[tree]**2,alpha*x[tree]**4
    q,f=depth_weighted(tree[0],x,depth+1)
    r,g=depth_weighted(tree[1],x,depth+1)
    return q+r,f+g+F(depth+1)*q*r


states=list(product(map(F,(-1,0,2)),repeat=4))
checks=0
for entries in states:
    x=dict(enumerate(entries))
    q=sum(v*v for v in entries)
    expected=alpha*sum(v**4 for v in entries)+beta*sum(
        entries[i]**2*entries[j]**2 for i in range(4) for j in range(i+1,4))
    expected_gradient={i:4*alpha*x[i]**3+2*beta*x[i]*(q-x[i]**2) for i in x}
    for tree in all_routes:
        assert evaluate(tree,x)==(q,expected)
        assert gradient(tree,x)[1]==expected_gradient
        # The linearized least-change return is therefore route-independent.
        norm=sum(v*v for v in expected_gradient.values())
        if norm:
            returned={i:F(1,7)*v/norm for i,v in gradient(tree,x)[1].items()}
            assert sum(expected_gradient[i]*returned[i] for i in x)==F(1,7)
        # Change to an additive coordinate: this bilinear merge term is a coboundary.
        assert expected-beta*q*q/2==(alpha-beta/2)*sum(v**4 for v in entries)
        checks+=1

# History-sensitive coefficients do not descend, even without swapping IDs.
x={0:F(1),1:F(2),2:F(3),3:F(4)}
assert len({depth_weighted(tree,x)[1] for tree in ordered})>1
balanced=((0,1),(2,3)); crossed=((0,2),(1,3))
assert depth_weighted(balanced,x)!=depth_weighted(crossed,x)
# The associator is exactly the additive2-cocycle identity.
for q,r,s in product(map(F,(-2,0,3)),repeat=3):
    assert beta*q*r+beta*(q+r)*s==beta*r*s+beta*q*(r+s)
    assert merge(merge((q,F(1)),(r,F(2))),(s,F(3)))==merge((q,F(1)),merge((r,F(2)),(s,F(3))))
print(f'{coverage} full-relation arrow-quadruple/bracketing reconstructions passed.')
print('All120 bracketed factor-order routes preserve named content; the5 ordered bracketings retain distinct histories.')
print(f'{checks} quartic/gradient route checks passed; differential minimum-change returns agree.')
print('Uniform bilinear composition F(L,R)=F(L)+F(R)+beta*Q(L)*Q(R) is associative and exchange-invariant.')
print('Depth-dependent coupling fails ordered rebracketing; its readout needs construction history.')
print('F-beta*Q^2/2 is additive: coherent quartic composition leaves coefficients free and admits an additive coordinate.')
