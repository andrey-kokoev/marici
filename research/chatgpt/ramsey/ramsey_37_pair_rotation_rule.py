"""Direct cyclic choice in the six-point pair-incidence construction. No offset search."""
from itertools import combinations
from pathlib import Path
from pauli_realization_audit import independent_witness, triangle_free


def build(k=7):
    # Six ground points: five cyclic points and the fixed point infinity.
    if k != 7:
        raise ValueError('The three pairing types below require k-1 = 6.')
    size=k-2; inf=size
    pairs=list(combinations(range(k-1),2));labels=[()]+[(v,) for v in range(k-1)]+pairs
    edges=set()
    def join(a,b):edges.add(tuple(sorted((labels.index(a),labels.index(b)))))
    for v in range(k-1):join((),(v,))
    for p in pairs:
        for v in p:join((v,),p)
    for p,q in combinations(pairs,2):
        if set(p).isdisjoint(q):join(p,q)
    # In each partition into three pairs distinguish one pair. Delete the
    # edge between the other two. Translate these three rows modulo five.
    types=[((1,2),(inf,0),(3,4)),((1,3),(inf,0),(2,4)),((inf,0),(1,4),(2,3))]
    marked=set(); partitions=set()
    for j in range(size):
        for pattern in types:
            p,q,r=(tuple(sorted(inf if v==inf else (v+j)%size for v in t)) for t in pattern)
            marked.add(p);partitions.add(tuple(sorted((p,q,r))))
            edges.remove(tuple(sorted((labels.index(q),labels.index(r)))))
    assert marked==set(pairs) and len(partitions)==15
    rows=[0]*len(labels)
    for i,j in edges:rows[i]|=1<<j;rows[j]|=1<<i
    return rows

if __name__=='__main__':
    a=build();assert triangle_free(a) and independent_witness(a,7) is None
    assert all(x.bit_count()==6 for x in a)
    print(len(a),'vertices;',sum(r.bit_count() for r in a)//2,'red edges; alpha = 6 (six singleton labels).')
    Path(__file__).with_name('ramsey_3_7_pair_rotation_22.csv').write_text(''.join(','.join(str(r>>j&1) for j in range(len(a)))+'\n' for r in a))
