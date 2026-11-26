"""Independent terminal block replay for (1,2). For each nonempty local seam reconstruct labeled panel options directly from support sizes and adjacency to the two named seam vertices. Form explicit sets of 5-by-4 matrices by querying individual edges in each direction. Verify disjointness without selecting a common bit encoding or relying on earlier conflict certificates."""
from ramsey_k33_12_mutual import H,J,T,P,aut,mor,json,itertools,collections,lru_cache
from concurrent.futures import ProcessPoolExecutor

def init():
 global dck
 dck={(n,d['i'],d['e']):d['panels'] for n,k in [(15,5),(16,4)] for d in json.loads((T/f'k12deck{k}.json').read_text())}
@lru_cache(maxsize=5000)
def lib(n,idx,e):
 choices=set()
 for panel in dck[n,idx,e]:
  for p in aut(n,idx):choices.add(tuple(sorted(mor(s,p) for s in panel)))
 return choices
@lru_cache(maxsize=30000)
def assign(n,idx,e,z,signature):
 valid=[]
 for panel in lib(n,idx,e):
  fields=[(s.bit_count(),s>>z[0]&1,s>>z[1]&1) for s in panel]
  if sorted(fields)!=sorted(signature):continue
  for perm in itertools.permutations(range(len(panel))):
   if all(fields[j]==sig for j,sig in zip(perm,signature)):valid.append(tuple(panel[j] for j in perm))
 return valid

def test(record):
 i,j,a,b,c,f,g,h,z,t,kind,flags=record;u=a|b|c;v=f|g|h;X=[x for x in range(16) if a>>x&1];sig=lambda arr,inside,seq,zz:tuple((7-(arr[x]&inside).bit_count(),arr[x]>>zz[0]&1,arr[x]>>zz[1]&1) for x in seq);cross=lambda graph,s,t:sum((k&t).bit_count() for n,k in enumerate(graph) if s>>n&1);A=assign(15,j,44+cross(H[i],b,c),tuple(t),sig(H[i],u,X,z));assert A;failed=0;edges=0
 for end,other in [(h,g),(g,h)]:
  Y=[y for y in range(15) if end&~f&1<<y];R=assign(16,i,44+cross(J[j],f,other),tuple(z),sig(J[j],v,Y,t));assert R;Lset={tuple((s>>y)&1 for s in m for y in Y) for m in A};Rset={tuple((s>>x)&1 for x in X for s in m) for m in R};failed+=Lset.isdisjoint(Rset);edges+=sum(set(col).isdisjoint(other) for col,other in zip(zip(*Lset),zip(*Rset)))
 assert failed and bool(edges)==(kind=='edge');return failed,edges
if __name__=='__main__':
 src=json.loads((P/'ramsey_k33_12_seam.json').read_text());assert not src['remaining'] and len(src['certificates'])==src['counts']['three_domains'];
 with ProcessPoolExecutor(6,initializer=init) as ex:rows=list(ex.map(test,src['certificates'],chunksize=64));
 res=dict(total=len(rows),failed_blocks=dict(collections.Counter(n for n,e in rows)),with_single_edge=sum(bool(e) for n,e in rows),block_only=sum(not e for n,e in rows));print(res);(P/'ramsey_k33_12_verified.json').write_text(json.dumps(res)+'\n')
