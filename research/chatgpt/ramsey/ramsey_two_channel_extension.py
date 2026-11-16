#!/usr/bin/env python3
"""Exact two-channel Ramsey vertex-extension law.

G is red.  A candidate neighborhood S of a new red vertex is independent,
with alpha(G-S) <= k-2.  This script verifies the exact recursive update for
all triangle-free unlabeled graphs with at most seven vertices and k=3,4,5.
It also calculates explicit branch and compatibility examples.

Dependencies: networkx for the graph atlas only. All certificate tests use
integer masks, DP and exact integer arithmetic. No Ramsey threshold is input.
"""
from itertools import combinations
from collections import Counter
import networkx as nx


def adjacency(g):
    n = len(g)
    assert sorted(g.nodes()) == list(range(n))
    return tuple(sum(1 << j for j in g.neighbors(i)) for i in range(n))


def alpha_table(adj):
    n = len(adj)
    table = [0] * (1 << n)
    for mask in range(1,1<<n):
        vbit=mask & -mask
        v=vbit.bit_length()-1
        rest=mask ^ vbit
        table[mask]=max(table[rest],1+table[rest & ~adj[v]])
    return table


def independent(adj, mask):
    while mask:
        vbit=mask & -mask
        v=vbit.bit_length()-1
        mask ^= vbit
        if adj[v] & mask: return False
    return True


def eligible(adj, k, alpha=None):
    n=len(adj)
    alpha = alpha if alpha is not None else alpha_table(adj)
    allverts=(1<<n)-1
    return {S for S in range(1<<n)
            if independent(adj,S) and alpha[allverts^S] <= k-2}


def extend(adj,S):
    n=len(adj)
    assert independent(adj,S)
    old=tuple(a | ((1<<n) if (S>>v)&1 else 0) for v,a in enumerate(adj))
    return old+(S,)


def two_channel_prediction(adj,k,S,eligible_old=None,alpha=None):
    n=len(adj)
    alpha=alpha if alpha is not None else alpha_table(adj)
    eligible_old = eligible_old if eligible_old is not None else eligible(adj,k,alpha)
    allverts=(1<<n)-1
    no_new={R for R in eligible_old
            if alpha[allverts & ~(R|S)] <= k-3}
    with_new={(1<<n)|R for R in eligible_old if not (R&S)}
    return no_new,with_new


def max_independent_sets(adj,alpha=None):
    n=len(adj)
    alpha=alpha if alpha is not None else alpha_table(adj)
    a=alpha[(1<<n)-1]
    return [S for S in range(1<<n) if S.bit_count()==a and independent(adj,S)]


def compatibility_faces(adj):
    """Return f-vector of the compatibility simplicial complex.
    Intended for small cases; expensive for many maximum independent sets.
    """
    n=len(adj)
    maxima=max_independent_sets(adj)
    alpha=alpha_table(adj)
    size=len(maxima)
    Slist=[S for S in range(1<<n) if independent(adj,S)]
    support=[sum(1<<i for i,I in enumerate(maxima) if I&S) for S in Slist]
    compatible=set()
    for hit in support:
        # Every subset of the hit-mask is a compatible face.
        sub=hit
        while True:
            compatible.add(sub)
            if sub==0:break
            sub=(sub-1)&hit
    f=Counter(x.bit_count() for x in compatible)
    return maxima,compatible,[f[i] for i in range(size+1)]


def homology_mod2(faces,vertex_count):
    groups=[[s for s in faces if s.bit_count()==d] for d in range(vertex_count+1)]
    ranks=[]
    for d in range(1,vertex_count+1):
        idx={s:j for j,s in enumerate(groups[d-1])}
        pivots={}
        for face in groups[d]:
            boundary=0
            bits=face
            while bits:
                bit=bits & -bits
                boundary ^= 1<<idx[face^bit]
                bits^=bit
            while boundary:
                pos=boundary.bit_length()-1
                if pos not in pivots:
                    pivots[pos]=boundary;break
                boundary^=pivots[pos]
        ranks.append(len(pivots))
    unred=[len(groups[d])-(ranks[d-1] if d else 0)-(ranks[d] if d<len(ranks) else 0)
           for d in range(vertex_count+1)]
    # The empty face is the augmented chain group C_{-1}.
    # Therefore unred[d] is reduced homology in topological degree d-1.
    return unred[1:]


def example(name,g,k,S):
    adj=adjacency(g); alpha=alpha_table(adj); E=eligible(adj,k,alpha)
    assert S in E
    newadj=extend(adj,S)
    Enew=eligible(newadj,k)
    A,B=two_channel_prediction(adj,k,S,E,alpha)
    assert Enew == A|B and not A&B
    oldmax=max_independent_sets(adj)
    newmax=max_independent_sets(newadj)
    print(name,'k',k,'G vertices',len(g),'alpha',alpha[-1],
          'S',sorted(v for v in range(len(g)) if (S>>v)&1),
          'old extension neighborhoods',len(E),
          'H extension neighborhoods',len(Enew),
          'type no-new',len(A),'type with-new',len(B),
          'old max independent sets',len(oldmax),'new',len(newmax))
    if len(newmax)<=12:
        oldM,oldC,oldf=compatibility_faces(adj)
        newM,newC,newf=compatibility_faces(newadj)
        print('  compatibility f-vectors',oldf,newf)
        print('  reduced mod2 Betti',homology_mod2(oldC,len(oldM)),
              homology_mod2(newC,len(newM)))
    return len(Enew)



