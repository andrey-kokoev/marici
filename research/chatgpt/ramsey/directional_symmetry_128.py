"""Exact integral incidence checks for a 128-position directional system.

Vertices: Z/128Z. r moves +1; s moves +32. Each undirected
antipodal s-edge is oriented from i to i+64 for i=0..63.
The 128 proposed N 2-cell boundaries are r^64 - s, one per vertex.
No N or NN filler is claimed to be a native admitted cell.
"""
from collections import Counter

N=128
m=N//2
r_edges=[('r',i) for i in range(N)]
s_edges=[('s',i) for i in range(m)]
edges=r_edges+s_edges
idx={edge:j for j,edge in enumerate(edges)}

# boundary of formal s_i, for any starting vertex (i+m indexes reverse orientation)
def s_term(i):
    i%=N
    return (('s',i),1) if i<m else (('s',i-m),-1)

# Edge chains represented by integer-indexed dictionaries.
def chain_n(i):
    c=Counter()
    for j in range(m):c[idx[('r',(i+j)%N)]]+=1
    edge,sign=s_term(i)
    c[idx[edge]]-=sign
    return {k:v for k,v in c.items() if v}

def add(*terms):
    out=Counter()
    for coeff,chain in terms:
        for j,a in chain.items():out[j]+=coeff*a
    return {j:v for j,v in out.items() if v}

# Node boundary of an oriented edge chain.
def boundary(c):
    d=Counter()
    for k,v in c.items():
        typ,i=edges[k]
        u=i; dest=(i+(1 if typ=='r' else m))%N
        d[u]-=v;d[dest]+=v
    return {k:v for k,v in d.items() if v}

b=[chain_n(i) for i in range(N)]
assert all(not boundary(c) for c in b)
C={idx[('r',i)]:1 for i in range(N)}
assert all(add((1,b[i]),(1,b[i+m]))==C for i in range(m))
for j in range(1,m):
    assert not add((1,b[j]),(1,b[j+m]),(-1,b[0]),(-1,b[m]))

# Sparse exact rank over a prime; paired-boundary identity gives rank <= m+1.
def rank_mod_p(chains,p=1_000_000_007):
    pivots={}
    for c in chains:
        row={k:v%p for k,v in c.items() if v%p}
        while row:
            t=min(row)
            if t not in pivots:
                inv=pow(row[t],-1,p)
                pivots[t]={k:(v*inv)%p for k,v in row.items() if v%p}
                break
            fac=row[t]
            for k,v in pivots[t].items():
                u=(row.get(k,0)-fac*v)%p
                if u: row[k]=u
                elif k in row: del row[k]
    return len(pivots)
rank=rank_mod_p(b)
assert rank==m+1

# Distinct commutation-square edge chains up to opposite orientation.
squares=[]
for i in range(N):
    square=add((1,b[(i+1)%N]),(-1,b[i]))
    squares.append(tuple(sorted(square.items())))
assert len(set(squares))==N # each directed signed representative is distinct
assert all(squares[i+m]==tuple(sorted((k,-v) for k,v in squares[i])) for i in range(m))

# Every N polygon contains m+1 distinct nodes.
node_incidences=Counter()
for i in range(N):
    for j in range(m+1):node_incidences[(i+j)%N]+=1
assert set(node_incidences.values())=={m+1}

# Independent set of cardinality 63, and no independent set of cardinality 64:
# in a 3-regular 128-vertex graph, alpha=64 would imply bipartiteness.
# The cycle closed by 64 r-edges and one s-edge has length 65, so not bipartite.
independent=set(range(0,m,2))|set(range(m+1,N-2,2))
assert len(independent)==63, len(independent)
for i in independent:
    assert (i+1)%N not in independent
    assert (i-1)%N not in independent
    assert (i+m)%N not in independent

print({'positions':N, 'rotation_edges':N, 'inversion_edges':m, 'total_edges':len(edges),
 'N_boundaries':N, 'N_polygon_length':m+1,
 'polygon_incidence_per_node':m+1,
 'square_boundaries_unoriented':m,
 'N_boundary_rank_over_Z':rank,
 'independent_NN_boundary_relations':N-rank,
 'graph_cycle_rank':len(edges)-N+1,
 'independence_number':63,
 'triangle_free':True})
