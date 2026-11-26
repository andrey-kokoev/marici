"""Look for a short forcing proof, not an enumeration of supports. Branch on tightest unmet blue seven; options include exactly its first selected eligible vertex. Red adjacency bans co-selection. Rooted comparison also branches over the four permissible corner pairs (conditional on breaking footprint separation). Free search verifies without this premise."""
import json,gzip,collections,itertools
from ramsey_retention_slice import CAT,D,decode
P=D.parent;pos=json.loads((P/'ramsey_regrow_counterexamples.json').read_text());neg=json.loads((P/'ramsey_block_patch_release26.json').read_text());R=pos+neg;ids={r['row'] for r in R};A={i:decode(l.strip()) for i,l in enumerate(gzip.open(CAT/'r38_27.g6.gz','rt')) if i in ids};out=[];hist=collections.defaultdict(collections.Counter)
for r in R:
 a=A[r['row']][:];dl=r['dl'];F=((1<<27)-1)^(1<<dl);a=[v&F for v in a];a[dl]=0
 for u,v in r.get('add',[]):a[u]|=1<<v;a[v]|=1<<u
 I=[0]
 for i,v in enumerate(a):
  if i!=dl:I.extend([s|1<<i for s in I if not s&v]);
 Q=[q for q in I if q.bit_count()==7];goal=r.get('regrowth',[]);c=r['c'];runs=[]
 def search(s,avail):
  steps=[]
  while True:
   q=min((q for q in Q if not q&s),key=lambda q:(q&avail).bit_count(),default=0)
   if not q:
    assert not avail and s in goal;return dict(steps=steps,sol=s)
   t=q&avail
   if not t:return dict(steps=steps,fail=q)
   if t&(t-1):break
   i=t.bit_length()-1;steps.append([q,i]);s|=t;avail&=~(t|a[i])
  ch=[]
  while t:
   bit=t&-t;t^=bit;avail^=bit;ch.append(search(s|bit,avail&~a[bit.bit_length()-1]))
  return dict(steps=steps,branch=q,ch=ch)
 def measure(t):
  z=[measure(v) for v in t.get('ch',[])];return (int(bool(z))+max((d for d,b in z),default=0),int(bool(z))+sum(b for d,b in z))
 for i,j in itertools.product(c[::2],c[1::2]):
  s=(1<<i)|(1<<j);t=search(s,F&~(s|a[i]|a[j]));runs.append(dict(pair=[i,j],tree=t));hist[bool(goal),'corner'][measure(t)[0]]+=1
 t=search(0,F);hist[bool(goal),'free'][measure(t)[0]]+=1;out.append(dict(row=r['row'],dl=dl,positive=bool(goal),corners=runs,free=t))
print({str(k):dict(v) for k,v in hist.items()});(P/'ramsey_regrowth_propagate.json').write_text(json.dumps(out,separators=(',',':'))+'\n')
