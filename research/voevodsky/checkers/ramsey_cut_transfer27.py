"""Fixed-seed uniform 128-core transfer. Minimum balanced cuts, not assumed isoperimetric minima. Check all footprint pairs including exterior test; no conditioning on positives."""
import gzip,random,sys,json,itertools,subprocess,collections
from ramsey_retention_slice import D,CAT,decode,has
P=D.parent;ids=set(random.Random(22027).sample(range(477142),128));src=[(i,s.strip()) for i,s in enumerate(gzip.open(CAT/'r38_27.g6.gz','rt')) if i in ids];A=[decode(s) for i,s in src];cmd=[sys.argv[1]];out=[];F=(1<<27)-1
for base in range(0,len(A),16):
 group=A[base:base+16];ls=subprocess.check_output(cmd,input=''.join(' '.join(map(str,a))+'\n' for a in group),text=True).splitlines()
 for ix,(a,l) in enumerate(zip(group,ls,strict=True),base):
  cost,*ms=map(int,l.split());E=[(1<<i|1<<j,a[i]|a[j]) for i in range(27) for j in range(i) if a[i]>>j&1];B=[~v for v in a];score={};hist=collections.defaultdict(lambda:[0,0,0]);
  for m in ms:
   assert m.bit_count()==13 and sum((v&~m).bit_count() for i,v in enumerate(a) if m>>i&1)==cost
   X=[(i,(b&~m).bit_count(),(b&m).bit_count()) for i,(e,b) in enumerate(E) if e&m==e];Y=[(j,(b&m).bit_count(),(b&~m).bit_count()) for j,(e,b) in enumerate(E) if not e&m];
   for i,u,v in X:
    for j,w,z in Y:
     if u+z>14 or w+v>13:continue
     k=tuple(sorted((i,j)));score[k]=min(score.get(k,99),u+w)
  for i,(e,b) in enumerate(E):
   for j in range(i):
    f,c=E[j];
    if e&f:continue
    hh=hist[score.get((j,i),99)];hh[0]+=1
    if not b&c:hh[1]+=1;hh[2]+=not has(B,F&~(b|c),5)
  out.append(dict(id=src[ix][0],graph=src[ix][1],cost=cost,mincuts=len(ms),hist=hist))
 print(len(out),flush=True)
(P/'ramsey_cut_transfer27.json').write_text(json.dumps(out)+'\n');print([(k,[sum(sum(v[j] for s,v in r['hist'].items() if s<=k) for r in out) for j in range(3)]) for k in [2,3,4,5,8,98,99]])