def assemble_several(adj, neighborhoods, red_new_edges):
    """Add m new vertices, with old red neighbors and prescribed red-new edges."""
    n=len(adj);m=len(neighborhoods)
    out=list(adj)+[0]*m
    for j,S in enumerate(neighborhoods):
        for v in range(n):
            if (S>>v)&1:
                out[v] |= 1<<(n+j)
                out[n+j] |= 1<<v
    for j,l in combinations(range(m),2):
        if (j,l) in red_new_edges:
            out[n+j] |= 1<<(n+l)
            out[n+l] |= 1<<(n+j)
    return tuple(out)


def multivertex_alpha_prediction(adj,neighborhoods,red_new_edges):
    """Exact maximum: max over independent subsets of the new-vertex graph."""
    m=len(neighborhoods)
    base_alpha=alpha_table(adj)
    allold=(1<<len(adj))-1
    out=0
    for J in range(1<<m):
        if any((J>>i)&1 and (J>>j)&1 for i,j in red_new_edges):continue
        union=0
        for j in range(m):
            if (J>>j)&1: union |= neighborhoods[j]
        out=max(out,J.bit_count()+base_alpha[allold & ~union])
    return out


def multivertex_regression():
    """Full 3-new-vertex audit over all 512 neighborhood triples and 8 red patterns."""
    old=adjacency(nx.empty_graph(3)); k=4
    patterns=list(combinations(range(3),2))
    tested=0
    pairwise_legal_but_triple_illegal=0
    for S0 in range(8):
      for S1 in range(8):
       for S2 in range(8):
        neighborhoods=(S0,S1,S2)
        for flag in range(8):
            red={pair for bit,pair in enumerate(patterns) if flag>>bit&1}
            combined=assemble_several(old,neighborhoods,red)
            predicted=multivertex_alpha_prediction(old,neighborhoods,red)
            assert predicted == alpha_table(combined)[-1]
            # Triangle-freeness is equivalent to the graph on the new vertices
            # being triangle-free and every red new pair having disjoint old
            # red neighborhoods. The base is triangle-free and each S_j is.
            triangle_free = flag!=7 and all(not(neighborhoods[i]&neighborhoods[j])
                                               for i,j in red)
            actual_triangle_free=all(not(combined[i]&combined[j])
                                     for i in range(6) for j in range(i+1,6)
                                     if combined[i]>>j&1)
            assert triangle_free == actual_triangle_free
            tested+=1
            if flag==0: # all three new vertices are mutually blue
                singly_legal=all(1+(3-S.bit_count())<=3 for S in neighborhoods)
                pairwise_legal=all(2+(3-(neighborhoods[i]|neighborhoods[j]).bit_count())<=3
                                   for i,j in patterns)
                if singly_legal and pairwise_legal and predicted>3:
                    pairwise_legal_but_triple_illegal+=1
    assert tested==4096
    assert pairwise_legal_but_triple_illegal==39
    print('triple exact regression:',{'assembled_graphs':tested,
          'pairwise_legal_but_triple_forbidden':pairwise_legal_but_triple_illegal})

def atlas_regression():
    tests=Counter()
    for g in nx.graph_atlas_g():
        n=len(g)
        if n>7:continue
        adj=adjacency(g)
        if any((adj[i]&adj[j]) for i,j in g.edges()):continue
        alpha=alpha_table(adj)
        for k in (3,4,5):
            if alpha[-1]>k-1:continue
            E=eligible(adj,k,alpha)
            tests[f'graphs_k{k}']+=1
            for S in E:
                A,B=two_channel_prediction(adj,k,S,E,alpha)
                H=extend(adj,S)
                exact=eligible(H,k)
                assert exact==A|B and not A&B,(n,k,S)
                tests['extensions_verified']+=1
                tests[f'extensions_k{k}']+=1
                tests['type_no_new']+=len(A)
                tests['type_with_new']+=len(B)
                # Necessary/sufficient at the actual maximum-set boundary.
                if alpha[-1]==k-1:
                    maxsets=max_independent_sets(adj,alpha)
                    for R in E:
                        assert all(R&I for I in maxsets)
                    assert bool(E)==any(
                        independent(adj,R) and all(R&I for I in maxsets)
                        for R in range(1<<n))
    print('atlas exact regression:',dict(tests))


if __name__=='__main__':
    p3=nx.path_graph(3)
    assert example('P3 -> P4',p3,3,1<<0)>0
    assert example('P3 -> C4',p3,3,(1<<0)|(1<<2))==0
    p4=nx.path_graph(4)
    assert example('P4 -> C5',p4,3,(1<<0)|(1<<3))==0
    atlas_regression()
    multivertex_regression()
