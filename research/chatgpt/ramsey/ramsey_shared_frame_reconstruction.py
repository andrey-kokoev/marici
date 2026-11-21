"""Construct every labelled external wiring on the common 187/188 frame."""
from itertools import combinations,permutations
from collections import Counter
from ramsey_six_point_reconstruction import independent
T=['a','b','c','d','ab','cd','ae','be','cf','df','ef','ef','ace','bdf','abcd'];n=len(T)
allowed=[{j for j,t in enumerate(T) if set(s).isdisjoint(t)} for s in T];degree=[6-len(t) for t in T];N=[set() for _ in T];counts=Counter();goods=[]
def search(left,visit=None):
    if not left:
        if visit is not None:
            visit(N);return
        A=[0]*22
        def add(i,j):A[i]|=1<<j;A[j]|=1<<i
        for i in range(1,7):add(0,i)
        for v,t in enumerate(T):
            for c in t:add(7+v,1+ord(c)-ord('a'))
            for w in N[v]:add(7+v,7+w)
        good=not independent(A,(1<<22)-1,7);counts[good]+=1
        if good:goods.append(frozenset((i,j) for i in range(n) for j in N[i] if i<j))
        return
    opts=[]
    for i in left:
        need=degree[i]-len(N[i]);avail=[j for j in allowed[i]&left if len(N[j])<degree[j] and not N[i]&N[j]]
        if need>len(avail):return
        from math import comb
        opts.append((comb(len(avail),need),i,need,avail))
    _,i,k,avail=min(opts)
    for subset in combinations(avail,k):
        if any(v in N[u] for u,v in combinations(subset,2)):continue
        for j in subset:N[i].add(j);N[j].add(i)
        search(left-{i},visit)
        for j in subset:N[i].remove(j);N[j].remove(i)

if __name__=='__main__':
    search(set(range(n)));print('labelled counts',counts);autos=[]
    for p in permutations('abcdef'):
        im=[''.join(sorted(p[ord(c)-97] for c in t)) for t in T]
        if Counter(im)!=Counter(T):continue
        q=[T.index(t) for t in im];a,b=[i for i,t in enumerate(im) if t=='ef'];q[b]+=1;autos.append(q[:]);q[a],q[b]=q[b],q[a];autos.append(q)
    rest=set(goods);sizes=[]
    while rest:
        E=next(iter(rest));orb={frozenset(tuple(sorted((q[i],q[j]))) for i,j in E) for q in autos};assert orb<=rest;rest-=orb;sizes.append(len(orb))
    print('frame automorphisms',len(autos),'valid rooted orbit sizes',sizes)
