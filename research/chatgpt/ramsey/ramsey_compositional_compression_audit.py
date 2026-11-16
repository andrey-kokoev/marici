"""Ramsey compositional witness audit: reproducible, Python standard library only.

A denotes triangle-free edge color and B denotes nonedge.
Checks all 352 one-deletion instances from one critical (3,5,13) graph,
all seven (3,6,17) critical graphs, and ten (3,7,22) examples.
The ten (3,7,22) examples are not the complete catalogue.

One-step attachment contexts N are A-independent, have |N| <= t-1,
and use only old vertices with degree < t-1.  The exact minimal
witness cover is measured relative to this context set.

Also certifies explicit two-step obstructions in three Ramsey cases.
"""
from itertools import combinations
from collections import Counter

G6_17 = ('P??GaOo`XMGsIcT?pSLaGuA?', 'P?C?I_h`SDEQQcLAh`dU?tG?', 'P@oGQA?`ACcdCtDYC]Ah?goC', 'PG?OSAKccKGiGwJSI[@oWUA_', 'PGD?OkeO_WAEGQobP_s`cgU?', 'Ps`A?WIDGeCdGsQEKK?oLL_O', 'Ps`A?_KChFCiBoQSKCOoXL_O')
G6_22 = ('U???GOOGIGPB`SQgg[cEoKaagg@iI@w@`ROCrGA?', 'U???GOWH@CAGn?O{hBbHGTQ@y?CHWKSgQPWOgwG?', 'U???GOcEKBGRPACoag`SDoWEcPEPBAsOG{CGgs_?', 'U???GQ?HGhHACxPWGX@SQh@IPOSobAt?QbK?Z?`?', 'U???GSOGKCgIb@RAOkAT?K?}adBBS@wWATOOUcG?', 'U???GWI_?ch@HLO[CYDOQd@XkOCeGLBO@S_oU__O', 'U???OGOGIGOROwQXPJCWcKQEgg@wK@kB@ROCpgA?', 'U???OGOGIGOTOwQTPJCWcKQEgg@wK@kB@ROCpgA?', 'U???OGPGhwEWI?D?gXKESQDUCedPAAgcFXO?xg??', 'U???OGUCooCHHEPaHGS@JRCCx@CkHDEOR?eCyK??')

def graph6(s):
    n=ord(s[0])-63
    A=[0]*n
    bits=((ord(c)-63>>k)&1 for c in s[1:] for k in range(5,-1,-1))
    for (i,j),b in zip(((i,j) for j in range(1,n) for i in range(j)),bits):
        if b:A[i]|=1<<j;A[j]|=1<<i
    return A

def circulant(n,steps):
    return [sum(1<<j for j in range(n) if i!=j and min((i-j)%n,(j-i)%n) in steps) for i in range(n)]

def deletion(A,v):
    keep=[x for x in range(len(A)) if x!=v]
    return [sum(1<<j for j,u in enumerate(keep) if (A[w]>>u)&1) for w in keep]

def add_vertex(A,N):
    B=A.copy()+[N]
    z=len(A)
    for u in range(z):
        if N>>u&1:B[u]|=1<<z
    return B

def is_triangle_free(A):
    return all(not (A[i]&A[j]) for i in range(len(A)) for j in range(i+1,len(A)) if A[i]>>j&1)

def independent_sets_of_size(A,k,subset=None):
    n=len(A)
    if subset is None:subset=(1<<n)-1
    out=[]
    def rec(cands,selected,remaining):
        if remaining==0:out.append(selected);return
        if cands.bit_count()<remaining:return
        while cands:
            b=cands&-cands;cands^=b
            v=b.bit_length()-1
            rec(cands&~A[v],selected|b,remaining-1)
    rec(subset,0,k)
    return out

def valid(A,t):
    return is_triangle_free(A) and not independent_sets_of_size(A,t)

def legal_neighborhoods(A,t):
    eligible=[v for v in range(len(A)) if A[v].bit_count()<t-1]
    out=[]
    def rec(start,selected):
        out.append(selected)
        if selected.bit_count()==t-1:return
        for j in range(start,len(eligible)):
            v=eligible[j]
            if not(A[v]&selected):rec(j+1,selected|1<<v)
    rec(0,0)
    return out

