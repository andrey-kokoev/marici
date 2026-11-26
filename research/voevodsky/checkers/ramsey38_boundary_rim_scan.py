"""Necessary disk-rim test, not a ball-existence decision. Root 1, graph record 1."""
from itertools import combinations, permutations
from ramsey38_support_ball_completion import N,P,rows

supports={v:frozenset(N[1]&N[v]) for v in N if v!=1 and v not in N[1]}

def scan(center):
    # Every original support is required to remain a face, not only the tetrahedra.
    links={tuple(e) for r in rows if center in r for e in combinations(sorted(r-{center}),2)}
    demands={v:r-{center} for v,r in supports.items() if center in r and 2<=len(r)<=3}
    # A request forces either a vertex or an edge onto the link disk's rim.
    # Enumerate possible rim subsets on current labels; allow 1,2 marked vertices
    # as well (unmarked subdivision vertices on the rim need not be named).
    feasible={frozenset()}
    others=sorted(set(P)-{center})
    for k in range(1,len(others)+1):
        for S in combinations(others,k):
            for tail in permutations(S[1:]):
                cycle=S[:1]+tail
                if k>2 and cycle[1]>cycle[-1]:continue
                pairs={frozenset((cycle[i-1],b)) for i,b in enumerate(cycle)}
                chords=[tuple(sorted((cycle.index(a),cycle.index(b)))) for a,b in links if a in S and b in S]
                if any(a<c<b<d or c<a<d<b for (a,b),(c,d) in combinations(chords,2)):continue
                ok=[v for v,r in demands.items() if r<=set(S) and (len(r)==1 or r in pairs)]
                feasible.update(frozenset(q) for n in range(1,len(ok)+1) for q in combinations(ok,n))
    bad=[]
    for n in range(1,len(demands)+1):
        for q in combinations(sorted(demands),n):
            s=frozenset(q)
            if s not in feasible and not any(t<=s for t in bad):bad.append(s)
    return sorted(demands),[sorted(s) for s in bad]

if __name__=='__main__':
    obstructions={p:scan(p)[1] for p in P};print(obstructions)
    assert obstructions=={p:([[6,10,17]] if p==15 else []) for p in P}
    # These hidden sets have actual ball certificates in the visibility and
    # joint-budget checkers respectively (not just passing local orders).
    short={v for v,r in supports.items() if len(r)<4};counts={}
    for n in range(len(short)+1):
        for q in combinations(short,n):
            s=set(q);cost=5 if 6 not in s or 17 not in s else (6 if 10 not in s else None)
            assert (cost is None)==({6,10,17}<=s)
            counts[cost]=counts.get(cost,0)+1
    print('minimum added tetrahedra -> number of boundary requests:',counts)
