"""All one-vertex triangle-free (3,8) regrowth supports on the 61 edited cores. Do not maximalize: a smaller neighborhood might preserve the square. Count old blue sevens missed by triangle-free supports constrained to touch at most one footprint. Exact witness verification."""
import json,collections,gzip,itertools
from ramsey_retention_slice import D,CAT,decode,check
P=D.parent;R=json.loads((P/'ramsey_block_patch_release26.json').read_text());ids={r['row'] for r in R};A={i:decode(l.strip()) for i,l in enumerate(gzip.open(CAT/'r38_27.g6.gz','rt')) if i in ids};out=[];hist=collections.Counter()
for r in R:
 a=A[r['row']][:];dl=r['dl'];mask=((1<<27)-1)^(1<<dl);a=[v&mask for v in a];a[dl]=0
 for u,v in r['add']:a[u]|=1<<v;a[v]|=1<<u
 I=[0]
 for i,v in enumerate(a):
  if dl!=i:I.extend([s|1<<i for s in I if not s&v]);
 qs=[q for q in I if q.bit_count()==7];allq=(1<<len(qs))-1;hit=[sum(1<<j for j,q in enumerate(qs) if q>>i&1) for i in range(27)];hits={0:0};c=r['c'];d0=(1<<c[0])|(1<<c[2]);d1=(1<<c[1])|(1<<c[3]);stats=collections.Counter();solutions=[];best={};corners=collections.Counter()
 for s in I:
  if s:hits[s]=hits[s&(s-1)]|hit[(s&-s).bit_length()-1];
  n=(allq^hits[s]).bit_count();tag=int(bool(s&d0))+int(bool(s&d1));
  if tag not in best or n<best[tag][0]:best[tag]=(n,s)
  if n:continue
  g=a[:];g[dl]=s
  for i in range(27):g[i]|=((s>>i)&1)<<dl
  assert check(g,(1<<27)-1,3,8);stats[tag]+=1;solutions.append(s);corners[str((s&(d0|d1)).bit_count())]+=1
 hist[bool(solutions),bool(r['replacement'])]+=1;out.append(dict(row=r['row'],dl=dl,c=c,added=r['add'],sevens=len(qs),by_footprints=stats,best=best,solutions=solutions))
print(hist,'extensions',sum(len(r['solutions']) for r in out),'counts',collections.Counter(len(r['solutions']) for r in out));print('best preserving',collections.Counter(min(r['best'][j][0] for j in (0,1)) for r in out));(P/'ramsey_blocked_regrowth27.json').write_text(json.dumps(out)+'\n')
