"""Test necessity of single-unlocked-row repair. Enumerate old/new maximal rows
separately: enlarging an old-legal row within its class never hurts coverage.
Bit-parallel exhaustive budget check, repeated rows allowed.
"""
from itertools import combinations
from random import Random

def blue(n,edges):
    sets=[0]
    for i in range(n):
        adj=sum(1<<j for j in range(i) if (j,i) in edges)
        sets += [s|1<<i for s in sets if not s&adj]
    return sets

def maximal(ss):return [s for s in ss if not any(t!=s and t&s==s for t in ss)]

def fit(B,k,rows,d):
    levels=tuple(sum(1<<i for i,b in enumerate(B) if k-1-b.bit_count()==v) for v in range(k))
    ms=[sum(1<<i for i,b in enumerate(B) if not b&r) for r in rows]
    def rec(rem,st,lv):
        if not rem:return ()
        for i in range(st,len(rows)):
            m=ms[i]
            if m&lv[0]:continue
            z=rec(rem-1,i,tuple((v&~m)|((lv[j+1]&m) if j+1<k else 0) for j,v in enumerate(lv)))
            if z is not None:return (rows[i],)+z
        return None
    return rec(d,0,levels)

def audit(n,k,E):
    B=blue(n,E);old=maximal(B)
    if max(map(int.bit_count,B))>k-2:return
    d=next(i for i in reversed(range(k)) if fit(B,k,old,i)!=None)
    if d==k-1:return
    for u,v in sorted(E):
        C=blue(n,E-{(u,v)});new=[s for s in maximal(C) if s>>u&s>>v&1];
        if max(map(int.bit_count,C))>k-2:continue
        win=fit(C,k,maximal(C),d+1)
        if win is None:continue
        # Fix one new row; every remaining row must be old-legal. Encode
        # its misses by raising the size of each missed clique by one dummy bit.
        if all(fit([b if b&r else b|(1<<n) for b in C],k,old,d) is None for r in new):
            return d,(u,v),win

if __name__=='__main__':
    rng=Random(123); 
    for n,k in [(7,5),(8,5),(9,5),(10,6),(11,6),(12,6)]:
        for trial in range(4000):
            pairs=list(combinations(range(n),2));rng.shuffle(pairs);E=set();density=rng.uniform(.35,1)
            for u,v in pairs:
                if rng.random()<density and not any(tuple(sorted((u,w))) in E and tuple(sorted((v,w))) in E for w in range(n)):E.add((u,v))
            a=audit(n,k,E)
            if a:print(n,k,sorted(E),a,flush=True);quit()
        print('completed',n,k,flush=True)
