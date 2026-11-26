"""Test the downward closure of the outside supports, not an arbitrary gluing."""
from itertools import combinations
from collections import Counter
from pathlib import Path
import gzip

catalogue = Path(__file__).resolve().parents[2] / 'chatgpt/ramsey/pauli-realization-catalogues/r38_27.g6.gz'
with gzip.open(catalogue, 'rt') as f:
    word = f.readline().strip()
assert ord(word[0])-63 == 27
bits = ''.join(f'{ord(c)-63:06b}' for c in word[1:])
N = {v:set() for v in range(1,28)}
for b,(i,j) in zip(bits, ((i,j) for j in N for i in range(1,j))):
    if b=='1': N[i].add(j); N[j].add(i)

def audit(root):
    points=N[root]
    supports={frozenset(points & N[v]) for v in N if v!=root and v not in points}
    facets={s for s in supports if s and not any(s<t for t in supports)}
    faces={f for s in facets for k in range(1,len(s)+1) for f in combinations(sorted(s),k)}
    sizes=Counter(map(len,faces))
    # Even if each four-set is filled as a tetrahedron, what is its exposed boundary?
    tetra=[s for s in facets if len(s)==4]
    multiplicity=Counter(t for s in tetra for t in combinations(sorted(s),3))
    boundary=[t for t,m in multiplicity.items() if m==1]
    assert all(m<=2 for m in multiplicity.values())
    edge_hits=Counter(e for t in boundary for e in combinations(t,2))
    # Connected components of the link graph at each boundary vertex.
    links={}
    for v in sorted(set().union(*map(set,boundary)) if boundary else set()):
        edges=[set(t)-{v} for t in boundary if v in t]; seen={next(iter(edges[0]))}
        while True:
            new=seen.union(*(e for e in edges if e & seen))
            if new==seen: break
            seen=new
        if seen!=set.union(*edges): links[v]='disconnected'
    return dict(facets=[sorted(s) for s in sorted(facets,key=lambda s:(len(s),sorted(s)))],f_vector=[sizes[k] for k in range(1,max(sizes)+1)],boundary_edge_degrees=dict(sorted(Counter(edge_hits.values()).items())),bad_vertex_links=links)

if __name__=='__main__':
    print('root 1:',audit(1))
    print('degree-seven roots:',sum(len(n)==7 for n in N.values()))
    for v,n in N.items():
        if len(n)==7:
            a=audit(v);print(v,a['f_vector'],a['boundary_edge_degrees'],a['bad_vertex_links'])
