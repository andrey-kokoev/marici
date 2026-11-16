#!/usr/bin/env python3
"""Exact small-model checks of the Ramsey transversal-matroid circuit theorem.

No external packages. The complete graph extension conditions, the Hall
capacity model (including submaximum maximal independent sets), and the
circuit-cover criterion are independently evaluated from integer bitsets.
"""
from itertools import combinations, product


def independent(mask, edges):
    return all(not (mask & (1 << u) and mask & (1 << v)) for u, v in edges)


def all_independent(n, edges):
    return [s for s in range(1 << n) if independent(s, edges)]


def alpha(n, edges, universe=None):
    if universe is None:
        universe=(1 << n)-1
    return max((s & universe).bit_count() for s in all_independent(n,edges))


def max_ind_sets(n, edges):
    indeps=all_independent(n,edges)
    return [s for s in indeps if not any(s != t and s & t == s for t in indeps)]


def triangle_free(n, edges):
    E = {tuple(sorted(e)) for e in edges}
    return not any((a,b) in E and (a,c) in E and (b,c) in E
                   for a,b,c in combinations(range(n),3))


def valid_assembly_direct(n,k,edges,neighborhoods,new_edges):
    m=len(neighborhoods)
    E=list(edges)
    E += [(i,n+j) for j,S in enumerate(neighborhoods) for i in range(n) if S & (1 << i)]
    E += [(n+i,n+j) for i,j in new_edges]
    return triangle_free(n+m, E) and alpha(n+m,E) <= k-1


def matroid_independent(subset, n, k, I, neighborhoods):
    """Hall test of the transversal matroid with k-1-|I| universal dummy ports."""
    d = k-1-I.bit_count()
    assert d>=0
    for T in range(1, 1<<len(neighborhoods)):
        if T & subset != T:
            continue
        covered=0
        for i,S in enumerate(neighborhoods):
            if T & (1 << i):
                covered |= S & I
        if T.bit_count() > covered.bit_count() + d:
            return False
    return True


def matching_rank(I, neighborhoods, subset):
    """Maximum bipartite matching from selected new vertices to real I-sites."""
    matched={}  # old site -> new index
    def augment(i, seen):
        available = I & neighborhoods[i]
        for x in range(I.bit_length()):
            if not (available & (1<<x)) or x in seen:
                continue
            seen.add(x)
            if x not in matched or augment(matched[x], seen):
                matched[x]=i
                return True
        return False
    for i in range(len(neighborhoods)):
        if subset & (1<<i):
            augment(i,set())
    return len(matched)


def elongated_matroid_independent(subset,n,k,I,neighborhoods):
    b=k-1-I.bit_count()
    return subset.bit_count()-matching_rank(I, neighborhoods, subset) <= b


def circuits(n, k, I, neighborhoods):
    m=len(neighborhoods)
    return [T for T in range(1,1<<m) if not matroid_independent(T,n,k,I,neighborhoods)
            and all(matroid_independent(T & ~(1<<i),n,k,I,neighborhoods)
                    for i in range(m) if T & (1<<i))]


def valid_via_circuits(n,k,edges,neighborhoods,new_edges):
    m=len(neighborhoods)
    H=list(new_edges)
    if alpha(n,edges)>k-1 or not all(independent(S,edges) for S in neighborhoods):
        return False
    if any(neighborhoods[i] & neighborhoods[j] for i,j in H):
        return False
    if not triangle_free(m, H):
        return False
    for I in max_ind_sets(n,edges):
        for C in circuits(n,k,I,neighborhoods):
            if independent(C,H):
                return False
    return True


def valid_via_inequalities(n,k,edges,neighborhoods,new_edges):
    m=len(neighborhoods)
    if alpha(n,edges)>k-1 or not all(independent(S,edges) for S in neighborhoods):
        return False
    if any(neighborhoods[i] & neighborhoods[j] for i,j in new_edges):
        return False
    if not triangle_free(m, new_edges):
        return False
    for J in all_independent(m,new_edges):
        U=0
        for i,S in enumerate(neighborhoods):
            if J&(1<<i): U|=S
        if J.bit_count()+alpha(n,edges,((1<<n)-1)&~U)>k-1:
            return False
    return True


def maximal_update(n,edges,S):
    """Predicted maximal independent sets after attaching a vertex at S."""
    old=[I for I in max_ind_sets(n,edges) if I & S]
    free=n
    surviving=(1<<n)-1-S
    E0=[(a,b) for a,b in edges if not (S&(1<<a) or S&(1<<b))]
    sub_ind=[I for I in range(1<<n) if I & ~surviving==0 and independent(I,E0)]
    new=[(1<<free)|I for I in sub_ind if not any(I != T and (I&T)==I for T in sub_ind)]
    return set(old+new)


def graph_extensions(n,edges,S):
    return list(edges)+[(i,n) for i in range(n) if S&(1<<i)]


