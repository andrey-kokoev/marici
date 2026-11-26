"""Minimum additive single-row patch: cover all originally overfull core cliques missed by that row, subject to independence. Replay a smallest endpoint per occurrence."""
import json,collections,gzip,itertools
from ramsey_retention_slice import CAT,D,decode,check
P=D.parent;R=json.loads((P/'ramsey_repair_square27.json').read_text());ids={r['row'] for r in R};A={i:decode(s.strip()) for i,s in enumerate(gzip.open(CAT/'r38_27.g6.gz','rt')) if i in ids};out=[];hist=collections.Counter()
for r in R:
 a=A[r['row']];I=[0]
 for i,v in enumerate(a):I.extend([s|1<<i for s in I if not s&v]);
 best=None;count=0
 for c in (r['runs'][0]['c'],r['runs'][4]['c']):
  rows=[a[c[(j+2)%4]]|1<<c[(j+1)%4] for j in range(4)];bad=[q for q in I if q.bit_count()+sum(not q&s for s in rows)>8];assert all(q.bit_count()+sum(not q&s for s in rows)==9 for q in bad)
  for j,s in enumerate(rows):
   if any(s&q for q in bad):continue
   candidates=[t for t in I if t&s==s and all(t&q for q in bad)];
   for t in candidates:
    size=(t^s).bit_count()
    if best is None or size<best[0]:best=(size,c,j,t^s);count=0
    if size==best[0]:count+=1
 size,c,j,patch=best;hist[r['n'],size]+=1;rows=[a[c[(h+2)%4]]|1<<c[(h+1)%4] for h in range(4)];rows[j]|=patch;g=a[:]+[0]*5
 for h,z in enumerate(rows,27):
  g[h]=z|1<<31;g[31]|=1<<h
  for i in range(27):g[i]|=(z>>i&1)<<h
 assert check(g,(1<<32)-1,3,9);out.append(dict(row=r['row'],e=r['e'],f=r['f'],n=r['n'],minimum=size,patch=patch,c=c,j=j,count=count))
print(hist);(P/'ramsey_patch_edge27.json').write_text(json.dumps(out)+'\n')
