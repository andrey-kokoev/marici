"""On all generated blocked cases test arbitrary simultaneous additions, then arbitrary single-row replacement. Direct check positives."""
import json,collections,gzip,itertools
from ramsey_retention_slice import D,CAT,decode,check
P=D.parent;R=json.loads((P/'ramsey_block_patch26.json').read_text())['solutions'];ids={r['row'] for r in R};A={i:decode(l.strip()) for i,l in enumerate(gzip.open(CAT/'r38_27.g6.gz','rt')) if i in ids};out=[];hist=collections.Counter()
for r in R:
 a=A[r['row']][:];dl=r['dl'];mask=((1<<27)-1)^(1<<dl);a=[v&mask for v in a];a[dl]=0
 for u,v in r['add']:a[u]|=1<<v;a[v]|=1<<u
 I=[0]
 for i,v in enumerate(a):
  if i!=dl:I.extend([s|1<<i for s in I if not s&v]);
 Q=[q for q in I if q.bit_count()>=5];S=[s for s in I if all(i==dl or s&(v|1<<i) for i,v in enumerate(a))];blocked=any(all(all(a[i]&a[v] for i in r['c']) for v in range(27) if q>>v&1) for q in r['q']);sol=None
 for c in (r['c'],[r['c'][i] for i in (0,3,2,1)]):
  rows=[a[c[(j+2)%4]]|1<<c[(j+1)%4] for j in range(4)]
  for j in range(4):
   keep=rows[:j]+rows[j+1:];tight=[q for q in Q if q.bit_count()+sum(not q&s for s in keep)>=8];
   for s in S:
    if not all(q&s for q in tight):continue
    g=a[:]+[0]*5
    for h,t in enumerate(keep+[s],27):
     g[h]=t|1<<31;g[31]|=1<<h
     for i in range(27):g[i]|=(t>>i&1)<<h
    assert check(g,mask|(31<<27),3,9);sol=dict(c=c,j=j,s=s);break
   if sol:break
  if sol:break
 hist[blocked,bool(sol)]+=1;out.append(dict(**r,fully_blocked_quintuple=blocked,replacement=sol))
print(hist);(P/'ramsey_block_patch_release26.json').write_text(json.dumps(out)+'\n')
