"""All 73 exterior-failed squares. Hold three rows fixed, replace the fourth with any independent set. Also ask whether changes can be additions only to that row. Use maximal supports (coverage monotone); direct-check every saved 32-vertex endpoint."""
import json,gzip,collections,itertools
from ramsey_retention_slice import CAT,D,decode,check
P=D.parent;cases=[r for r in json.loads((P/'ramsey_cut_match_exterior27.json').read_text()) if r['illegal']];ids={r['row'] for r in cases};graphs={i:g.strip() for i,g in enumerate(gzip.open(CAT/'r38_27.g6.gz','rt')) if i in ids};out=[];stats=collections.Counter()
for r in cases:
 a=decode(graphs[r['row']]);I=[0];
 for i,v in enumerate(a):I.extend([s|1<<i for s in I if not s&v]);
 S=[s for s in I if all(s&(v|1<<i) for i,v in enumerate(a))];Q=[q for q in I if q.bit_count()>=5];bits=lambda s:[i for i in range(27) if s>>i&1];u,w=bits(r['e']);v,x=bits(r['f']);runs=[]
 for c in ((u,v,w,x),(u,x,w,v)):
  rows=[a[c[(j+2)%4]]|1<<c[(j+1)%4] for j in range(4)];assert any(q.bit_count()+sum(not s&q for s in rows)>8 for q in Q)
  for j,s in enumerate(rows):
   keep=rows[:j]+rows[j+1:];tight=[];over=False
   for q in Q:
    val=q.bit_count()+sum(not t&q for t in keep);over|=val>8
    if val==8:tight.append(q)
   ok=[] if over else [t for t in S if all(t&q for q in tight)];add=[t for t in ok if s&t==s];rec=dict(c=c,j=j,over=over,tight=len(tight),choices=len(ok),add=len(add));
   if ok:
    t=min(add or ok,key=lambda t:(s^t).bit_count());rec['replacement']=t;g=a[:]+[0]*5
    for h,z in enumerate(keep+[t],27):
     g[h]=z|1<<31;g[31]|=1<<h
     for i in bits(z):g[i]|=1<<h
    assert check(g,(1<<32)-1,3,9)
   runs.append(rec)
 stats[bool(any(z['choices'] for z in runs)),bool(any(z['add'] for z in runs))]+=1;out.append(dict(row=r['row'],e=r['e'],f=r['f'],n=r['n'],runs=runs))
print(stats);(P/'ramsey_repair_square27.json').write_text(json.dumps(out)+'\n')
