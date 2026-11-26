"""Exact fixed-seed two-repair test. Count failed demands containing the new vertex and verify the resulting monochromatic eight-cliques directly."""
import itertools,json,collections
from ramsey_retention_slice import D,decode,check,has
P=D.parent;r=json.loads((P/'ramsey_38_reverse_seed.json').read_text());g=decode(next(s['graph6'] for s in json.loads(D.read_text()) if (s['l'],s['k'])==(3,8)));C,J=r['core_mask'],r['neighbor_mask'];T=r['best'][1]['red_core'];bits=lambda p:[i for i in range(28) if p>>i&1]
for i,j in [(5,22),(21,26)]:assert g[i]>>j&1;g[i]^=1<<j;g[j]^=1<<i
valid=check(g,(1<<27)-1,3,8);print('old legal',valid);ind=[0]
for i in bits(C):ind += [q|1<<i for q in ind if not q&g[i]]
E=sum((g[i]&C).bit_count() for i in bits(C))//2;six=[q for q in ind if q.bit_count()==6];opts=[s for s in ind if 45<=E+s.bit_count()<=49 and all(q&s for q in six)];assert opts==[T];avail=[i for i in bits(J) if not g[i]&T];out=[]
for n in range(len(avail)+1):
 for links in itertools.combinations(avail,n):
  hit0=sum(1<<i for i in links);bad=collections.Counter();w=None
  for q in sorted(ind,key=int.bit_count):
   if q&T:continue
   hit=hit0
   for i in bits(q):hit|=g[i]&J
   k=q.bit_count()+1
   if hit.bit_count()<k:
    bad[k]+=1
    if w is None:w=[27]+bits(q)+bits(J&~hit)[:8-k]
  a=g.copy()+[T|hit0];
  for i in bits(a[27]):a[i]|=1<<27
  assert not has(a,2**28-1,3) and (not w or (len(w)==8 and all(not(a[i]>>j&1) for i,j in itertools.combinations(w,2))))
  out.append(dict(links=links,failures=bad,blue_eight=w));print(out[-1])
(P/'ramsey_38_double_link.json').write_text(json.dumps(dict(old_legal=valid,available=avail,tests=out),indent=1)+'\n')
