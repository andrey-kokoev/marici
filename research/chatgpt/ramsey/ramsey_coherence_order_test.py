"""Support-sensitive composition obstruction for Ramsey extension.

1. Audits graph-independent local necessary conditions on McKay's 191
   Ramsey(3,7;22) red graphs (requires existing local dataset/scripts).
2. Constructs triangle-free star-forest examples whose independent hitting
   requirements are jointly impossible but every proper subfamily is feasible.
3. Computes mod-2 Betti numbers of their independence complexes.

The forest examples have arbitrarily high minimal obstruction order; their
marked sets are *not* claimed to be neighborhoods of saturated vertices in a
Ramsey-critical graph.
"""
from itertools import product
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent


def graph(m):
    # 3 vertices per star: (a_i, b_i, c_i), edges a_i-b_i, a_i-c_i.
    n=3*m
    adjacency=[0]*n
    for i in range(m):
        a,b,c=3*i,3*i+1,3*i+2
        for v in (b,c):
            adjacency[a]|=1<<v
            adjacency[v]|=1<<a
    # Q0 is all centers, Q_i (i >=1) is its star's leaf pair.
    Q=[sum(1<<(3*i) for i in range(m))]
    Q += [(1<<(3*i+1))|(1<<(3*i+2)) for i in range(m)]
    return adjacency,Q


def independent(mask,adj):
    while mask:
        b=mask&-mask;mask^=b
        v=b.bit_length()-1
        if mask & adj[v]:
            return False
    return True


def independent_hits(adj,Q):
    # Existence of a single independent set meeting each marked set.
    # Since vertices outside union(Q) are irrelevant, it suffices to enumerate it.
    union=0
    for q in Q:union|=q
    if any(q==0 for q in Q):return False
    for s in range(1<<len(adj)):
        if s&~union: continue
        if all(s&q for q in Q) and independent(s,adj):
            return True
    return False


def simplices_by_size(adj):
    faces_by_size={0:[0]}
    for s in range(1,1<<len(adj)):
        if independent(s,adj):
            faces_by_size.setdefault(s.bit_count(),[]).append(s)
    return faces_by_size


def rank_mod2(vectors):
    pivots={}
    for v in vectors:
        while v:
            k=v.bit_length()-1
            if k not in pivots:
                pivots[k]=v;break
            v ^= pivots[k]
    return len(pivots)


def betti_reduced(adj):
    faces=simplices_by_size(adj)
    largest=max(faces)
    bdry_rank={0:1} # reduced boundary C_0 -> C_{-1} has rank one
    for k in range(2,largest+1):
        rows={s:i for i,s in enumerate(faces.get(k-1,[]))}
        vectors=[]
        for s in faces.get(k,[]):
            b=s;vec=0
            while b:
                v=b&-b;b^=v
                vec ^= 1 << rows[s^v]
            vectors.append(vec)
        bdry_rank[k-1]=rank_mod2(vectors)
    result={}
    for k in range(1,largest+1):
        result[k-1]=len(faces.get(k,[]))-bdry_rank.get(k-1,0)-bdry_rank.get(k,0)
    return {i:beta for i,beta in result.items() if beta}


def main():
    for m in (2,3,4):
        A,Q=graph(m)
        assert not independent_hits(A,Q)
        for drop in range(len(Q)):
            assert independent_hits(A,Q[:drop]+Q[drop+1:])
        # For a nonempty *proper* subfamily, extending the independent hit
        # set to the removed requirements is impossible only at full family.
        # Cross-polytope cycle: choose one of (a_i,b_i) for each star.
        # The mod-2 boundary vanishes because each codimension-one face
        # admits two completions, which cancel.
        Z=[sum(1 << (3*i + choice) for i,choice in enumerate(bits))
           for bits in product((0,1),repeat=m)]
        boundary=Counter()
        for f in Z:
            for i in range(3*m):
                if f>>i&1:boundary[f^(1<<i)]+=1
        assert all(n%2==0 for n in boundary.values())
        assert all(independent(f,A) for f in Z)
        # The all-center face is maximal: its evaluation cochain is closed.
        sigma=sum(1<<(3*i) for i in range(m))
        assert sigma in Z
        assert not any(independent(sigma|(1<<v),A)
                       for v in range(3*m) if not sigma>>v&1)
        # Pairing evaluation cochain with cycle is one. By Stokes, Z cannot
        # be a boundary: <d(omega), W>=<omega, d(W)> would give 0=1.
        assert sum(f==sigma for f in Z)%2 == 1
        betti=betti_reduced(A)
        assert betti=={m-1:1},(m,betti)
        print('stars',m,'marked sets',m+1,'all-hit',False,'every deletion feasible',True,
              'reduced F2 Betti',betti)

    # This audit is optional and is distinct from the *unbounded* examples.
    if (HERE/'r37_22_mckay.g6').exists():
        from ramsey_r37_local_certificates import G6_PATH,decode_graph6,faces,certificate,verify_certificate
        counts=Counter()
        for row in G6_PATH.read_text().splitlines():
            A=decode_graph6(row)
            K=faces(A)
            cert=certificate(A,K)
            assert verify_certificate(A,K,cert)
            counts[cert[0]]+=1
        assert counts==Counter({'capacity':162,'zero-neighbor':11,
                               'blocked-neighbor':15,'bipartite-square':3})
        print('191 critical (3,7) graph certificate counts:',dict(counts))

    # McKay's unique (3,9;35) graph is 8-regular, hence D is empty.
    g6=('bsaCCA?O?O_aC??`c@O@b?RcHQ?DcA@H?PC_@QO@@Q?DA@MP?RgKADoH?aR?'
        'KCbOC_JE?xO@AALC@AJPG?__V?_K@ROO_A@dOG@?_')
    n=ord(g6[0])-63
    bits=''.join(f'{ord(c)-63:06b}' for c in g6[1:]); A=[0]*n
    for bit,(i,j) in zip(bits,((i,j) for j in range(1,n) for i in range(j))):
        if bit=='1':
            A[i] |=1<<j; A[j] |=1<<i
    assert n==35 and set(a.bit_count() for a in A)=={8}
    print('35-node (3,9) red degree histogram:',dict(Counter(a.bit_count() for a in A)),
          'extension impossible by capacity alone')

if __name__=='__main__':main()
