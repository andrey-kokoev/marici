"""Independent final replay from incidence labels and the selected core's red edges. Compare to archived witness only AFTER verifying the construction. No optimization or nonedges inferred from endpoint. Graph6 encode and round-trip for reuse."""
import json,itertools,collections,igraph as ig
from ramsey_retention_slice import D,decode,check
P=D.parent;R=json.loads((P/'ramsey_incidence_joint_beam.json').read_text());z=next(z for z in R['nodes'] if z['score']==56);m=z['m'];a=[0]*35;rows=[sum(1<<i for i,s in enumerate(m) if s>>j&1) for j in range(8)]
for u,v in z['edges']:a[u]|=1<<v;a[v]|=1<<u
for j,s in enumerate(rows,26):
 a[j]=s|1<<34;a[34]|=1<<j
 for i in range(26):a[i]|=(s>>i&1)<<j
assert check(a,(1<<35)-1,3,9) and all(v.bit_count()==8 for v in a);edges=lambda a:[(i,j) for i,v in enumerate(a) for j in range(i) if v>>j&1];G=ig.Graph(35,edges(a));alpha=G.independence_number();omega=G.clique_number();assert(alpha,omega)==(8,2)
bits=''.join(str(v>>j&1) for i,v in enumerate(a) for j in range(i));bits+='0'*(-len(bits)%6);g6=chr(35+63)+''.join(chr(63+int(bits[i:i+6],2)) for i in range(0,len(bits),6));assert decode(g6)==a
archive=next(r['graph6'] for r in json.loads(D.read_text()) if (r['l'],r['k'])==(3,9));iso=G.isomorphic(ig.Graph(35,edges(decode(archive))));path=[R['nodes'].index(z)]
while path[-1]:path.append(R['nodes'][path[-1]]['parent'])
xyz=[0,3,6,5,1,2,4,7];cells=[1<<i for i in range(8)]+[1<<i|1<<j for i,j in itertools.combinations(range(8),2) if (xyz[i]^xyz[j]).bit_count()==1]+[sum(1<<i for i,v in enumerate(xyz) if (v>>d&1)==b) for d in range(3) for b in range(2)];assert sorted(cells)==sorted(m)
res=dict(cube_coordinates=xyz,graph6=g6,root=34,core_order=26,rows=rows,red_core_edges=z['edges'],masks=m,alpha=alpha,omega=omega,isomorphic_to_stored=iso,path=[dict(node=i,score=R['nodes'][i]['score'],trade=R['nodes'][i].get('trade')) for i in reversed(path)]);(P/'ramsey_incidence35_endpoint.json').write_text(json.dumps(res)+'\n');print(alpha,omega,iso,[x['score'] for x in res['path']],collections.Counter(s.bit_count() for s in m));
