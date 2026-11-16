#!/usr/bin/env python3
"""Tests an unfitted candidate Ramsey successor selector:
minimize red cross-incidence between consecutively attached neighborhoods.

Includes the smallest counterexample to greedy local completion, a positive
13-to-17 test, and checks both by exact bitset independent-set recurrence.
Does not claim universal successor or an upper-bound theorem.
"""
from itertools import product


def graph(n, edges):
    out=[0]*n
    for i,j in edges:
        assert 0<=i<j<n
        out[i] |= 1<<j
        out[j] |= 1<<i
    return tuple(out)


def alpha_table(g):
    vals=[0]*(1<<len(g))
    for mask in range(1, len(vals)):
        bit=mask & -mask
        v=bit.bit_length()-1
        rest=mask^bit
        vals[mask]=max(vals[rest],1+vals[rest & ~g[v]])
    return vals


def independent(g, mask):
    while mask:
        bit=mask & -mask
        i=bit.bit_length()-1
        mask^=bit
        if mask & g[i]:return False
    return True


def append_vertex(g,S):
    n=len(g)
    assert independent(g,S)
    return tuple((g[i] | (((S>>i)&1)<<n)) for i in range(n)) + (S,)


def eligible(g,k):
    a=alpha_table(g)
    full=(1<<len(g))-1
    return [S for S in range(1<<len(g)) if independent(g,S) and a[full^S] <= k-2]


def has_triangle(g):
    return any(g[i] & g[j] for i in range(len(g)) for j in range(i+1,len(g)) if g[i]>>j&1)


def orbit(g,S,sigma,q):
    result=[]
    for _ in range(q):
        result.append(S)
        S=sum(1<<sigma[v] for v in range(len(g)) if S>>v&1)
    assert S==result[0]
    return result


def cross_edges(g,S,T):
    return sum((g[v]&T).bit_count() for v in range(len(g)) if S>>v&1)


def test_c5():
    c5=graph(5,[(i,(i+1)%5) if i<(i+1)%5 else ((i+1)%5,i) for i in range(5)])
    assert alpha_table(c5)[-1]==2 and not has_triangle(c5)
    first=append_vertex(c5,1<<0) # new a=5, red to 0
    r=[]
    for i in (1,2,3,4):
        second=(1<<5)|(1<<i) # new b=6, red to a and old i
        assert second in eligible(first,4)
        h=append_vertex(first,second)
        assert not has_triangle(h) and alpha_table(h)[-1]==3
        count=len(eligible(h,4))
        r.append((i, int((c5[0]>>i)&1), count))
    assert r == [(1,1,0),(2,0,2),(3,0,2),(4,1,0)]
    # One available valid extension of non-adjacent branch.
    h=append_vertex(first,(1<<5)|(1<<2))
    third=(1<<1)|(1<<3)|(1<<5)
    assert third in eligible(h,4)
    h8=append_vertex(h,third)
    assert len(h8)==8 and not has_triangle(h8) and alpha_table(h8)[-1]==3
    assert not eligible(h8,4)
    return r


def test_c13():
    n=13
    diffs=(1,5,8,12)
    old=tuple(sum(1<<((i+d)%n) for d in diffs) for i in range(n))
    assert not has_triangle(old) and alpha_table(old)[-1]==4
    sigma=tuple((5*i)%13 for i in range(13))
    assert all(sum(1<<sigma[v] for v in range(n) if old[i]>>v&1)==old[sigma[i]] for i in range(n))
    rem=set(range(1,13)); cycles=[]
    while rem:
        start=min(rem); o=[]; x=start
        for _ in range(4): o.append(x); x=sigma[x]
        assert x==start and len(set(o))==4
        rem.difference_update(o);cycles.append(o)
    assert len(cycles)==3
    canonical={}
    for seed in product(*cycles):
        S=sum(1<<v for v in seed)
        if not independent(old,S):continue
        o=orbit(old,S,sigma,4)
        key=min(o)
        if key in canonical:continue
        a=cross_edges(old,o[0],o[1])
        b=cross_edges(old,o[0],o[2])
        assert all(sum((old[v]&o[t]).bit_count() for v in range(n) if (o[t]>>v)&1)==0 for t in range(4))
        assert 4*a+2*b==22
        assert all((o[i]&o[j])==0 for i in range(4) for j in range(i+1,4))
        h=old
        for S_t in o:
            h=append_vertex(h,S_t)
        # add red cycle on the four new vertices
        g=list(h)
        for t in range(4):
            i,j=13+t,13+(t+1)%4
            g[i]|=1<<j;g[j]|=1<<i
        g=tuple(g)
        assert not has_triangle(g)
        alpha=alpha_table(g)[-1]
        canonical[key]=(tuple(sorted(seed)),a,b,alpha)
    assert len(canonical)==5
    values=sorted(canonical.values(),key=lambda x:(x[1],x[0]))
    assert [(x[1],x[2],x[3]) for x in values] == [(2,7,5),(3,5,6),(3,5,6),(4,3,6),(4,3,6)]
    return values

if __name__=='__main__':
    c5=test_c5(); c13=test_c13()
    print('C5: old 0; new a attaches to 0; new b attaches to a and old i')
    print('i | A_old[0,i] | available next red neighborhoods')
    for a,b,c in c5:print(f'{a:1d} | {b:10d} | {c}')
    print('\nC13 orbit representatives (one vertex from each 4-cycle):')
    print('seed | adjacent-phase cross incidence | opposite-phase cross incidence | alpha extended')
    for seed,a,b,al in c13:print(seed,a,b,al)
    print('\nPASS: all exact checks')
