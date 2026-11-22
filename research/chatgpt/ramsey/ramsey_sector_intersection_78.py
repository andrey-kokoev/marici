"""Compare two rooted signature tables with the eight actual surface positions. Integer coordinates = three times the source tetrahedron/centroid coordinates. Distinguish ray incidence from literal affine planes."""
from ramsey_address_to_cube import S,D,json,permutations,combinations
from itertools import product
from math import prod
from collections import Counter
T=json.loads((D.parents[1]/'nima/results/twelve-triangle-positive-geometry.json').read_text())['triangles_and_transports'];P={v for t in T for v in t['triangle']};V=dict(zip('ABCD',[(3,3,3),(3,-3,-3),(-3,3,-3),(-3,-3,3)]));V.update({f:tuple(sum(V[v][k] for v in f[2:])//3 for k in range(3)) for f in P if f.startswith('F_')});assert set(V)==P
X=list(V.values());bits=lambda m:[i for i in range(8) if m>>i&1];sign=lambda x:tuple(v>0 for v in x);dist=lambda x,y:sum(a!=b for a,b in zip(sign(x),sign(y)));mask=lambda ids:sum(1<<i for i in ids)
def det(a,b,c,d):
    u,v,w=([p[i]-a[i] for i in range(3)] for p in [b,c,d]);return sum(u[i]*(v[(i+1)%3]*w[(i+2)%3]-v[(i+2)%3]*w[(i+1)%3]) for i in range(3))
faces={mask(i for i,x in enumerate(X) if (x[k]>0)==s) for k in range(3) for s in (True,False)};edges={mask([i,j]) for i,j in combinations(range(8),2) if dist(X[i],X[j])==1};assert len(edges)==12 and len(faces)==6;counts=Counter()
for p in permutations(range(8)):
    f=lambda m:mask(p[i] for i in bits(m));
    if all(f(m) in edges for m in S if m.bit_count()==2) and all(f(m) in faces for m in S if m.bit_count()==4):counts['nine_bindings']+=1
    if all(dist(X[p[i]],X[p[i+1]])==3 for i in (0,2,4)):
        counts['eight_bindings']+=1;assert det(*(X[p[i]] for i in (2,3,4,5)))==0
counts['nine_coplanar_quartets']=sum(det(*(X[i] for i in bits(m)))==0 for m in faces);counts['nine_sector_sides']=sum(any({list(V)[i] for i in bits(m)}<=set(t['triangle']) for t in T) for m in edges);print(counts);(D/'ramsey_sector_intersection_78.json').write_text(json.dumps(counts)+'\n')
