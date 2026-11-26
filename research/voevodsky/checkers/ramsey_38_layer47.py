"""One-edge augmentation of the complete 46 layer; independent low-degree-root enumeration and finite pair-compatibility test. Output canonical types and compare the low-degree intersection by key, not just counts."""
import gzip,json,itertools,igraph as ig
from ramsey_retention_slice import CAT,D,decode,check
P=D.parent;E=[(i,j) for j in range(20) for i in range(j)];bits={(i,j):1<<k for k,(i,j) in enumerate(E)}
def edges(m):return [e for e in E if m&bits[e]]
def key(es):
 g=ig.Graph(20,es);return sum(bits[tuple(sorted(e))] for e in g.permute_vertices(g.canonical_permutation()).get_edgelist())
def unpack(es):
 a=[0]*20
 for i,j in es:a[i]|=1<<j;a[j]|=1<<i
 return a
def ind(a):
 I=[0]
 for i,v in enumerate(a):I.extend([s|1<<i for s in I if not s&v])
 return I
parents={int(s,16) for s in json.load(gzip.open(P/'ramsey_38_layer46_deletable.json.gz'))};parents.update(int(r['core'],16) for r in json.loads((P/'ramsey_38_layer46.json').read_text())['low']);
for name in ('degree3_inventory_0_37_46','degree4_inventory46'):
 for a in json.loads((P/f'ramsey_38_{name}.json').read_text())['resistant']:parents.add(key([e for e in E if a[e[0]]>>e[1]&1]))
assert len(parents)==10119;children=set();low_aug=set();moves=0
for m in sorted(parents):
 es=edges(m);a=unpack(es);mind=[i for i,v in enumerate(a) if v.bit_count()==2]
 for i,j in E:
  if a[i]>>j&1 or a[i]&a[j]:continue
  c=key(es+[(i,j)]);children.add(c);moves+=1
  if any(h!=i and h!=j for h in mind):low_aug.add(c)
print('moves, types',moves,len(children),flush=True)
with gzip.open(P/'ramsey_38_layer47_deletable.json.gz','wt') as f:json.dump(sorted(map(hex,children)),f)
low=set()
for s in (CAT/'r36_17.g6').read_text().splitlines():
 a=decode(s);I=ind(a);Q=[q for q in I if q.bit_count()==5];budget=45-sum(v.bit_count() for v in a)//2
 for t,u in itertools.combinations_with_replacement([q for q in I if 0<q.bit_count()<budget],2):
  if t.bit_count()+u.bit_count()!=budget or any(not q&(t|u) for q in Q):continue
  es=[(i,j) for i,j in E if j<17 and a[i]>>j&1]+[(17,19),(18,19)]+[(i,j) for j,x in enumerate((t,u),17) for i in range(17) if x>>i&1];b=unpack(es);assert len(es)==47 and check(b,2**20-1,3,7);low.add(key(es))
assert low&children==low_aug;rec=[]
for m in sorted(low):
 a=unpack(edges(m));I=ind(a);S=[s for s in I if all(s&(v|1<<i) for i,v in enumerate(a))];Q=[q for q in I if q.bit_count()==6];miss=[sum(1<<i for i,q in enumerate(Q) if not q&s) for s in S];omega=None if not all(miss) else ig.Graph(len(S),[(i,j) for j,y in enumerate(miss) for i in range(j) if not y&miss[i]]).clique_number();rec.append(dict(core=hex(m),deletable=m in children,omega=omega))
out=dict(parents=len(parents),moves=moves,deletable=len(children),low=rec);(P/'ramsey_38_layer47.json').write_text(json.dumps(out)+'\n');print('min2, deletable, excluded',len(low),len(low_aug),sum(r['omega'] is not None and r['omega']<7 for r in rec))
