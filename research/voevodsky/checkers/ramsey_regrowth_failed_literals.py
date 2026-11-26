"""Independent control on stored 62 sparse cores and replay on unselected deletions. Test inclusion of each vertex with unit propagation; a contradiction proves the vertex globally forbidden. Iterate exclusions simultaneously. Independently enumerate legal neighborhoods to validate every deduction. No parent labels used by propagation."""
import json,collections,itertools,gzip
from ramsey_retention_slice import D,CAT,decode
P=D.parent;old=json.loads((P/'ramsey_regrowth_unselected.json').read_text());ids={r['row']:r['dl'] for r in old};gs=[('sparse',i,decode(s)) for i,s in enumerate((P/'ramsey38_26_e73_hog.g6').read_text().splitlines())];
for i,s in enumerate(gzip.open(CAT/'r38_27.g6.gz','rt')):
 if i in ids:
  a=decode(s.strip());vs=[v for v in range(27) if v!=ids[i]];gs.append(('deletion',i,[sum(1<<j for j,v in enumerate(vs) if a[u]>>v&1) for u in vs]))
out=[];F=(1<<26)-1
for src,row,a in gs:
 I=[0]
 for i,v in enumerate(a):I.extend([s|1<<i for s in I if not s&v]);
 Q=[s for s in I if s.bit_count()==7];ok=[s for s in I if all(s&q for q in Q)];
 def close(s,avail):
  while True:
   z=0;full=True
   for q in Q:
    if s&q:continue
    full=False;z=q&avail
    if not z:return -1
    if not z&(z-1):break
   else:return s if full else 0
   s|=z;avail&=~(z|a[z.bit_length()-1])
 cand=F;rounds=[];states=[]
 for seed in (s for s in I if s.bit_count()==2):
  i=(seed&-seed).bit_length()-1;j=seed.bit_length()-1;states.append(close(seed,F&~(seed|a[i]|a[j])))
 pair=[sum(x<0 for x in states),states.count(0),sum(x>0 for x in states)];
 while True:
  res=close(0,cand)
  if res:break
  rem=0;sols=[]
  for i in range(26):
   b=1<<i
   if b&cand:
    z=close(b,cand&~(b|a[i]));
    if z<0:rem|=b
    if z>0:sols.append(z)
  assert not any(rem&s for s in ok);rounds.append(rem)
  if sols:res=sols[0];break
  if not rem:break
  cand&=~rem
 assert res==0 or (res==-1 and not ok) or res in ok;out.append(dict(src=src,row=row,solutions=len(ok),pair=pair,rounds=rounds,result=res))
(P/'ramsey_regrowth_failed_literals.json').write_text(json.dumps(out)+'\n');
for src in ['sparse','deletion']:
 t=[r for r in out if r['src']==src];print(src,collections.Counter((bool(r['solutions']), (r['result']>0)-(r['result']<0),len(r['rounds'])) for r in t),[sum(r['pair'][i] for r in t) for i in range(3)])
