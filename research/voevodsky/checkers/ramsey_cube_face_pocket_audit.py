"""Replay the structural reduction separately from the bounded SAT search. Verify the pocket in the known witness; certify the enumeration of pairwise joint hitting options; compare all geometries for four erased labels."""
from ramsey_cube_face_pocket import P,a,rep,orbit,Q,I,goodpairs,M
import json,itertools,collections
from ramsey_retention_slice import decode
z=json.loads((P/'ramsey_incidence35_endpoint.json').read_text());g=decode(z['graph6']);xyz=z['cube_coordinates'];lab=[xyz[j] for j in range(8)];m=[sum(1<<lab[j] for j in range(8) if s>>j&1) for s in z['masks']];old=15;empty=[i for i,s in enumerate(m) if not s&~old];front=[i for i in range(26) if i not in empty];pocket=empty+[j+26 for j in range(8) if old>>lab[j]&1];assert len(empty)==9 and all(sum(g[i]>>j&1 for j in pocket)==4 for i in pocket);ps=[sum((g[i]>>j&1)<<k for k,j in enumerate(pocket)) for i in front];assert sum(s.bit_count() for s in ps)==48
h=collections.Counter((s|t).bit_count() for s,t in goodpairs);sym=[[u^sum((i>>j&1)<<k for k,j in enumerate(p)) for i in range(8)] for p in itertools.permutations(range(3)) for u in range(8)];geo={}
for c in itertools.combinations(range(8),4):
 k=min(tuple(sorted(t[i] for i in c)) for t in sym);b=sum(1<<i for i in c);size=4+sum(not s&~b for s in M);geo[str(k)]=size
res=dict(four_erasure_pocket_orders=geo,blue_fours=len(Q),orbits=[len(orbit(q)) for q in rep],pair_union_hist={s:n//2 for s,n in h.items()},outer_pocket_edges=sum(s.bit_count() for s in ps),inner17_edges=sum((g[i]>>j)&1 for i,j in itertools.combinations(front,2)));assert res['inner17_edges']==30;print(res);(P/'ramsey_cube_face_pocket_audit.json').write_text(json.dumps(res)+'\n')
