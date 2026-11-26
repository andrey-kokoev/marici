"""Marked bridge tests for a specified edge layer. A pocket vertex in either marked four has precisely three neighbors outside H's five pocket vertices R. Enumerate triples, with fixed red adjacencies to labeled R; check four supports jointly on blue six/five/four cliques of H. Sufficient for ONE (3,8) projection; surviving projections still must coexist in (3,9)."""
import itertools,sys,json,gzip,collections,functools
from ramsey_retention_slice import CAT,D,decode
P=D.parent;R=json.loads((P/'ramsey_face_double_root.json').read_text());e=int(sys.argv[1]);rows=[r for r in R['marked'] if r['e']==e and r['catalogue']];groups={v['type']:dict(v['matches']) for v in json.loads((P/'ramsey_face_bridge_screen.json').read_text())};ids=set.union(*(set(groups[r['type']]) for r in rows));A={i:decode(l.strip()) for i,l in enumerate(gzip.open(CAT.parent/'r37_21.g6.gz','rt')) if i in ids};b=decode((CAT/'r35_13.g6').read_text().strip());F=(1<<21)-1;out=[]
for r in rows:
 q,t=r['q'],r['t'];p=[i for i in range(13) if not(q|t)>>i&1];P4=[[i for i in range(13) if s>>i&1] for s in (q,t)];rec=collections.Counter();cert=None
 for idx in groups[r['type']]:
  a=A[idx];I=[0]
  for j,v in enumerate(a):I.extend([s|1<<j for s in I if not s&v]);
  Iset=set(I);three=[s for s in I if s.bit_count()==3];qs={k:[s for s in I if s.bit_count()==k] for k in (4,5,6)}
  @functools.cache
  def misses(s,k):return sum(1<<i for i,v in enumerate(qs[k]) if not v&s)
  def panel(cs,chosen,once,twice,m4):
   if not cs:return chosen
   for s in cs[0]:
    if misses(s,6)&once or misses(s,5)&twice or len(chosen)==3 and misses(s,4)&m4:continue
    z=panel(cs[1:],chosen+[s],once|misses(s,6),twice|(misses(s,5)&functools.reduce(int.__or__,(misses(v,5) for v in chosen),0)),m4&misses(s,4))
    if z is not None:return z
  degrees=[4+sum(b[i]>>j&1 for j in p) for i in p];
  for ls in itertools.product(*[[i for i,v in enumerate(a) if v.bit_count()==d] for d in degrees]):
   if len(set(ls))!=5 or any((a[ls[i]]>>ls[j]&1)!=(b[p[i]]>>p[j]&1) for i,j in itertools.combinations(range(5),2)):continue
   mask=sum(1<<i for i in ls);avail=[s for s in three if not s&mask];both=[];rec['embeddings']+=1
   for group in P4:
    cs=[]
    for i in group:
     req=sum(1<<v for j,v in zip(p,ls) if b[i]>>j&1);cs.append([v|req for v in avail if (v|req) in Iset]);
    z=panel(sorted(cs,key=len),[],0,0,-1)
    if z is None:break
    both.append(z)
   rec[f'passed{len(both)}']+=1
   if len(both)==2 and cert is None:cert=dict(idx=idx,embedding=ls,panels=both)
 out.append(dict(q=q,t=t,stats=rec,example=cert));print(q,t,rec,flush=True)
(P/f'ramsey_face_bridge_triples{e}.json').write_text(json.dumps(out)+'\n')
