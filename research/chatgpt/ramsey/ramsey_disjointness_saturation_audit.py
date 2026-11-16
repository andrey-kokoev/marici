#!/usr/bin/env python3
"""Exact disjointness-saturation block decomposition and exhaustive R(3,3),R(3,4) growth.

Uses graph atlas only as independent cross-check to seven vertices, never as an
input for generating the Ramsey families. Every extension is evaluated by exact
bitsets, and all generated graphs are reduced modulo ordinary isomorphism.
"""
import networkx as nx
from collections import Counter
from ramsey_two_channel_extension import adjacency, alpha_table, independent, eligible, extend
from ramsey_incidence_core_audit import G6_K4, G6_K5, G6_K6


def independent_sets(adj):
    n=len(adj); alpha=alpha_table(adj)[-1]
    maximal=[]
    for mask in range(1<<n):
        if not independent(adj,mask):continue
        if all(adj[v]&mask for v in range(n) if not mask>>v&1):
            maximal.append(mask)
    maximum=[s for s in maximal if s.bit_count()==alpha]
    return alpha,sorted(maximal),sorted(maximum)


def status(adj,k):
    alpha,maximal,maximum=independent_sets(adj)
    degrees={T:sum((T&I)==0 for I in maximum) for T in maximal}
    E=eligible(adj,k)
    if alpha<=k-1:
        assert bool(E)==(alpha<k-1 or 0 in degrees.values())
        if alpha==k-1:
            for v in range(len(adj)):
                # Cloning v is valid iff no maximum independent set contains v.
                assert (adj[v] in E) == (not any(I>>v & 1 for I in maximum))
    return dict(alpha=alpha,maximal=maximal,maximum=maximum,
                degrees=degrees,E=E,terminal=not E)


def induced_maximal(adj,alive):
    return [T for T in range(1<<len(adj)) if T&~alive==0 and independent(adj,T)
            and all(adj[v]&T for v in range(len(adj)) if (alive>>v)&1 and not (T>>v)&1)]


def check_extension(adj,k,S,st=None):
    st=st or status(adj,k)
    assert st['alpha']==k-1 and S in st['E']
    n=len(adj); bit=1<<n; alive=(bit-1)&~S
    G_S_max=induced_maximal(adj,alive)
    a_del=alpha_table(adj)[alive]
    tight=a_del==k-2
    inherited_maximal=[T for T in st['maximal'] if T&S]
    born_maximal=[bit|T for T in G_S_max]
    inherited_maximum=st['maximum']
    born_maximum=[bit|T for T in G_S_max if T.bit_count()==k-2] if tight else []
    H=extend(adj,S)
    hs=status(H,k)
    assert sorted(inherited_maximal+born_maximal)==hs['maximal']
    assert sorted(inherited_maximum+born_maximum)==hs['maximum']
    # Four blocks of rows/columns, bottom-right zero, other blocks literal disjointness.
    rowsA={T:sum((T&I)==0 for I in inherited_maximum) for T in inherited_maximal}
    rowsAplus={T:sum((T&J)==0 for J in born_maximum) for T in inherited_maximal}
    rowsB={T:sum((T&I)==0 for I in inherited_maximum) for T in born_maximal}
    assert all(hs['degrees'][T]==rowsA[T]+rowsAplus[T] for T in inherited_maximal)
    assert all(hs['degrees'][T]==rowsB[T] for T in born_maximal)
    assert all((T & J) != 0 for T in born_maximal for J in born_maximum)  # both contain v
    assert hs['terminal']==(
        all(rowsA[T]+rowsAplus[T]>0 for T in inherited_maximal) and
        all(rowsB[T]>0 for T in born_maximal))
    if not tight:
        assert not hs['terminal']
        assert S in hs['E'] # second blue twin with the same neighborhood
    return dict(H=H,st=hs,tight=tight,old_rows=len(inherited_maximal),born_rows=len(born_maximal),
                old_unsatisfied=sum(rowsA[T]+rowsAplus[T]==0 for T in inherited_maximal),
                born_unsatisfied=sum(rowsB[T]==0 for T in born_maximal),
                repaired_old_rows=sum(rowsA[T]==0 and rowsAplus[T]>0 for T in inherited_maximal),
                born_max=len(born_maximum),old_max=len(inherited_maximum))


