"""Census failures and sample controls without replacement matched by exterior size. All minimum bisections, count each diagonal pair once. No fitting thresholds."""
import sys,json,collections,gzip,subprocess,itertools,random
from ramsey_retention_slice import D,CAT,decode
P=D.parent;cases=collections.defaultdict(list);controls=collections.defaultdict(list);rng=random.Random(27073)
with gzip.open(CAT/'r38_27.g6.gz','rt') as f:
 off=0
 while chunk:=list(itertools.islice(f,8192)):
  for l in subprocess.check_output([sys.argv[1],'ids'],text=True,input=''.join(chunk)).splitlines():
   ix,g,*nums=l.split();i,j,k,h,*a=map(int,nums);n=len(a);bad=any(all(not a[u]>>v&1 for u,v in itertools.combinations(s,2)) for s in itertools.combinations(range(n),5));(cases if bad else controls)[n].append((int(ix)+off,g,(1<<i|1<<j),(1<<k|1<<h),n,bad,sum(v.bit_count() for v in a)//2))
  off+=len(chunk)
rows=sum(cases.values(),[])+[r for n,c in cases.items() for r in rng.sample(controls[n],len(c))];gs=list(dict.fromkeys(r[1] for r in rows));costs={}
for i in range(0,len(gs),32):
 chunk=gs[i:i+32];ls=subprocess.check_output([sys.argv[2]],input=''.join(' '.join(map(str,decode(g)))+'\n' for g in chunk),text=True).splitlines();costs.update(zip(chunk,[list(map(int,l.split())) for l in ls],strict=True))
out=[];hist=collections.defaultdict(collections.Counter)
for ix,g,e,f,n,bad,edges in rows:
 cost,*ms=costs[g];a=decode(g);fp=lambda e: __import__('functools').reduce(int.__or__,(a[i] for i in range(27) if e>>i&1));b,c=fp(e),fp(f);leaks=[]
 for m in ms:
  if e&m==e and not f&m:leaks.append((b&~m).bit_count()+(c&m).bit_count())
  if f&m==f and not e&m:leaks.append((c&~m).bit_count()+(b&m).bit_count())
 score=min(leaks,default=99);hist[bad][score]+=1;out.append(dict(row=ix,e=e,f=f,n=n,illegal=bad,cost=cost,mincuts=len(ms),opposite=len(leaks),leak=score,exterior_edges=edges))
print({n:len(x) for n,x in cases.items()},hist);(P/'ramsey_cut_match_exterior27.json').write_text(json.dumps(out)+'\n')
