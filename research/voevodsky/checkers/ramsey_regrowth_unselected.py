"""Fixed seed random 27-parent and deletion (not uniform core types). Reconstruct *all* extension neighborhoods independently. Count forced closures of every singleton and blue pair; never consult parent or valid supports when choosing seeds. Flag any disjoint-footprint square in surviving core."""
import json,collections,gzip,random,itertools
from ramsey_retention_slice import D,CAT,decode
P=D.parent;rng=random.Random(262702);ids={i:rng.randrange(27) for i in rng.sample(range(477142),256)};out=[]
for row,l in enumerate(gzip.open(CAT/'r38_27.g6.gz','rt')):
 if row not in ids:continue
 a=decode(l.strip());dl=ids[row];F=((1<<27)-1)^(1<<dl);I=[0]
 for i,v in enumerate(a):
  if i!=dl:I.extend([s|1<<i for s in I if not s&v]);
 Q=[q for q in I if q.bit_count()==7];M={0:(1<<len(Q))-1};hit=[sum(1<<i for i,q in enumerate(Q) if q>>j&1) for j in range(27)];ok=[]
 for s in I[1:]:
  b=s&-s;M[s]=M[s^b]&~hit[b.bit_length()-1];
  if not M[s]:ok.append(s)
 assert a[dl] in ok;E=[(a[i]|a[j])&F for i in range(27) for j in range(i) if dl not in (i,j) and a[i]>>j&1];sq=any(not b&c for b,c in itertools.combinations(E,2));counts=collections.defaultdict(collections.Counter);wins=collections.defaultdict(list)
 for seed in (s for s in I if s.bit_count()<=2):
  s=seed;avail=F&~s
  for i in range(27):
   if s>>i&1:avail&=~a[i]
  while True:
   if not M[s]:
    assert s in ok;wins[s].append(seed);kind='success';break
   forced=0;kind='stuck'
   for q in Q:
    if s&q:continue
    v=q&avail
    if not v:kind='fail';break
    if not v&(v-1):forced=v;break
   if kind=='fail' or not forced:break
   s|=forced;avail&=~(forced|a[forced.bit_length()-1])
  counts[seed.bit_count()][kind]+=1
 out.append(dict(row=row,dl=dl,parent_support=a[dl],square=sq,ok=ok,wins=wins,counts=counts))
(P/'ramsey_regrowth_unselected.json').write_text(json.dumps(out)+'\n');print('core profile',collections.Counter((r['square'],bool(r['wins']),len(r['wins'])==len(r['ok'])) for r in out));print('return parent',sum(r['parent_support'] in r['wins'] for r in out),'supports',sum(len(r['wins']) for r in out),sum(len(r['ok']) for r in out));print('min seed',collections.Counter(min(s.bit_count() for z in r['wins'].values() for s in z) if r['wins'] else None for r in out));print('seeds',sum((r['counts'][2] for r in out),collections.Counter()))