def canonical_isomorphism_insert(graphs,H):
    for i,g in enumerate(graphs):
        if len(g)==len(H) and sum(v.bit_count() for v in g)//2==sum(v.bit_count() for v in H)//2:
            if nx.is_isomorphic(as_graph(g),as_graph(H)):return i
    graphs.append(H)
    return len(graphs)-1


def as_graph(adj):
    g=nx.Graph();g.add_nodes_from(range(len(adj)))
    g.add_edges_from((u,v) for u in range(len(adj)) for v in range(u+1,len(adj)) if adj[u]>>v&1)
    return g


def construct(k,max_n,atlas_check=True):
    family=[((),)]
    results=[]
    for n in range(max_n+1):
        states=family[-1]
        count_terminal=0; count_sat=0;count_eligible=0;pending=[]; count_tight=0
        transitions=Counter()
        for adj in states:
            st=status(adj,k)
            assert st['alpha']<=k-1
            count_terminal+=st['terminal']; count_sat+=(st['alpha']==k-1)
            count_eligible+=len(st['E'])
            for S in st['E']:
                if st['alpha']==k-1:
                    r=check_extension(adj,k,S,st)
                    H=r['H']
                    count_tight+=r['tight']
                    if r['st']['terminal']:
                        transitions['terminal_births']+=1
                        assert r['tight']
                    if r['repaired_old_rows']:transitions['repaired_rows']+=1
                    if r['born_unsatisfied']:transitions['born_unsatisfied']+=1
                    if r['old_unsatisfied']:transitions['old_unsatisfied']+=1
                else:
                    H=extend(adj,S)
                    assert status(H,k)['alpha']<=k-1
                pending.append(H)
        results.append(dict(n=n,states=len(states),saturated=count_sat,terminal=count_terminal,
                            choices=count_eligible,tight=count_tight,**transitions))
        if atlas_check and n<=7:
            atlas=[adjacency(g) for g in nx.graph_atlas_g() if len(g)==n and all(not (set(g.neighbors(u)) & set(g.neighbors(v))) for u,v in g.edges()) and alpha_table(adjacency(g))[-1]<=k-1]
            assert len(atlas)==len(states),(k,n,len(atlas),len(states))
            for a in states:assert any(nx.is_isomorphic(as_graph(a),as_graph(b)) for b in atlas)
        if n==max_n:break
        nxt=[]
        for H in pending:canonical_isomorphism_insert(nxt,H)
        family.append(tuple(nxt))
    return results,family


def cyclic_graph(n,steps):
    G=nx.Graph();G.add_nodes_from(range(n))
    G.add_edges_from((i,(i+d)%n) for i in range(n) for d in steps)
    return G


def cyclic_shift(mask,n,step):
    return sum(1<<((v+step)%n) for v in range(n) if mask>>v&1)


def cyclic_disjointness_report(n,steps,k):
    G=cyclic_graph(n,steps)
    st=status(adjacency(G),k)
    assert st['terminal'] and st['alpha']==k-1
    universe=set(st['maximum'])
    representatives=[]
    while universe:
        r=min(universe)
        orbit={cyclic_shift(r,n,j) for j in range(n)}
        assert orbit<=universe
        representatives.append(r)
        universe-=orbit
    offsets=[[tuple(j for j in range(n) if not(A&cyclic_shift(B,n,j)))
              for B in representatives] for A in representatives]
    B=[[len(a) for a in row] for row in offsets]
    # Confirm the 3x3 circulant representation reconstructs the full matrix.
    for i,A in enumerate(representatives):
        for a in range(n):
            X=cyclic_shift(A,n,a)
            for j,C in enumerate(representatives):
                for b in range(n):
                    Y=cyclic_shift(C,n,b)
                    assert (not (X & Y)) == (((b-a)%n) in offsets[i][j])
    print('cyclic group ring k',k,'n',n,'rep_count',len(representatives),
          'orbit_sizes',n,'block_sums',B)
    print('  representatives', [tuple(v for v in range(n) if r>>v&1) for r in representatives])
    print('  offset arrays', offsets)
    if len(representatives)==1:
        H=nx.Graph();H.add_nodes_from(range(n))
        H.add_edges_from((i,j) for i in range(n) for j in range(i+1,n)
                         if (j-i)%n in offsets[0][0])
        assert nx.is_isomorphic(G,H)
        print('  exact self-duality: TRUE')
    if n==13:
        assert B==[[6,4,1],[4,4,4],[1,4,6]]
        assert nx.is_isomorphic(G,nx.from_graph6_bytes(G6_K5.encode()))
    return offsets


