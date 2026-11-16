"""Ramsey pair-attachment witness geometry: exact critical-core census.

A-edge = graph edge; B-edge = nonedge.  For every 2-vertex deletion
of the critical graphs listed below:
  - enumerate every legal one-vertex A-neighborhood (degree-constrained),
  - enumerate A-independent (t-2)-witnesses,
  - compute their *shadows* on legal attachments,
  - select inclusion-maximal shadows,
  - prove minimum pair-conflict witness cover using private pair certificates,
  - independently verify the minimum via exact branch-and-bound,
  - test whether the pair-compatibility graph contains a triangle.

Data: one R(3,5) critical graph on 13 vertices; all seven R(3,6)
critical graphs on 17 vertices; ten sampled R(3,7) critical graphs on
22 vertices.  Not all 191 R(3,7) critical graphs are included.

Requires Python 3 only.  Run: python ramsey_pair_attachment_witness_geometry.py
"""
from collections import Counter
from itertools import combinations

G6_17 = (
    'P??GaOo`XMGsIcT?pSLaGuA?',
    'P?C?I_h`SDEQQcLAh`dU?tG?',
    'P@oGQA?`ACcdCtDYC]Ah?goC',
    'PG?OSAKccKGiGwJSI[@oWUA_',
    'PGD?OkeO_WAEGQobP_s`cgU?',
    'Ps`A?WIDGeCdGsQEKK?oLL_O',
    'Ps`A?_KChFCiBoQSKCOoXL_O',
)
G6_22_SAMPLE = (
    'U???GOOGIGPB`SQgg[cEoKaagg@iI@w@`ROCrGA?',
    'U???GOWH@CAGn?O{hBbHGTQ@y?CHWKSgQPWOgwG?',
    'U???GOcEKBGRPACoag`SDoWEcPEPBAsOG{CGgs_?',
    'U???GQ?HGhHACxPWGX@SQh@IPOSobAt?QbK?Z?`?',
    'U???GSOGKCgIb@RAOkAT?K?}adBBS@wWATOOUcG?',
    'U???GWI_?ch@HLO[CYDOQd@XkOCeGLBO@S_oU__O',
    'U???OGOGIGOROwQXPJCWcKQEgg@wK@kB@ROCpgA?',
    'U???OGOGIGOTOwQTPJCWcKQEgg@wK@kB@ROCpgA?',
    'U???OGPGhwEWI?D?gXKESQDUCedPAAgcFXO?xg??',
    'U???OGUCooCHHEPaHGS@JRCCx@CkHDEOR?eCyK??',
)


def graph6(s):
    n = ord(s[0]) - 63
    adj = [0]*n
    bits = ((ord(c)-63 >> j) & 1 for c in s[1:] for j in range(5,-1,-1))
    for (a,b),bit in zip(((a,b) for b in range(1,n) for a in range(b)),bits):
        if bit:
            adj[a] |= 1<<b
            adj[b] |= 1<<a
    return adj


def circulant(n, distances):
    return [sum(1<<j for j in range(n) if j!=i and min((j-i)%n,(i-j)%n) in distances) for i in range(n)]


def delete_two(adj, u, v):
    assert u<v
    keep = [i for i in range(len(adj)) if i not in (u,v)]
    return [sum(1<<j for j,x in enumerate(keep) if adj[y]>>x&1) for y in keep]


def independent_sets(adj, k):
    result=[]
    def rec(candidates, chosen, remaining):
        if remaining==0:
            result.append(chosen)
            return
        if candidates.bit_count()<remaining:
            return
        while candidates:
            bit=candidates & -candidates
            candidates ^=bit
            v=bit.bit_length()-1
            rec(candidates&~adj[v],chosen|bit,remaining-1)
    rec((1<<len(adj))-1,0,k)
    return result


def verify_base(adj,t):
    assert all(not (adj[u]&adj[v]) for u in range(len(adj))
               for v in range(u+1,len(adj)) if adj[u]>>v&1)
    assert not independent_sets(adj,t)
    assert max(a.bit_count() for a in adj)<=t-1


def legal_attachments(adj,t):
    # Implied by Ramsey: the A-neighbors of every vertex are B-complete.
    eligible = [u for u,a in enumerate(adj) if a.bit_count()<t-1]
    maxind = independent_sets(adj,t-1)
    out=[]
    def rec(j, selected):
        if all(selected&w for w in maxind): out.append(selected)
        if selected.bit_count()==t-1: return
        for k in range(j,len(eligible)):
            u=eligible[k]
            if not(adj[u]&selected):rec(k+1,selected|1<<u)
    rec(0,0)
    return out


def witness_shadows(adj,t,L):
    all_witnesses=independent_sets(adj,t-2)
    footprints={}
    for W in all_witnesses:
        B=sum(1<<i for i,N in enumerate(L) if not(W&N))
        if B and B not in footprints: footprints[B]=W
    maximal=[]
    for B in sorted(footprints,key=lambda b:(b.bit_count(),b),reverse=True):
        if not any(B&~C==0 for C in maximal):maximal.append(B)
    return all_witnesses,maximal,footprints


def clash_pairs(shadows,L_count):
    return [(i,j) for i in range(L_count) for j in range(i,L_count)
            if any((B>>i&1) and (B>>j&1) for B in shadows)]


