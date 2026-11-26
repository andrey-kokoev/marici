"""Re-run failed-inclusion propagation over every subset of the 61 matched edit sequences. After a rejection, shrink its first exclusion set to a smallest replayable certificate when of size <=3; otherwise retain greedy inclusion-minimal proof. Save trace of blue sevens needed for each proof; check against independent exhaustive verdicts."""
import json,collections,gzip,itertools
from ramsey_retention_slice import CAT,D,decode
P=D.parent;R=json.loads((P/'ramsey_regrowth_edit_lattice.json').read_text());ids={r['row'] for r in R};A={i:decode(l.strip()) for i,l in enumerate(gzip.open(CAT/'r38_27.g6.gz','rt')) if i in ids};out=[];hist=collections.Counter()
for r in R:
 dl=r['dl'];F=((1<<27)-1)^(1<<dl)
 for run in r['runs']:
  a=[v&F for v in A[r['row']]];a[dl]=0
  for u,v in run['edges']:a[u]|=1<<v;a[v]|=1<<u
  I=[0]
  for i,v in enumerate(a):
   if i!=dl:I.extend([s|1<<i for s in I if not s&v]);
  Q=[s for s in I if s.bit_count()==7]
  def close(s,avail):
   trace=[]
   while True:
    unmet=False
    for q in Q:
     if q&s:continue
     unmet=True;z=q&avail
     if not z:return -1,trace+[q]
     if z&(z-1)==0:break
    else:return (0 if unmet else s),trace
    trace.append(q);s|=z;avail&=~(z|a[z.bit_length()-1])
  cand=F;rounds=[];short=None
  while True:
   res,_=close(0,cand)
   if res:break
   dead=[];wins=[]
   for i in range(27):
    if not cand>>i&1:continue
    b=1<<i;z,_=close(b,cand&~(b|a[i]));
    if z<0:dead.append(i)
    if z>0:wins.append(z)
   rounds.append(dead)
   if wins:res=wins[0];break
   if not dead:break
   cand&=~sum(1<<i for i in dead)
  assert res==0 or (res>0)==bool(run['extensions']);
  if res==-1 and len(rounds)==1:
   dead=rounds[0];test=lambda v:close(0,F^sum(1<<i for i in v));v=next((v for k in (1,2,3) for v in itertools.combinations(dead,k) if test(v)[0]<0),None)
   if v is None:
    v=dead[:]
    for i in dead:
     w=[j for j in v if j!=i];
     if test(w)[0]<0:v=w
   tr={i:close(1<<i,F&~((1<<i)|a[i]))[1] for i in dead};m=sum(1<<i for i in dead);q=min((q for q in Q if not q&~m),key=lambda q:sum(len(t) for i,t in tr.items() if q>>i&1));short=dict(exclusions={i:tr[i] for i in v},root=test(v)[1],blocked_seven=q,branches={i:t for i,t in tr.items() if q>>i&1});
  hist[len(run['edges']),bool(run['extensions']),(res>0)-(res<0),len(rounds)]+=1;out.append(dict(row=r['row'],dl=dl,edges=run['edges'],verdict=res,rounds=rounds,short=short))
print(hist);print(collections.Counter(len(r['short']['exclusions']) for r in out if r['short']));(P/'ramsey_regrowth_near_proofs.json').write_text(json.dumps(out)+'\n')
