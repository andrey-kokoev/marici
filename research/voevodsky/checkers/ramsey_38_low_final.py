"""Complete minimum-degree-two census at 48 and 49 edges; replay 47 as a control. Arguments: compiled six and joint screen executables. For a (3,7) graph, a degree-2 root leaves a (3,6) 17-core. A shared missed blue five is precisely the obstruction across both mutually blue neighbors."""
import sys,json,itertools,subprocess,igraph as ig
from ramsey_retention_slice import CAT,D,decode,check
P=D.parent;E=[(u,v) for v in range(20) for u in range(v)]
def adj(es):
 a=[0]*20
 for u,v in es:a[u]|=1<<v;a[v]|=1<<u
 return a
def solve(cmd,rows):return subprocess.check_output([cmd],input='\n'.join(' '.join(map(str,a)) for a in rows)+'\n',text=True).splitlines() if rows else []
for target in (47,48,49):
 cores={}
 for s in (CAT/'r36_17.g6').read_text().splitlines():
  a=decode(s);es=[(u,v) for u,v in E if v<17 and a[u]>>v&1];need=target-2-len(es);I=[0]
  for i,v in enumerate(a):I.extend([q|1<<i for q in I if q&v==0])
  F=[q for q in I if q.bit_count()==5];S=[q for q in I if 0<q.bit_count()<need];M=[sum(1<<j for j,q in enumerate(F) if not q&t) for t in S]
  for i,t in enumerate(S):
   for j in range(i,len(S)):
    u=S[j]
    if u.bit_count()+t.bit_count()!=need or M[i]&M[j]:continue
    ed=es+[(17,19),(18,19)]+[(v,z) for z,b in enumerate((t,u),17) for v in range(17) if b>>v&1];g=ig.Graph(20,ed);ce=g.permute_vertices(g.canonical_permutation()).get_edgelist();m=sum(1<<(max(v,w)*(max(v,w)-1)//2+min(v,w)) for v,w in ce);cores[m]=adj(ce)
 keys=list(cores);rows=list(cores.values());assert all(min(v.bit_count() for v in a)==2 and check(a,2**20-1,3,7) for a in rows)
 if target==47:assert set(keys)=={int(r['core'],16) for r in json.loads((P/'ramsey_38_layer47.json').read_text())['low']}
 v=list(map(int,solve(sys.argv[1],rows)));assert len(v)==len(rows);idx=[i for i,b in enumerate(v) if b];vs=[list(map(int,l.split())) for l in solve(sys.argv[2],[rows[i] for i in idx])];assert len(vs)==len(idx) and all(c[5]>0 for c in vs);out=dict(target=target,types=sorted(map(hex,keys)),survivors=[dict(core=hex(keys[i]),counts=c) for i,c in zip(idx,vs)]);print(target,len(keys),[sum(c[j]>0 for c in vs) for j in range(5,-1,-1)],flush=True);(P/f'ramsey_38_low_final_{target}.json').write_text(json.dumps(out)+'\n')
