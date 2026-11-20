"""Carry the actual labeled Hall matching across a row-compatible restart. Test equality of the output and next input, as distinct from being symmetry-related."""
from ramsey_strip_next_row_restart import first,swapped,r,P,T

def flag(i,j):return (min(i,j),max(i,j))
def fills(rest):
    if not rest:
        yield frozenset();return
    i=min(rest)
    for j in rest:
        if not(i<15<=j and P[i] in T[j-15]):continue
        edges={flag(i,j),flag(r[i],r[j])};vs={x for e in edges for x in e}
        if vs<=rest and len(vs)==2*len(edges):
            for f in fills(rest-vs):yield f|edges

def matches(p):
    cycle=p+swapped(p)[-2:0:-1];alt={flag(cycle[i],cycle[i+1]) for i in range(0,22,2)}
    return {frozenset(alt|f) for f in fills(set(range(30))-set(cycle))}

def turn(m):return frozenset(flag(r[i],r[j]) for i,j in m)
tracks=sorted(first);M=list(map(matches,tracks));nexts=[matches(swapped(p)) for p in tracks];assert [{turn(m) for m in S} for S in M]==nexts
for i,S in enumerate(M):
 out={turn(m) for m in S};counts=[len(out&n) for n in nexts];print(i+1,'completions',len(S),'exact handoffs',counts);assert all(v==0 for j,v in enumerate(counts) if i!=j)
