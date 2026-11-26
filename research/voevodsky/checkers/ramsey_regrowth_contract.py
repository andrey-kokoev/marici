"""Descend blue hitting demands by one red fork at a time. If T+u and T+v must be hit, where uv is red, T must be hit. One pass per size, no weaker supersets reused. Test on all sparse controls before and after removing individually disproved vertices."""
import json,collections,itertools
from ramsey_retention_slice import D,decode
P=D.parent;R=json.loads((P/'ramsey_sparse_interaction.json').read_text());G=(P/'ramsey38_26_e73_hog.g6').read_text().splitlines();out=[]
for r,g in zip(R,G):
 a=decode(g);I=[0]
 for i,v in enumerate(a):I.extend([s|1<<i for s in I if not s&v]);
 active=set(s for s in I if s.bit_count()==7);lev=[]
 for k in range(7,0,-1):
  lev.append(dict(k=k,n=len(active),dead=sum(not s&r['live'] for s in active)));nxt=set()
  for t in I:
   if t.bit_count()!=k-1:continue
   ext=0
   for i,v in enumerate(a):
    if not t>>i&1 and t|1<<i in active:
     if ext&v:nxt.add(t);break
     ext|=1<<i
  active=nxt
 out.append(dict(row=r['row'],levels=lev,empty=bool(active)))
print([(k,sum(r['levels'][7-k]['n']>0 for r in out),sum(r['levels'][7-k]['dead']>0 for r in out)) for k in range(7,0,-1)],sum(r['empty'] for r in out));(P/'ramsey_regrowth_contract.json').write_text(json.dumps(out)+'\n')
