"""Compile exact forbidden partial assignments for the nine single-flippable pairs of record 1499."""
from itertools import combinations
from collections import Counter
from ramsey_38_cube_inversion import sign
V=range(27);pairs=list(combinations(V,2));N=[sum(1<<j for j in V if sign(i,j)) for i in V];sets=[0]
for i in V:sets += [s|1<<i for s in sets if not s&N[i]]
six=[s for s in sets if s.bit_count()==6];F=[(i,j) for i,j in pairs if not(N[i]&N[j]) and not any(not s&(N[i]|N[j]|1<<i|1<<j) for s in six)]
assert len(F)==9
clauses=set()
for red,k in [(True,3),(False,8)]:
    # Enumerate vertex sets whose already-fixed edges all have the target color.
    ok=[sum(1<<j for j in V if i!=j and (sign(i,j)==red or tuple(sorted((i,j))) in F)) for i in V]
    def walk(m,s,left):
        if left==0:
            mask=sum(1<<a for a,(i,j) in enumerate(F) if s>>i&s>>j&1);assert mask;clauses.add((red,mask));return
        while m.bit_count()>=left:
            b=m&-m;m^=b;walk(m&ok[b.bit_length()-1],s|b,left-1)
    walk((1<<27)-1,0,k)
valid=[x for x in range(512) if all((x&m!=m if r else x&m!=0) for r,m in clauses)]
print('legal',len(valid),'distinct forbidden patterns by (red,size)',Counter((r,m.bit_count()) for r,m in clauses))
