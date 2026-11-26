import sys,json,gzip,subprocess,igraph as ig
from ramsey_retention_slice import D,check
P=D.parent;cores=[int(h,16) for h in json.loads((P/'ramsey_38_degree4_children47.json').read_text())];E=[(i,j) for j in range(20) for i in range(j)];defedges=lambda h:[e for k,e in enumerate(E) if h>>k&1];
def adj(es,n):
 a=[0]*n
 for i,j in es:a[i]|=1<<j;a[j]|=1<<i
 return a
seen=set();present=0
for start in range(0,len(cores),512):
 if len(sys.argv)>2 and start//512%6!=int(sys.argv[2]):continue
 ck=P/'ramsey_38_four_parts47'/f'{start}.json.gz';ck.parent.mkdir(exist_ok=True)
 if ck.exists():
  n,hs=json.load(gzip.open(ck));present+=n;seen.update(int(h,16) for h in hs);continue
 chunk=set();batch=cores[start:start+512];bs=[defedges(m) for m in batch];lines=[' '.join(map(str,adj(es,15))) for es in bs];raw=subprocess.check_output([sys.argv[1]],input='\n'.join(lines)+'\n',text=True)
 for line in raw.splitlines():
  i,*rows=map(int,line.split());es=bs[i]+[(j,19) for j in range(15,19)]+[(u,j) for j,t in enumerate(rows,15) for u in range(15) if t>>u&1];assert len(es)==47;g=ig.Graph(20,es);key=sum(1<<(max(x,y)*(max(x,y)-1)//2+min(x,y)) for x,y in g.permute_vertices(g.canonical_permutation()).get_edgelist());chunk.add(key)
 n=len(raw.splitlines());seen.update(chunk);present+=n;tmp=ck.with_suffix('.tmp');
 with gzip.open(tmp,'wt') as f:json.dump([n,sorted(map(hex,chunk))],f)
 tmp.replace(ck)
if len(sys.argv)>2:sys.exit()
aug={int(s,16) for s in json.load(gzip.open(P/'ramsey_38_layer47_deletable.json.gz'))};assert len(seen&aug)==58630;res=seen-aug
for h in res:
 es=defedges(h);a=adj(es,20);assert check(a,2**20-1,3,7);I=[0]
 for i,v in enumerate(a):I.extend([t|1<<i for t in I if not t&v])
 Q=[t for t in I if t.bit_count()==5];assert all(any(not t&(a[u]|a[v]|1<<u|1<<v) for t in Q) for u,v in es)
print(len(cores),present,len(seen),len(res));(P/'ramsey_38_degree4_inventory47.json').write_text(json.dumps(dict(children=len(cores),presentations=present,types=len(seen),resistant=sorted(map(hex,res))))+'\n')
