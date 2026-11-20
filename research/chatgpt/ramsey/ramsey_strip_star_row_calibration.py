"""Distinguish the two affine charts using a single literal row block (no cage poles). Check the scope: this is role-sensitive, not a condition valid at every edge."""
from ramsey_strip_affine_star_dictionary import cycle,fixed,X
rows=['BRNN','BNRN'];br=lambda w:X.index(tuple(i+1 for i,c in enumerate(w) if c in 'BR'));nn=lambda w:X.index(tuple(i+1 for i,c in enumerate(w) if c=='N'))
assert cycle==[br(rows[0]),nn(rows[0]),br(rows[1]),nn(rows[1])]
for m in (2,3):
    chart={pow(m,i,5):edge for i,edge in enumerate(cycle)};coord={e:k for k,e in chart.items()}
    # The two finite entries of a block centered at x sum to 2*x; hence partner(0)=2*x.
    out=[]
    for w in rows:
        B,N=br(w),nn(w);out.append((chart[2*coord[B]%5]==N,chart[2*coord[N]%5]==B))
    assert out==([(True,False)]*2 if m==2 else [(False,True)]*2);print(m,'(same row at BR center, same row at NN center)',out)
