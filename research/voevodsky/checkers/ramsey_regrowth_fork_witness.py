"""Build and replay a red-fork refutation DAG from the empty set; enumerate viable final seven-sets only at leaves. Test all positive/negative blocked and sparse cores."""
import json,gzip,collections,itertools,functools
from ramsey_retention_slice import D,CAT,decode
P=D.parent;neg=json.loads((P/'ramsey_block_patch_release26.json').read_text());pos=json.loads((P/'ramsey_regrow_counterexamples.json').read_text());ids={r['row'] for r in neg+pos};A={i:decode(s.strip()) for i,s in enumerate(gzip.open(CAT/'r38_27.g6.gz','rt')) if i in ids};gs=[('sparse',i,decode(s),(1<<26)-1) for i,s in enumerate((P/'ramsey38_26_e73_hog.g6').read_text().splitlines())];
for r in neg+pos:
 a=A[r['row']][:];
 for u,v in r.get('add',[]):a[u]|=1<<v;a[v]|=1<<u
 gs.append(('edited' if 'add' in r else 'extendible',r['row'],a,((1<<27)-1)^(1<<r['dl'])))
out=[];h=collections.Counter()
for tag,i,a,F in gs:
 @functools.lru_cache(None)
 def proof(t,avail):
  if t.bit_count()==7:return True
  if t.bit_count()+avail.bit_count()<7:return False
  u=[]
  for j,v in enumerate(a):
   b=1<<j
   if avail&b and proof(t|b,avail&~(b|v)):
    for k in u:
     if v>>k&1:choice[t]=[j,k];return True
    u.append(j)
  return False
 choice={};ok=proof(0,F);dag={}
 def replay(t):
  if t in dag or t.bit_count()==7:return
  j,k=choice[t];assert a[j]>>k&1 and all(not (t&(a[v]|1<<v)) and F>>v&1 for v in (j,k));dag[t]=[j,k];replay(t|1<<j);replay(t|1<<k)
 if ok:replay(0)
 assert not(tag=='extendible' and ok);h[tag,ok]+=1;out.append(dict(tag=tag,row=i,mask=F,dag=dag))
print(h);(P/'ramsey_regrowth_fork_witness.json').write_text(json.dumps(out)+'\n')