def exact_min_cover(A,t):
    candidates=legal_neighborhoods(A,t)
    W=independent_sets_of_size(A,t-1)
    invalid=[N for N in candidates if any(not(N&w) for w in W)]
    if not invalid:return len(candidates),len(candidates),len(W),0
    U=(1<<len(invalid))-1
    patterns=set()
    for w in W:
        coverage=0
        for j,N in enumerate(invalid):
            if not (N&w):coverage|=1<<j
        if coverage:patterns.add(coverage)
    ordered=sorted(patterns,key=int.bit_count,reverse=True)
    nondominated=[]
    for p in ordered:
        if not any(p&~q==0 for q in nondominated):nondominated.append(p)
    for k in range(1,len(nondominated)+1):
        for choices in combinations(nondominated,k):
            c=0
            for p in choices:c|=p
            if c==U:return len(candidates),len(candidates)-len(invalid),len(W),k
    raise AssertionError('no cover')

def check_two_step(t,source,index,N1_vertices,N2_vertices,I_vertices):
    A=deletion(deletion(source,0),0)
    n=len(A)
    N1=sum(1<<u for u in N1_vertices)
    N2=sum(1<<u for u in N2_vertices)
    I=sum(1<<u for u in I_vertices)
    assert valid(A,t)
    assert N1 in legal_neighborhoods(A,t)
    assert N2 in legal_neighborhoods(A,t)
    assert valid(add_vertex(A,N1),t)
    assert valid(add_vertex(A,N2),t)
    assert all(A[u].bit_count() + ((N1>>u)&1)+((N2>>u)&1)<=t-1 for u in range(n))
    assert not (I&(N1|N2)) and I in independent_sets_of_size(A,t-2)
    B=add_vertex(add_vertex(A,N1),N2)
    assert is_triangle_free(B)
    assert not valid(B,t)
    assert all(not(B[u]>>w&1) for u,w in combinations([*I_vertices,n,n+1],2))
    return (t,n,tuple(N1_vertices),tuple(N2_vertices),tuple(I_vertices))

def main():
    data={5:[circulant(13,{2,3})],6:[graph6(g) for g in G6_17],7:[graph6(g) for g in G6_22]}
    for t,graphs in data.items():
        critical_sat=0
        summary=[]
        for G in graphs:
            assert valid(G,t)
            assert max(g.bit_count() for g in G)<=t-1
            sat=sum(1<<i for i,g in enumerate(G) if g.bit_count()==t-1)
            assert independent_sets_of_size(G,t-1,sat)
            critical_sat+=1
            for v in range(len(G)):
                D=deletion(G,v)
                assert valid(D,t)
                summary.append(exact_min_cover(D,t))
        print('R(3,{}) critical checked {} saturated witnesses {}; deletions {} | min-cover histogram {} | old witness range {} | allowed attachments range {} | valid attachment range {}'.format(t,len(graphs),critical_sat,len(summary),dict(sorted(Counter(x[3] for x in summary).items())),(min(x[2] for x in summary),max(x[2] for x in summary)),(min(x[0] for x in summary),max(x[0] for x in summary)),(min(x[1] for x in summary),max(x[1] for x in summary))))
    # C6: each extension works; both together with a B-edge fail.
    C=[(1<<((i+1)%6))|(1<<((i-1)%6)) for i in range(6)]
    assert valid(C,4)
    U=add_vertex(C,(1<<0)|(1<<3))
    assert valid(U,4)
    V=add_vertex(C,(1<<1)|(1<<4))
    assert valid(V,4)
    Both=add_vertex(U,(1<<1)|(1<<4))
    assert is_triangle_free(Both) and not valid(Both,4)
    assert all(not(Both[a]>>b&1) for a,b in combinations((2,5,6,7),2))
    print('C6: individually valid, joint invalid via B4 (2,5,6,7)')
    # Two-step examples from vertex deletions 0,1. Graph6 indices 1-based.
    tests=[
     check_two_step(5,data[5][0],1,(0,1,8,9),(1,2,9),(3,4,10)),
     check_two_step(6,data[6][5],6,(0,1,2),(3,4,11,12),(5,6,13,14)),
     check_two_step(7,data[7][0],1,(0,8,11,12,18,19),(1,10,13,15,19),(3,5,6,9,14)),
    ]
    for t in tests:print('TWO STEP',t)
    print('ALL EXACT CHECKS PASSED')
if __name__=='__main__':main()
