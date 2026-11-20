"""Current-state crossing bits on (R position a, B aim j, destination b), equivariant under relabeling. Tests proper tetrahedral frame rotation separately from mere reversibility of the observed mark."""
from itertools import permutations,product
V=range(4);G=list(permutations(V));T={(a,j,b) for a in V for j in V for b in V if j!=a!=b};orbits={frozenset((g[a],g[j],g[b]) for g in G) for a,j,b in T};assert sorted(map(len,orbits))==[12,24]
verts=[(1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1)]
def volume(v):
    a,b,c=[[p[i]-v[0][i] for i in range(3)] for p in v[1:]];return sum(a[i]*(b[(i+1)%3]*c[(i+2)%3]-b[(i+2)%3]*c[(i+1)%3]) for i in range(3))
seen=set()
for on,off in product([0,1],repeat=2):
    images=[];proper=True
    for a,j,b in sorted(T):
        c,d=set(V)-{a,b};g=list(V);g[a],g[b]=b,a
        if (on if j==b else off):g[c],g[d]=d,c
        images.append(g[j]);proper &= volume([verts[i] for i in g])==volume(verts)
        back=list(V);back[b],back[a]=a,b
        if (on if g[j]==a else off):back[c],back[d]=d,c
        assert back[g[j]]==j
    seen.add(tuple(images));assert proper==(on==off==1)
assert len(seen)==2
print('2 input orbits; 4 bit policies; 2 distinct mark updates; unique everywhere-proper slot policy: always swap the complementary slots.')
