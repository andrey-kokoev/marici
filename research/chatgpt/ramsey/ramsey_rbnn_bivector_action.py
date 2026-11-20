"""Conditional model: R and B are ordered distinct roles, N slots indistinguishable. S4 acts by permuting slots; no color semantics or transition probabilities assumed."""
from itertools import permutations
V=range(4); G=list(permutations(V)); W=set(permutations('RBNN'))
def word(i,j): return tuple('R' if k==i else 'B' if k==j else 'N' for k in V)
def act(g,w): return tuple(w[g.index(k)] for k in V)
assert W=={word(i,j) for i,j in permutations(V,2)}
for g in G:
    for i,j in permutations(V,2):assert act(g,word(i,j))==word(g[i],g[j])
fiber={w for w in W if w[0]=='R'};pair={word(0,1),word(1,0)}
for S,n in [(fiber,6),(pair,4),({word(0,1)},2)]:assert sum({act(g,w) for w in S}==S for g in G)==n
for flat in (False,True):
    def move(a,b,w):
        assert w[a]=='R';g=list(V);g[a],g[b]=b,a
        if flat:
            c,d=sorted(set(V)-{a,b});g[c],g[d]=d,c
        return act(g,w)
    for a,b,c in permutations(V,3):
        for j in set(V)-{a}:
            w=word(a,j);assert move(b,a,move(a,b,w))==w
            z=move(c,a,move(b,c,move(a,b,w)));assert z==word(a,j if flat else {b:c,c:b}.get(j,j))
print('12 words; stabilizers 6/4/2; both reversible updates and all triangle loops verified')
