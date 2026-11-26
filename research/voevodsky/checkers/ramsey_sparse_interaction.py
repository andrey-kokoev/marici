"""Explain interaction of individually disproved seeds. Project every blue-seven demand onto surviving vertices. Compare direct contradiction, mandatory adjacent pair, mandatory set dominating another demand, then short implication chains. Save checkable demand masks (pre-projection)."""
import json,itertools,collections
from ramsey_retention_slice import D,decode
P=D.parent;recs=[r for r in json.loads((P/'ramsey_regrowth_failed_literals.json').read_text()) if r['src']=='sparse'];G=(P/'ramsey38_26_e73_hog.g6').read_text().splitlines();F=(1<<26)-1;out=[];h=collections.Counter()
for r,g in zip(recs,G,strict=True):
 a=decode(g);I=[0]
 for i,v in enumerate(a):I.extend([s|1<<i for s in I if not s&v]);
 Q=[s for s in I if s.bit_count()==7];
 def fail(b):
  s=b;avail=F&~(s|a[b.bit_length()-1]);steps=[]
  while True:
   for q in Q:
    if s&q:continue
    z=q&avail
    if not z:return steps+[q]
    if not z&(z-1):break
   else:return None
   steps.append(q);s|=z;avail&=~(z|a[z.bit_length()-1])
 proofs={i:t for i in range(26) if (t:=fail(1<<i)) is not None};dead=sum(1<<i for i in proofs);assert dead==r['rounds'][0];live=F^dead;pr={q&live:q for q in Q};sing={p.bit_length()-1:q for p,q in pr.items() if p.bit_count()==1};adj=[(i,j) for i,j in itertools.combinations(sing,2) if a[i]>>j&1];
 if 0 in pr:kind='empty';cert=[pr[0]]
 elif adj:kind='mandatory red pair';i,j=adj[0];cert=[sing[i],sing[j]]
 else:
  cand=[]
  for q in Q:
   if any(q>>i&1 for i in sing):continue
   opts=q&live
   for k in range(1,len(sing)+1):
    hit=next((z for z in itertools.combinations(sing,k) if all(any(a[i]>>j&1 for i in z) for j in range(26) if opts>>j&1)),None)
    if hit:cand.append(([sing[i] for i in hit]+[q],opts.bit_count()));break
  if cand:cert,width=min(cand,key=lambda z:(len(z[0]),z[1]));kind='forced exclusion'
  else:cert=[];kind='deeper'
 needed=dead&__import__('functools').reduce(int.__or__,cert,0);h[kind,len(cert)]+=1;out.append(dict(row=r['row'],kind=kind,clauses=cert,projected=[s&live for s in cert],forced_proofs={i:proofs[i] for i in proofs if needed>>i&1},live=live,mandatory=list(sing)))
print(h);(P/'ramsey_sparse_interaction.json').write_text(json.dumps(out)+'\n')