def private_pair_certificates(maximal, conflict_pairs):
    priv={i:None for i in range(len(maximal))}
    for a,b in conflict_pairs:
        owners=[i for i,B in enumerate(maximal) if (B>>a&1) and (B>>b&1)]
        if len(owners)==1:
            priv[owners[0]]=(a,b)
    return {i:p for i,p in priv.items() if p is not None}


def exact_min_cover(maximal,pairs):
    if not pairs:return 0
    masks=[sum(1<<j for j,(a,b) in enumerate(pairs) if (B>>a&1) and (B>>b&1))
           for B in maximal]
    all_mask=(1<<len(pairs))-1
    hit=[[] for _ in pairs]
    for i,M in enumerate(masks):
        for j in range(len(pairs)):
            if M>>j&1: hit[j].append(i)
    best=[len(masks)]
    seen={}
    def rec(rem,depth):
        if rem==0:
            if depth<best[0]:best[0]=depth
            return
        if depth>=best[0] or seen.get(rem,999999)<=depth:return
        seen[rem]=depth
        nextpair=min((i for i in range(len(pairs)) if rem>>i&1),
                     key=lambda i:len(hit[i]))
        for choice in sorted(hit[nextpair],key=lambda i:-(masks[i]&rem).bit_count()):
            rec(rem&~masks[choice],depth+1)
    rec(all_mask,0)
    return best[0]


def census(t,graphs):
    hist=Counter(); gaps=Counter(); cases=0; total_triangles=0
    all_private_covers=True
    maxcase=None
    for gi,source in enumerate(graphs):
        verify_base(source,t)
        for u,v in combinations(range(len(source)),2):
            G=delete_two(source,u,v)
            L=legal_attachments(G,t)
            witnesses,maximal,all_shadows=witness_shadows(G,t,L)
            pairs=clash_pairs(maximal,len(L))
            private=private_pair_certificates(maximal,pairs)
            # Check if only the unavoidable private-shadow generators cover all pairs.
            private_covers=all(any((maximal[i]>>a&1) and (maximal[i]>>b&1)
                                  for i in private) for a,b in pairs)
            all_private_covers &=private_covers
            minimum=exact_min_cover(maximal,pairs)
            if private_covers: assert minimum==len(private)
            # The largest tested critical graphs have no pairwise-compatible
            # triple of distinct B-adjacent attachments.
            def compatible(a,b):
                return not any((B>>a&1) and (B>>b&1) for B in maximal)
            assert all(not compatible(a,a) for a in range(len(L)))
            for a,b,c in combinations(range(len(L)),3):
                if compatible(a,b) and compatible(a,c) and compatible(b,c):
                    total_triangles+=1
            diag_count=sum(1 for a in range(len(L)) if compatible(a,a))
            assert diag_count==0
            hist[minimum]+=1
            gaps[minimum-len(private)]+=1
            if maxcase is None or (minimum,len(L))>(maxcase['kappa'],maxcase['legal']):
                maxcase={'source_1based':gi+1,'removed_0based':[u,v],
                         'kappa':minimum,'legal':len(L),'all_witnesses':len(witnesses),
                         'all_distinct_nonempty_shadows':len(all_shadows),
                         'maximal_shadows':len(maximal),'private_shadows':len(private),
                         'conflict_pairs_with_diagonal':len(pairs),
                         'private_pair_examples':{str(i):list(pair) for i,pair in private.items()}}
            cases+=1
    assert all_private_covers and total_triangles==0
    return {'t':t,'critical_graphs':len(graphs),'two_deletion_cases':cases,
            'kappa_distribution':dict(sorted(hist.items())),
            'private_cover_gaps':dict(sorted(gaps.items())),
            'pair_compatibility_triangles':total_triangles,
            'max_case':maxcase}


def triple_countermodel(t):
    # Old graph: a star with center 0 and leaves 1,2,3, plus t-4 isolated vertices.
    # Three distinct legal one-step attachments connect A to leaves 1,2,3.
    # Every pair is B-compatible; all three are incompatible.
    assert t>=5
    n=t
    A=[0]*n
    for v in (1,2,3):
        A[0]|=1<<v;A[v]|=1
    verify_base(A,t)
    L=legal_attachments(A,t)
    one=[1<<i for i in (1,2,3)]
    assert all(N in L for N in one)
    W2=independent_sets(A,t-2)
    W3=independent_sets(A,t-3)
    assert all(all(w&(one[i]|one[j]) for w in W2) for i,j in combinations(range(3),2))
    assert any(not (w&(one[0]|one[1]|one[2])) for w in W3)
    return True


def main():
    data={5:[circulant(13,{2,3})],6:[graph6(s) for s in G6_17],
          7:[graph6(s) for s in G6_22_SAMPLE]}
    for t in (5,6,7):
        r=census(t,data[t])
        print('t=',t,'cases=',r['two_deletion_cases'],'kappa_hist=',r['kappa_distribution'],
              'private_coverage_verified=',r['private_cover_gaps'],
              'compatibility_triangles=',r['pair_compatibility_triangles'])
        print('MAX:',r['max_case'])
        assert triple_countermodel(t)
    print('ALL EXACT CHECKS PASSED')

if __name__=='__main__':main()