def test_exhaustive():
    cases=0
    triangle_free_bases=0
    update_checks=0
    # Exhaust all labeled triangle-free base graphs through n=3,
    # every k from alpha+1 through 5, all repeated primitive neighborhoods,
    # and all triangle-free red graphs H on up to 3 new vertices.
    for n in range(1,4):
        pairs=list(combinations(range(n),2))
        for edge_mask in range(1<<len(pairs)):
            edges=[e for j,e in enumerate(pairs) if edge_mask&(1<<j)]
            if not triangle_free(n, edges):
                continue
            triangle_free_bases +=1
            base_alpha=alpha(n,edges)
            for S in all_independent(n,edges):
                result=maximal_update(n,edges,S)
                truth=set(max_ind_sets(n+1,graph_extensions(n,edges,S)))
                assert result==truth, (n,edges,S,result,truth)
                update_checks+=1
            choices=all_independent(n,edges)
            for k in range(base_alpha+1,6):
                for m in range(1,4):
                    new_pairs=list(combinations(range(m),2))
                    for Svec in product(choices, repeat=m):
                        for hm in range(1<<len(new_pairs)):
                            new_edges=[e for j,e in enumerate(new_pairs) if hm&(1<<j)]
                            a=valid_assembly_direct(n,k,edges,Svec,new_edges)
                            b=valid_via_inequalities(n,k,edges,Svec,new_edges)
                            c=valid_via_circuits(n,k,edges,Svec,new_edges)
                            assert a==b==c, (n,k,edges,Svec,new_edges,a,b,c)
                            cases += 1
    return cases, triangle_free_bases, update_checks


def test_examples():
    # Model A: purely repeated coverage capacity on edgeless base.
    G=[]; n=3;k=4
    E=[0b011]*3  # three neighborhoods sharing just two of the three old sites
    direct=[valid_assembly_direct(n,k,G,E[:j],[]) for j in range(0,4)]
    assert direct==[True,True,True,False]
    I=max_ind_sets(n,G)[0]
    assert I==0b111
    cs=circuits(n,k,I,E)
    assert cs==[0b111]
    
    # Model B: a submaximum maximal independent set drives a 3-way obstruction
    # despite perfect matching on the unique maximum independent set.
    G=[(0,1),(0,2),(0,3)]
    n=4;k=4;E=[0b0010,0b0100,0b1000]
    direct=[valid_assembly_direct(n,k,G,E[:j],[]) for j in range(0,4)]
    assert direct==[True,True,True,False]
    maximals=set(max_ind_sets(n,G))
    assert maximals=={0b0001,0b1110}
    assert circuits(n,k,0b1110,E)==[]
    assert circuits(n,k,0b0001,E)==[0b111]

    # A latent independent-set mode has size 1,2,3,4 after 0,1,2,3 additions.
    latent=[]
    for j in range(4):
        edges=list(G)+[(i,n+p) for p,S in enumerate(E[:j]) for i in range(n) if S&(1<<i)]
        chosen=(1<<0) | sum(1<<(n+p) for p in range(j))
        assert chosen in max_ind_sets(n+j,edges)
        latent.append(chosen.bit_count())
    assert latent==[1,2,3,4]
    
    # Arbitrarily high minimal arity: every t<=k is constructible.
    for k in range(3,10):
        n=k-1
        for t in range(2,k+1):
            S=(1<<(t-1))-1
            assert [valid_assembly_direct(n,k,[],[S]*j,[]) for j in range(t+1)] == ([True]*t+[False]),(k,t)
            assert circuits(n,k,(1<<n)-1,[S]*t)==[(1<<t)-1]
    # Matching nullity equals the formal universal-dummy elongation law.
    matched_checks=0
    for n in range(1,5):
        for I in range(1<<n):
            for k in range(I.bit_count()+1, n+3):
                for Svec in product(range(1<<n),repeat=2):
                    for J in range(1<<len(Svec)):
                        a=matroid_independent(J,n,k,I,Svec)
                        b=elongated_matroid_independent(J,n,k,I,Svec)
                        assert a==b,(n,I,k,Svec,J,a,b)
                        matched_checks+=1
    print('Matching-nullity/elongation checks:',matched_checks)
    # One additional unit of Ramsey allowance repairs each size-b+1 circuit.
    assert not elongated_matroid_independent(0b111,3,4,0b111,[3,3,3])
    assert elongated_matroid_independent(0b111,3,5,0b111,[3,3,3])
    assert valid_assembly_direct(4,4,[(0,1),(0,2),(0,3)],[2,4,8],[(0,1)])
    assert not valid_assembly_direct(3,4,[],[3,3,3],[(0,1)])
    return latent


if __name__ == '__main__':
    r=test_exhaustive()
    print('Exhaustive equivalence cases:',r[0])
    print('Triangle-free labeled bases:',r[1])
    print('Maximal-independent-set update tests:',r[2])
    print('Latent mode sizes:',test_examples())
    print('PASS')