def high_level_terminal_regression():
    for k,lines in ((4,G6_K4),(5,[G6_K5]),(6,G6_K6)):
        stats=[]
        for line in lines:
            st=status(adjacency(nx.from_graph6_bytes(line.encode())),k)
            assert st['terminal']
            cover=0
            for I in st['maximum']:cover|=I
            assert all(any((I>>v)&1 for I in st['maximum'])
                       for v in range(len(nx.from_graph6_bytes(line.encode()))))
            stats.append((len(st['maximal']),len(st['maximum']),min(st['degrees'].values())))
        print('critical terminal k',k,'(maximal rows, maximum columns, min row degree)',stats)


def main():
    for k,nmax in [(3,6),(4,9)]:
        res,fam=construct(k,nmax)
        print('k',k,'census:')
        for r in res:print('  ',r)
        assert not fam[-1]
        assert len(fam[-2])>0
        if k==4:
            assert len(fam[8])==3
            assert all(status(a,k)['terminal'] for a in fam[8])
            assert sum(len(status(a,k)['E']) for a in fam[7])==8
            assert all(S not in a for a in fam[7] for S in status(a,k)['E'])
            assert all(all(any(I>>v & 1 for I in status(a,k)['maximum']) for v in range(len(a))) for a in fam[7])
            critical=[nx.from_graph6_bytes(t.encode()) for t in G6_K4]
            assert all(any(nx.is_isomorphic(as_graph(g),h) for g in fam[8]) for h in critical)
            print('  final three critical graphs:')
            for adj in fam[8]:
                st=status(adj,k)
                print('  ',nx.to_graph6_bytes(as_graph(adj),header=False).decode().strip(),
                      'maximal rows',len(st['maximal']),'maximum cols',len(st['maximum']),
                      'D min/max row sums',min(st['degrees'].values()),max(st['degrees'].values()))

    # Single-row/single-neighborhood checks at all small levels.
    counts=Counter();samples={}
    for g in nx.graph_atlas_g():
        adj=adjacency(g)
        if any(adj[u]&adj[v] for u,v in g.edges()):continue
        for k in (3,4,5,6):
            st=status(adj,k)
            if st['alpha']!=k-1:continue
            for S in st['E']:
                r=check_extension(adj,k,S,st)
                counts['tested']+=1
                for attr in ('tight','repaired_old_rows','born_unsatisfied','old_unsatisfied'):
                    if r[attr]:
                        counts[attr]+=1
                        if attr not in samples:
                            samples[attr]=(k,nx.to_graph6_bytes(g,header=False).decode().strip(),S,r)
                if r['st']['terminal']:counts['terminal']+=1
    print('atlas block checks:',dict(counts))
    for name,(k,code,S,r) in samples.items():
        print('example',name,'k',k,'graph6',code,'S',S,
              'tight',r['tight'],'repaired rows',r['repaired_old_rows'],
              'old unsat',r['old_unsatisfied'],'born unsat',r['born_unsatisfied'])
    assert counts['tested']>3000
    for n,steps,k in [(5,[1],3),(8,[1,4],4),(13,[1,5],5)]:
        cyclic_disjointness_report(n,steps,k)
    high_level_terminal_regression()

if __name__=='__main__':main()
