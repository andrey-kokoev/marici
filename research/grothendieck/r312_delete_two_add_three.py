"""Search all two-vertex deletions up to dihedral symmetry."""
from test_r312_extension import full, maximal
from itertools import combinations_with_replacement

def run(d):
    sets=list(maximal(0,full ^ 1 ^ (1<<d),0))
    large=[s for s in sets if s.bit_count()==11]
    assert max(map(int.bit_count,sets))==11
    legal=set()
    def down(t):
        if t in legal or not all(t&s for s in large): return
        legal.add(t)
        bits=t
        while bits:
            b=bits&-bits; bits ^= b; down(t^b)
    for m in sets: down(m)
    L=sorted(legal); links=[{} for t in L]
    ten=[s for s in sets if s.bit_count()>=10]
    for i,j in combinations_with_replacement(range(len(L)),2):
        a,b=L[i],L[j]; opts=[]
        if not a&b: opts.append(1)
        if all((s&~(a|b)).bit_count()<10 for s in ten): opts.append(0)
        if opts: links[i][j]=opts
    triangles=0
    for i,neighbors in enumerate(links):
        for j in neighbors:
            for k in neighbors.keys() & links[j].keys():
                triangles+=1
                for x in neighbors[j]:
                    for y in neighbors[k]:
                        for z in links[j][k]:
                            if x+y+z==3: continue
                            if x+y+z==0 and any((s&~(L[i]|L[j]|L[k])).bit_count()>=9 for s in sets): continue
                            raise RuntimeError(('witness',d,L[i],L[j],L[k],x,y,z))
    print(d,len(L),sum(map(len,links)),triangles,flush=True)

if __name__=='__main__':
    for d in range(1,25): run(d)
